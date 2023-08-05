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
    from . import _itkBackwardDifferenceOperatorPython
else:
    import _itkBackwardDifferenceOperatorPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkBackwardDifferenceOperatorPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkBackwardDifferenceOperatorPython.SWIG_PyStaticMethod_New

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


import itkNeighborhoodOperatorPython
import itkNeighborhoodPython
import itkVectorPython
import vnl_vector_refPython
import stdcomplexPython
import pyBasePython
import vnl_vectorPython
import vnl_matrixPython
import itkFixedArrayPython
import ITKCommonBasePython
import itkCovariantVectorPython
import itkSizePython
import itkOffsetPython
import itkRGBPixelPython
class itkBackwardDifferenceOperatorD2(itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD2):
    r"""Proxy of C++ itkBackwardDifferenceOperatorD2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkBackwardDifferenceOperatorPython.delete_itkBackwardDifferenceOperatorD2

    def __init__(self, *args):
        r"""
        __init__(itkBackwardDifferenceOperatorD2 self) -> itkBackwardDifferenceOperatorD2
        __init__(itkBackwardDifferenceOperatorD2 self, itkBackwardDifferenceOperatorD2 arg0) -> itkBackwardDifferenceOperatorD2
        """
        _itkBackwardDifferenceOperatorPython.itkBackwardDifferenceOperatorD2_swiginit(self, _itkBackwardDifferenceOperatorPython.new_itkBackwardDifferenceOperatorD2(*args))

# Register itkBackwardDifferenceOperatorD2 in _itkBackwardDifferenceOperatorPython:
_itkBackwardDifferenceOperatorPython.itkBackwardDifferenceOperatorD2_swigregister(itkBackwardDifferenceOperatorD2)

class itkBackwardDifferenceOperatorD3(itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD3):
    r"""Proxy of C++ itkBackwardDifferenceOperatorD3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkBackwardDifferenceOperatorPython.delete_itkBackwardDifferenceOperatorD3

    def __init__(self, *args):
        r"""
        __init__(itkBackwardDifferenceOperatorD3 self) -> itkBackwardDifferenceOperatorD3
        __init__(itkBackwardDifferenceOperatorD3 self, itkBackwardDifferenceOperatorD3 arg0) -> itkBackwardDifferenceOperatorD3
        """
        _itkBackwardDifferenceOperatorPython.itkBackwardDifferenceOperatorD3_swiginit(self, _itkBackwardDifferenceOperatorPython.new_itkBackwardDifferenceOperatorD3(*args))

# Register itkBackwardDifferenceOperatorD3 in _itkBackwardDifferenceOperatorPython:
_itkBackwardDifferenceOperatorPython.itkBackwardDifferenceOperatorD3_swigregister(itkBackwardDifferenceOperatorD3)

class itkBackwardDifferenceOperatorF2(itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF2):
    r"""Proxy of C++ itkBackwardDifferenceOperatorF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkBackwardDifferenceOperatorPython.delete_itkBackwardDifferenceOperatorF2

    def __init__(self, *args):
        r"""
        __init__(itkBackwardDifferenceOperatorF2 self) -> itkBackwardDifferenceOperatorF2
        __init__(itkBackwardDifferenceOperatorF2 self, itkBackwardDifferenceOperatorF2 arg0) -> itkBackwardDifferenceOperatorF2
        """
        _itkBackwardDifferenceOperatorPython.itkBackwardDifferenceOperatorF2_swiginit(self, _itkBackwardDifferenceOperatorPython.new_itkBackwardDifferenceOperatorF2(*args))

# Register itkBackwardDifferenceOperatorF2 in _itkBackwardDifferenceOperatorPython:
_itkBackwardDifferenceOperatorPython.itkBackwardDifferenceOperatorF2_swigregister(itkBackwardDifferenceOperatorF2)

class itkBackwardDifferenceOperatorF3(itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF3):
    r"""Proxy of C++ itkBackwardDifferenceOperatorF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkBackwardDifferenceOperatorPython.delete_itkBackwardDifferenceOperatorF3

    def __init__(self, *args):
        r"""
        __init__(itkBackwardDifferenceOperatorF3 self) -> itkBackwardDifferenceOperatorF3
        __init__(itkBackwardDifferenceOperatorF3 self, itkBackwardDifferenceOperatorF3 arg0) -> itkBackwardDifferenceOperatorF3
        """
        _itkBackwardDifferenceOperatorPython.itkBackwardDifferenceOperatorF3_swiginit(self, _itkBackwardDifferenceOperatorPython.new_itkBackwardDifferenceOperatorF3(*args))

# Register itkBackwardDifferenceOperatorF3 in _itkBackwardDifferenceOperatorPython:
_itkBackwardDifferenceOperatorPython.itkBackwardDifferenceOperatorF3_swigregister(itkBackwardDifferenceOperatorF3)



