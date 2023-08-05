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
    from . import _itkKernelTransformPython
else:
    import _itkKernelTransformPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkKernelTransformPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkKernelTransformPython.SWIG_PyStaticMethod_New

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
import stdcomplexPython
import vnl_matrixPython
import itkPointSetPython
import ITKCommonBasePython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkCovariantVectorPython
import itkVectorContainerPython
import itkContinuousIndexPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkTransformBasePython
import itkSymmetricSecondRankTensorPython
import itkArrayPython
import itkDiffusionTensor3DPython
import itkOptimizerParametersPython
import itkArray2DPython
import itkVariableLengthVectorPython

def itkKernelTransformD3_New():
  return itkKernelTransformD3.New()


def itkKernelTransformD2_New():
  return itkKernelTransformD2.New()

class itkKernelTransformD2(itkTransformBasePython.itkTransformD22):
    r"""Proxy of C++ itkKernelTransformD2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkKernelTransformPython.itkKernelTransformD2___New_orig__)
    Clone = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD2_Clone)
    GetModifiableSourceLandmarks = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD2_GetModifiableSourceLandmarks)
    GetSourceLandmarks = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD2_GetSourceLandmarks)
    SetSourceLandmarks = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD2_SetSourceLandmarks)
    GetModifiableTargetLandmarks = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD2_GetModifiableTargetLandmarks)
    GetTargetLandmarks = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD2_GetTargetLandmarks)
    SetTargetLandmarks = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD2_SetTargetLandmarks)
    GetModifiableDisplacements = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD2_GetModifiableDisplacements)
    GetDisplacements = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD2_GetDisplacements)
    ComputeWMatrix = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD2_ComputeWMatrix)
    TransformVector = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD2_TransformVector)
    UpdateParameters = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD2_UpdateParameters)
    SetStiffness = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD2_SetStiffness)
    GetStiffness = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD2_GetStiffness)
    __swig_destroy__ = _itkKernelTransformPython.delete_itkKernelTransformD2
    cast = _swig_new_static_method(_itkKernelTransformPython.itkKernelTransformD2_cast)

    def New(*args, **kargs):
        """New() -> itkKernelTransformD2

        Create a new object of the class itkKernelTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkKernelTransformD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkKernelTransformD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkKernelTransformD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkKernelTransformD2 in _itkKernelTransformPython:
_itkKernelTransformPython.itkKernelTransformD2_swigregister(itkKernelTransformD2)
itkKernelTransformD2___New_orig__ = _itkKernelTransformPython.itkKernelTransformD2___New_orig__
itkKernelTransformD2_cast = _itkKernelTransformPython.itkKernelTransformD2_cast

class itkKernelTransformD3(itkTransformBasePython.itkTransformD33):
    r"""Proxy of C++ itkKernelTransformD3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkKernelTransformPython.itkKernelTransformD3___New_orig__)
    Clone = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD3_Clone)
    GetModifiableSourceLandmarks = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD3_GetModifiableSourceLandmarks)
    GetSourceLandmarks = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD3_GetSourceLandmarks)
    SetSourceLandmarks = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD3_SetSourceLandmarks)
    GetModifiableTargetLandmarks = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD3_GetModifiableTargetLandmarks)
    GetTargetLandmarks = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD3_GetTargetLandmarks)
    SetTargetLandmarks = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD3_SetTargetLandmarks)
    GetModifiableDisplacements = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD3_GetModifiableDisplacements)
    GetDisplacements = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD3_GetDisplacements)
    ComputeWMatrix = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD3_ComputeWMatrix)
    TransformVector = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD3_TransformVector)
    UpdateParameters = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD3_UpdateParameters)
    SetStiffness = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD3_SetStiffness)
    GetStiffness = _swig_new_instance_method(_itkKernelTransformPython.itkKernelTransformD3_GetStiffness)
    __swig_destroy__ = _itkKernelTransformPython.delete_itkKernelTransformD3
    cast = _swig_new_static_method(_itkKernelTransformPython.itkKernelTransformD3_cast)

    def New(*args, **kargs):
        """New() -> itkKernelTransformD3

        Create a new object of the class itkKernelTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkKernelTransformD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkKernelTransformD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkKernelTransformD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkKernelTransformD3 in _itkKernelTransformPython:
_itkKernelTransformPython.itkKernelTransformD3_swigregister(itkKernelTransformD3)
itkKernelTransformD3___New_orig__ = _itkKernelTransformPython.itkKernelTransformD3___New_orig__
itkKernelTransformD3_cast = _itkKernelTransformPython.itkKernelTransformD3_cast



