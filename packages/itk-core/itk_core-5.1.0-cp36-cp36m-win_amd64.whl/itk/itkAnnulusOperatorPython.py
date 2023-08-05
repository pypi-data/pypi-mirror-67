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
    from . import _itkAnnulusOperatorPython
else:
    import _itkAnnulusOperatorPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkAnnulusOperatorPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkAnnulusOperatorPython.SWIG_PyStaticMethod_New

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


import itkVectorPython
import itkFixedArrayPython
import pyBasePython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import ITKCommonBasePython
import itkNeighborhoodOperatorPython
import itkNeighborhoodPython
import itkRGBPixelPython
import itkSizePython
import itkCovariantVectorPython
import itkOffsetPython
class itkAnnulusOperatorD2(itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD2):
    r"""Proxy of C++ itkAnnulusOperatorD2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    CreateOperator = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD2_CreateOperator)
    SetInnerRadius = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD2_SetInnerRadius)
    GetInnerRadius = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD2_GetInnerRadius)
    SetThickness = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD2_SetThickness)
    GetThickness = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD2_GetThickness)
    SetSpacing = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD2_SetSpacing)
    GetSpacing = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD2_GetSpacing)
    SetNormalize = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD2_SetNormalize)
    GetNormalize = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD2_GetNormalize)
    NormalizeOn = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD2_NormalizeOn)
    NormalizeOff = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD2_NormalizeOff)
    SetBrightCenter = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD2_SetBrightCenter)
    GetBrightCenter = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD2_GetBrightCenter)
    BrightCenterOn = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD2_BrightCenterOn)
    BrightCenterOff = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD2_BrightCenterOff)
    SetInteriorValue = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD2_SetInteriorValue)
    GetInteriorValue = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD2_GetInteriorValue)
    SetAnnulusValue = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD2_SetAnnulusValue)
    GetAnnulusValue = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD2_GetAnnulusValue)
    SetExteriorValue = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD2_SetExteriorValue)
    GetExteriorValue = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD2_GetExteriorValue)
    __swig_destroy__ = _itkAnnulusOperatorPython.delete_itkAnnulusOperatorD2

    def __init__(self, *args):
        r"""
        __init__(itkAnnulusOperatorD2 self, itkAnnulusOperatorD2 arg0) -> itkAnnulusOperatorD2
        __init__(itkAnnulusOperatorD2 self) -> itkAnnulusOperatorD2
        """
        _itkAnnulusOperatorPython.itkAnnulusOperatorD2_swiginit(self, _itkAnnulusOperatorPython.new_itkAnnulusOperatorD2(*args))

# Register itkAnnulusOperatorD2 in _itkAnnulusOperatorPython:
_itkAnnulusOperatorPython.itkAnnulusOperatorD2_swigregister(itkAnnulusOperatorD2)

class itkAnnulusOperatorD3(itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD3):
    r"""Proxy of C++ itkAnnulusOperatorD3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    CreateOperator = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD3_CreateOperator)
    SetInnerRadius = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD3_SetInnerRadius)
    GetInnerRadius = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD3_GetInnerRadius)
    SetThickness = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD3_SetThickness)
    GetThickness = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD3_GetThickness)
    SetSpacing = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD3_SetSpacing)
    GetSpacing = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD3_GetSpacing)
    SetNormalize = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD3_SetNormalize)
    GetNormalize = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD3_GetNormalize)
    NormalizeOn = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD3_NormalizeOn)
    NormalizeOff = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD3_NormalizeOff)
    SetBrightCenter = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD3_SetBrightCenter)
    GetBrightCenter = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD3_GetBrightCenter)
    BrightCenterOn = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD3_BrightCenterOn)
    BrightCenterOff = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD3_BrightCenterOff)
    SetInteriorValue = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD3_SetInteriorValue)
    GetInteriorValue = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD3_GetInteriorValue)
    SetAnnulusValue = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD3_SetAnnulusValue)
    GetAnnulusValue = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD3_GetAnnulusValue)
    SetExteriorValue = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD3_SetExteriorValue)
    GetExteriorValue = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorD3_GetExteriorValue)
    __swig_destroy__ = _itkAnnulusOperatorPython.delete_itkAnnulusOperatorD3

    def __init__(self, *args):
        r"""
        __init__(itkAnnulusOperatorD3 self, itkAnnulusOperatorD3 arg0) -> itkAnnulusOperatorD3
        __init__(itkAnnulusOperatorD3 self) -> itkAnnulusOperatorD3
        """
        _itkAnnulusOperatorPython.itkAnnulusOperatorD3_swiginit(self, _itkAnnulusOperatorPython.new_itkAnnulusOperatorD3(*args))

# Register itkAnnulusOperatorD3 in _itkAnnulusOperatorPython:
_itkAnnulusOperatorPython.itkAnnulusOperatorD3_swigregister(itkAnnulusOperatorD3)

class itkAnnulusOperatorF2(itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF2):
    r"""Proxy of C++ itkAnnulusOperatorF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    CreateOperator = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF2_CreateOperator)
    SetInnerRadius = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF2_SetInnerRadius)
    GetInnerRadius = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF2_GetInnerRadius)
    SetThickness = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF2_SetThickness)
    GetThickness = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF2_GetThickness)
    SetSpacing = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF2_SetSpacing)
    GetSpacing = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF2_GetSpacing)
    SetNormalize = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF2_SetNormalize)
    GetNormalize = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF2_GetNormalize)
    NormalizeOn = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF2_NormalizeOn)
    NormalizeOff = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF2_NormalizeOff)
    SetBrightCenter = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF2_SetBrightCenter)
    GetBrightCenter = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF2_GetBrightCenter)
    BrightCenterOn = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF2_BrightCenterOn)
    BrightCenterOff = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF2_BrightCenterOff)
    SetInteriorValue = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF2_SetInteriorValue)
    GetInteriorValue = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF2_GetInteriorValue)
    SetAnnulusValue = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF2_SetAnnulusValue)
    GetAnnulusValue = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF2_GetAnnulusValue)
    SetExteriorValue = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF2_SetExteriorValue)
    GetExteriorValue = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF2_GetExteriorValue)
    __swig_destroy__ = _itkAnnulusOperatorPython.delete_itkAnnulusOperatorF2

    def __init__(self, *args):
        r"""
        __init__(itkAnnulusOperatorF2 self, itkAnnulusOperatorF2 arg0) -> itkAnnulusOperatorF2
        __init__(itkAnnulusOperatorF2 self) -> itkAnnulusOperatorF2
        """
        _itkAnnulusOperatorPython.itkAnnulusOperatorF2_swiginit(self, _itkAnnulusOperatorPython.new_itkAnnulusOperatorF2(*args))

# Register itkAnnulusOperatorF2 in _itkAnnulusOperatorPython:
_itkAnnulusOperatorPython.itkAnnulusOperatorF2_swigregister(itkAnnulusOperatorF2)

class itkAnnulusOperatorF3(itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF3):
    r"""Proxy of C++ itkAnnulusOperatorF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    CreateOperator = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF3_CreateOperator)
    SetInnerRadius = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF3_SetInnerRadius)
    GetInnerRadius = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF3_GetInnerRadius)
    SetThickness = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF3_SetThickness)
    GetThickness = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF3_GetThickness)
    SetSpacing = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF3_SetSpacing)
    GetSpacing = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF3_GetSpacing)
    SetNormalize = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF3_SetNormalize)
    GetNormalize = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF3_GetNormalize)
    NormalizeOn = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF3_NormalizeOn)
    NormalizeOff = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF3_NormalizeOff)
    SetBrightCenter = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF3_SetBrightCenter)
    GetBrightCenter = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF3_GetBrightCenter)
    BrightCenterOn = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF3_BrightCenterOn)
    BrightCenterOff = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF3_BrightCenterOff)
    SetInteriorValue = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF3_SetInteriorValue)
    GetInteriorValue = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF3_GetInteriorValue)
    SetAnnulusValue = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF3_SetAnnulusValue)
    GetAnnulusValue = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF3_GetAnnulusValue)
    SetExteriorValue = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF3_SetExteriorValue)
    GetExteriorValue = _swig_new_instance_method(_itkAnnulusOperatorPython.itkAnnulusOperatorF3_GetExteriorValue)
    __swig_destroy__ = _itkAnnulusOperatorPython.delete_itkAnnulusOperatorF3

    def __init__(self, *args):
        r"""
        __init__(itkAnnulusOperatorF3 self, itkAnnulusOperatorF3 arg0) -> itkAnnulusOperatorF3
        __init__(itkAnnulusOperatorF3 self) -> itkAnnulusOperatorF3
        """
        _itkAnnulusOperatorPython.itkAnnulusOperatorF3_swiginit(self, _itkAnnulusOperatorPython.new_itkAnnulusOperatorF3(*args))

# Register itkAnnulusOperatorF3 in _itkAnnulusOperatorPython:
_itkAnnulusOperatorPython.itkAnnulusOperatorF3_swigregister(itkAnnulusOperatorF3)



