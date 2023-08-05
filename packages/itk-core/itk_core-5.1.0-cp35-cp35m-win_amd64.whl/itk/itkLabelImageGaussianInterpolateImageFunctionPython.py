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
    from . import _itkLabelImageGaussianInterpolateImageFunctionPython
else:
    import _itkLabelImageGaussianInterpolateImageFunctionPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkLabelImageGaussianInterpolateImageFunctionPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkLabelImageGaussianInterpolateImageFunctionPython.SWIG_PyStaticMethod_New

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


import itkGaussianInterpolateImageFunctionPython
import vnl_vectorPython
import stdcomplexPython
import pyBasePython
import vnl_matrixPython
import itkInterpolateImageFunctionPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkRGBAPixelPython
import itkFixedArrayPython
import itkRGBPixelPython
import itkCovariantVectorPython
import itkVectorPython
import vnl_vector_refPython
import itkPointPython
import itkImageFunctionBasePython
import itkImagePython
import ITKCommonBasePython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkImageRegionPython
import itkSymmetricSecondRankTensorPython
import itkContinuousIndexPython
import itkFunctionBasePython
import itkArrayPython

def itkLabelImageGaussianInterpolateImageFunctionIUS3D_New():
  return itkLabelImageGaussianInterpolateImageFunctionIUS3D.New()


def itkLabelImageGaussianInterpolateImageFunctionIUC3D_New():
  return itkLabelImageGaussianInterpolateImageFunctionIUC3D.New()


def itkLabelImageGaussianInterpolateImageFunctionISS3D_New():
  return itkLabelImageGaussianInterpolateImageFunctionISS3D.New()


def itkLabelImageGaussianInterpolateImageFunctionIUS2D_New():
  return itkLabelImageGaussianInterpolateImageFunctionIUS2D.New()


def itkLabelImageGaussianInterpolateImageFunctionIUC2D_New():
  return itkLabelImageGaussianInterpolateImageFunctionIUC2D.New()


def itkLabelImageGaussianInterpolateImageFunctionISS2D_New():
  return itkLabelImageGaussianInterpolateImageFunctionISS2D.New()

class itkLabelImageGaussianInterpolateImageFunctionISS2D(itkGaussianInterpolateImageFunctionPython.itkGaussianInterpolateImageFunctionISS2D):
    r"""Proxy of C++ itkLabelImageGaussianInterpolateImageFunctionISS2D class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionISS2D___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionISS2D_Clone)
    __swig_destroy__ = _itkLabelImageGaussianInterpolateImageFunctionPython.delete_itkLabelImageGaussianInterpolateImageFunctionISS2D
    cast = _swig_new_static_method(_itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionISS2D_cast)

    def New(*args, **kargs):
        """New() -> itkLabelImageGaussianInterpolateImageFunctionISS2D

        Create a new object of the class itkLabelImageGaussianInterpolateImageFunctionISS2D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelImageGaussianInterpolateImageFunctionISS2D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelImageGaussianInterpolateImageFunctionISS2D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelImageGaussianInterpolateImageFunctionISS2D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelImageGaussianInterpolateImageFunctionISS2D in _itkLabelImageGaussianInterpolateImageFunctionPython:
_itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionISS2D_swigregister(itkLabelImageGaussianInterpolateImageFunctionISS2D)
itkLabelImageGaussianInterpolateImageFunctionISS2D___New_orig__ = _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionISS2D___New_orig__
itkLabelImageGaussianInterpolateImageFunctionISS2D_cast = _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionISS2D_cast

class itkLabelImageGaussianInterpolateImageFunctionISS3D(itkGaussianInterpolateImageFunctionPython.itkGaussianInterpolateImageFunctionISS3D):
    r"""Proxy of C++ itkLabelImageGaussianInterpolateImageFunctionISS3D class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionISS3D___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionISS3D_Clone)
    __swig_destroy__ = _itkLabelImageGaussianInterpolateImageFunctionPython.delete_itkLabelImageGaussianInterpolateImageFunctionISS3D
    cast = _swig_new_static_method(_itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionISS3D_cast)

    def New(*args, **kargs):
        """New() -> itkLabelImageGaussianInterpolateImageFunctionISS3D

        Create a new object of the class itkLabelImageGaussianInterpolateImageFunctionISS3D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelImageGaussianInterpolateImageFunctionISS3D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelImageGaussianInterpolateImageFunctionISS3D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelImageGaussianInterpolateImageFunctionISS3D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelImageGaussianInterpolateImageFunctionISS3D in _itkLabelImageGaussianInterpolateImageFunctionPython:
_itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionISS3D_swigregister(itkLabelImageGaussianInterpolateImageFunctionISS3D)
itkLabelImageGaussianInterpolateImageFunctionISS3D___New_orig__ = _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionISS3D___New_orig__
itkLabelImageGaussianInterpolateImageFunctionISS3D_cast = _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionISS3D_cast

class itkLabelImageGaussianInterpolateImageFunctionIUC2D(itkGaussianInterpolateImageFunctionPython.itkGaussianInterpolateImageFunctionIUC2D):
    r"""Proxy of C++ itkLabelImageGaussianInterpolateImageFunctionIUC2D class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUC2D___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUC2D_Clone)
    __swig_destroy__ = _itkLabelImageGaussianInterpolateImageFunctionPython.delete_itkLabelImageGaussianInterpolateImageFunctionIUC2D
    cast = _swig_new_static_method(_itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUC2D_cast)

    def New(*args, **kargs):
        """New() -> itkLabelImageGaussianInterpolateImageFunctionIUC2D

        Create a new object of the class itkLabelImageGaussianInterpolateImageFunctionIUC2D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelImageGaussianInterpolateImageFunctionIUC2D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelImageGaussianInterpolateImageFunctionIUC2D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelImageGaussianInterpolateImageFunctionIUC2D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelImageGaussianInterpolateImageFunctionIUC2D in _itkLabelImageGaussianInterpolateImageFunctionPython:
_itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUC2D_swigregister(itkLabelImageGaussianInterpolateImageFunctionIUC2D)
itkLabelImageGaussianInterpolateImageFunctionIUC2D___New_orig__ = _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUC2D___New_orig__
itkLabelImageGaussianInterpolateImageFunctionIUC2D_cast = _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUC2D_cast

class itkLabelImageGaussianInterpolateImageFunctionIUC3D(itkGaussianInterpolateImageFunctionPython.itkGaussianInterpolateImageFunctionIUC3D):
    r"""Proxy of C++ itkLabelImageGaussianInterpolateImageFunctionIUC3D class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUC3D___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUC3D_Clone)
    __swig_destroy__ = _itkLabelImageGaussianInterpolateImageFunctionPython.delete_itkLabelImageGaussianInterpolateImageFunctionIUC3D
    cast = _swig_new_static_method(_itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUC3D_cast)

    def New(*args, **kargs):
        """New() -> itkLabelImageGaussianInterpolateImageFunctionIUC3D

        Create a new object of the class itkLabelImageGaussianInterpolateImageFunctionIUC3D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelImageGaussianInterpolateImageFunctionIUC3D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelImageGaussianInterpolateImageFunctionIUC3D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelImageGaussianInterpolateImageFunctionIUC3D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelImageGaussianInterpolateImageFunctionIUC3D in _itkLabelImageGaussianInterpolateImageFunctionPython:
_itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUC3D_swigregister(itkLabelImageGaussianInterpolateImageFunctionIUC3D)
itkLabelImageGaussianInterpolateImageFunctionIUC3D___New_orig__ = _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUC3D___New_orig__
itkLabelImageGaussianInterpolateImageFunctionIUC3D_cast = _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUC3D_cast

class itkLabelImageGaussianInterpolateImageFunctionIUS2D(itkGaussianInterpolateImageFunctionPython.itkGaussianInterpolateImageFunctionIUS2D):
    r"""Proxy of C++ itkLabelImageGaussianInterpolateImageFunctionIUS2D class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUS2D___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUS2D_Clone)
    __swig_destroy__ = _itkLabelImageGaussianInterpolateImageFunctionPython.delete_itkLabelImageGaussianInterpolateImageFunctionIUS2D
    cast = _swig_new_static_method(_itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUS2D_cast)

    def New(*args, **kargs):
        """New() -> itkLabelImageGaussianInterpolateImageFunctionIUS2D

        Create a new object of the class itkLabelImageGaussianInterpolateImageFunctionIUS2D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelImageGaussianInterpolateImageFunctionIUS2D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelImageGaussianInterpolateImageFunctionIUS2D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelImageGaussianInterpolateImageFunctionIUS2D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelImageGaussianInterpolateImageFunctionIUS2D in _itkLabelImageGaussianInterpolateImageFunctionPython:
_itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUS2D_swigregister(itkLabelImageGaussianInterpolateImageFunctionIUS2D)
itkLabelImageGaussianInterpolateImageFunctionIUS2D___New_orig__ = _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUS2D___New_orig__
itkLabelImageGaussianInterpolateImageFunctionIUS2D_cast = _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUS2D_cast

class itkLabelImageGaussianInterpolateImageFunctionIUS3D(itkGaussianInterpolateImageFunctionPython.itkGaussianInterpolateImageFunctionIUS3D):
    r"""Proxy of C++ itkLabelImageGaussianInterpolateImageFunctionIUS3D class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUS3D___New_orig__)
    Clone = _swig_new_instance_method(_itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUS3D_Clone)
    __swig_destroy__ = _itkLabelImageGaussianInterpolateImageFunctionPython.delete_itkLabelImageGaussianInterpolateImageFunctionIUS3D
    cast = _swig_new_static_method(_itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUS3D_cast)

    def New(*args, **kargs):
        """New() -> itkLabelImageGaussianInterpolateImageFunctionIUS3D

        Create a new object of the class itkLabelImageGaussianInterpolateImageFunctionIUS3D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelImageGaussianInterpolateImageFunctionIUS3D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelImageGaussianInterpolateImageFunctionIUS3D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelImageGaussianInterpolateImageFunctionIUS3D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLabelImageGaussianInterpolateImageFunctionIUS3D in _itkLabelImageGaussianInterpolateImageFunctionPython:
_itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUS3D_swigregister(itkLabelImageGaussianInterpolateImageFunctionIUS3D)
itkLabelImageGaussianInterpolateImageFunctionIUS3D___New_orig__ = _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUS3D___New_orig__
itkLabelImageGaussianInterpolateImageFunctionIUS3D_cast = _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUS3D_cast



