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
    from . import _itkDistanceMetricPython
else:
    import _itkDistanceMetricPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkDistanceMetricPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkDistanceMetricPython.SWIG_PyStaticMethod_New

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


import ITKCommonBasePython
import pyBasePython
import itkFunctionBasePython
import itkRGBAPixelPython
import itkFixedArrayPython
import itkPointPython
import itkVectorPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import vnl_vector_refPython
import itkImagePython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkRGBPixelPython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkImageRegionPython
import itkSymmetricSecondRankTensorPython
import itkArrayPython
import itkContinuousIndexPython

def itkDistanceMetricVF3_New():
  return itkDistanceMetricVF3.New()


def itkDistanceMetricVF2_New():
  return itkDistanceMetricVF2.New()

class itkDistanceMetricVF2(itkFunctionBasePython.itkFunctionBaseVF2D):
    r"""Proxy of C++ itkDistanceMetricVF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetOrigin = _swig_new_instance_method(_itkDistanceMetricPython.itkDistanceMetricVF2_SetOrigin)
    GetOrigin = _swig_new_instance_method(_itkDistanceMetricPython.itkDistanceMetricVF2_GetOrigin)
    Evaluate = _swig_new_instance_method(_itkDistanceMetricPython.itkDistanceMetricVF2_Evaluate)
    SetMeasurementVectorSize = _swig_new_instance_method(_itkDistanceMetricPython.itkDistanceMetricVF2_SetMeasurementVectorSize)
    GetMeasurementVectorSize = _swig_new_instance_method(_itkDistanceMetricPython.itkDistanceMetricVF2_GetMeasurementVectorSize)
    __swig_destroy__ = _itkDistanceMetricPython.delete_itkDistanceMetricVF2
    cast = _swig_new_static_method(_itkDistanceMetricPython.itkDistanceMetricVF2_cast)

    def New(*args, **kargs):
        """New() -> itkDistanceMetricVF2

        Create a new object of the class itkDistanceMetricVF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDistanceMetricVF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDistanceMetricVF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDistanceMetricVF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkDistanceMetricVF2 in _itkDistanceMetricPython:
_itkDistanceMetricPython.itkDistanceMetricVF2_swigregister(itkDistanceMetricVF2)
itkDistanceMetricVF2_cast = _itkDistanceMetricPython.itkDistanceMetricVF2_cast

class itkDistanceMetricVF3(itkFunctionBasePython.itkFunctionBaseVF3D):
    r"""Proxy of C++ itkDistanceMetricVF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetOrigin = _swig_new_instance_method(_itkDistanceMetricPython.itkDistanceMetricVF3_SetOrigin)
    GetOrigin = _swig_new_instance_method(_itkDistanceMetricPython.itkDistanceMetricVF3_GetOrigin)
    Evaluate = _swig_new_instance_method(_itkDistanceMetricPython.itkDistanceMetricVF3_Evaluate)
    SetMeasurementVectorSize = _swig_new_instance_method(_itkDistanceMetricPython.itkDistanceMetricVF3_SetMeasurementVectorSize)
    GetMeasurementVectorSize = _swig_new_instance_method(_itkDistanceMetricPython.itkDistanceMetricVF3_GetMeasurementVectorSize)
    __swig_destroy__ = _itkDistanceMetricPython.delete_itkDistanceMetricVF3
    cast = _swig_new_static_method(_itkDistanceMetricPython.itkDistanceMetricVF3_cast)

    def New(*args, **kargs):
        """New() -> itkDistanceMetricVF3

        Create a new object of the class itkDistanceMetricVF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDistanceMetricVF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDistanceMetricVF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDistanceMetricVF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkDistanceMetricVF3 in _itkDistanceMetricPython:
_itkDistanceMetricPython.itkDistanceMetricVF3_swigregister(itkDistanceMetricVF3)
itkDistanceMetricVF3_cast = _itkDistanceMetricPython.itkDistanceMetricVF3_cast



