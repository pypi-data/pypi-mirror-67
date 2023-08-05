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
    from . import _itkRGBAPixelPython
else:
    import _itkRGBAPixelPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkRGBAPixelPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkRGBAPixelPython.SWIG_PyStaticMethod_New

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
class itkRGBAPixelD(itkFixedArrayPython.itkFixedArrayD4):
    r"""Proxy of C++ itkRGBAPixelD class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __swig_destroy__ = _itkRGBAPixelPython.delete_itkRGBAPixelD

    def __init__(self, *args):
        r"""
        __init__(itkRGBAPixelD self) -> itkRGBAPixelD
        __init__(itkRGBAPixelD self, itkRGBAPixelD arg0) -> itkRGBAPixelD
        __init__(itkRGBAPixelD self, double const * r) -> itkRGBAPixelD
        __init__(itkRGBAPixelD self, double const & r) -> itkRGBAPixelD
        """
        _itkRGBAPixelPython.itkRGBAPixelD_swiginit(self, _itkRGBAPixelPython.new_itkRGBAPixelD(*args))
    __add__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelD___add__)
    __sub__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelD___sub__)
    __mul__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelD___mul__)

    def __truediv__(self, *args):
        return _itkRGBAPixelPython.itkRGBAPixelD___truediv__(self, *args)
    __div__ = __truediv__


    __iadd__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelD___iadd__)
    __isub__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelD___isub__)
    __imul__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelD___imul__)

    def __itruediv__(self, *args):
        return _itkRGBAPixelPython.itkRGBAPixelD___itruediv__(self, *args)
    __idiv__ = __itruediv__


    __lt__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelD___lt__)
    __eq__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelD___eq__)
    GetNumberOfComponents = _swig_new_static_method(_itkRGBAPixelPython.itkRGBAPixelD_GetNumberOfComponents)
    GetNthComponent = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelD_GetNthComponent)
    GetScalarValue = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelD_GetScalarValue)
    SetNthComponent = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelD_SetNthComponent)
    SetRed = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelD_SetRed)
    SetGreen = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelD_SetGreen)
    SetBlue = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelD_SetBlue)
    SetAlpha = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelD_SetAlpha)
    Set = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelD_Set)
    GetRed = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelD_GetRed)
    GetGreen = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelD_GetGreen)
    GetBlue = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelD_GetBlue)
    GetAlpha = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelD_GetAlpha)
    GetLuminance = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelD_GetLuminance)
    __getitem__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelD___getitem__)
    __setitem__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelD___setitem__)
    __len__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelD___len__)
    __repr__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelD___repr__)

# Register itkRGBAPixelD in _itkRGBAPixelPython:
_itkRGBAPixelPython.itkRGBAPixelD_swigregister(itkRGBAPixelD)
itkRGBAPixelD_GetNumberOfComponents = _itkRGBAPixelPython.itkRGBAPixelD_GetNumberOfComponents

class itkRGBAPixelF(itkFixedArrayPython.itkFixedArrayF4):
    r"""Proxy of C++ itkRGBAPixelF class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __swig_destroy__ = _itkRGBAPixelPython.delete_itkRGBAPixelF

    def __init__(self, *args):
        r"""
        __init__(itkRGBAPixelF self) -> itkRGBAPixelF
        __init__(itkRGBAPixelF self, itkRGBAPixelF arg0) -> itkRGBAPixelF
        __init__(itkRGBAPixelF self, float const * r) -> itkRGBAPixelF
        __init__(itkRGBAPixelF self, float const & r) -> itkRGBAPixelF
        """
        _itkRGBAPixelPython.itkRGBAPixelF_swiginit(self, _itkRGBAPixelPython.new_itkRGBAPixelF(*args))
    __add__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelF___add__)
    __sub__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelF___sub__)
    __mul__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelF___mul__)

    def __truediv__(self, *args):
        return _itkRGBAPixelPython.itkRGBAPixelF___truediv__(self, *args)
    __div__ = __truediv__


    __iadd__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelF___iadd__)
    __isub__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelF___isub__)
    __imul__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelF___imul__)

    def __itruediv__(self, *args):
        return _itkRGBAPixelPython.itkRGBAPixelF___itruediv__(self, *args)
    __idiv__ = __itruediv__


    __lt__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelF___lt__)
    __eq__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelF___eq__)
    GetNumberOfComponents = _swig_new_static_method(_itkRGBAPixelPython.itkRGBAPixelF_GetNumberOfComponents)
    GetNthComponent = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelF_GetNthComponent)
    GetScalarValue = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelF_GetScalarValue)
    SetNthComponent = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelF_SetNthComponent)
    SetRed = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelF_SetRed)
    SetGreen = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelF_SetGreen)
    SetBlue = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelF_SetBlue)
    SetAlpha = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelF_SetAlpha)
    Set = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelF_Set)
    GetRed = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelF_GetRed)
    GetGreen = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelF_GetGreen)
    GetBlue = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelF_GetBlue)
    GetAlpha = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelF_GetAlpha)
    GetLuminance = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelF_GetLuminance)
    __getitem__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelF___getitem__)
    __setitem__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelF___setitem__)
    __len__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelF___len__)
    __repr__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelF___repr__)

# Register itkRGBAPixelF in _itkRGBAPixelPython:
_itkRGBAPixelPython.itkRGBAPixelF_swigregister(itkRGBAPixelF)
itkRGBAPixelF_GetNumberOfComponents = _itkRGBAPixelPython.itkRGBAPixelF_GetNumberOfComponents

class itkRGBAPixelUC(itkFixedArrayPython.itkFixedArrayUC4):
    r"""Proxy of C++ itkRGBAPixelUC class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __swig_destroy__ = _itkRGBAPixelPython.delete_itkRGBAPixelUC

    def __init__(self, *args):
        r"""
        __init__(itkRGBAPixelUC self) -> itkRGBAPixelUC
        __init__(itkRGBAPixelUC self, itkRGBAPixelUC arg0) -> itkRGBAPixelUC
        __init__(itkRGBAPixelUC self, unsigned char const * r) -> itkRGBAPixelUC
        __init__(itkRGBAPixelUC self, unsigned char const & r) -> itkRGBAPixelUC
        """
        _itkRGBAPixelPython.itkRGBAPixelUC_swiginit(self, _itkRGBAPixelPython.new_itkRGBAPixelUC(*args))
    __add__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelUC___add__)
    __sub__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelUC___sub__)
    __mul__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelUC___mul__)

    def __truediv__(self, *args):
        return _itkRGBAPixelPython.itkRGBAPixelUC___truediv__(self, *args)
    __div__ = __truediv__


    __iadd__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelUC___iadd__)
    __isub__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelUC___isub__)
    __imul__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelUC___imul__)

    def __itruediv__(self, *args):
        return _itkRGBAPixelPython.itkRGBAPixelUC___itruediv__(self, *args)
    __idiv__ = __itruediv__


    __lt__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelUC___lt__)
    __eq__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelUC___eq__)
    GetNumberOfComponents = _swig_new_static_method(_itkRGBAPixelPython.itkRGBAPixelUC_GetNumberOfComponents)
    GetNthComponent = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelUC_GetNthComponent)
    GetScalarValue = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelUC_GetScalarValue)
    SetNthComponent = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelUC_SetNthComponent)
    SetRed = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelUC_SetRed)
    SetGreen = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelUC_SetGreen)
    SetBlue = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelUC_SetBlue)
    SetAlpha = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelUC_SetAlpha)
    Set = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelUC_Set)
    GetRed = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelUC_GetRed)
    GetGreen = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelUC_GetGreen)
    GetBlue = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelUC_GetBlue)
    GetAlpha = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelUC_GetAlpha)
    GetLuminance = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelUC_GetLuminance)
    __getitem__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelUC___getitem__)
    __setitem__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelUC___setitem__)
    __len__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelUC___len__)
    __repr__ = _swig_new_instance_method(_itkRGBAPixelPython.itkRGBAPixelUC___repr__)

# Register itkRGBAPixelUC in _itkRGBAPixelPython:
_itkRGBAPixelPython.itkRGBAPixelUC_swigregister(itkRGBAPixelUC)
itkRGBAPixelUC_GetNumberOfComponents = _itkRGBAPixelPython.itkRGBAPixelUC_GetNumberOfComponents



