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
    from . import _itkAffineTransformPython
else:
    import _itkAffineTransformPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkAffineTransformPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkAffineTransformPython.SWIG_PyStaticMethod_New

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
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkCovariantVectorPython
import itkTransformBasePython
import itkSymmetricSecondRankTensorPython
import itkArrayPython
import itkDiffusionTensor3DPython
import ITKCommonBasePython
import itkOptimizerParametersPython
import itkArray2DPython
import itkVariableLengthVectorPython
import itkMatrixOffsetTransformBasePython

def itkAffineTransformD3_New():
  return itkAffineTransformD3.New()


def itkAffineTransformD2_New():
  return itkAffineTransformD2.New()

class itkAffineTransformD2(itkMatrixOffsetTransformBasePython.itkMatrixOffsetTransformBaseD22):
    r"""Proxy of C++ itkAffineTransformD2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAffineTransformPython.itkAffineTransformD2___New_orig__)
    Clone = _swig_new_instance_method(_itkAffineTransformPython.itkAffineTransformD2_Clone)
    Translate = _swig_new_instance_method(_itkAffineTransformPython.itkAffineTransformD2_Translate)
    Scale = _swig_new_instance_method(_itkAffineTransformPython.itkAffineTransformD2_Scale)
    Rotate = _swig_new_instance_method(_itkAffineTransformPython.itkAffineTransformD2_Rotate)
    Rotate2D = _swig_new_instance_method(_itkAffineTransformPython.itkAffineTransformD2_Rotate2D)
    Rotate3D = _swig_new_instance_method(_itkAffineTransformPython.itkAffineTransformD2_Rotate3D)
    Shear = _swig_new_instance_method(_itkAffineTransformPython.itkAffineTransformD2_Shear)
    GetInverse = _swig_new_instance_method(_itkAffineTransformPython.itkAffineTransformD2_GetInverse)
    Metric = _swig_new_instance_method(_itkAffineTransformPython.itkAffineTransformD2_Metric)
    __swig_destroy__ = _itkAffineTransformPython.delete_itkAffineTransformD2
    cast = _swig_new_static_method(_itkAffineTransformPython.itkAffineTransformD2_cast)

    def New(*args, **kargs):
        """New() -> itkAffineTransformD2

        Create a new object of the class itkAffineTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAffineTransformD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAffineTransformD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAffineTransformD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAffineTransformD2 in _itkAffineTransformPython:
_itkAffineTransformPython.itkAffineTransformD2_swigregister(itkAffineTransformD2)
itkAffineTransformD2___New_orig__ = _itkAffineTransformPython.itkAffineTransformD2___New_orig__
itkAffineTransformD2_cast = _itkAffineTransformPython.itkAffineTransformD2_cast

class itkAffineTransformD3(itkMatrixOffsetTransformBasePython.itkMatrixOffsetTransformBaseD33):
    r"""Proxy of C++ itkAffineTransformD3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAffineTransformPython.itkAffineTransformD3___New_orig__)
    Clone = _swig_new_instance_method(_itkAffineTransformPython.itkAffineTransformD3_Clone)
    Translate = _swig_new_instance_method(_itkAffineTransformPython.itkAffineTransformD3_Translate)
    Scale = _swig_new_instance_method(_itkAffineTransformPython.itkAffineTransformD3_Scale)
    Rotate = _swig_new_instance_method(_itkAffineTransformPython.itkAffineTransformD3_Rotate)
    Rotate2D = _swig_new_instance_method(_itkAffineTransformPython.itkAffineTransformD3_Rotate2D)
    Rotate3D = _swig_new_instance_method(_itkAffineTransformPython.itkAffineTransformD3_Rotate3D)
    Shear = _swig_new_instance_method(_itkAffineTransformPython.itkAffineTransformD3_Shear)
    GetInverse = _swig_new_instance_method(_itkAffineTransformPython.itkAffineTransformD3_GetInverse)
    Metric = _swig_new_instance_method(_itkAffineTransformPython.itkAffineTransformD3_Metric)
    __swig_destroy__ = _itkAffineTransformPython.delete_itkAffineTransformD3
    cast = _swig_new_static_method(_itkAffineTransformPython.itkAffineTransformD3_cast)

    def New(*args, **kargs):
        """New() -> itkAffineTransformD3

        Create a new object of the class itkAffineTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAffineTransformD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAffineTransformD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAffineTransformD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAffineTransformD3 in _itkAffineTransformPython:
_itkAffineTransformPython.itkAffineTransformD3_swigregister(itkAffineTransformD3)
itkAffineTransformD3___New_orig__ = _itkAffineTransformPython.itkAffineTransformD3___New_orig__
itkAffineTransformD3_cast = _itkAffineTransformPython.itkAffineTransformD3_cast



