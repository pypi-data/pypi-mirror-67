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
    from . import _itkCenteredRigid2DTransformPython
else:
    import _itkCenteredRigid2DTransformPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkCenteredRigid2DTransformPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkCenteredRigid2DTransformPython.SWIG_PyStaticMethod_New

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


import itkTransformBasePython
import itkVectorPython
import itkFixedArrayPython
import pyBasePython
import vnl_vector_refPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkCovariantVectorPython
import itkArrayPython
import itkDiffusionTensor3DPython
import ITKCommonBasePython
import itkOptimizerParametersPython
import itkArray2DPython
import itkVariableLengthVectorPython
import itkRigid2DTransformPython
import itkMatrixOffsetTransformBasePython

def itkCenteredRigid2DTransformD_New():
  return itkCenteredRigid2DTransformD.New()

class itkCenteredRigid2DTransformD(itkRigid2DTransformPython.itkRigid2DTransformD):
    r"""Proxy of C++ itkCenteredRigid2DTransformD class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCenteredRigid2DTransformPython.itkCenteredRigid2DTransformD___New_orig__)
    Clone = _swig_new_instance_method(_itkCenteredRigid2DTransformPython.itkCenteredRigid2DTransformD_Clone)
    CloneInverseTo = _swig_new_instance_method(_itkCenteredRigid2DTransformPython.itkCenteredRigid2DTransformD_CloneInverseTo)
    GetInverse = _swig_new_instance_method(_itkCenteredRigid2DTransformPython.itkCenteredRigid2DTransformD_GetInverse)
    CloneTo = _swig_new_instance_method(_itkCenteredRigid2DTransformPython.itkCenteredRigid2DTransformD_CloneTo)
    __swig_destroy__ = _itkCenteredRigid2DTransformPython.delete_itkCenteredRigid2DTransformD
    cast = _swig_new_static_method(_itkCenteredRigid2DTransformPython.itkCenteredRigid2DTransformD_cast)

    def New(*args, **kargs):
        """New() -> itkCenteredRigid2DTransformD

        Create a new object of the class itkCenteredRigid2DTransformD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCenteredRigid2DTransformD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCenteredRigid2DTransformD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCenteredRigid2DTransformD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCenteredRigid2DTransformD in _itkCenteredRigid2DTransformPython:
_itkCenteredRigid2DTransformPython.itkCenteredRigid2DTransformD_swigregister(itkCenteredRigid2DTransformD)
itkCenteredRigid2DTransformD___New_orig__ = _itkCenteredRigid2DTransformPython.itkCenteredRigid2DTransformD___New_orig__
itkCenteredRigid2DTransformD_cast = _itkCenteredRigid2DTransformPython.itkCenteredRigid2DTransformD_cast



