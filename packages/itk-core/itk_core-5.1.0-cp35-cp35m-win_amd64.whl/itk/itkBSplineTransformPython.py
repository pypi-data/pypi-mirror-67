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
    from . import _itkBSplineTransformPython
else:
    import _itkBSplineTransformPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkBSplineTransformPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkBSplineTransformPython.SWIG_PyStaticMethod_New

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


import itkSizePython
import pyBasePython
import ITKCommonBasePython
import itkVectorPython
import itkFixedArrayPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import vnl_vector_refPython
import itkMatrixPython
import itkPointPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkArray2DPython
import itkArrayPython
import itkBSplineBaseTransformPython
import itkTransformBasePython
import itkSymmetricSecondRankTensorPython
import itkVariableLengthVectorPython
import itkDiffusionTensor3DPython
import itkOptimizerParametersPython
import itkContinuousIndexPython
import itkIndexPython
import itkOffsetPython
import itkBSplineInterpolationWeightFunctionPython
import itkFunctionBasePython
import itkRGBAPixelPython
import itkImagePython
import itkRGBPixelPython
import itkImageRegionPython

def itkBSplineTransformD33_New():
  return itkBSplineTransformD33.New()


def itkBSplineTransformD23_New():
  return itkBSplineTransformD23.New()

class itkBSplineTransformD23(itkBSplineBaseTransformPython.itkBSplineBaseTransformD23):
    r"""Proxy of C++ itkBSplineTransformD23 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineTransformPython.itkBSplineTransformD23___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD23_Clone)
    SetTransformDomainOrigin = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD23_SetTransformDomainOrigin)
    GetTransformDomainOrigin = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD23_GetTransformDomainOrigin)
    SetTransformDomainPhysicalDimensions = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD23_SetTransformDomainPhysicalDimensions)
    GetTransformDomainPhysicalDimensions = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD23_GetTransformDomainPhysicalDimensions)
    SetTransformDomainDirection = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD23_SetTransformDomainDirection)
    GetTransformDomainDirection = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD23_GetTransformDomainDirection)
    SetTransformDomainMeshSize = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD23_SetTransformDomainMeshSize)
    GetTransformDomainMeshSize = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD23_GetTransformDomainMeshSize)
    __swig_destroy__ = _itkBSplineTransformPython.delete_itkBSplineTransformD23
    cast = _swig_new_static_method(_itkBSplineTransformPython.itkBSplineTransformD23_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineTransformD23

        Create a new object of the class itkBSplineTransformD23 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineTransformD23.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineTransformD23.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineTransformD23.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineTransformD23 in _itkBSplineTransformPython:
_itkBSplineTransformPython.itkBSplineTransformD23_swigregister(itkBSplineTransformD23)
itkBSplineTransformD23___New_orig__ = _itkBSplineTransformPython.itkBSplineTransformD23___New_orig__
itkBSplineTransformD23_cast = _itkBSplineTransformPython.itkBSplineTransformD23_cast

class itkBSplineTransformD33(itkBSplineBaseTransformPython.itkBSplineBaseTransformD33):
    r"""Proxy of C++ itkBSplineTransformD33 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineTransformPython.itkBSplineTransformD33___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD33_Clone)
    SetTransformDomainOrigin = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD33_SetTransformDomainOrigin)
    GetTransformDomainOrigin = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD33_GetTransformDomainOrigin)
    SetTransformDomainPhysicalDimensions = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD33_SetTransformDomainPhysicalDimensions)
    GetTransformDomainPhysicalDimensions = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD33_GetTransformDomainPhysicalDimensions)
    SetTransformDomainDirection = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD33_SetTransformDomainDirection)
    GetTransformDomainDirection = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD33_GetTransformDomainDirection)
    SetTransformDomainMeshSize = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD33_SetTransformDomainMeshSize)
    GetTransformDomainMeshSize = _swig_new_instance_method(_itkBSplineTransformPython.itkBSplineTransformD33_GetTransformDomainMeshSize)
    __swig_destroy__ = _itkBSplineTransformPython.delete_itkBSplineTransformD33
    cast = _swig_new_static_method(_itkBSplineTransformPython.itkBSplineTransformD33_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineTransformD33

        Create a new object of the class itkBSplineTransformD33 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineTransformD33.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineTransformD33.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineTransformD33.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineTransformD33 in _itkBSplineTransformPython:
_itkBSplineTransformPython.itkBSplineTransformD33_swigregister(itkBSplineTransformD33)
itkBSplineTransformD33___New_orig__ = _itkBSplineTransformPython.itkBSplineTransformD33___New_orig__
itkBSplineTransformD33_cast = _itkBSplineTransformPython.itkBSplineTransformD33_cast



