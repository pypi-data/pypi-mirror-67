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
    from . import _itkSymmetricSecondRankTensorPython
else:
    import _itkSymmetricSecondRankTensorPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkSymmetricSecondRankTensorPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkSymmetricSecondRankTensorPython.SWIG_PyStaticMethod_New

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
import itkMatrixPython
import vnl_matrixPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrix_fixedPython
import itkPointPython
import itkVectorPython
import vnl_vector_refPython
import itkCovariantVectorPython
class itkSymmetricSecondRankTensorD2(itkFixedArrayPython.itkFixedArrayD3):
    r"""Proxy of C++ itkSymmetricSecondRankTensorD2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkSymmetricSecondRankTensorPython.delete_itkSymmetricSecondRankTensorD2

    def __init__(self, *args):
        r"""
        __init__(itkSymmetricSecondRankTensorD2 self) -> itkSymmetricSecondRankTensorD2
        __init__(itkSymmetricSecondRankTensorD2 self, itkSymmetricSecondRankTensorD2 arg0) -> itkSymmetricSecondRankTensorD2
        __init__(itkSymmetricSecondRankTensorD2 self, double const & r) -> itkSymmetricSecondRankTensorD2
        __init__(itkSymmetricSecondRankTensorD2 self, double const * r) -> itkSymmetricSecondRankTensorD2
        """
        _itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD2_swiginit(self, _itkSymmetricSecondRankTensorPython.new_itkSymmetricSecondRankTensorD2(*args))
    __add__ = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD2___add__)
    __sub__ = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD2___sub__)
    __iadd__ = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD2___iadd__)
    __isub__ = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD2___isub__)
    __mul__ = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD2___mul__)

    def __truediv__(self, *args):
        return _itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD2___truediv__(self, *args)
    __div__ = __truediv__


    __imul__ = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD2___imul__)

    def __itruediv__(self, *args):
        return _itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD2___itruediv__(self, *args)
    __idiv__ = __itruediv__


    GetNumberOfComponents = _swig_new_static_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD2_GetNumberOfComponents)
    GetNthComponent = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD2_GetNthComponent)
    SetNthComponent = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD2_SetNthComponent)
    __call__ = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD2___call__)
    SetIdentity = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD2_SetIdentity)
    GetTrace = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD2_GetTrace)
    ComputeEigenValues = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD2_ComputeEigenValues)
    ComputeEigenAnalysis = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD2_ComputeEigenAnalysis)
    PreMultiply = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD2_PreMultiply)
    PostMultiply = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD2_PostMultiply)

# Register itkSymmetricSecondRankTensorD2 in _itkSymmetricSecondRankTensorPython:
_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD2_swigregister(itkSymmetricSecondRankTensorD2)
itkSymmetricSecondRankTensorD2_GetNumberOfComponents = _itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD2_GetNumberOfComponents

class itkSymmetricSecondRankTensorD3(itkFixedArrayPython.itkFixedArrayD6):
    r"""Proxy of C++ itkSymmetricSecondRankTensorD3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkSymmetricSecondRankTensorPython.delete_itkSymmetricSecondRankTensorD3

    def __init__(self, *args):
        r"""
        __init__(itkSymmetricSecondRankTensorD3 self) -> itkSymmetricSecondRankTensorD3
        __init__(itkSymmetricSecondRankTensorD3 self, itkSymmetricSecondRankTensorD3 arg0) -> itkSymmetricSecondRankTensorD3
        __init__(itkSymmetricSecondRankTensorD3 self, double const & r) -> itkSymmetricSecondRankTensorD3
        __init__(itkSymmetricSecondRankTensorD3 self, double const * r) -> itkSymmetricSecondRankTensorD3
        """
        _itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD3_swiginit(self, _itkSymmetricSecondRankTensorPython.new_itkSymmetricSecondRankTensorD3(*args))
    __add__ = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD3___add__)
    __sub__ = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD3___sub__)
    __iadd__ = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD3___iadd__)
    __isub__ = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD3___isub__)
    __mul__ = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD3___mul__)

    def __truediv__(self, *args):
        return _itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD3___truediv__(self, *args)
    __div__ = __truediv__


    __imul__ = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD3___imul__)

    def __itruediv__(self, *args):
        return _itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD3___itruediv__(self, *args)
    __idiv__ = __itruediv__


    GetNumberOfComponents = _swig_new_static_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD3_GetNumberOfComponents)
    GetNthComponent = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD3_GetNthComponent)
    SetNthComponent = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD3_SetNthComponent)
    __call__ = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD3___call__)
    SetIdentity = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD3_SetIdentity)
    GetTrace = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD3_GetTrace)
    ComputeEigenValues = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD3_ComputeEigenValues)
    ComputeEigenAnalysis = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD3_ComputeEigenAnalysis)
    PreMultiply = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD3_PreMultiply)
    PostMultiply = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD3_PostMultiply)

# Register itkSymmetricSecondRankTensorD3 in _itkSymmetricSecondRankTensorPython:
_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD3_swigregister(itkSymmetricSecondRankTensorD3)
itkSymmetricSecondRankTensorD3_GetNumberOfComponents = _itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorD3_GetNumberOfComponents

class itkSymmetricSecondRankTensorF2(itkFixedArrayPython.itkFixedArrayF3):
    r"""Proxy of C++ itkSymmetricSecondRankTensorF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkSymmetricSecondRankTensorPython.delete_itkSymmetricSecondRankTensorF2

    def __init__(self, *args):
        r"""
        __init__(itkSymmetricSecondRankTensorF2 self) -> itkSymmetricSecondRankTensorF2
        __init__(itkSymmetricSecondRankTensorF2 self, itkSymmetricSecondRankTensorF2 arg0) -> itkSymmetricSecondRankTensorF2
        __init__(itkSymmetricSecondRankTensorF2 self, float const & r) -> itkSymmetricSecondRankTensorF2
        __init__(itkSymmetricSecondRankTensorF2 self, float const * r) -> itkSymmetricSecondRankTensorF2
        """
        _itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF2_swiginit(self, _itkSymmetricSecondRankTensorPython.new_itkSymmetricSecondRankTensorF2(*args))
    __add__ = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF2___add__)
    __sub__ = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF2___sub__)
    __iadd__ = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF2___iadd__)
    __isub__ = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF2___isub__)
    __mul__ = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF2___mul__)

    def __truediv__(self, *args):
        return _itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF2___truediv__(self, *args)
    __div__ = __truediv__


    __imul__ = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF2___imul__)

    def __itruediv__(self, *args):
        return _itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF2___itruediv__(self, *args)
    __idiv__ = __itruediv__


    GetNumberOfComponents = _swig_new_static_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF2_GetNumberOfComponents)
    GetNthComponent = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF2_GetNthComponent)
    SetNthComponent = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF2_SetNthComponent)
    __call__ = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF2___call__)
    SetIdentity = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF2_SetIdentity)
    GetTrace = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF2_GetTrace)
    ComputeEigenValues = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF2_ComputeEigenValues)
    ComputeEigenAnalysis = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF2_ComputeEigenAnalysis)
    PreMultiply = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF2_PreMultiply)
    PostMultiply = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF2_PostMultiply)

# Register itkSymmetricSecondRankTensorF2 in _itkSymmetricSecondRankTensorPython:
_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF2_swigregister(itkSymmetricSecondRankTensorF2)
itkSymmetricSecondRankTensorF2_GetNumberOfComponents = _itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF2_GetNumberOfComponents

class itkSymmetricSecondRankTensorF3(itkFixedArrayPython.itkFixedArrayF6):
    r"""Proxy of C++ itkSymmetricSecondRankTensorF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkSymmetricSecondRankTensorPython.delete_itkSymmetricSecondRankTensorF3

    def __init__(self, *args):
        r"""
        __init__(itkSymmetricSecondRankTensorF3 self) -> itkSymmetricSecondRankTensorF3
        __init__(itkSymmetricSecondRankTensorF3 self, itkSymmetricSecondRankTensorF3 arg0) -> itkSymmetricSecondRankTensorF3
        __init__(itkSymmetricSecondRankTensorF3 self, float const & r) -> itkSymmetricSecondRankTensorF3
        __init__(itkSymmetricSecondRankTensorF3 self, float const * r) -> itkSymmetricSecondRankTensorF3
        """
        _itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF3_swiginit(self, _itkSymmetricSecondRankTensorPython.new_itkSymmetricSecondRankTensorF3(*args))
    __add__ = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF3___add__)
    __sub__ = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF3___sub__)
    __iadd__ = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF3___iadd__)
    __isub__ = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF3___isub__)
    __mul__ = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF3___mul__)

    def __truediv__(self, *args):
        return _itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF3___truediv__(self, *args)
    __div__ = __truediv__


    __imul__ = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF3___imul__)

    def __itruediv__(self, *args):
        return _itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF3___itruediv__(self, *args)
    __idiv__ = __itruediv__


    GetNumberOfComponents = _swig_new_static_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF3_GetNumberOfComponents)
    GetNthComponent = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF3_GetNthComponent)
    SetNthComponent = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF3_SetNthComponent)
    __call__ = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF3___call__)
    SetIdentity = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF3_SetIdentity)
    GetTrace = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF3_GetTrace)
    ComputeEigenValues = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF3_ComputeEigenValues)
    ComputeEigenAnalysis = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF3_ComputeEigenAnalysis)
    PreMultiply = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF3_PreMultiply)
    PostMultiply = _swig_new_instance_method(_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF3_PostMultiply)

# Register itkSymmetricSecondRankTensorF3 in _itkSymmetricSecondRankTensorPython:
_itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF3_swigregister(itkSymmetricSecondRankTensorF3)
itkSymmetricSecondRankTensorF3_GetNumberOfComponents = _itkSymmetricSecondRankTensorPython.itkSymmetricSecondRankTensorF3_GetNumberOfComponents



