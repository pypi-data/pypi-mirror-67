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
    from . import _itkCompositeTransformPython
else:
    import _itkCompositeTransformPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkCompositeTransformPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkCompositeTransformPython.SWIG_PyStaticMethod_New

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
import vnl_vector_refPython
import stdcomplexPython
import pyBasePython
import vnl_vectorPython
import vnl_matrixPython
import itkFixedArrayPython
import itkPointPython
import itkCovariantVectorPython
import itkArray2DPython
import ITKCommonBasePython
import itkArrayPython
import itkVariableLengthVectorPython
import itkOptimizerParametersPython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkMultiTransformPython
import itkTransformBasePython

def itkCompositeTransformD3_New():
  return itkCompositeTransformD3.New()


def itkCompositeTransformD2_New():
  return itkCompositeTransformD2.New()

class itkCompositeTransformD2(itkMultiTransformPython.itkMultiTransformD22):
    r"""Proxy of C++ itkCompositeTransformD2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCompositeTransformPython.itkCompositeTransformD2___New_orig__)
    Clone = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_Clone)
    SetNthTransformToOptimize = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_SetNthTransformToOptimize)
    SetNthTransformToOptimizeOn = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_SetNthTransformToOptimizeOn)
    SetNthTransformToOptimizeOff = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_SetNthTransformToOptimizeOff)
    SetAllTransformsToOptimize = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_SetAllTransformsToOptimize)
    SetAllTransformsToOptimizeOn = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_SetAllTransformsToOptimizeOn)
    SetAllTransformsToOptimizeOff = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_SetAllTransformsToOptimizeOff)
    SetOnlyMostRecentTransformToOptimizeOn = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_SetOnlyMostRecentTransformToOptimizeOn)
    GetNthTransformToOptimize = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_GetNthTransformToOptimize)
    GetTransformsToOptimizeFlags = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_GetTransformsToOptimizeFlags)
    GetInverse = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_GetInverse)
    TransformVector = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_TransformVector)
    TransformCovariantVector = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_TransformCovariantVector)
    TransformDiffusionTensor3D = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_TransformDiffusionTensor3D)
    TransformSymmetricSecondRankTensor = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_TransformSymmetricSecondRankTensor)
    UpdateTransformParameters = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_UpdateTransformParameters)
    FlattenTransformQueue = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD2_FlattenTransformQueue)
    __swig_destroy__ = _itkCompositeTransformPython.delete_itkCompositeTransformD2
    cast = _swig_new_static_method(_itkCompositeTransformPython.itkCompositeTransformD2_cast)

    def New(*args, **kargs):
        """New() -> itkCompositeTransformD2

        Create a new object of the class itkCompositeTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCompositeTransformD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCompositeTransformD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCompositeTransformD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCompositeTransformD2 in _itkCompositeTransformPython:
_itkCompositeTransformPython.itkCompositeTransformD2_swigregister(itkCompositeTransformD2)
itkCompositeTransformD2___New_orig__ = _itkCompositeTransformPython.itkCompositeTransformD2___New_orig__
itkCompositeTransformD2_cast = _itkCompositeTransformPython.itkCompositeTransformD2_cast

class itkCompositeTransformD3(itkMultiTransformPython.itkMultiTransformD33):
    r"""Proxy of C++ itkCompositeTransformD3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCompositeTransformPython.itkCompositeTransformD3___New_orig__)
    Clone = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_Clone)
    SetNthTransformToOptimize = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_SetNthTransformToOptimize)
    SetNthTransformToOptimizeOn = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_SetNthTransformToOptimizeOn)
    SetNthTransformToOptimizeOff = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_SetNthTransformToOptimizeOff)
    SetAllTransformsToOptimize = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_SetAllTransformsToOptimize)
    SetAllTransformsToOptimizeOn = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_SetAllTransformsToOptimizeOn)
    SetAllTransformsToOptimizeOff = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_SetAllTransformsToOptimizeOff)
    SetOnlyMostRecentTransformToOptimizeOn = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_SetOnlyMostRecentTransformToOptimizeOn)
    GetNthTransformToOptimize = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_GetNthTransformToOptimize)
    GetTransformsToOptimizeFlags = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_GetTransformsToOptimizeFlags)
    GetInverse = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_GetInverse)
    TransformVector = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_TransformVector)
    TransformCovariantVector = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_TransformCovariantVector)
    TransformDiffusionTensor3D = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_TransformDiffusionTensor3D)
    TransformSymmetricSecondRankTensor = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_TransformSymmetricSecondRankTensor)
    UpdateTransformParameters = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_UpdateTransformParameters)
    FlattenTransformQueue = _swig_new_instance_method(_itkCompositeTransformPython.itkCompositeTransformD3_FlattenTransformQueue)
    __swig_destroy__ = _itkCompositeTransformPython.delete_itkCompositeTransformD3
    cast = _swig_new_static_method(_itkCompositeTransformPython.itkCompositeTransformD3_cast)

    def New(*args, **kargs):
        """New() -> itkCompositeTransformD3

        Create a new object of the class itkCompositeTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCompositeTransformD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCompositeTransformD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCompositeTransformD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCompositeTransformD3 in _itkCompositeTransformPython:
_itkCompositeTransformPython.itkCompositeTransformD3_swigregister(itkCompositeTransformD3)
itkCompositeTransformD3___New_orig__ = _itkCompositeTransformPython.itkCompositeTransformD3___New_orig__
itkCompositeTransformD3_cast = _itkCompositeTransformPython.itkCompositeTransformD3_cast



