"""
This module is all about its 'aliases' (v.) class decorator
"""

from itertools import chain


# TODO - remove this, we don't need the python2 compatibility anymore
def super_dir(obj):
    """
    A python2/3 compatible way of getting the default ('super') behavior of __dir__
    """
    return sorted(set(chain(dir(type(obj)), obj.__dict__)))


# Python 3.4 does not have RecursionError - it throws a RuntimeError instead
try:
    _RecursionError = RecursionError
except NameError:
    _RecursionError = RuntimeError


class AliasingMixin():
    @property
    def _aliased(self):
        try:
            return getattr(self, self._ALIAS)
        except AttributeError:
            raise RuntimeError("object %r does no contain aliased object %r" % (self, self._ALIAS))

    def __dir__(self):
        members = set(super_dir(self))
        members.update(n for n in dir(self._aliased) if not n.startswith("_"))
        return sorted(members)

    def __getattr__(self, attr):
        if attr.startswith("_"):
            raise AttributeError(attr)
        try:
            return getattr(self._aliased, attr)
        except _RecursionError as e:
            if type(e) is RuntimeError and str(e) != 'maximum recursion depth exceeded':
                raise
            raise _RecursionError('Infinite recursion trying to access {attr!r} on {obj!r} (via {type_name}.{alias}.{attr})'.format(
                attr=attr,
                obj=self,
                type_name=type(self).__name__,
                alias=self._ALIAS))


def aliases(name, static=True):
    """
    A class decorator that makes objects of a class delegate to an object they contain.
    Inspired by D's "alias this".

    Example::

        class B():
            def foo(self):
                print('foo')

        @aliases('b')
        class A():
            b = B()

        a = A()
        a.foo()  # delegated to b.foo()


        @aliases('b', static=False)
        class A():
            def __init__(self):
                self.b = B()

        a = A()
        a.foo()  # delegated to b.foo()

    """
    def deco(cls):
        assert not static or hasattr(cls, name)
        return type(cls.__name__, (cls, AliasingMixin), dict(_ALIAS=name, __module__=cls.__module__))
    return deco
