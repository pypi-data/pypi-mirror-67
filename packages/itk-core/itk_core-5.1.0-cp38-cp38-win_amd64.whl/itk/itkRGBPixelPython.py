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
    from . import _itkRGBPixelPython
else:
    import _itkRGBPixelPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkRGBPixelPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkRGBPixelPython.SWIG_PyStaticMethod_New

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
class itkRGBPixelD(itkFixedArrayPython.itkFixedArrayD3):
    r"""Proxy of C++ itkRGBPixelD class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __swig_destroy__ = _itkRGBPixelPython.delete_itkRGBPixelD

    def __init__(self, *args):
        r"""
        __init__(itkRGBPixelD self) -> itkRGBPixelD
        __init__(itkRGBPixelD self, itkRGBPixelD arg0) -> itkRGBPixelD
        __init__(itkRGBPixelD self, double const & r) -> itkRGBPixelD
        __init__(itkRGBPixelD self, double const * r) -> itkRGBPixelD
        """
        _itkRGBPixelPython.itkRGBPixelD_swiginit(self, _itkRGBPixelPython.new_itkRGBPixelD(*args))
    __add__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelD___add__)
    __sub__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelD___sub__)
    __mul__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelD___mul__)

    def __truediv__(self, *args):
        return _itkRGBPixelPython.itkRGBPixelD___truediv__(self, *args)
    __div__ = __truediv__


    __iadd__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelD___iadd__)
    __isub__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelD___isub__)
    __imul__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelD___imul__)

    def __itruediv__(self, *args):
        return _itkRGBPixelPython.itkRGBPixelD___itruediv__(self, *args)
    __idiv__ = __itruediv__


    __lt__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelD___lt__)
    __eq__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelD___eq__)
    GetNumberOfComponents = _swig_new_static_method(_itkRGBPixelPython.itkRGBPixelD_GetNumberOfComponents)
    GetNthComponent = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelD_GetNthComponent)
    GetScalarValue = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelD_GetScalarValue)
    SetNthComponent = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelD_SetNthComponent)
    SetRed = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelD_SetRed)
    SetGreen = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelD_SetGreen)
    SetBlue = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelD_SetBlue)
    Set = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelD_Set)
    GetRed = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelD_GetRed)
    GetGreen = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelD_GetGreen)
    GetBlue = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelD_GetBlue)
    GetLuminance = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelD_GetLuminance)
    __getitem__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelD___getitem__)
    __setitem__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelD___setitem__)
    __len__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelD___len__)
    __repr__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelD___repr__)

# Register itkRGBPixelD in _itkRGBPixelPython:
_itkRGBPixelPython.itkRGBPixelD_swigregister(itkRGBPixelD)
itkRGBPixelD_GetNumberOfComponents = _itkRGBPixelPython.itkRGBPixelD_GetNumberOfComponents

class itkRGBPixelF(itkFixedArrayPython.itkFixedArrayF3):
    r"""Proxy of C++ itkRGBPixelF class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __swig_destroy__ = _itkRGBPixelPython.delete_itkRGBPixelF

    def __init__(self, *args):
        r"""
        __init__(itkRGBPixelF self) -> itkRGBPixelF
        __init__(itkRGBPixelF self, itkRGBPixelF arg0) -> itkRGBPixelF
        __init__(itkRGBPixelF self, float const & r) -> itkRGBPixelF
        __init__(itkRGBPixelF self, float const * r) -> itkRGBPixelF
        """
        _itkRGBPixelPython.itkRGBPixelF_swiginit(self, _itkRGBPixelPython.new_itkRGBPixelF(*args))
    __add__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelF___add__)
    __sub__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelF___sub__)
    __mul__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelF___mul__)

    def __truediv__(self, *args):
        return _itkRGBPixelPython.itkRGBPixelF___truediv__(self, *args)
    __div__ = __truediv__


    __iadd__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelF___iadd__)
    __isub__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelF___isub__)
    __imul__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelF___imul__)

    def __itruediv__(self, *args):
        return _itkRGBPixelPython.itkRGBPixelF___itruediv__(self, *args)
    __idiv__ = __itruediv__


    __lt__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelF___lt__)
    __eq__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelF___eq__)
    GetNumberOfComponents = _swig_new_static_method(_itkRGBPixelPython.itkRGBPixelF_GetNumberOfComponents)
    GetNthComponent = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelF_GetNthComponent)
    GetScalarValue = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelF_GetScalarValue)
    SetNthComponent = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelF_SetNthComponent)
    SetRed = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelF_SetRed)
    SetGreen = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelF_SetGreen)
    SetBlue = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelF_SetBlue)
    Set = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelF_Set)
    GetRed = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelF_GetRed)
    GetGreen = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelF_GetGreen)
    GetBlue = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelF_GetBlue)
    GetLuminance = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelF_GetLuminance)
    __getitem__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelF___getitem__)
    __setitem__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelF___setitem__)
    __len__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelF___len__)
    __repr__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelF___repr__)

# Register itkRGBPixelF in _itkRGBPixelPython:
_itkRGBPixelPython.itkRGBPixelF_swigregister(itkRGBPixelF)
itkRGBPixelF_GetNumberOfComponents = _itkRGBPixelPython.itkRGBPixelF_GetNumberOfComponents

class itkRGBPixelUC(itkFixedArrayPython.itkFixedArrayUC3):
    r"""Proxy of C++ itkRGBPixelUC class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __swig_destroy__ = _itkRGBPixelPython.delete_itkRGBPixelUC

    def __init__(self, *args):
        r"""
        __init__(itkRGBPixelUC self) -> itkRGBPixelUC
        __init__(itkRGBPixelUC self, itkRGBPixelUC arg0) -> itkRGBPixelUC
        __init__(itkRGBPixelUC self, unsigned char const & r) -> itkRGBPixelUC
        __init__(itkRGBPixelUC self, unsigned char const * r) -> itkRGBPixelUC
        """
        _itkRGBPixelPython.itkRGBPixelUC_swiginit(self, _itkRGBPixelPython.new_itkRGBPixelUC(*args))
    __add__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUC___add__)
    __sub__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUC___sub__)
    __mul__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUC___mul__)

    def __truediv__(self, *args):
        return _itkRGBPixelPython.itkRGBPixelUC___truediv__(self, *args)
    __div__ = __truediv__


    __iadd__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUC___iadd__)
    __isub__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUC___isub__)
    __imul__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUC___imul__)

    def __itruediv__(self, *args):
        return _itkRGBPixelPython.itkRGBPixelUC___itruediv__(self, *args)
    __idiv__ = __itruediv__


    __lt__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUC___lt__)
    __eq__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUC___eq__)
    GetNumberOfComponents = _swig_new_static_method(_itkRGBPixelPython.itkRGBPixelUC_GetNumberOfComponents)
    GetNthComponent = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUC_GetNthComponent)
    GetScalarValue = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUC_GetScalarValue)
    SetNthComponent = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUC_SetNthComponent)
    SetRed = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUC_SetRed)
    SetGreen = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUC_SetGreen)
    SetBlue = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUC_SetBlue)
    Set = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUC_Set)
    GetRed = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUC_GetRed)
    GetGreen = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUC_GetGreen)
    GetBlue = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUC_GetBlue)
    GetLuminance = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUC_GetLuminance)
    __getitem__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUC___getitem__)
    __setitem__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUC___setitem__)
    __len__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUC___len__)
    __repr__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUC___repr__)

# Register itkRGBPixelUC in _itkRGBPixelPython:
_itkRGBPixelPython.itkRGBPixelUC_swigregister(itkRGBPixelUC)
itkRGBPixelUC_GetNumberOfComponents = _itkRGBPixelPython.itkRGBPixelUC_GetNumberOfComponents

class itkRGBPixelUS(itkFixedArrayPython.itkFixedArrayUS3):
    r"""Proxy of C++ itkRGBPixelUS class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __swig_destroy__ = _itkRGBPixelPython.delete_itkRGBPixelUS

    def __init__(self, *args):
        r"""
        __init__(itkRGBPixelUS self) -> itkRGBPixelUS
        __init__(itkRGBPixelUS self, itkRGBPixelUS arg0) -> itkRGBPixelUS
        __init__(itkRGBPixelUS self, unsigned short const & r) -> itkRGBPixelUS
        __init__(itkRGBPixelUS self, unsigned short const * r) -> itkRGBPixelUS
        """
        _itkRGBPixelPython.itkRGBPixelUS_swiginit(self, _itkRGBPixelPython.new_itkRGBPixelUS(*args))
    __add__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUS___add__)
    __sub__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUS___sub__)
    __mul__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUS___mul__)

    def __truediv__(self, *args):
        return _itkRGBPixelPython.itkRGBPixelUS___truediv__(self, *args)
    __div__ = __truediv__


    __iadd__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUS___iadd__)
    __isub__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUS___isub__)
    __imul__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUS___imul__)

    def __itruediv__(self, *args):
        return _itkRGBPixelPython.itkRGBPixelUS___itruediv__(self, *args)
    __idiv__ = __itruediv__


    __lt__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUS___lt__)
    __eq__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUS___eq__)
    GetNumberOfComponents = _swig_new_static_method(_itkRGBPixelPython.itkRGBPixelUS_GetNumberOfComponents)
    GetNthComponent = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUS_GetNthComponent)
    GetScalarValue = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUS_GetScalarValue)
    SetNthComponent = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUS_SetNthComponent)
    SetRed = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUS_SetRed)
    SetGreen = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUS_SetGreen)
    SetBlue = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUS_SetBlue)
    Set = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUS_Set)
    GetRed = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUS_GetRed)
    GetGreen = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUS_GetGreen)
    GetBlue = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUS_GetBlue)
    GetLuminance = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUS_GetLuminance)
    __getitem__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUS___getitem__)
    __setitem__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUS___setitem__)
    __len__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUS___len__)
    __repr__ = _swig_new_instance_method(_itkRGBPixelPython.itkRGBPixelUS___repr__)

# Register itkRGBPixelUS in _itkRGBPixelPython:
_itkRGBPixelPython.itkRGBPixelUS_swigregister(itkRGBPixelUS)
itkRGBPixelUS_GetNumberOfComponents = _itkRGBPixelPython.itkRGBPixelUS_GetNumberOfComponents



