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
    from . import _itkImportImageFilterPython
else:
    import _itkImportImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkImportImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkImportImageFilterPython.SWIG_PyStaticMethod_New

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
import vnl_matrixPython
import stdcomplexPython
import ITKCommonBasePython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageRegionPython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkImagePython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import itkCovariantVectorPython
import itkPointPython
import vnl_matrix_fixedPython
import itkVectorImagePython
import itkVariableLengthVectorPython

def itkImportImageFilterD3_New():
  return itkImportImageFilterD3.New()


def itkImportImageFilterF3_New():
  return itkImportImageFilterF3.New()


def itkImportImageFilterUS3_New():
  return itkImportImageFilterUS3.New()


def itkImportImageFilterUC3_New():
  return itkImportImageFilterUC3.New()


def itkImportImageFilterSS3_New():
  return itkImportImageFilterSS3.New()


def itkImportImageFilterD2_New():
  return itkImportImageFilterD2.New()


def itkImportImageFilterF2_New():
  return itkImportImageFilterF2.New()


def itkImportImageFilterUS2_New():
  return itkImportImageFilterUS2.New()


def itkImportImageFilterUC2_New():
  return itkImportImageFilterUC2.New()


def itkImportImageFilterSS2_New():
  return itkImportImageFilterSS2.New()

class itkImportImageFilterD2(itkImageSourcePython.itkImageSourceID2):
    r"""Proxy of C++ itkImportImageFilterD2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkImportImageFilterPython.itkImportImageFilterD2___New_orig__)
    Clone = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterD2_Clone)
    GetImportPointer = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterD2_GetImportPointer)
    SetImportPointer = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterD2_SetImportPointer)
    SetRegion = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterD2_SetRegion)
    GetRegion = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterD2_GetRegion)
    GetSpacing = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterD2_GetSpacing)
    SetSpacing = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterD2_SetSpacing)
    GetOrigin = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterD2_GetOrigin)
    SetOrigin = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterD2_SetOrigin)
    SetDirection = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterD2_SetDirection)
    GetDirection = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterD2_GetDirection)
    __swig_destroy__ = _itkImportImageFilterPython.delete_itkImportImageFilterD2
    cast = _swig_new_static_method(_itkImportImageFilterPython.itkImportImageFilterD2_cast)

    def New(*args, **kargs):
        """New() -> itkImportImageFilterD2

        Create a new object of the class itkImportImageFilterD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImportImageFilterD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImportImageFilterD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImportImageFilterD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImportImageFilterD2 in _itkImportImageFilterPython:
_itkImportImageFilterPython.itkImportImageFilterD2_swigregister(itkImportImageFilterD2)
itkImportImageFilterD2___New_orig__ = _itkImportImageFilterPython.itkImportImageFilterD2___New_orig__
itkImportImageFilterD2_cast = _itkImportImageFilterPython.itkImportImageFilterD2_cast

class itkImportImageFilterD3(itkImageSourcePython.itkImageSourceID3):
    r"""Proxy of C++ itkImportImageFilterD3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkImportImageFilterPython.itkImportImageFilterD3___New_orig__)
    Clone = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterD3_Clone)
    GetImportPointer = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterD3_GetImportPointer)
    SetImportPointer = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterD3_SetImportPointer)
    SetRegion = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterD3_SetRegion)
    GetRegion = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterD3_GetRegion)
    GetSpacing = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterD3_GetSpacing)
    SetSpacing = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterD3_SetSpacing)
    GetOrigin = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterD3_GetOrigin)
    SetOrigin = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterD3_SetOrigin)
    SetDirection = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterD3_SetDirection)
    GetDirection = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterD3_GetDirection)
    __swig_destroy__ = _itkImportImageFilterPython.delete_itkImportImageFilterD3
    cast = _swig_new_static_method(_itkImportImageFilterPython.itkImportImageFilterD3_cast)

    def New(*args, **kargs):
        """New() -> itkImportImageFilterD3

        Create a new object of the class itkImportImageFilterD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImportImageFilterD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImportImageFilterD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImportImageFilterD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImportImageFilterD3 in _itkImportImageFilterPython:
_itkImportImageFilterPython.itkImportImageFilterD3_swigregister(itkImportImageFilterD3)
itkImportImageFilterD3___New_orig__ = _itkImportImageFilterPython.itkImportImageFilterD3___New_orig__
itkImportImageFilterD3_cast = _itkImportImageFilterPython.itkImportImageFilterD3_cast

class itkImportImageFilterF2(itkImageSourcePython.itkImageSourceIF2):
    r"""Proxy of C++ itkImportImageFilterF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkImportImageFilterPython.itkImportImageFilterF2___New_orig__)
    Clone = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterF2_Clone)
    GetImportPointer = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterF2_GetImportPointer)
    SetImportPointer = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterF2_SetImportPointer)
    SetRegion = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterF2_SetRegion)
    GetRegion = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterF2_GetRegion)
    GetSpacing = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterF2_GetSpacing)
    SetSpacing = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterF2_SetSpacing)
    GetOrigin = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterF2_GetOrigin)
    SetOrigin = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterF2_SetOrigin)
    SetDirection = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterF2_SetDirection)
    GetDirection = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterF2_GetDirection)
    __swig_destroy__ = _itkImportImageFilterPython.delete_itkImportImageFilterF2
    cast = _swig_new_static_method(_itkImportImageFilterPython.itkImportImageFilterF2_cast)

    def New(*args, **kargs):
        """New() -> itkImportImageFilterF2

        Create a new object of the class itkImportImageFilterF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImportImageFilterF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImportImageFilterF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImportImageFilterF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImportImageFilterF2 in _itkImportImageFilterPython:
_itkImportImageFilterPython.itkImportImageFilterF2_swigregister(itkImportImageFilterF2)
itkImportImageFilterF2___New_orig__ = _itkImportImageFilterPython.itkImportImageFilterF2___New_orig__
itkImportImageFilterF2_cast = _itkImportImageFilterPython.itkImportImageFilterF2_cast

class itkImportImageFilterF3(itkImageSourcePython.itkImageSourceIF3):
    r"""Proxy of C++ itkImportImageFilterF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkImportImageFilterPython.itkImportImageFilterF3___New_orig__)
    Clone = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterF3_Clone)
    GetImportPointer = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterF3_GetImportPointer)
    SetImportPointer = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterF3_SetImportPointer)
    SetRegion = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterF3_SetRegion)
    GetRegion = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterF3_GetRegion)
    GetSpacing = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterF3_GetSpacing)
    SetSpacing = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterF3_SetSpacing)
    GetOrigin = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterF3_GetOrigin)
    SetOrigin = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterF3_SetOrigin)
    SetDirection = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterF3_SetDirection)
    GetDirection = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterF3_GetDirection)
    __swig_destroy__ = _itkImportImageFilterPython.delete_itkImportImageFilterF3
    cast = _swig_new_static_method(_itkImportImageFilterPython.itkImportImageFilterF3_cast)

    def New(*args, **kargs):
        """New() -> itkImportImageFilterF3

        Create a new object of the class itkImportImageFilterF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImportImageFilterF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImportImageFilterF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImportImageFilterF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImportImageFilterF3 in _itkImportImageFilterPython:
_itkImportImageFilterPython.itkImportImageFilterF3_swigregister(itkImportImageFilterF3)
itkImportImageFilterF3___New_orig__ = _itkImportImageFilterPython.itkImportImageFilterF3___New_orig__
itkImportImageFilterF3_cast = _itkImportImageFilterPython.itkImportImageFilterF3_cast

class itkImportImageFilterSS2(itkImageSourcePython.itkImageSourceISS2):
    r"""Proxy of C++ itkImportImageFilterSS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkImportImageFilterPython.itkImportImageFilterSS2___New_orig__)
    Clone = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterSS2_Clone)
    GetImportPointer = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterSS2_GetImportPointer)
    SetImportPointer = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterSS2_SetImportPointer)
    SetRegion = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterSS2_SetRegion)
    GetRegion = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterSS2_GetRegion)
    GetSpacing = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterSS2_GetSpacing)
    SetSpacing = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterSS2_SetSpacing)
    GetOrigin = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterSS2_GetOrigin)
    SetOrigin = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterSS2_SetOrigin)
    SetDirection = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterSS2_SetDirection)
    GetDirection = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterSS2_GetDirection)
    __swig_destroy__ = _itkImportImageFilterPython.delete_itkImportImageFilterSS2
    cast = _swig_new_static_method(_itkImportImageFilterPython.itkImportImageFilterSS2_cast)

    def New(*args, **kargs):
        """New() -> itkImportImageFilterSS2

        Create a new object of the class itkImportImageFilterSS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImportImageFilterSS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImportImageFilterSS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImportImageFilterSS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImportImageFilterSS2 in _itkImportImageFilterPython:
_itkImportImageFilterPython.itkImportImageFilterSS2_swigregister(itkImportImageFilterSS2)
itkImportImageFilterSS2___New_orig__ = _itkImportImageFilterPython.itkImportImageFilterSS2___New_orig__
itkImportImageFilterSS2_cast = _itkImportImageFilterPython.itkImportImageFilterSS2_cast

class itkImportImageFilterSS3(itkImageSourcePython.itkImageSourceISS3):
    r"""Proxy of C++ itkImportImageFilterSS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkImportImageFilterPython.itkImportImageFilterSS3___New_orig__)
    Clone = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterSS3_Clone)
    GetImportPointer = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterSS3_GetImportPointer)
    SetImportPointer = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterSS3_SetImportPointer)
    SetRegion = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterSS3_SetRegion)
    GetRegion = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterSS3_GetRegion)
    GetSpacing = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterSS3_GetSpacing)
    SetSpacing = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterSS3_SetSpacing)
    GetOrigin = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterSS3_GetOrigin)
    SetOrigin = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterSS3_SetOrigin)
    SetDirection = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterSS3_SetDirection)
    GetDirection = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterSS3_GetDirection)
    __swig_destroy__ = _itkImportImageFilterPython.delete_itkImportImageFilterSS3
    cast = _swig_new_static_method(_itkImportImageFilterPython.itkImportImageFilterSS3_cast)

    def New(*args, **kargs):
        """New() -> itkImportImageFilterSS3

        Create a new object of the class itkImportImageFilterSS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImportImageFilterSS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImportImageFilterSS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImportImageFilterSS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImportImageFilterSS3 in _itkImportImageFilterPython:
_itkImportImageFilterPython.itkImportImageFilterSS3_swigregister(itkImportImageFilterSS3)
itkImportImageFilterSS3___New_orig__ = _itkImportImageFilterPython.itkImportImageFilterSS3___New_orig__
itkImportImageFilterSS3_cast = _itkImportImageFilterPython.itkImportImageFilterSS3_cast

class itkImportImageFilterUC2(itkImageSourcePython.itkImageSourceIUC2):
    r"""Proxy of C++ itkImportImageFilterUC2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkImportImageFilterPython.itkImportImageFilterUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUC2_Clone)
    GetImportPointer = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUC2_GetImportPointer)
    SetImportPointer = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUC2_SetImportPointer)
    SetRegion = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUC2_SetRegion)
    GetRegion = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUC2_GetRegion)
    GetSpacing = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUC2_GetSpacing)
    SetSpacing = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUC2_SetSpacing)
    GetOrigin = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUC2_GetOrigin)
    SetOrigin = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUC2_SetOrigin)
    SetDirection = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUC2_SetDirection)
    GetDirection = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUC2_GetDirection)
    __swig_destroy__ = _itkImportImageFilterPython.delete_itkImportImageFilterUC2
    cast = _swig_new_static_method(_itkImportImageFilterPython.itkImportImageFilterUC2_cast)

    def New(*args, **kargs):
        """New() -> itkImportImageFilterUC2

        Create a new object of the class itkImportImageFilterUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImportImageFilterUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImportImageFilterUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImportImageFilterUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImportImageFilterUC2 in _itkImportImageFilterPython:
_itkImportImageFilterPython.itkImportImageFilterUC2_swigregister(itkImportImageFilterUC2)
itkImportImageFilterUC2___New_orig__ = _itkImportImageFilterPython.itkImportImageFilterUC2___New_orig__
itkImportImageFilterUC2_cast = _itkImportImageFilterPython.itkImportImageFilterUC2_cast

class itkImportImageFilterUC3(itkImageSourcePython.itkImageSourceIUC3):
    r"""Proxy of C++ itkImportImageFilterUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkImportImageFilterPython.itkImportImageFilterUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUC3_Clone)
    GetImportPointer = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUC3_GetImportPointer)
    SetImportPointer = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUC3_SetImportPointer)
    SetRegion = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUC3_SetRegion)
    GetRegion = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUC3_GetRegion)
    GetSpacing = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUC3_GetSpacing)
    SetSpacing = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUC3_SetSpacing)
    GetOrigin = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUC3_GetOrigin)
    SetOrigin = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUC3_SetOrigin)
    SetDirection = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUC3_SetDirection)
    GetDirection = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUC3_GetDirection)
    __swig_destroy__ = _itkImportImageFilterPython.delete_itkImportImageFilterUC3
    cast = _swig_new_static_method(_itkImportImageFilterPython.itkImportImageFilterUC3_cast)

    def New(*args, **kargs):
        """New() -> itkImportImageFilterUC3

        Create a new object of the class itkImportImageFilterUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImportImageFilterUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImportImageFilterUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImportImageFilterUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImportImageFilterUC3 in _itkImportImageFilterPython:
_itkImportImageFilterPython.itkImportImageFilterUC3_swigregister(itkImportImageFilterUC3)
itkImportImageFilterUC3___New_orig__ = _itkImportImageFilterPython.itkImportImageFilterUC3___New_orig__
itkImportImageFilterUC3_cast = _itkImportImageFilterPython.itkImportImageFilterUC3_cast

class itkImportImageFilterUS2(itkImageSourcePython.itkImageSourceIUS2):
    r"""Proxy of C++ itkImportImageFilterUS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkImportImageFilterPython.itkImportImageFilterUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUS2_Clone)
    GetImportPointer = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUS2_GetImportPointer)
    SetImportPointer = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUS2_SetImportPointer)
    SetRegion = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUS2_SetRegion)
    GetRegion = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUS2_GetRegion)
    GetSpacing = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUS2_GetSpacing)
    SetSpacing = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUS2_SetSpacing)
    GetOrigin = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUS2_GetOrigin)
    SetOrigin = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUS2_SetOrigin)
    SetDirection = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUS2_SetDirection)
    GetDirection = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUS2_GetDirection)
    __swig_destroy__ = _itkImportImageFilterPython.delete_itkImportImageFilterUS2
    cast = _swig_new_static_method(_itkImportImageFilterPython.itkImportImageFilterUS2_cast)

    def New(*args, **kargs):
        """New() -> itkImportImageFilterUS2

        Create a new object of the class itkImportImageFilterUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImportImageFilterUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImportImageFilterUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImportImageFilterUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImportImageFilterUS2 in _itkImportImageFilterPython:
_itkImportImageFilterPython.itkImportImageFilterUS2_swigregister(itkImportImageFilterUS2)
itkImportImageFilterUS2___New_orig__ = _itkImportImageFilterPython.itkImportImageFilterUS2___New_orig__
itkImportImageFilterUS2_cast = _itkImportImageFilterPython.itkImportImageFilterUS2_cast

class itkImportImageFilterUS3(itkImageSourcePython.itkImageSourceIUS3):
    r"""Proxy of C++ itkImportImageFilterUS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkImportImageFilterPython.itkImportImageFilterUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUS3_Clone)
    GetImportPointer = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUS3_GetImportPointer)
    SetImportPointer = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUS3_SetImportPointer)
    SetRegion = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUS3_SetRegion)
    GetRegion = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUS3_GetRegion)
    GetSpacing = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUS3_GetSpacing)
    SetSpacing = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUS3_SetSpacing)
    GetOrigin = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUS3_GetOrigin)
    SetOrigin = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUS3_SetOrigin)
    SetDirection = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUS3_SetDirection)
    GetDirection = _swig_new_instance_method(_itkImportImageFilterPython.itkImportImageFilterUS3_GetDirection)
    __swig_destroy__ = _itkImportImageFilterPython.delete_itkImportImageFilterUS3
    cast = _swig_new_static_method(_itkImportImageFilterPython.itkImportImageFilterUS3_cast)

    def New(*args, **kargs):
        """New() -> itkImportImageFilterUS3

        Create a new object of the class itkImportImageFilterUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImportImageFilterUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImportImageFilterUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImportImageFilterUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImportImageFilterUS3 in _itkImportImageFilterPython:
_itkImportImageFilterPython.itkImportImageFilterUS3_swigregister(itkImportImageFilterUS3)
itkImportImageFilterUS3___New_orig__ = _itkImportImageFilterPython.itkImportImageFilterUS3___New_orig__
itkImportImageFilterUS3_cast = _itkImportImageFilterPython.itkImportImageFilterUS3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def import_image_filter(*args, **kwargs):
    """Procedural interface for ImportImageFilter"""
    import itk
    instance = itk.ImportImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def import_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.ImportImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.ImportImageFilter.values()[0]
    else:
        filter_object = itk.ImportImageFilter

    import_image_filter.__doc__ = filter_object.__doc__
    import_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    import_image_filter.__doc__ += "Available Keyword Arguments:\n"
    import_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



