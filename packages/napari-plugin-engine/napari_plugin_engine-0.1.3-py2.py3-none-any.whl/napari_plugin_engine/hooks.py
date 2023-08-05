"""
Internal hook annotation, representation and calling machinery.
"""
import warnings
from collections.abc import Sequence
from typing import Any, Callable, List, Optional, Union

from .callers import HookCallError, HookResult, _multicall
from .exceptions import PluginCallError
from .implementation import HookImpl, HookSpec

HookExecFunc = Callable[['HookCaller', List[HookImpl], dict], HookResult]
"""A function that loops calling a list of :class:`~napari_plugin_engine.HookImpl` s and
returns a :class:`~napari_plugin_engine.HookResult`.

Parameters
----------
hook_caller : HookCaller
    a :class:`HookCaller` instance.
hook_impls : List[HookImpl]
    a list of :class:`~napari_plugin_engine.HookImpl` instances to call.
kwargs : dict
    a mapping of keyword arguments to provide to the implementation.

Returns
-------
result : HookResult
    The :class:`~napari_plugin_engine.HookResult` object resulting from the call loop.
"""


class HookCaller:
    """The primary hook-calling object.

    A :class:`PluginManager` may have multiple ``HookCaller`` objects and they
    are stored in the ``plugin_manager.hook`` namespace, named after the `hook
    specification` that they represent.  For instance:

    .. code-block:: python

       pm = PluginManager("demo")
       pm.add_hookspec(some_module)
       # assuming `some_module` had an @hookspec named `my specification`
       assert isinstance(pm.hook.my_specification, HookCaller)

    Each ``HookCaller`` instance stores all of the :class:`HookImpl` objects
    discovered during :meth:`plugin registration <PluginManager.register>`
    (each of which capture the implementation of a specific plugin for this
    hook specification).

    The ``HookCaller`` instance also usually creates and stores a reference to
    the :class:`HookSpec` instance that encapsulates information about the hook
    specification, (at ``HookCaller.spec``)

    Parameters
    ----------
    name : str
        The name of the `hook specification` that this ``HookCaller``
        represents.
    hook_execute : Callable
        A :data:`.HookExecFunc` function.  In almost every case, this will be
        provided by the :class:`PluginManager` during hook registration as
        :meth:`PluginManager._hookexec`... which is, in turn, mostly just a
        wrapper around :func:`._multicall`.
    namespace : Any, optional
        An namespace (such as a module or class) to search during `HookSpec`
        creation for functions decorated with ``@hookspec`` named with the
        string ``name``.
    spec_opts : Optional[dict], optional
        keyword arguments to be passed when creating the :class:`HookSpec`
        instance at ``self.spec``.
    """

    def __init__(
        self,
        name: str,
        hook_execute: HookExecFunc,
        namespace: Any = None,
        spec_opts: Optional[dict] = None,
    ):
        self.name = name
        self._wrappers: List[HookImpl] = []
        self._nonwrappers: List[HookImpl] = []
        self._hookexec = hook_execute
        self.argnames = None
        self.kwargnames = None
        self.multicall = _multicall
        self.spec: Optional[HookSpec] = None
        if namespace is not None:
            assert spec_opts is not None
            self.set_specification(namespace, spec_opts)

    def has_spec(self) -> bool:
        return self.spec is not None

    @property
    def is_firstresult(self) -> bool:
        return self.spec.firstresult if self.spec else False

    def set_specification(self, namespace, spec_opts):
        assert not self.has_spec()
        self.spec = HookSpec(namespace, self.name, **spec_opts)
        if spec_opts.get("historic"):
            self._call_history = []

    def is_historic(self) -> bool:
        return hasattr(self, "_call_history")

    def _remove_plugin(self, plugin: Any):
        def remove(wrappers):
            for i, method in enumerate(wrappers):
                if method.plugin == plugin:
                    del wrappers[i]
                    return True

        if remove(self._wrappers) is None:
            if remove(self._nonwrappers) is None:
                raise ValueError("plugin %r not found" % (plugin,))

    def get_hookimpls(self) -> List[HookImpl]:
        # Order is important for _hookexec
        return self._nonwrappers + self._wrappers

    def _add_hookimpl(self, hookimpl: HookImpl):
        """Add an implementation to the callback chain.
        """
        if hookimpl.hookwrapper:
            methods = self._wrappers
        else:
            methods = self._nonwrappers

        if hookimpl.trylast:
            methods.insert(0, hookimpl)
        elif hookimpl.tryfirst:
            methods.append(hookimpl)
        else:
            # find last non-tryfirst method
            i = len(methods) - 1
            while i >= 0 and methods[i].tryfirst:
                i -= 1
            methods.insert(i + 1, hookimpl)

    def __repr__(self) -> str:
        return f"<HookCaller {self.name}>"

    def call_historic(self, result_callback=None, kwargs=None):
        """Call the hook with given ``kwargs`` for all registered plugins and
        for all plugins which will be registered afterwards.

        If ``result_callback`` is not ``None`` it will be called for for each
        non-``None`` result obtained from a hook implementation.
        """
        self._call_history.append((kwargs or {}, result_callback))
        # historizing hooks don't return results
        res = self._hookexec(self, self.get_hookimpls(), kwargs).result
        if result_callback is None:
            return
        # XXX: remember firstresult isn't compat with historic
        for x in res or []:
            result_callback(x)

    def call_extra(self, methods: List[Callable], kwargs: dict):
        """ Call the hook with some additional temporarily participating
        methods using the specified ``kwargs`` as call parameters. """
        old = list(self._nonwrappers), list(self._wrappers)
        for method in methods:
            self._add_hookimpl(HookImpl(method))
        try:
            return self(**kwargs)
        finally:
            self._nonwrappers, self._wrappers = old

    def _maybe_apply_history(self, method):
        """Apply call history to a new hookimpl if it is marked as historic.
        """
        if self.is_historic():
            for kwargs, result_callback in self._call_history:
                res = self._hookexec(self, [method], kwargs).result
                if res and result_callback is not None:
                    result_callback(res[0])

    def get_plugin_implementation(self, plugin_name: str):
        """Return hook implementation instance for ``plugin_name`` if found."""
        try:
            return next(
                imp
                for imp in self.get_hookimpls()
                if imp.plugin_name == plugin_name
            )
        except StopIteration:
            raise KeyError(
                f"No implementation of {self.name} found "
                f"for plugin {plugin_name}."
            )

    def index(self, value: Union[str, HookImpl]) -> int:
        """Return index of plugin_name or a HookImpl in self._nonwrappers"""
        if isinstance(value, HookImpl):
            return self._nonwrappers.index(value)
        elif isinstance(value, str):
            plugin_names = [imp.plugin_name for imp in self._nonwrappers]
            return plugin_names.index(value)
        else:
            raise TypeError(
                "argument provided to index must either be the "
                "(string) name of a plugin, or a HookImpl instance"
            )

    def bring_to_front(self, new_order: Union[List[str], List[HookImpl]]):
        """Move items in ``new_order`` to the front of the call order.

        By default, hook implementations are called in last-in-first-out order
        of registration, and pluggy does not provide a built-in way to
        rearrange the call order of hook implementations.

        This function accepts a `HookCaller` instance and the desired
        ``new_order`` of the hook implementations (in the form of list of
        plugin names, or a list of actual ``HookImpl`` instances) and reorders
        the implementations in the hook caller accordingly.

        NOTE: hook implementations are actually stored in *two* separate list
        attributes in the hook caller: ``HookCaller._wrappers`` and
        ``HookCaller._nonwrappers``, according to whether the corresponding
        ``HookImpl`` instance was marked as a wrapper or not.  This method
        *only* sorts _nonwrappers.
        For more, see: https://pluggy.readthedocs.io/en/latest/#wrappers

        Parameters
        ----------
        new_order :  list of str or list of ``HookImpl`` instances
            The desired CALL ORDER of the hook implementations.  The list
            does *not* need to include every hook implementation in
            :meth:`~HookCaller.get_hookimpls`, but those that are not included
            will be left at the end of the call order.

        Raises
        ------
        TypeError
            If any item in ``new_order`` is neither a string (plugin_name) or a
            ``HookImpl`` instance.
        ValueError
            If any item in ``new_order`` is neither the name of a plugin or a
            ``HookImpl`` instance that is present in self._nonwrappers.
        ValueError
            If ``new_order`` argument has multiple entries for the same
            implementation.

        Examples
        --------
        Imagine you had a hook specification named ``print_plugin_name``, that
        expected plugins to simply print their own name. An implementation
        might look like:

        >>> # hook implementation for ``plugin_1``
        >>> @hook_implementation
        ... def print_plugin_name():
        ...     print("plugin_1")

        If three different plugins provided hook implementations. An example
        call for that hook might look like:

        >>> plugin_manager.hook.print_plugin_name()
        plugin_1
        plugin_2
        plugin_3

        If you wanted to rearrange their call order, you could do this:

        >>> new_order = ["plugin_2", "plugin_3", "plugin_1"]
        >>> plugin_manager.hook.print_plugin_name.bring_to_front(new_order)
        >>> plugin_manager.hook.print_plugin_name()
        plugin_2
        plugin_3
        plugin_1

        You can also just specify one or more item to move them to the front
        of the call order:
        >>> plugin_manager.hook.print_plugin_name.bring_to_front(["plugin_3"])
        >>> plugin_manager.hook.print_plugin_name()
        plugin_3
        plugin_2
        plugin_1
        """

        if not isinstance(new_order, Sequence) or isinstance(new_order, str):
            raise TypeError(
                'The first argument to "bring_to_front" '
                'must be a non-string sequence type.'
            )

        # make sure items in order are unique
        if len(new_order) != len(set(new_order)):
            raise ValueError("repeated item in order")

        # make new lists for the rearranged _nonwrappers
        # for details on the difference between wrappers and nonwrappers, see:
        # https://pluggy.readthedocs.io/en/latest/#wrappers
        _old_nonwrappers = self._nonwrappers.copy()
        _new_nonwrappers: List[HookImpl] = []
        indices = [self.index(elem) for elem in new_order]
        for i in indices:
            # inserting because they get called in reverse order.
            _new_nonwrappers.insert(0, _old_nonwrappers[i])

        # remove items that have been pulled, leaving only items that
        # were not specified in ``new_order`` argument
        # do this rather than using .pop() above to avoid changing indices
        for i in sorted(indices, reverse=True):
            del _old_nonwrappers[i]

        # if there are any hook_implementations left over, add them to the
        # beginning of their respective lists (because at call time, these
        # lists are called in reverse order)
        if _old_nonwrappers:
            _new_nonwrappers = [x for x in _old_nonwrappers] + _new_nonwrappers

        # update the _nonwrappers list with the reordered list
        self._nonwrappers = _new_nonwrappers

    def _set_plugin_enabled(self, plugin_name: str, enabled: bool):
        """Enable or disable the hook implementation for a specific plugin.

        Parameters
        ----------
        plugin_name : str
            The name of a plugin implementing ``hook_spec``.
        enabled : bool
            Whether or not the implementation should be enabled.

        Raises
        ------
        KeyError
            If ``plugin_name`` has not provided a hook implementation for this
            hook specification.
        """
        self.get_plugin_implementation(plugin_name).enabled = enabled

    def enable_plugin(self, plugin_name: str):
        """enable implementation for ``plugin_name``."""
        self._set_plugin_enabled(plugin_name, True)

    def disable_plugin(self, plugin_name: str):
        """disable implementation for ``plugin_name``."""
        self._set_plugin_enabled(plugin_name, False)

    def _call_plugin(self, plugin_name: str, *args, **kwargs):
        """Call the hook implementation for a specific plugin

        Note: this method is not intended to be called directly. Instead, just
        call the instance directly, specifing the ``_plugin`` argument.
        See the ``__call__`` method below.

        Parameters
        ----------
        plugin_name : str
            Name of the plugin

        Returns
        -------
        Any
            Result of implementation call provided by plugin

        Raises
        ------
        TypeError
            If the implementation is a hook wrapper (cannot be called directly)
        TypeError
            If positional arguments are provided
        HookCallError
            If one of the required arguments in the hook specification is not
            present in ``kwargs``.
        PluginCallError
            If an exception is raised when calling the plugin
        """
        self._check_call_kwargs(kwargs)
        implementation = self.get_plugin_implementation(plugin_name)
        if implementation.hookwrapper:
            raise TypeError("Hook wrappers can not be called directly")

        # pluggy only allows calling hooks with keyword arguments
        if args:
            raise TypeError("hook calling supports only keyword arguments")
        _args: List[Any] = []
        # this converts kwargs into positional arguments in the correct order
        # for the hookspec
        try:
            _args = [kwargs[argname] for argname in implementation.argnames]
        except KeyError:
            for argname in implementation.argnames:
                if argname not in kwargs:
                    raise HookCallError(
                        f"hook call must provide argument {argname}"
                    )

        try:
            return implementation(*_args)
        except Exception as exc:
            raise PluginCallError(implementation) from exc

    def call_with_result_obj(
        self, *, _skip_impls: List[HookImpl] = list(), **kwargs
    ) -> HookResult:
        """Call hook implementation(s) for this spec and return HookResult.

        The :class:`HookResult` object carries the result (in its ``result``
        property) but also additional information about the hook call, such
        as the implementation that returned each result and any call errors.

        Parameters
        ----------
        _skip_impls : List[HookImpl], optional
            A list of HookImpl instances that should be *skipped* when calling
            hook implementations, by default None
        **kwargs
            keys should match the names of arguments in the corresponding hook
            specification, values will be passed as arguments to the hook
            implementations.

        Returns
        -------
        result : HookResult
            A :class:`HookResult` object that contains the results returned by
            plugins along with other metadata about the call.

        Raises
        ------
        HookCallError
            If one or more of the keys in ``kwargs`` is not present in
            one of the ``hook_impl.argnames``.
        PluginCallError
            If ``firstresult == True`` and a plugin raises an Exception.
        """
        # if not self.get_hookimpls():
        #     warnings.warn(
        #         'No hook implementations registered for this hook caller!'
        #     )
        self._check_call_kwargs(kwargs)
        impls = [imp for imp in self.get_hookimpls() if imp not in _skip_impls]
        return self._hookexec(self, impls, kwargs)

    def __call__(
        self,
        *args,
        _plugin: Optional[str] = None,
        _skip_impls: List[HookImpl] = list(),
        **kwargs,
    ) -> Union[Any, List[Any]]:
        """Call hook implementation(s) for this spec and return result(s).

        This is the primary way to call plugin hook implementations.

        Note: Parameters are prefaced by underscores to reduce potential
        conflicts with argument names in hook specifications.  There is a test
        in ``test_hook_specifications.test_annotation_on_hook_specification``
        to ensure that these argument names are never used in one of our
        hookspecs.

        Parameters
        ----------
        _plugin : str, optional
            The name of a specific plugin to use.  By default all
            implementations will be called (though if ``firstresult==True``,
            only the first non-None result will be returned).
        _skip_impls : List[HookImpl], optional
            A list of HookImpl instances that should be *skipped* when calling
            hook implementations, by default None
        **kwargs
            keys should match the names of arguments in the corresponding hook
            specification, values will be passed as arguments to the hook
            implementations.

        Raises
        ------
        HookCallError
            If one or more of the keys in ``kwargs`` is not present in one of
            the ``hook_impl.argnames``.
        PluginCallError
            If ``firstresult == True`` and a plugin raises an Exception.

        Returns
        -------
        result
            If the hookspec was declared with ``firstresult==True``, a single
            result will be returned. Otherwise will return a list of results
            from all hook implementations for this hook caller.

            If ``_plugin`` is provided, will return the single result from the
            specified plugin.
        """
        if args:
            raise TypeError("hook calling supports only keyword arguments")
        if _plugin:
            # if a plugin name is specified, just call it directly
            return self._call_plugin(_plugin, **kwargs)

        result = self.call_with_result_obj(_skip_impls=_skip_impls, **kwargs)
        return result.result

    def _check_call_kwargs(self, kwargs):
        """Warn if any keys in the hookspec are not present in this call.

        It's possible to add arguments to hook specifications (as they evolve).
        Here we just emit a warning if there are arguments in the hookspec that
        were not specified in this call, which may mean the call could be
        updated.
        """
        # "historic" hooks can be called with ``call_historic()`` *before*
        # having been registered.  However they must be called with
        # self.call_historic().
        # https://pluggy.readthedocs.io/en/latest/index.html#historic-hooks
        assert (
            not self.is_historic()
        ), 'Historic hooks must be called with `call_historic()`'

        if self.spec and self.spec.argnames:
            notincall = set(self.spec.argnames) - set(kwargs.keys())
            if notincall:
                warnings.warn(
                    "Argument(s) {} which are declared in the hookspec "
                    "can not be found in this hook call".format(
                        tuple(notincall)
                    ),
                    stacklevel=2,
                )
