# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkPointPython
else:
    import _itkPointPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkPointPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkPointPython.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import itkFixedArrayPython
import pyBasePython
import itkVectorPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import vnl_vector_refPython
class vectoritkPointF2(object):
    r"""Proxy of C++ std::vector< itkPointF2 > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkPointPython.vectoritkPointF2_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkPointPython.vectoritkPointF2___nonzero__)
    __bool__ = _swig_new_instance_method(_itkPointPython.vectoritkPointF2___bool__)
    __len__ = _swig_new_instance_method(_itkPointPython.vectoritkPointF2___len__)
    __getslice__ = _swig_new_instance_method(_itkPointPython.vectoritkPointF2___getslice__)
    __setslice__ = _swig_new_instance_method(_itkPointPython.vectoritkPointF2___setslice__)
    __delslice__ = _swig_new_instance_method(_itkPointPython.vectoritkPointF2___delslice__)
    __delitem__ = _swig_new_instance_method(_itkPointPython.vectoritkPointF2___delitem__)
    __getitem__ = _swig_new_instance_method(_itkPointPython.vectoritkPointF2___getitem__)
    __setitem__ = _swig_new_instance_method(_itkPointPython.vectoritkPointF2___setitem__)
    pop = _swig_new_instance_method(_itkPointPython.vectoritkPointF2_pop)
    append = _swig_new_instance_method(_itkPointPython.vectoritkPointF2_append)
    empty = _swig_new_instance_method(_itkPointPython.vectoritkPointF2_empty)
    size = _swig_new_instance_method(_itkPointPython.vectoritkPointF2_size)
    swap = _swig_new_instance_method(_itkPointPython.vectoritkPointF2_swap)
    begin = _swig_new_instance_method(_itkPointPython.vectoritkPointF2_begin)
    end = _swig_new_instance_method(_itkPointPython.vectoritkPointF2_end)
    rbegin = _swig_new_instance_method(_itkPointPython.vectoritkPointF2_rbegin)
    rend = _swig_new_instance_method(_itkPointPython.vectoritkPointF2_rend)
    clear = _swig_new_instance_method(_itkPointPython.vectoritkPointF2_clear)
    get_allocator = _swig_new_instance_method(_itkPointPython.vectoritkPointF2_get_allocator)
    pop_back = _swig_new_instance_method(_itkPointPython.vectoritkPointF2_pop_back)
    erase = _swig_new_instance_method(_itkPointPython.vectoritkPointF2_erase)

    def __init__(self, *args):
        r"""
        __init__(vectoritkPointF2 self) -> vectoritkPointF2
        __init__(vectoritkPointF2 self, vectoritkPointF2 other) -> vectoritkPointF2
        __init__(vectoritkPointF2 self, std::vector< itkPointF2 >::size_type size) -> vectoritkPointF2
        __init__(vectoritkPointF2 self, std::vector< itkPointF2 >::size_type size, itkPointF2 value) -> vectoritkPointF2
        """
        _itkPointPython.vectoritkPointF2_swiginit(self, _itkPointPython.new_vectoritkPointF2(*args))
    push_back = _swig_new_instance_method(_itkPointPython.vectoritkPointF2_push_back)
    front = _swig_new_instance_method(_itkPointPython.vectoritkPointF2_front)
    back = _swig_new_instance_method(_itkPointPython.vectoritkPointF2_back)
    assign = _swig_new_instance_method(_itkPointPython.vectoritkPointF2_assign)
    resize = _swig_new_instance_method(_itkPointPython.vectoritkPointF2_resize)
    insert = _swig_new_instance_method(_itkPointPython.vectoritkPointF2_insert)
    reserve = _swig_new_instance_method(_itkPointPython.vectoritkPointF2_reserve)
    capacity = _swig_new_instance_method(_itkPointPython.vectoritkPointF2_capacity)
    __swig_destroy__ = _itkPointPython.delete_vectoritkPointF2

# Register vectoritkPointF2 in _itkPointPython:
_itkPointPython.vectoritkPointF2_swigregister(vectoritkPointF2)

class vectoritkPointD2(object):
    r"""Proxy of C++ std::vector< itkPointD2 > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkPointPython.vectoritkPointD2_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkPointPython.vectoritkPointD2___nonzero__)
    __bool__ = _swig_new_instance_method(_itkPointPython.vectoritkPointD2___bool__)
    __len__ = _swig_new_instance_method(_itkPointPython.vectoritkPointD2___len__)
    __getslice__ = _swig_new_instance_method(_itkPointPython.vectoritkPointD2___getslice__)
    __setslice__ = _swig_new_instance_method(_itkPointPython.vectoritkPointD2___setslice__)
    __delslice__ = _swig_new_instance_method(_itkPointPython.vectoritkPointD2___delslice__)
    __delitem__ = _swig_new_instance_method(_itkPointPython.vectoritkPointD2___delitem__)
    __getitem__ = _swig_new_instance_method(_itkPointPython.vectoritkPointD2___getitem__)
    __setitem__ = _swig_new_instance_method(_itkPointPython.vectoritkPointD2___setitem__)
    pop = _swig_new_instance_method(_itkPointPython.vectoritkPointD2_pop)
    append = _swig_new_instance_method(_itkPointPython.vectoritkPointD2_append)
    empty = _swig_new_instance_method(_itkPointPython.vectoritkPointD2_empty)
    size = _swig_new_instance_method(_itkPointPython.vectoritkPointD2_size)
    swap = _swig_new_instance_method(_itkPointPython.vectoritkPointD2_swap)
    begin = _swig_new_instance_method(_itkPointPython.vectoritkPointD2_begin)
    end = _swig_new_instance_method(_itkPointPython.vectoritkPointD2_end)
    rbegin = _swig_new_instance_method(_itkPointPython.vectoritkPointD2_rbegin)
    rend = _swig_new_instance_method(_itkPointPython.vectoritkPointD2_rend)
    clear = _swig_new_instance_method(_itkPointPython.vectoritkPointD2_clear)
    get_allocator = _swig_new_instance_method(_itkPointPython.vectoritkPointD2_get_allocator)
    pop_back = _swig_new_instance_method(_itkPointPython.vectoritkPointD2_pop_back)
    erase = _swig_new_instance_method(_itkPointPython.vectoritkPointD2_erase)

    def __init__(self, *args):
        r"""
        __init__(vectoritkPointD2 self) -> vectoritkPointD2
        __init__(vectoritkPointD2 self, vectoritkPointD2 other) -> vectoritkPointD2
        __init__(vectoritkPointD2 self, std::vector< itkPointD2 >::size_type size) -> vectoritkPointD2
        __init__(vectoritkPointD2 self, std::vector< itkPointD2 >::size_type size, itkPointD2 value) -> vectoritkPointD2
        """
        _itkPointPython.vectoritkPointD2_swiginit(self, _itkPointPython.new_vectoritkPointD2(*args))
    push_back = _swig_new_instance_method(_itkPointPython.vectoritkPointD2_push_back)
    front = _swig_new_instance_method(_itkPointPython.vectoritkPointD2_front)
    back = _swig_new_instance_method(_itkPointPython.vectoritkPointD2_back)
    assign = _swig_new_instance_method(_itkPointPython.vectoritkPointD2_assign)
    resize = _swig_new_instance_method(_itkPointPython.vectoritkPointD2_resize)
    insert = _swig_new_instance_method(_itkPointPython.vectoritkPointD2_insert)
    reserve = _swig_new_instance_method(_itkPointPython.vectoritkPointD2_reserve)
    capacity = _swig_new_instance_method(_itkPointPython.vectoritkPointD2_capacity)
    __swig_destroy__ = _itkPointPython.delete_vectoritkPointD2

# Register vectoritkPointD2 in _itkPointPython:
_itkPointPython.vectoritkPointD2_swigregister(vectoritkPointD2)

class vectoritkPointF3(object):
    r"""Proxy of C++ std::vector< itkPointF3 > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkPointPython.vectoritkPointF3_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkPointPython.vectoritkPointF3___nonzero__)
    __bool__ = _swig_new_instance_method(_itkPointPython.vectoritkPointF3___bool__)
    __len__ = _swig_new_instance_method(_itkPointPython.vectoritkPointF3___len__)
    __getslice__ = _swig_new_instance_method(_itkPointPython.vectoritkPointF3___getslice__)
    __setslice__ = _swig_new_instance_method(_itkPointPython.vectoritkPointF3___setslice__)
    __delslice__ = _swig_new_instance_method(_itkPointPython.vectoritkPointF3___delslice__)
    __delitem__ = _swig_new_instance_method(_itkPointPython.vectoritkPointF3___delitem__)
    __getitem__ = _swig_new_instance_method(_itkPointPython.vectoritkPointF3___getitem__)
    __setitem__ = _swig_new_instance_method(_itkPointPython.vectoritkPointF3___setitem__)
    pop = _swig_new_instance_method(_itkPointPython.vectoritkPointF3_pop)
    append = _swig_new_instance_method(_itkPointPython.vectoritkPointF3_append)
    empty = _swig_new_instance_method(_itkPointPython.vectoritkPointF3_empty)
    size = _swig_new_instance_method(_itkPointPython.vectoritkPointF3_size)
    swap = _swig_new_instance_method(_itkPointPython.vectoritkPointF3_swap)
    begin = _swig_new_instance_method(_itkPointPython.vectoritkPointF3_begin)
    end = _swig_new_instance_method(_itkPointPython.vectoritkPointF3_end)
    rbegin = _swig_new_instance_method(_itkPointPython.vectoritkPointF3_rbegin)
    rend = _swig_new_instance_method(_itkPointPython.vectoritkPointF3_rend)
    clear = _swig_new_instance_method(_itkPointPython.vectoritkPointF3_clear)
    get_allocator = _swig_new_instance_method(_itkPointPython.vectoritkPointF3_get_allocator)
    pop_back = _swig_new_instance_method(_itkPointPython.vectoritkPointF3_pop_back)
    erase = _swig_new_instance_method(_itkPointPython.vectoritkPointF3_erase)

    def __init__(self, *args):
        r"""
        __init__(vectoritkPointF3 self) -> vectoritkPointF3
        __init__(vectoritkPointF3 self, vectoritkPointF3 other) -> vectoritkPointF3
        __init__(vectoritkPointF3 self, std::vector< itkPointF3 >::size_type size) -> vectoritkPointF3
        __init__(vectoritkPointF3 self, std::vector< itkPointF3 >::size_type size, itkPointF3 value) -> vectoritkPointF3
        """
        _itkPointPython.vectoritkPointF3_swiginit(self, _itkPointPython.new_vectoritkPointF3(*args))
    push_back = _swig_new_instance_method(_itkPointPython.vectoritkPointF3_push_back)
    front = _swig_new_instance_method(_itkPointPython.vectoritkPointF3_front)
    back = _swig_new_instance_method(_itkPointPython.vectoritkPointF3_back)
    assign = _swig_new_instance_method(_itkPointPython.vectoritkPointF3_assign)
    resize = _swig_new_instance_method(_itkPointPython.vectoritkPointF3_resize)
    insert = _swig_new_instance_method(_itkPointPython.vectoritkPointF3_insert)
    reserve = _swig_new_instance_method(_itkPointPython.vectoritkPointF3_reserve)
    capacity = _swig_new_instance_method(_itkPointPython.vectoritkPointF3_capacity)
    __swig_destroy__ = _itkPointPython.delete_vectoritkPointF3

# Register vectoritkPointF3 in _itkPointPython:
_itkPointPython.vectoritkPointF3_swigregister(vectoritkPointF3)

class vectoritkPointD3(object):
    r"""Proxy of C++ std::vector< itkPointD3 > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkPointPython.vectoritkPointD3_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkPointPython.vectoritkPointD3___nonzero__)
    __bool__ = _swig_new_instance_method(_itkPointPython.vectoritkPointD3___bool__)
    __len__ = _swig_new_instance_method(_itkPointPython.vectoritkPointD3___len__)
    __getslice__ = _swig_new_instance_method(_itkPointPython.vectoritkPointD3___getslice__)
    __setslice__ = _swig_new_instance_method(_itkPointPython.vectoritkPointD3___setslice__)
    __delslice__ = _swig_new_instance_method(_itkPointPython.vectoritkPointD3___delslice__)
    __delitem__ = _swig_new_instance_method(_itkPointPython.vectoritkPointD3___delitem__)
    __getitem__ = _swig_new_instance_method(_itkPointPython.vectoritkPointD3___getitem__)
    __setitem__ = _swig_new_instance_method(_itkPointPython.vectoritkPointD3___setitem__)
    pop = _swig_new_instance_method(_itkPointPython.vectoritkPointD3_pop)
    append = _swig_new_instance_method(_itkPointPython.vectoritkPointD3_append)
    empty = _swig_new_instance_method(_itkPointPython.vectoritkPointD3_empty)
    size = _swig_new_instance_method(_itkPointPython.vectoritkPointD3_size)
    swap = _swig_new_instance_method(_itkPointPython.vectoritkPointD3_swap)
    begin = _swig_new_instance_method(_itkPointPython.vectoritkPointD3_begin)
    end = _swig_new_instance_method(_itkPointPython.vectoritkPointD3_end)
    rbegin = _swig_new_instance_method(_itkPointPython.vectoritkPointD3_rbegin)
    rend = _swig_new_instance_method(_itkPointPython.vectoritkPointD3_rend)
    clear = _swig_new_instance_method(_itkPointPython.vectoritkPointD3_clear)
    get_allocator = _swig_new_instance_method(_itkPointPython.vectoritkPointD3_get_allocator)
    pop_back = _swig_new_instance_method(_itkPointPython.vectoritkPointD3_pop_back)
    erase = _swig_new_instance_method(_itkPointPython.vectoritkPointD3_erase)

    def __init__(self, *args):
        r"""
        __init__(vectoritkPointD3 self) -> vectoritkPointD3
        __init__(vectoritkPointD3 self, vectoritkPointD3 other) -> vectoritkPointD3
        __init__(vectoritkPointD3 self, std::vector< itkPointD3 >::size_type size) -> vectoritkPointD3
        __init__(vectoritkPointD3 self, std::vector< itkPointD3 >::size_type size, itkPointD3 value) -> vectoritkPointD3
        """
        _itkPointPython.vectoritkPointD3_swiginit(self, _itkPointPython.new_vectoritkPointD3(*args))
    push_back = _swig_new_instance_method(_itkPointPython.vectoritkPointD3_push_back)
    front = _swig_new_instance_method(_itkPointPython.vectoritkPointD3_front)
    back = _swig_new_instance_method(_itkPointPython.vectoritkPointD3_back)
    assign = _swig_new_instance_method(_itkPointPython.vectoritkPointD3_assign)
    resize = _swig_new_instance_method(_itkPointPython.vectoritkPointD3_resize)
    insert = _swig_new_instance_method(_itkPointPython.vectoritkPointD3_insert)
    reserve = _swig_new_instance_method(_itkPointPython.vectoritkPointD3_reserve)
    capacity = _swig_new_instance_method(_itkPointPython.vectoritkPointD3_capacity)
    __swig_destroy__ = _itkPointPython.delete_vectoritkPointD3

# Register vectoritkPointD3 in _itkPointPython:
_itkPointPython.vectoritkPointD3_swigregister(vectoritkPointD3)

class vectoritkPointF4(object):
    r"""Proxy of C++ std::vector< itkPointF4 > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkPointPython.vectoritkPointF4_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkPointPython.vectoritkPointF4___nonzero__)
    __bool__ = _swig_new_instance_method(_itkPointPython.vectoritkPointF4___bool__)
    __len__ = _swig_new_instance_method(_itkPointPython.vectoritkPointF4___len__)
    __getslice__ = _swig_new_instance_method(_itkPointPython.vectoritkPointF4___getslice__)
    __setslice__ = _swig_new_instance_method(_itkPointPython.vectoritkPointF4___setslice__)
    __delslice__ = _swig_new_instance_method(_itkPointPython.vectoritkPointF4___delslice__)
    __delitem__ = _swig_new_instance_method(_itkPointPython.vectoritkPointF4___delitem__)
    __getitem__ = _swig_new_instance_method(_itkPointPython.vectoritkPointF4___getitem__)
    __setitem__ = _swig_new_instance_method(_itkPointPython.vectoritkPointF4___setitem__)
    pop = _swig_new_instance_method(_itkPointPython.vectoritkPointF4_pop)
    append = _swig_new_instance_method(_itkPointPython.vectoritkPointF4_append)
    empty = _swig_new_instance_method(_itkPointPython.vectoritkPointF4_empty)
    size = _swig_new_instance_method(_itkPointPython.vectoritkPointF4_size)
    swap = _swig_new_instance_method(_itkPointPython.vectoritkPointF4_swap)
    begin = _swig_new_instance_method(_itkPointPython.vectoritkPointF4_begin)
    end = _swig_new_instance_method(_itkPointPython.vectoritkPointF4_end)
    rbegin = _swig_new_instance_method(_itkPointPython.vectoritkPointF4_rbegin)
    rend = _swig_new_instance_method(_itkPointPython.vectoritkPointF4_rend)
    clear = _swig_new_instance_method(_itkPointPython.vectoritkPointF4_clear)
    get_allocator = _swig_new_instance_method(_itkPointPython.vectoritkPointF4_get_allocator)
    pop_back = _swig_new_instance_method(_itkPointPython.vectoritkPointF4_pop_back)
    erase = _swig_new_instance_method(_itkPointPython.vectoritkPointF4_erase)

    def __init__(self, *args):
        r"""
        __init__(vectoritkPointF4 self) -> vectoritkPointF4
        __init__(vectoritkPointF4 self, vectoritkPointF4 other) -> vectoritkPointF4
        __init__(vectoritkPointF4 self, std::vector< itkPointF4 >::size_type size) -> vectoritkPointF4
        __init__(vectoritkPointF4 self, std::vector< itkPointF4 >::size_type size, itkPointF4 value) -> vectoritkPointF4
        """
        _itkPointPython.vectoritkPointF4_swiginit(self, _itkPointPython.new_vectoritkPointF4(*args))
    push_back = _swig_new_instance_method(_itkPointPython.vectoritkPointF4_push_back)
    front = _swig_new_instance_method(_itkPointPython.vectoritkPointF4_front)
    back = _swig_new_instance_method(_itkPointPython.vectoritkPointF4_back)
    assign = _swig_new_instance_method(_itkPointPython.vectoritkPointF4_assign)
    resize = _swig_new_instance_method(_itkPointPython.vectoritkPointF4_resize)
    insert = _swig_new_instance_method(_itkPointPython.vectoritkPointF4_insert)
    reserve = _swig_new_instance_method(_itkPointPython.vectoritkPointF4_reserve)
    capacity = _swig_new_instance_method(_itkPointPython.vectoritkPointF4_capacity)
    __swig_destroy__ = _itkPointPython.delete_vectoritkPointF4

# Register vectoritkPointF4 in _itkPointPython:
_itkPointPython.vectoritkPointF4_swigregister(vectoritkPointF4)

class vectoritkPointD4(object):
    r"""Proxy of C++ std::vector< itkPointD4 > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkPointPython.vectoritkPointD4_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkPointPython.vectoritkPointD4___nonzero__)
    __bool__ = _swig_new_instance_method(_itkPointPython.vectoritkPointD4___bool__)
    __len__ = _swig_new_instance_method(_itkPointPython.vectoritkPointD4___len__)
    __getslice__ = _swig_new_instance_method(_itkPointPython.vectoritkPointD4___getslice__)
    __setslice__ = _swig_new_instance_method(_itkPointPython.vectoritkPointD4___setslice__)
    __delslice__ = _swig_new_instance_method(_itkPointPython.vectoritkPointD4___delslice__)
    __delitem__ = _swig_new_instance_method(_itkPointPython.vectoritkPointD4___delitem__)
    __getitem__ = _swig_new_instance_method(_itkPointPython.vectoritkPointD4___getitem__)
    __setitem__ = _swig_new_instance_method(_itkPointPython.vectoritkPointD4___setitem__)
    pop = _swig_new_instance_method(_itkPointPython.vectoritkPointD4_pop)
    append = _swig_new_instance_method(_itkPointPython.vectoritkPointD4_append)
    empty = _swig_new_instance_method(_itkPointPython.vectoritkPointD4_empty)
    size = _swig_new_instance_method(_itkPointPython.vectoritkPointD4_size)
    swap = _swig_new_instance_method(_itkPointPython.vectoritkPointD4_swap)
    begin = _swig_new_instance_method(_itkPointPython.vectoritkPointD4_begin)
    end = _swig_new_instance_method(_itkPointPython.vectoritkPointD4_end)
    rbegin = _swig_new_instance_method(_itkPointPython.vectoritkPointD4_rbegin)
    rend = _swig_new_instance_method(_itkPointPython.vectoritkPointD4_rend)
    clear = _swig_new_instance_method(_itkPointPython.vectoritkPointD4_clear)
    get_allocator = _swig_new_instance_method(_itkPointPython.vectoritkPointD4_get_allocator)
    pop_back = _swig_new_instance_method(_itkPointPython.vectoritkPointD4_pop_back)
    erase = _swig_new_instance_method(_itkPointPython.vectoritkPointD4_erase)

    def __init__(self, *args):
        r"""
        __init__(vectoritkPointD4 self) -> vectoritkPointD4
        __init__(vectoritkPointD4 self, vectoritkPointD4 other) -> vectoritkPointD4
        __init__(vectoritkPointD4 self, std::vector< itkPointD4 >::size_type size) -> vectoritkPointD4
        __init__(vectoritkPointD4 self, std::vector< itkPointD4 >::size_type size, itkPointD4 value) -> vectoritkPointD4
        """
        _itkPointPython.vectoritkPointD4_swiginit(self, _itkPointPython.new_vectoritkPointD4(*args))
    push_back = _swig_new_instance_method(_itkPointPython.vectoritkPointD4_push_back)
    front = _swig_new_instance_method(_itkPointPython.vectoritkPointD4_front)
    back = _swig_new_instance_method(_itkPointPython.vectoritkPointD4_back)
    assign = _swig_new_instance_method(_itkPointPython.vectoritkPointD4_assign)
    resize = _swig_new_instance_method(_itkPointPython.vectoritkPointD4_resize)
    insert = _swig_new_instance_method(_itkPointPython.vectoritkPointD4_insert)
    reserve = _swig_new_instance_method(_itkPointPython.vectoritkPointD4_reserve)
    capacity = _swig_new_instance_method(_itkPointPython.vectoritkPointD4_capacity)
    __swig_destroy__ = _itkPointPython.delete_vectoritkPointD4

# Register vectoritkPointD4 in _itkPointPython:
_itkPointPython.vectoritkPointD4_swigregister(vectoritkPointD4)

class itkPointD2(itkFixedArrayPython.itkFixedArrayD2):
    r"""Proxy of C++ itkPointD2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    GetPointDimension = _swig_new_static_method(_itkPointPython.itkPointD2_GetPointDimension)
    __swig_destroy__ = _itkPointPython.delete_itkPointD2

    def __init__(self, *args):
        r"""
        __init__(itkPointD2 self) -> itkPointD2
        __init__(itkPointD2 self, itkPointD2 arg0) -> itkPointD2
        __init__(itkPointD2 self, double const * r) -> itkPointD2
        __init__(itkPointD2 self, double const & v) -> itkPointD2
        __init__(itkPointD2 self, std::array< double,2 > const & stdArray) -> itkPointD2
        """
        _itkPointPython.itkPointD2_swiginit(self, _itkPointPython.new_itkPointD2(*args))
    __eq__ = _swig_new_instance_method(_itkPointPython.itkPointD2___eq__)
    __ne__ = _swig_new_instance_method(_itkPointPython.itkPointD2___ne__)
    __iadd__ = _swig_new_instance_method(_itkPointPython.itkPointD2___iadd__)
    __isub__ = _swig_new_instance_method(_itkPointPython.itkPointD2___isub__)
    __add__ = _swig_new_instance_method(_itkPointPython.itkPointD2___add__)
    __sub__ = _swig_new_instance_method(_itkPointPython.itkPointD2___sub__)
    GetVectorFromOrigin = _swig_new_instance_method(_itkPointPython.itkPointD2_GetVectorFromOrigin)
    GetVnlVector = _swig_new_instance_method(_itkPointPython.itkPointD2_GetVnlVector)
    SetToMidPoint = _swig_new_instance_method(_itkPointPython.itkPointD2_SetToMidPoint)
    SetToBarycentricCombination = _swig_new_instance_method(_itkPointPython.itkPointD2_SetToBarycentricCombination)
    __getitem__ = _swig_new_instance_method(_itkPointPython.itkPointD2___getitem__)
    __setitem__ = _swig_new_instance_method(_itkPointPython.itkPointD2___setitem__)
    __len__ = _swig_new_static_method(_itkPointPython.itkPointD2___len__)
    __repr__ = _swig_new_instance_method(_itkPointPython.itkPointD2___repr__)

# Register itkPointD2 in _itkPointPython:
_itkPointPython.itkPointD2_swigregister(itkPointD2)
itkPointD2_GetPointDimension = _itkPointPython.itkPointD2_GetPointDimension
itkPointD2___len__ = _itkPointPython.itkPointD2___len__

class itkPointD3(itkFixedArrayPython.itkFixedArrayD3):
    r"""Proxy of C++ itkPointD3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    GetPointDimension = _swig_new_static_method(_itkPointPython.itkPointD3_GetPointDimension)
    __swig_destroy__ = _itkPointPython.delete_itkPointD3

    def __init__(self, *args):
        r"""
        __init__(itkPointD3 self) -> itkPointD3
        __init__(itkPointD3 self, itkPointD3 arg0) -> itkPointD3
        __init__(itkPointD3 self, double const * r) -> itkPointD3
        __init__(itkPointD3 self, double const & v) -> itkPointD3
        __init__(itkPointD3 self, std::array< double,3 > const & stdArray) -> itkPointD3
        """
        _itkPointPython.itkPointD3_swiginit(self, _itkPointPython.new_itkPointD3(*args))
    __eq__ = _swig_new_instance_method(_itkPointPython.itkPointD3___eq__)
    __ne__ = _swig_new_instance_method(_itkPointPython.itkPointD3___ne__)
    __iadd__ = _swig_new_instance_method(_itkPointPython.itkPointD3___iadd__)
    __isub__ = _swig_new_instance_method(_itkPointPython.itkPointD3___isub__)
    __add__ = _swig_new_instance_method(_itkPointPython.itkPointD3___add__)
    __sub__ = _swig_new_instance_method(_itkPointPython.itkPointD3___sub__)
    GetVectorFromOrigin = _swig_new_instance_method(_itkPointPython.itkPointD3_GetVectorFromOrigin)
    GetVnlVector = _swig_new_instance_method(_itkPointPython.itkPointD3_GetVnlVector)
    SetToMidPoint = _swig_new_instance_method(_itkPointPython.itkPointD3_SetToMidPoint)
    SetToBarycentricCombination = _swig_new_instance_method(_itkPointPython.itkPointD3_SetToBarycentricCombination)
    __getitem__ = _swig_new_instance_method(_itkPointPython.itkPointD3___getitem__)
    __setitem__ = _swig_new_instance_method(_itkPointPython.itkPointD3___setitem__)
    __len__ = _swig_new_static_method(_itkPointPython.itkPointD3___len__)
    __repr__ = _swig_new_instance_method(_itkPointPython.itkPointD3___repr__)

# Register itkPointD3 in _itkPointPython:
_itkPointPython.itkPointD3_swigregister(itkPointD3)
itkPointD3_GetPointDimension = _itkPointPython.itkPointD3_GetPointDimension
itkPointD3___len__ = _itkPointPython.itkPointD3___len__

class itkPointD4(itkFixedArrayPython.itkFixedArrayD4):
    r"""Proxy of C++ itkPointD4 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    GetPointDimension = _swig_new_static_method(_itkPointPython.itkPointD4_GetPointDimension)
    __swig_destroy__ = _itkPointPython.delete_itkPointD4

    def __init__(self, *args):
        r"""
        __init__(itkPointD4 self) -> itkPointD4
        __init__(itkPointD4 self, itkPointD4 arg0) -> itkPointD4
        __init__(itkPointD4 self, double const * r) -> itkPointD4
        __init__(itkPointD4 self, double const & v) -> itkPointD4
        __init__(itkPointD4 self, std::array< double,4 > const & stdArray) -> itkPointD4
        """
        _itkPointPython.itkPointD4_swiginit(self, _itkPointPython.new_itkPointD4(*args))
    __eq__ = _swig_new_instance_method(_itkPointPython.itkPointD4___eq__)
    __ne__ = _swig_new_instance_method(_itkPointPython.itkPointD4___ne__)
    __iadd__ = _swig_new_instance_method(_itkPointPython.itkPointD4___iadd__)
    __isub__ = _swig_new_instance_method(_itkPointPython.itkPointD4___isub__)
    __add__ = _swig_new_instance_method(_itkPointPython.itkPointD4___add__)
    __sub__ = _swig_new_instance_method(_itkPointPython.itkPointD4___sub__)
    GetVectorFromOrigin = _swig_new_instance_method(_itkPointPython.itkPointD4_GetVectorFromOrigin)
    GetVnlVector = _swig_new_instance_method(_itkPointPython.itkPointD4_GetVnlVector)
    SetToMidPoint = _swig_new_instance_method(_itkPointPython.itkPointD4_SetToMidPoint)
    SetToBarycentricCombination = _swig_new_instance_method(_itkPointPython.itkPointD4_SetToBarycentricCombination)
    __getitem__ = _swig_new_instance_method(_itkPointPython.itkPointD4___getitem__)
    __setitem__ = _swig_new_instance_method(_itkPointPython.itkPointD4___setitem__)
    __len__ = _swig_new_static_method(_itkPointPython.itkPointD4___len__)
    __repr__ = _swig_new_instance_method(_itkPointPython.itkPointD4___repr__)

# Register itkPointD4 in _itkPointPython:
_itkPointPython.itkPointD4_swigregister(itkPointD4)
itkPointD4_GetPointDimension = _itkPointPython.itkPointD4_GetPointDimension
itkPointD4___len__ = _itkPointPython.itkPointD4___len__

class itkPointF2(itkFixedArrayPython.itkFixedArrayF2):
    r"""Proxy of C++ itkPointF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    GetPointDimension = _swig_new_static_method(_itkPointPython.itkPointF2_GetPointDimension)
    __swig_destroy__ = _itkPointPython.delete_itkPointF2

    def __init__(self, *args):
        r"""
        __init__(itkPointF2 self) -> itkPointF2
        __init__(itkPointF2 self, itkPointF2 arg0) -> itkPointF2
        __init__(itkPointF2 self, float const * r) -> itkPointF2
        __init__(itkPointF2 self, float const & v) -> itkPointF2
        __init__(itkPointF2 self, std::array< float,2 > const & stdArray) -> itkPointF2
        """
        _itkPointPython.itkPointF2_swiginit(self, _itkPointPython.new_itkPointF2(*args))
    __eq__ = _swig_new_instance_method(_itkPointPython.itkPointF2___eq__)
    __ne__ = _swig_new_instance_method(_itkPointPython.itkPointF2___ne__)
    __iadd__ = _swig_new_instance_method(_itkPointPython.itkPointF2___iadd__)
    __isub__ = _swig_new_instance_method(_itkPointPython.itkPointF2___isub__)
    __add__ = _swig_new_instance_method(_itkPointPython.itkPointF2___add__)
    __sub__ = _swig_new_instance_method(_itkPointPython.itkPointF2___sub__)
    GetVectorFromOrigin = _swig_new_instance_method(_itkPointPython.itkPointF2_GetVectorFromOrigin)
    GetVnlVector = _swig_new_instance_method(_itkPointPython.itkPointF2_GetVnlVector)
    SetToMidPoint = _swig_new_instance_method(_itkPointPython.itkPointF2_SetToMidPoint)
    SetToBarycentricCombination = _swig_new_instance_method(_itkPointPython.itkPointF2_SetToBarycentricCombination)
    __getitem__ = _swig_new_instance_method(_itkPointPython.itkPointF2___getitem__)
    __setitem__ = _swig_new_instance_method(_itkPointPython.itkPointF2___setitem__)
    __len__ = _swig_new_static_method(_itkPointPython.itkPointF2___len__)
    __repr__ = _swig_new_instance_method(_itkPointPython.itkPointF2___repr__)

# Register itkPointF2 in _itkPointPython:
_itkPointPython.itkPointF2_swigregister(itkPointF2)
itkPointF2_GetPointDimension = _itkPointPython.itkPointF2_GetPointDimension
itkPointF2___len__ = _itkPointPython.itkPointF2___len__

class itkPointF3(itkFixedArrayPython.itkFixedArrayF3):
    r"""Proxy of C++ itkPointF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    GetPointDimension = _swig_new_static_method(_itkPointPython.itkPointF3_GetPointDimension)
    __swig_destroy__ = _itkPointPython.delete_itkPointF3

    def __init__(self, *args):
        r"""
        __init__(itkPointF3 self) -> itkPointF3
        __init__(itkPointF3 self, itkPointF3 arg0) -> itkPointF3
        __init__(itkPointF3 self, float const * r) -> itkPointF3
        __init__(itkPointF3 self, float const & v) -> itkPointF3
        __init__(itkPointF3 self, std::array< float,3 > const & stdArray) -> itkPointF3
        """
        _itkPointPython.itkPointF3_swiginit(self, _itkPointPython.new_itkPointF3(*args))
    __eq__ = _swig_new_instance_method(_itkPointPython.itkPointF3___eq__)
    __ne__ = _swig_new_instance_method(_itkPointPython.itkPointF3___ne__)
    __iadd__ = _swig_new_instance_method(_itkPointPython.itkPointF3___iadd__)
    __isub__ = _swig_new_instance_method(_itkPointPython.itkPointF3___isub__)
    __add__ = _swig_new_instance_method(_itkPointPython.itkPointF3___add__)
    __sub__ = _swig_new_instance_method(_itkPointPython.itkPointF3___sub__)
    GetVectorFromOrigin = _swig_new_instance_method(_itkPointPython.itkPointF3_GetVectorFromOrigin)
    GetVnlVector = _swig_new_instance_method(_itkPointPython.itkPointF3_GetVnlVector)
    SetToMidPoint = _swig_new_instance_method(_itkPointPython.itkPointF3_SetToMidPoint)
    SetToBarycentricCombination = _swig_new_instance_method(_itkPointPython.itkPointF3_SetToBarycentricCombination)
    __getitem__ = _swig_new_instance_method(_itkPointPython.itkPointF3___getitem__)
    __setitem__ = _swig_new_instance_method(_itkPointPython.itkPointF3___setitem__)
    __len__ = _swig_new_static_method(_itkPointPython.itkPointF3___len__)
    __repr__ = _swig_new_instance_method(_itkPointPython.itkPointF3___repr__)

# Register itkPointF3 in _itkPointPython:
_itkPointPython.itkPointF3_swigregister(itkPointF3)
itkPointF3_GetPointDimension = _itkPointPython.itkPointF3_GetPointDimension
itkPointF3___len__ = _itkPointPython.itkPointF3___len__

class itkPointF4(itkFixedArrayPython.itkFixedArrayF4):
    r"""Proxy of C++ itkPointF4 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    GetPointDimension = _swig_new_static_method(_itkPointPython.itkPointF4_GetPointDimension)
    __swig_destroy__ = _itkPointPython.delete_itkPointF4

    def __init__(self, *args):
        r"""
        __init__(itkPointF4 self) -> itkPointF4
        __init__(itkPointF4 self, itkPointF4 arg0) -> itkPointF4
        __init__(itkPointF4 self, float const * r) -> itkPointF4
        __init__(itkPointF4 self, float const & v) -> itkPointF4
        __init__(itkPointF4 self, std::array< float,4 > const & stdArray) -> itkPointF4
        """
        _itkPointPython.itkPointF4_swiginit(self, _itkPointPython.new_itkPointF4(*args))
    __eq__ = _swig_new_instance_method(_itkPointPython.itkPointF4___eq__)
    __ne__ = _swig_new_instance_method(_itkPointPython.itkPointF4___ne__)
    __iadd__ = _swig_new_instance_method(_itkPointPython.itkPointF4___iadd__)
    __isub__ = _swig_new_instance_method(_itkPointPython.itkPointF4___isub__)
    __add__ = _swig_new_instance_method(_itkPointPython.itkPointF4___add__)
    __sub__ = _swig_new_instance_method(_itkPointPython.itkPointF4___sub__)
    GetVectorFromOrigin = _swig_new_instance_method(_itkPointPython.itkPointF4_GetVectorFromOrigin)
    GetVnlVector = _swig_new_instance_method(_itkPointPython.itkPointF4_GetVnlVector)
    SetToMidPoint = _swig_new_instance_method(_itkPointPython.itkPointF4_SetToMidPoint)
    SetToBarycentricCombination = _swig_new_instance_method(_itkPointPython.itkPointF4_SetToBarycentricCombination)
    __getitem__ = _swig_new_instance_method(_itkPointPython.itkPointF4___getitem__)
    __setitem__ = _swig_new_instance_method(_itkPointPython.itkPointF4___setitem__)
    __len__ = _swig_new_static_method(_itkPointPython.itkPointF4___len__)
    __repr__ = _swig_new_instance_method(_itkPointPython.itkPointF4___repr__)

# Register itkPointF4 in _itkPointPython:
_itkPointPython.itkPointF4_swigregister(itkPointF4)
itkPointF4_GetPointDimension = _itkPointPython.itkPointF4_GetPointDimension
itkPointF4___len__ = _itkPointPython.itkPointF4___len__



