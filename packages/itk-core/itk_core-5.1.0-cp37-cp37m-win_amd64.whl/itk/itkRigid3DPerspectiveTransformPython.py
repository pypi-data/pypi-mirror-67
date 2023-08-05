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
    from . import _itkRigid3DPerspectiveTransformPython
else:
    import _itkRigid3DPerspectiveTransformPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkRigid3DPerspectiveTransformPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkRigid3DPerspectiveTransformPython.SWIG_PyStaticMethod_New

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
import itkCovariantVectorPython
import itkArray2DPython
import ITKCommonBasePython
import itkPointPython
import itkVersorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkOptimizerParametersPython
import itkArrayPython
import itkTransformBasePython
import itkVariableLengthVectorPython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython

def itkRigid3DPerspectiveTransformD_New():
  return itkRigid3DPerspectiveTransformD.New()

class itkRigid3DPerspectiveTransformD(itkTransformBasePython.itkTransformD32):
    r"""Proxy of C++ itkRigid3DPerspectiveTransformD class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD___New_orig__)
    Clone = _swig_new_instance_method(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_Clone)
    GetOffset = _swig_new_instance_method(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_GetOffset)
    GetRotation = _swig_new_instance_method(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_GetRotation)
    SetOffset = _swig_new_instance_method(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_SetOffset)
    SetRotation = _swig_new_instance_method(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_SetRotation)
    SetFocalDistance = _swig_new_instance_method(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_SetFocalDistance)
    GetFocalDistance = _swig_new_instance_method(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_GetFocalDistance)
    TransformVector = _swig_new_instance_method(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_TransformVector)
    GetRotationMatrix = _swig_new_instance_method(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_GetRotationMatrix)
    ComputeMatrix = _swig_new_instance_method(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_ComputeMatrix)
    GetFixedOffset = _swig_new_instance_method(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_GetFixedOffset)
    SetFixedOffset = _swig_new_instance_method(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_SetFixedOffset)
    SetCenterOfRotation = _swig_new_instance_method(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_SetCenterOfRotation)
    GetCenterOfRotation = _swig_new_instance_method(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_GetCenterOfRotation)
    __swig_destroy__ = _itkRigid3DPerspectiveTransformPython.delete_itkRigid3DPerspectiveTransformD
    cast = _swig_new_static_method(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_cast)

    def New(*args, **kargs):
        """New() -> itkRigid3DPerspectiveTransformD

        Create a new object of the class itkRigid3DPerspectiveTransformD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRigid3DPerspectiveTransformD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRigid3DPerspectiveTransformD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRigid3DPerspectiveTransformD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRigid3DPerspectiveTransformD in _itkRigid3DPerspectiveTransformPython:
_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_swigregister(itkRigid3DPerspectiveTransformD)
itkRigid3DPerspectiveTransformD___New_orig__ = _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD___New_orig__
itkRigid3DPerspectiveTransformD_cast = _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_cast



