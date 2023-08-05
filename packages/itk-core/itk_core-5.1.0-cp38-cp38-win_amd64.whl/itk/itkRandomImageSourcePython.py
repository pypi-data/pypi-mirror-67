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
    from . import _itkRandomImageSourcePython
else:
    import _itkRandomImageSourcePython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkRandomImageSourcePython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkRandomImageSourcePython.SWIG_PyStaticMethod_New

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


import itkMatrixPython
import vnl_matrixPython
import stdcomplexPython
import pyBasePython
import vnl_vectorPython
import vnl_matrix_fixedPython
import itkPointPython
import itkFixedArrayPython
import itkVectorPython
import vnl_vector_refPython
import itkCovariantVectorPython
import itkImageSourcePython
import ITKCommonBasePython
import itkVectorImagePython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkVariableLengthVectorPython
import itkImagePython
import itkSymmetricSecondRankTensorPython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkImageRegionPython
import itkImageSourceCommonPython

def itkRandomImageSourceID3_New():
  return itkRandomImageSourceID3.New()


def itkRandomImageSourceID2_New():
  return itkRandomImageSourceID2.New()


def itkRandomImageSourceIF3_New():
  return itkRandomImageSourceIF3.New()


def itkRandomImageSourceIF2_New():
  return itkRandomImageSourceIF2.New()


def itkRandomImageSourceIUS3_New():
  return itkRandomImageSourceIUS3.New()


def itkRandomImageSourceIUS2_New():
  return itkRandomImageSourceIUS2.New()


def itkRandomImageSourceIUC3_New():
  return itkRandomImageSourceIUC3.New()


def itkRandomImageSourceIUC2_New():
  return itkRandomImageSourceIUC2.New()


def itkRandomImageSourceISS3_New():
  return itkRandomImageSourceISS3.New()


def itkRandomImageSourceISS2_New():
  return itkRandomImageSourceISS2.New()

class itkRandomImageSourceID2(itkImageSourcePython.itkImageSourceID2):
    r"""Proxy of C++ itkRandomImageSourceID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRandomImageSourcePython.itkRandomImageSourceID2___New_orig__)
    Clone = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceID2_Clone)
    SetSize = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceID2_SetSize)
    GetSize = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceID2_GetSize)
    SetSpacing = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceID2_SetSpacing)
    GetSpacing = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceID2_GetSpacing)
    SetOrigin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceID2_SetOrigin)
    GetOrigin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceID2_GetOrigin)
    SetDirection = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceID2_SetDirection)
    GetDirection = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceID2_GetDirection)
    SetMin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceID2_SetMin)
    GetMin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceID2_GetMin)
    SetMax = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceID2_SetMax)
    GetMax = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceID2_GetMax)
    __swig_destroy__ = _itkRandomImageSourcePython.delete_itkRandomImageSourceID2
    cast = _swig_new_static_method(_itkRandomImageSourcePython.itkRandomImageSourceID2_cast)

    def New(*args, **kargs):
        """New() -> itkRandomImageSourceID2

        Create a new object of the class itkRandomImageSourceID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRandomImageSourceID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRandomImageSourceID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRandomImageSourceID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRandomImageSourceID2 in _itkRandomImageSourcePython:
_itkRandomImageSourcePython.itkRandomImageSourceID2_swigregister(itkRandomImageSourceID2)
itkRandomImageSourceID2___New_orig__ = _itkRandomImageSourcePython.itkRandomImageSourceID2___New_orig__
itkRandomImageSourceID2_cast = _itkRandomImageSourcePython.itkRandomImageSourceID2_cast

class itkRandomImageSourceID3(itkImageSourcePython.itkImageSourceID3):
    r"""Proxy of C++ itkRandomImageSourceID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRandomImageSourcePython.itkRandomImageSourceID3___New_orig__)
    Clone = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceID3_Clone)
    SetSize = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceID3_SetSize)
    GetSize = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceID3_GetSize)
    SetSpacing = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceID3_SetSpacing)
    GetSpacing = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceID3_GetSpacing)
    SetOrigin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceID3_SetOrigin)
    GetOrigin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceID3_GetOrigin)
    SetDirection = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceID3_SetDirection)
    GetDirection = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceID3_GetDirection)
    SetMin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceID3_SetMin)
    GetMin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceID3_GetMin)
    SetMax = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceID3_SetMax)
    GetMax = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceID3_GetMax)
    __swig_destroy__ = _itkRandomImageSourcePython.delete_itkRandomImageSourceID3
    cast = _swig_new_static_method(_itkRandomImageSourcePython.itkRandomImageSourceID3_cast)

    def New(*args, **kargs):
        """New() -> itkRandomImageSourceID3

        Create a new object of the class itkRandomImageSourceID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRandomImageSourceID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRandomImageSourceID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRandomImageSourceID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRandomImageSourceID3 in _itkRandomImageSourcePython:
_itkRandomImageSourcePython.itkRandomImageSourceID3_swigregister(itkRandomImageSourceID3)
itkRandomImageSourceID3___New_orig__ = _itkRandomImageSourcePython.itkRandomImageSourceID3___New_orig__
itkRandomImageSourceID3_cast = _itkRandomImageSourcePython.itkRandomImageSourceID3_cast

class itkRandomImageSourceIF2(itkImageSourcePython.itkImageSourceIF2):
    r"""Proxy of C++ itkRandomImageSourceIF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRandomImageSourcePython.itkRandomImageSourceIF2___New_orig__)
    Clone = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIF2_Clone)
    SetSize = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIF2_SetSize)
    GetSize = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIF2_GetSize)
    SetSpacing = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIF2_SetSpacing)
    GetSpacing = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIF2_GetSpacing)
    SetOrigin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIF2_SetOrigin)
    GetOrigin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIF2_GetOrigin)
    SetDirection = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIF2_SetDirection)
    GetDirection = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIF2_GetDirection)
    SetMin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIF2_SetMin)
    GetMin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIF2_GetMin)
    SetMax = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIF2_SetMax)
    GetMax = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIF2_GetMax)
    __swig_destroy__ = _itkRandomImageSourcePython.delete_itkRandomImageSourceIF2
    cast = _swig_new_static_method(_itkRandomImageSourcePython.itkRandomImageSourceIF2_cast)

    def New(*args, **kargs):
        """New() -> itkRandomImageSourceIF2

        Create a new object of the class itkRandomImageSourceIF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRandomImageSourceIF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRandomImageSourceIF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRandomImageSourceIF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRandomImageSourceIF2 in _itkRandomImageSourcePython:
_itkRandomImageSourcePython.itkRandomImageSourceIF2_swigregister(itkRandomImageSourceIF2)
itkRandomImageSourceIF2___New_orig__ = _itkRandomImageSourcePython.itkRandomImageSourceIF2___New_orig__
itkRandomImageSourceIF2_cast = _itkRandomImageSourcePython.itkRandomImageSourceIF2_cast

class itkRandomImageSourceIF3(itkImageSourcePython.itkImageSourceIF3):
    r"""Proxy of C++ itkRandomImageSourceIF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRandomImageSourcePython.itkRandomImageSourceIF3___New_orig__)
    Clone = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIF3_Clone)
    SetSize = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIF3_SetSize)
    GetSize = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIF3_GetSize)
    SetSpacing = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIF3_SetSpacing)
    GetSpacing = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIF3_GetSpacing)
    SetOrigin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIF3_SetOrigin)
    GetOrigin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIF3_GetOrigin)
    SetDirection = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIF3_SetDirection)
    GetDirection = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIF3_GetDirection)
    SetMin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIF3_SetMin)
    GetMin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIF3_GetMin)
    SetMax = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIF3_SetMax)
    GetMax = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIF3_GetMax)
    __swig_destroy__ = _itkRandomImageSourcePython.delete_itkRandomImageSourceIF3
    cast = _swig_new_static_method(_itkRandomImageSourcePython.itkRandomImageSourceIF3_cast)

    def New(*args, **kargs):
        """New() -> itkRandomImageSourceIF3

        Create a new object of the class itkRandomImageSourceIF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRandomImageSourceIF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRandomImageSourceIF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRandomImageSourceIF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRandomImageSourceIF3 in _itkRandomImageSourcePython:
_itkRandomImageSourcePython.itkRandomImageSourceIF3_swigregister(itkRandomImageSourceIF3)
itkRandomImageSourceIF3___New_orig__ = _itkRandomImageSourcePython.itkRandomImageSourceIF3___New_orig__
itkRandomImageSourceIF3_cast = _itkRandomImageSourcePython.itkRandomImageSourceIF3_cast

class itkRandomImageSourceISS2(itkImageSourcePython.itkImageSourceISS2):
    r"""Proxy of C++ itkRandomImageSourceISS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRandomImageSourcePython.itkRandomImageSourceISS2___New_orig__)
    Clone = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceISS2_Clone)
    SetSize = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceISS2_SetSize)
    GetSize = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceISS2_GetSize)
    SetSpacing = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceISS2_SetSpacing)
    GetSpacing = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceISS2_GetSpacing)
    SetOrigin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceISS2_SetOrigin)
    GetOrigin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceISS2_GetOrigin)
    SetDirection = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceISS2_SetDirection)
    GetDirection = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceISS2_GetDirection)
    SetMin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceISS2_SetMin)
    GetMin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceISS2_GetMin)
    SetMax = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceISS2_SetMax)
    GetMax = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceISS2_GetMax)
    __swig_destroy__ = _itkRandomImageSourcePython.delete_itkRandomImageSourceISS2
    cast = _swig_new_static_method(_itkRandomImageSourcePython.itkRandomImageSourceISS2_cast)

    def New(*args, **kargs):
        """New() -> itkRandomImageSourceISS2

        Create a new object of the class itkRandomImageSourceISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRandomImageSourceISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRandomImageSourceISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRandomImageSourceISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRandomImageSourceISS2 in _itkRandomImageSourcePython:
_itkRandomImageSourcePython.itkRandomImageSourceISS2_swigregister(itkRandomImageSourceISS2)
itkRandomImageSourceISS2___New_orig__ = _itkRandomImageSourcePython.itkRandomImageSourceISS2___New_orig__
itkRandomImageSourceISS2_cast = _itkRandomImageSourcePython.itkRandomImageSourceISS2_cast

class itkRandomImageSourceISS3(itkImageSourcePython.itkImageSourceISS3):
    r"""Proxy of C++ itkRandomImageSourceISS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRandomImageSourcePython.itkRandomImageSourceISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceISS3_Clone)
    SetSize = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceISS3_SetSize)
    GetSize = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceISS3_GetSize)
    SetSpacing = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceISS3_SetSpacing)
    GetSpacing = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceISS3_GetSpacing)
    SetOrigin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceISS3_SetOrigin)
    GetOrigin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceISS3_GetOrigin)
    SetDirection = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceISS3_SetDirection)
    GetDirection = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceISS3_GetDirection)
    SetMin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceISS3_SetMin)
    GetMin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceISS3_GetMin)
    SetMax = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceISS3_SetMax)
    GetMax = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceISS3_GetMax)
    __swig_destroy__ = _itkRandomImageSourcePython.delete_itkRandomImageSourceISS3
    cast = _swig_new_static_method(_itkRandomImageSourcePython.itkRandomImageSourceISS3_cast)

    def New(*args, **kargs):
        """New() -> itkRandomImageSourceISS3

        Create a new object of the class itkRandomImageSourceISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRandomImageSourceISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRandomImageSourceISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRandomImageSourceISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRandomImageSourceISS3 in _itkRandomImageSourcePython:
_itkRandomImageSourcePython.itkRandomImageSourceISS3_swigregister(itkRandomImageSourceISS3)
itkRandomImageSourceISS3___New_orig__ = _itkRandomImageSourcePython.itkRandomImageSourceISS3___New_orig__
itkRandomImageSourceISS3_cast = _itkRandomImageSourcePython.itkRandomImageSourceISS3_cast

class itkRandomImageSourceIUC2(itkImageSourcePython.itkImageSourceIUC2):
    r"""Proxy of C++ itkRandomImageSourceIUC2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRandomImageSourcePython.itkRandomImageSourceIUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUC2_Clone)
    SetSize = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUC2_SetSize)
    GetSize = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUC2_GetSize)
    SetSpacing = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUC2_SetSpacing)
    GetSpacing = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUC2_GetSpacing)
    SetOrigin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUC2_SetOrigin)
    GetOrigin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUC2_GetOrigin)
    SetDirection = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUC2_SetDirection)
    GetDirection = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUC2_GetDirection)
    SetMin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUC2_SetMin)
    GetMin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUC2_GetMin)
    SetMax = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUC2_SetMax)
    GetMax = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUC2_GetMax)
    __swig_destroy__ = _itkRandomImageSourcePython.delete_itkRandomImageSourceIUC2
    cast = _swig_new_static_method(_itkRandomImageSourcePython.itkRandomImageSourceIUC2_cast)

    def New(*args, **kargs):
        """New() -> itkRandomImageSourceIUC2

        Create a new object of the class itkRandomImageSourceIUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRandomImageSourceIUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRandomImageSourceIUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRandomImageSourceIUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRandomImageSourceIUC2 in _itkRandomImageSourcePython:
_itkRandomImageSourcePython.itkRandomImageSourceIUC2_swigregister(itkRandomImageSourceIUC2)
itkRandomImageSourceIUC2___New_orig__ = _itkRandomImageSourcePython.itkRandomImageSourceIUC2___New_orig__
itkRandomImageSourceIUC2_cast = _itkRandomImageSourcePython.itkRandomImageSourceIUC2_cast

class itkRandomImageSourceIUC3(itkImageSourcePython.itkImageSourceIUC3):
    r"""Proxy of C++ itkRandomImageSourceIUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRandomImageSourcePython.itkRandomImageSourceIUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUC3_Clone)
    SetSize = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUC3_SetSize)
    GetSize = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUC3_GetSize)
    SetSpacing = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUC3_SetSpacing)
    GetSpacing = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUC3_GetSpacing)
    SetOrigin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUC3_SetOrigin)
    GetOrigin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUC3_GetOrigin)
    SetDirection = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUC3_SetDirection)
    GetDirection = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUC3_GetDirection)
    SetMin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUC3_SetMin)
    GetMin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUC3_GetMin)
    SetMax = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUC3_SetMax)
    GetMax = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUC3_GetMax)
    __swig_destroy__ = _itkRandomImageSourcePython.delete_itkRandomImageSourceIUC3
    cast = _swig_new_static_method(_itkRandomImageSourcePython.itkRandomImageSourceIUC3_cast)

    def New(*args, **kargs):
        """New() -> itkRandomImageSourceIUC3

        Create a new object of the class itkRandomImageSourceIUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRandomImageSourceIUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRandomImageSourceIUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRandomImageSourceIUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRandomImageSourceIUC3 in _itkRandomImageSourcePython:
_itkRandomImageSourcePython.itkRandomImageSourceIUC3_swigregister(itkRandomImageSourceIUC3)
itkRandomImageSourceIUC3___New_orig__ = _itkRandomImageSourcePython.itkRandomImageSourceIUC3___New_orig__
itkRandomImageSourceIUC3_cast = _itkRandomImageSourcePython.itkRandomImageSourceIUC3_cast

class itkRandomImageSourceIUS2(itkImageSourcePython.itkImageSourceIUS2):
    r"""Proxy of C++ itkRandomImageSourceIUS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRandomImageSourcePython.itkRandomImageSourceIUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUS2_Clone)
    SetSize = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUS2_SetSize)
    GetSize = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUS2_GetSize)
    SetSpacing = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUS2_SetSpacing)
    GetSpacing = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUS2_GetSpacing)
    SetOrigin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUS2_SetOrigin)
    GetOrigin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUS2_GetOrigin)
    SetDirection = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUS2_SetDirection)
    GetDirection = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUS2_GetDirection)
    SetMin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUS2_SetMin)
    GetMin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUS2_GetMin)
    SetMax = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUS2_SetMax)
    GetMax = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUS2_GetMax)
    __swig_destroy__ = _itkRandomImageSourcePython.delete_itkRandomImageSourceIUS2
    cast = _swig_new_static_method(_itkRandomImageSourcePython.itkRandomImageSourceIUS2_cast)

    def New(*args, **kargs):
        """New() -> itkRandomImageSourceIUS2

        Create a new object of the class itkRandomImageSourceIUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRandomImageSourceIUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRandomImageSourceIUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRandomImageSourceIUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRandomImageSourceIUS2 in _itkRandomImageSourcePython:
_itkRandomImageSourcePython.itkRandomImageSourceIUS2_swigregister(itkRandomImageSourceIUS2)
itkRandomImageSourceIUS2___New_orig__ = _itkRandomImageSourcePython.itkRandomImageSourceIUS2___New_orig__
itkRandomImageSourceIUS2_cast = _itkRandomImageSourcePython.itkRandomImageSourceIUS2_cast

class itkRandomImageSourceIUS3(itkImageSourcePython.itkImageSourceIUS3):
    r"""Proxy of C++ itkRandomImageSourceIUS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRandomImageSourcePython.itkRandomImageSourceIUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUS3_Clone)
    SetSize = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUS3_SetSize)
    GetSize = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUS3_GetSize)
    SetSpacing = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUS3_SetSpacing)
    GetSpacing = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUS3_GetSpacing)
    SetOrigin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUS3_SetOrigin)
    GetOrigin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUS3_GetOrigin)
    SetDirection = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUS3_SetDirection)
    GetDirection = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUS3_GetDirection)
    SetMin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUS3_SetMin)
    GetMin = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUS3_GetMin)
    SetMax = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUS3_SetMax)
    GetMax = _swig_new_instance_method(_itkRandomImageSourcePython.itkRandomImageSourceIUS3_GetMax)
    __swig_destroy__ = _itkRandomImageSourcePython.delete_itkRandomImageSourceIUS3
    cast = _swig_new_static_method(_itkRandomImageSourcePython.itkRandomImageSourceIUS3_cast)

    def New(*args, **kargs):
        """New() -> itkRandomImageSourceIUS3

        Create a new object of the class itkRandomImageSourceIUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRandomImageSourceIUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRandomImageSourceIUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRandomImageSourceIUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRandomImageSourceIUS3 in _itkRandomImageSourcePython:
_itkRandomImageSourcePython.itkRandomImageSourceIUS3_swigregister(itkRandomImageSourceIUS3)
itkRandomImageSourceIUS3___New_orig__ = _itkRandomImageSourcePython.itkRandomImageSourceIUS3___New_orig__
itkRandomImageSourceIUS3_cast = _itkRandomImageSourcePython.itkRandomImageSourceIUS3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def random_image_source(*args, **kwargs):
    """Procedural interface for RandomImageSource"""
    import itk
    instance = itk.RandomImageSource.New(*args, **kwargs)
    return instance.__internal_call__()

def random_image_source_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.RandomImageSource, itkTemplate.itkTemplate):
        filter_object = itk.RandomImageSource.values()[0]
    else:
        filter_object = itk.RandomImageSource

    random_image_source.__doc__ = filter_object.__doc__
    random_image_source.__doc__ += "\n Args are Input(s) to the filter.\n"
    random_image_source.__doc__ += "Available Keyword Arguments:\n"
    random_image_source.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



