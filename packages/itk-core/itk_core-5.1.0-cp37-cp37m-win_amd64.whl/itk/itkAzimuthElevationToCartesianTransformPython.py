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
    from . import _itkAzimuthElevationToCartesianTransformPython
else:
    import _itkAzimuthElevationToCartesianTransformPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkAzimuthElevationToCartesianTransformPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkAzimuthElevationToCartesianTransformPython.SWIG_PyStaticMethod_New

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


import itkAffineTransformPython
import itkVectorPython
import vnl_vector_refPython
import stdcomplexPython
import pyBasePython
import vnl_vectorPython
import vnl_matrixPython
import itkFixedArrayPython
import ITKCommonBasePython
import itkMatrixOffsetTransformBasePython
import itkPointPython
import itkCovariantVectorPython
import itkArray2DPython
import itkOptimizerParametersPython
import itkArrayPython
import itkVariableLengthVectorPython
import vnl_matrix_fixedPython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import itkTransformBasePython

def itkAzimuthElevationToCartesianTransformD3_New():
  return itkAzimuthElevationToCartesianTransformD3.New()


def itkAzimuthElevationToCartesianTransformD2_New():
  return itkAzimuthElevationToCartesianTransformD2.New()

class itkAzimuthElevationToCartesianTransformD2(itkAffineTransformPython.itkAffineTransformD2):
    r"""Proxy of C++ itkAzimuthElevationToCartesianTransformD2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2___New_orig__)
    Clone = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_Clone)
    SetAzimuthElevationToCartesianParameters = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_SetAzimuthElevationToCartesianParameters)
    BackTransform = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_BackTransform)
    BackTransformPoint = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_BackTransformPoint)
    SetForwardAzimuthElevationToCartesian = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_SetForwardAzimuthElevationToCartesian)
    SetForwardCartesianToAzimuthElevation = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_SetForwardCartesianToAzimuthElevation)
    TransformAzElToCartesian = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_TransformAzElToCartesian)
    TransformCartesianToAzEl = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_TransformCartesianToAzEl)
    SetMaxAzimuth = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_SetMaxAzimuth)
    GetMaxAzimuth = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_GetMaxAzimuth)
    SetMaxElevation = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_SetMaxElevation)
    GetMaxElevation = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_GetMaxElevation)
    SetRadiusSampleSize = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_SetRadiusSampleSize)
    GetRadiusSampleSize = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_GetRadiusSampleSize)
    SetAzimuthAngularSeparation = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_SetAzimuthAngularSeparation)
    GetAzimuthAngularSeparation = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_GetAzimuthAngularSeparation)
    SetElevationAngularSeparation = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_SetElevationAngularSeparation)
    GetElevationAngularSeparation = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_GetElevationAngularSeparation)
    SetFirstSampleDistance = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_SetFirstSampleDistance)
    GetFirstSampleDistance = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_GetFirstSampleDistance)
    __swig_destroy__ = _itkAzimuthElevationToCartesianTransformPython.delete_itkAzimuthElevationToCartesianTransformD2
    cast = _swig_new_static_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_cast)

    def New(*args, **kargs):
        """New() -> itkAzimuthElevationToCartesianTransformD2

        Create a new object of the class itkAzimuthElevationToCartesianTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAzimuthElevationToCartesianTransformD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAzimuthElevationToCartesianTransformD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAzimuthElevationToCartesianTransformD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAzimuthElevationToCartesianTransformD2 in _itkAzimuthElevationToCartesianTransformPython:
_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_swigregister(itkAzimuthElevationToCartesianTransformD2)
itkAzimuthElevationToCartesianTransformD2___New_orig__ = _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2___New_orig__
itkAzimuthElevationToCartesianTransformD2_cast = _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD2_cast

class itkAzimuthElevationToCartesianTransformD3(itkAffineTransformPython.itkAffineTransformD3):
    r"""Proxy of C++ itkAzimuthElevationToCartesianTransformD3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3___New_orig__)
    Clone = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_Clone)
    SetAzimuthElevationToCartesianParameters = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_SetAzimuthElevationToCartesianParameters)
    BackTransform = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_BackTransform)
    BackTransformPoint = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_BackTransformPoint)
    SetForwardAzimuthElevationToCartesian = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_SetForwardAzimuthElevationToCartesian)
    SetForwardCartesianToAzimuthElevation = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_SetForwardCartesianToAzimuthElevation)
    TransformAzElToCartesian = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_TransformAzElToCartesian)
    TransformCartesianToAzEl = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_TransformCartesianToAzEl)
    SetMaxAzimuth = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_SetMaxAzimuth)
    GetMaxAzimuth = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_GetMaxAzimuth)
    SetMaxElevation = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_SetMaxElevation)
    GetMaxElevation = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_GetMaxElevation)
    SetRadiusSampleSize = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_SetRadiusSampleSize)
    GetRadiusSampleSize = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_GetRadiusSampleSize)
    SetAzimuthAngularSeparation = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_SetAzimuthAngularSeparation)
    GetAzimuthAngularSeparation = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_GetAzimuthAngularSeparation)
    SetElevationAngularSeparation = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_SetElevationAngularSeparation)
    GetElevationAngularSeparation = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_GetElevationAngularSeparation)
    SetFirstSampleDistance = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_SetFirstSampleDistance)
    GetFirstSampleDistance = _swig_new_instance_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_GetFirstSampleDistance)
    __swig_destroy__ = _itkAzimuthElevationToCartesianTransformPython.delete_itkAzimuthElevationToCartesianTransformD3
    cast = _swig_new_static_method(_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_cast)

    def New(*args, **kargs):
        """New() -> itkAzimuthElevationToCartesianTransformD3

        Create a new object of the class itkAzimuthElevationToCartesianTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAzimuthElevationToCartesianTransformD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAzimuthElevationToCartesianTransformD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAzimuthElevationToCartesianTransformD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAzimuthElevationToCartesianTransformD3 in _itkAzimuthElevationToCartesianTransformPython:
_itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_swigregister(itkAzimuthElevationToCartesianTransformD3)
itkAzimuthElevationToCartesianTransformD3___New_orig__ = _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3___New_orig__
itkAzimuthElevationToCartesianTransformD3_cast = _itkAzimuthElevationToCartesianTransformPython.itkAzimuthElevationToCartesianTransformD3_cast



