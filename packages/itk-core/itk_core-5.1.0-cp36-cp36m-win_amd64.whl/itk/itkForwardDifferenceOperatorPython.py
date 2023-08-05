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
    from . import _itkForwardDifferenceOperatorPython
else:
    import _itkForwardDifferenceOperatorPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkForwardDifferenceOperatorPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkForwardDifferenceOperatorPython.SWIG_PyStaticMethod_New

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
import itkRGBPixelPython
import itkFixedArrayPython
import pyBasePython
import itkVectorPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkSizePython
import ITKCommonBasePython
import itkCovariantVectorPython
import itkOffsetPython
class itkForwardDifferenceOperatorD2(itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD2):
    r"""Proxy of C++ itkForwardDifferenceOperatorD2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkForwardDifferenceOperatorPython.delete_itkForwardDifferenceOperatorD2

    def __init__(self, *args):
        r"""
        __init__(itkForwardDifferenceOperatorD2 self) -> itkForwardDifferenceOperatorD2
        __init__(itkForwardDifferenceOperatorD2 self, itkForwardDifferenceOperatorD2 arg0) -> itkForwardDifferenceOperatorD2
        """
        _itkForwardDifferenceOperatorPython.itkForwardDifferenceOperatorD2_swiginit(self, _itkForwardDifferenceOperatorPython.new_itkForwardDifferenceOperatorD2(*args))

# Register itkForwardDifferenceOperatorD2 in _itkForwardDifferenceOperatorPython:
_itkForwardDifferenceOperatorPython.itkForwardDifferenceOperatorD2_swigregister(itkForwardDifferenceOperatorD2)

class itkForwardDifferenceOperatorD3(itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD3):
    r"""Proxy of C++ itkForwardDifferenceOperatorD3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkForwardDifferenceOperatorPython.delete_itkForwardDifferenceOperatorD3

    def __init__(self, *args):
        r"""
        __init__(itkForwardDifferenceOperatorD3 self) -> itkForwardDifferenceOperatorD3
        __init__(itkForwardDifferenceOperatorD3 self, itkForwardDifferenceOperatorD3 arg0) -> itkForwardDifferenceOperatorD3
        """
        _itkForwardDifferenceOperatorPython.itkForwardDifferenceOperatorD3_swiginit(self, _itkForwardDifferenceOperatorPython.new_itkForwardDifferenceOperatorD3(*args))

# Register itkForwardDifferenceOperatorD3 in _itkForwardDifferenceOperatorPython:
_itkForwardDifferenceOperatorPython.itkForwardDifferenceOperatorD3_swigregister(itkForwardDifferenceOperatorD3)

class itkForwardDifferenceOperatorF2(itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF2):
    r"""Proxy of C++ itkForwardDifferenceOperatorF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkForwardDifferenceOperatorPython.delete_itkForwardDifferenceOperatorF2

    def __init__(self, *args):
        r"""
        __init__(itkForwardDifferenceOperatorF2 self) -> itkForwardDifferenceOperatorF2
        __init__(itkForwardDifferenceOperatorF2 self, itkForwardDifferenceOperatorF2 arg0) -> itkForwardDifferenceOperatorF2
        """
        _itkForwardDifferenceOperatorPython.itkForwardDifferenceOperatorF2_swiginit(self, _itkForwardDifferenceOperatorPython.new_itkForwardDifferenceOperatorF2(*args))

# Register itkForwardDifferenceOperatorF2 in _itkForwardDifferenceOperatorPython:
_itkForwardDifferenceOperatorPython.itkForwardDifferenceOperatorF2_swigregister(itkForwardDifferenceOperatorF2)

class itkForwardDifferenceOperatorF3(itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF3):
    r"""Proxy of C++ itkForwardDifferenceOperatorF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkForwardDifferenceOperatorPython.delete_itkForwardDifferenceOperatorF3

    def __init__(self, *args):
        r"""
        __init__(itkForwardDifferenceOperatorF3 self) -> itkForwardDifferenceOperatorF3
        __init__(itkForwardDifferenceOperatorF3 self, itkForwardDifferenceOperatorF3 arg0) -> itkForwardDifferenceOperatorF3
        """
        _itkForwardDifferenceOperatorPython.itkForwardDifferenceOperatorF3_swiginit(self, _itkForwardDifferenceOperatorPython.new_itkForwardDifferenceOperatorF3(*args))

# Register itkForwardDifferenceOperatorF3 in _itkForwardDifferenceOperatorPython:
_itkForwardDifferenceOperatorPython.itkForwardDifferenceOperatorF3_swigregister(itkForwardDifferenceOperatorF3)



