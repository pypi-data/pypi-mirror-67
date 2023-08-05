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
    from . import _itkBSplineTransformInitializerPython
else:
    import _itkBSplineTransformInitializerPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkBSplineTransformInitializerPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkBSplineTransformInitializerPython.SWIG_PyStaticMethod_New

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


import ITKCommonBasePython
import pyBasePython
import itkSizePython
import itkImagePython
import stdcomplexPython
import itkVectorPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import itkFixedArrayPython
import itkOffsetPython
import itkCovariantVectorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkSymmetricSecondRankTensorPython
import itkRGBAPixelPython
import itkImageRegionPython
import itkIndexPython
import itkRGBPixelPython
import itkBSplineTransformPython
import itkArray2DPython
import itkArrayPython
import itkBSplineBaseTransformPython
import itkOptimizerParametersPython
import itkContinuousIndexPython
import itkTransformBasePython
import itkVariableLengthVectorPython
import itkDiffusionTensor3DPython
import itkBSplineInterpolationWeightFunctionPython
import itkFunctionBasePython

def itkBSplineTransformInitializerBSTD33ID3_New():
  return itkBSplineTransformInitializerBSTD33ID3.New()


def itkBSplineTransformInitializerBSTD33IF3_New():
  return itkBSplineTransformInitializerBSTD33IF3.New()


def itkBSplineTransformInitializerBSTD33IUS3_New():
  return itkBSplineTransformInitializerBSTD33IUS3.New()


def itkBSplineTransformInitializerBSTD33IUC3_New():
  return itkBSplineTransformInitializerBSTD33IUC3.New()


def itkBSplineTransformInitializerBSTD33ISS3_New():
  return itkBSplineTransformInitializerBSTD33ISS3.New()


def itkBSplineTransformInitializerBSTD23ID2_New():
  return itkBSplineTransformInitializerBSTD23ID2.New()


def itkBSplineTransformInitializerBSTD23IF2_New():
  return itkBSplineTransformInitializerBSTD23IF2.New()


def itkBSplineTransformInitializerBSTD23IUS2_New():
  return itkBSplineTransformInitializerBSTD23IUS2.New()


def itkBSplineTransformInitializerBSTD23IUC2_New():
  return itkBSplineTransformInitializerBSTD23IUC2.New()


def itkBSplineTransformInitializerBSTD23ISS2_New():
  return itkBSplineTransformInitializerBSTD23ISS2.New()

class itkBSplineTransformInitializerBSTD23ID2(ITKCommonBasePython.itkObject):
    r"""Proxy of C++ itkBSplineTransformInitializerBSTD23ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23ID2_Clone)
    GetTransform = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23ID2_GetTransform)
    SetTransform = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23ID2_SetTransform)
    GetImage = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23ID2_GetImage)
    SetImage = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23ID2_SetImage)
    GetTransformDomainMeshSize = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23ID2_GetTransformDomainMeshSize)
    SetTransformDomainMeshSize = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23ID2_SetTransformDomainMeshSize)
    InitializeTransform = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23ID2_InitializeTransform)
    __swig_destroy__ = _itkBSplineTransformInitializerPython.delete_itkBSplineTransformInitializerBSTD23ID2
    cast = _swig_new_static_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23ID2_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineTransformInitializerBSTD23ID2

        Create a new object of the class itkBSplineTransformInitializerBSTD23ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineTransformInitializerBSTD23ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineTransformInitializerBSTD23ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineTransformInitializerBSTD23ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineTransformInitializerBSTD23ID2 in _itkBSplineTransformInitializerPython:
_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23ID2_swigregister(itkBSplineTransformInitializerBSTD23ID2)
itkBSplineTransformInitializerBSTD23ID2___New_orig__ = _itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23ID2___New_orig__
itkBSplineTransformInitializerBSTD23ID2_cast = _itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23ID2_cast

class itkBSplineTransformInitializerBSTD23IF2(ITKCommonBasePython.itkObject):
    r"""Proxy of C++ itkBSplineTransformInitializerBSTD23IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IF2_Clone)
    GetTransform = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IF2_GetTransform)
    SetTransform = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IF2_SetTransform)
    GetImage = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IF2_GetImage)
    SetImage = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IF2_SetImage)
    GetTransformDomainMeshSize = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IF2_GetTransformDomainMeshSize)
    SetTransformDomainMeshSize = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IF2_SetTransformDomainMeshSize)
    InitializeTransform = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IF2_InitializeTransform)
    __swig_destroy__ = _itkBSplineTransformInitializerPython.delete_itkBSplineTransformInitializerBSTD23IF2
    cast = _swig_new_static_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IF2_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineTransformInitializerBSTD23IF2

        Create a new object of the class itkBSplineTransformInitializerBSTD23IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineTransformInitializerBSTD23IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineTransformInitializerBSTD23IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineTransformInitializerBSTD23IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineTransformInitializerBSTD23IF2 in _itkBSplineTransformInitializerPython:
_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IF2_swigregister(itkBSplineTransformInitializerBSTD23IF2)
itkBSplineTransformInitializerBSTD23IF2___New_orig__ = _itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IF2___New_orig__
itkBSplineTransformInitializerBSTD23IF2_cast = _itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IF2_cast

class itkBSplineTransformInitializerBSTD23ISS2(ITKCommonBasePython.itkObject):
    r"""Proxy of C++ itkBSplineTransformInitializerBSTD23ISS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23ISS2___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23ISS2_Clone)
    GetTransform = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23ISS2_GetTransform)
    SetTransform = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23ISS2_SetTransform)
    GetImage = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23ISS2_GetImage)
    SetImage = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23ISS2_SetImage)
    GetTransformDomainMeshSize = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23ISS2_GetTransformDomainMeshSize)
    SetTransformDomainMeshSize = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23ISS2_SetTransformDomainMeshSize)
    InitializeTransform = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23ISS2_InitializeTransform)
    __swig_destroy__ = _itkBSplineTransformInitializerPython.delete_itkBSplineTransformInitializerBSTD23ISS2
    cast = _swig_new_static_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23ISS2_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineTransformInitializerBSTD23ISS2

        Create a new object of the class itkBSplineTransformInitializerBSTD23ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineTransformInitializerBSTD23ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineTransformInitializerBSTD23ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineTransformInitializerBSTD23ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineTransformInitializerBSTD23ISS2 in _itkBSplineTransformInitializerPython:
_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23ISS2_swigregister(itkBSplineTransformInitializerBSTD23ISS2)
itkBSplineTransformInitializerBSTD23ISS2___New_orig__ = _itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23ISS2___New_orig__
itkBSplineTransformInitializerBSTD23ISS2_cast = _itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23ISS2_cast

class itkBSplineTransformInitializerBSTD23IUC2(ITKCommonBasePython.itkObject):
    r"""Proxy of C++ itkBSplineTransformInitializerBSTD23IUC2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IUC2_Clone)
    GetTransform = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IUC2_GetTransform)
    SetTransform = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IUC2_SetTransform)
    GetImage = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IUC2_GetImage)
    SetImage = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IUC2_SetImage)
    GetTransformDomainMeshSize = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IUC2_GetTransformDomainMeshSize)
    SetTransformDomainMeshSize = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IUC2_SetTransformDomainMeshSize)
    InitializeTransform = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IUC2_InitializeTransform)
    __swig_destroy__ = _itkBSplineTransformInitializerPython.delete_itkBSplineTransformInitializerBSTD23IUC2
    cast = _swig_new_static_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IUC2_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineTransformInitializerBSTD23IUC2

        Create a new object of the class itkBSplineTransformInitializerBSTD23IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineTransformInitializerBSTD23IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineTransformInitializerBSTD23IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineTransformInitializerBSTD23IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineTransformInitializerBSTD23IUC2 in _itkBSplineTransformInitializerPython:
_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IUC2_swigregister(itkBSplineTransformInitializerBSTD23IUC2)
itkBSplineTransformInitializerBSTD23IUC2___New_orig__ = _itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IUC2___New_orig__
itkBSplineTransformInitializerBSTD23IUC2_cast = _itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IUC2_cast

class itkBSplineTransformInitializerBSTD23IUS2(ITKCommonBasePython.itkObject):
    r"""Proxy of C++ itkBSplineTransformInitializerBSTD23IUS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IUS2_Clone)
    GetTransform = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IUS2_GetTransform)
    SetTransform = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IUS2_SetTransform)
    GetImage = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IUS2_GetImage)
    SetImage = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IUS2_SetImage)
    GetTransformDomainMeshSize = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IUS2_GetTransformDomainMeshSize)
    SetTransformDomainMeshSize = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IUS2_SetTransformDomainMeshSize)
    InitializeTransform = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IUS2_InitializeTransform)
    __swig_destroy__ = _itkBSplineTransformInitializerPython.delete_itkBSplineTransformInitializerBSTD23IUS2
    cast = _swig_new_static_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IUS2_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineTransformInitializerBSTD23IUS2

        Create a new object of the class itkBSplineTransformInitializerBSTD23IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineTransformInitializerBSTD23IUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineTransformInitializerBSTD23IUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineTransformInitializerBSTD23IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineTransformInitializerBSTD23IUS2 in _itkBSplineTransformInitializerPython:
_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IUS2_swigregister(itkBSplineTransformInitializerBSTD23IUS2)
itkBSplineTransformInitializerBSTD23IUS2___New_orig__ = _itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IUS2___New_orig__
itkBSplineTransformInitializerBSTD23IUS2_cast = _itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD23IUS2_cast

class itkBSplineTransformInitializerBSTD33ID3(ITKCommonBasePython.itkObject):
    r"""Proxy of C++ itkBSplineTransformInitializerBSTD33ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33ID3_Clone)
    GetTransform = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33ID3_GetTransform)
    SetTransform = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33ID3_SetTransform)
    GetImage = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33ID3_GetImage)
    SetImage = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33ID3_SetImage)
    GetTransformDomainMeshSize = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33ID3_GetTransformDomainMeshSize)
    SetTransformDomainMeshSize = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33ID3_SetTransformDomainMeshSize)
    InitializeTransform = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33ID3_InitializeTransform)
    __swig_destroy__ = _itkBSplineTransformInitializerPython.delete_itkBSplineTransformInitializerBSTD33ID3
    cast = _swig_new_static_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33ID3_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineTransformInitializerBSTD33ID3

        Create a new object of the class itkBSplineTransformInitializerBSTD33ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineTransformInitializerBSTD33ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineTransformInitializerBSTD33ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineTransformInitializerBSTD33ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineTransformInitializerBSTD33ID3 in _itkBSplineTransformInitializerPython:
_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33ID3_swigregister(itkBSplineTransformInitializerBSTD33ID3)
itkBSplineTransformInitializerBSTD33ID3___New_orig__ = _itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33ID3___New_orig__
itkBSplineTransformInitializerBSTD33ID3_cast = _itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33ID3_cast

class itkBSplineTransformInitializerBSTD33IF3(ITKCommonBasePython.itkObject):
    r"""Proxy of C++ itkBSplineTransformInitializerBSTD33IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IF3_Clone)
    GetTransform = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IF3_GetTransform)
    SetTransform = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IF3_SetTransform)
    GetImage = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IF3_GetImage)
    SetImage = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IF3_SetImage)
    GetTransformDomainMeshSize = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IF3_GetTransformDomainMeshSize)
    SetTransformDomainMeshSize = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IF3_SetTransformDomainMeshSize)
    InitializeTransform = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IF3_InitializeTransform)
    __swig_destroy__ = _itkBSplineTransformInitializerPython.delete_itkBSplineTransformInitializerBSTD33IF3
    cast = _swig_new_static_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IF3_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineTransformInitializerBSTD33IF3

        Create a new object of the class itkBSplineTransformInitializerBSTD33IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineTransformInitializerBSTD33IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineTransformInitializerBSTD33IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineTransformInitializerBSTD33IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineTransformInitializerBSTD33IF3 in _itkBSplineTransformInitializerPython:
_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IF3_swigregister(itkBSplineTransformInitializerBSTD33IF3)
itkBSplineTransformInitializerBSTD33IF3___New_orig__ = _itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IF3___New_orig__
itkBSplineTransformInitializerBSTD33IF3_cast = _itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IF3_cast

class itkBSplineTransformInitializerBSTD33ISS3(ITKCommonBasePython.itkObject):
    r"""Proxy of C++ itkBSplineTransformInitializerBSTD33ISS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33ISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33ISS3_Clone)
    GetTransform = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33ISS3_GetTransform)
    SetTransform = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33ISS3_SetTransform)
    GetImage = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33ISS3_GetImage)
    SetImage = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33ISS3_SetImage)
    GetTransformDomainMeshSize = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33ISS3_GetTransformDomainMeshSize)
    SetTransformDomainMeshSize = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33ISS3_SetTransformDomainMeshSize)
    InitializeTransform = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33ISS3_InitializeTransform)
    __swig_destroy__ = _itkBSplineTransformInitializerPython.delete_itkBSplineTransformInitializerBSTD33ISS3
    cast = _swig_new_static_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33ISS3_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineTransformInitializerBSTD33ISS3

        Create a new object of the class itkBSplineTransformInitializerBSTD33ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineTransformInitializerBSTD33ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineTransformInitializerBSTD33ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineTransformInitializerBSTD33ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineTransformInitializerBSTD33ISS3 in _itkBSplineTransformInitializerPython:
_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33ISS3_swigregister(itkBSplineTransformInitializerBSTD33ISS3)
itkBSplineTransformInitializerBSTD33ISS3___New_orig__ = _itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33ISS3___New_orig__
itkBSplineTransformInitializerBSTD33ISS3_cast = _itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33ISS3_cast

class itkBSplineTransformInitializerBSTD33IUC3(ITKCommonBasePython.itkObject):
    r"""Proxy of C++ itkBSplineTransformInitializerBSTD33IUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IUC3_Clone)
    GetTransform = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IUC3_GetTransform)
    SetTransform = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IUC3_SetTransform)
    GetImage = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IUC3_GetImage)
    SetImage = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IUC3_SetImage)
    GetTransformDomainMeshSize = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IUC3_GetTransformDomainMeshSize)
    SetTransformDomainMeshSize = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IUC3_SetTransformDomainMeshSize)
    InitializeTransform = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IUC3_InitializeTransform)
    __swig_destroy__ = _itkBSplineTransformInitializerPython.delete_itkBSplineTransformInitializerBSTD33IUC3
    cast = _swig_new_static_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IUC3_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineTransformInitializerBSTD33IUC3

        Create a new object of the class itkBSplineTransformInitializerBSTD33IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineTransformInitializerBSTD33IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineTransformInitializerBSTD33IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineTransformInitializerBSTD33IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineTransformInitializerBSTD33IUC3 in _itkBSplineTransformInitializerPython:
_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IUC3_swigregister(itkBSplineTransformInitializerBSTD33IUC3)
itkBSplineTransformInitializerBSTD33IUC3___New_orig__ = _itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IUC3___New_orig__
itkBSplineTransformInitializerBSTD33IUC3_cast = _itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IUC3_cast

class itkBSplineTransformInitializerBSTD33IUS3(ITKCommonBasePython.itkObject):
    r"""Proxy of C++ itkBSplineTransformInitializerBSTD33IUS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IUS3_Clone)
    GetTransform = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IUS3_GetTransform)
    SetTransform = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IUS3_SetTransform)
    GetImage = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IUS3_GetImage)
    SetImage = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IUS3_SetImage)
    GetTransformDomainMeshSize = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IUS3_GetTransformDomainMeshSize)
    SetTransformDomainMeshSize = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IUS3_SetTransformDomainMeshSize)
    InitializeTransform = _swig_new_instance_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IUS3_InitializeTransform)
    __swig_destroy__ = _itkBSplineTransformInitializerPython.delete_itkBSplineTransformInitializerBSTD33IUS3
    cast = _swig_new_static_method(_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IUS3_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineTransformInitializerBSTD33IUS3

        Create a new object of the class itkBSplineTransformInitializerBSTD33IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineTransformInitializerBSTD33IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineTransformInitializerBSTD33IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineTransformInitializerBSTD33IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineTransformInitializerBSTD33IUS3 in _itkBSplineTransformInitializerPython:
_itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IUS3_swigregister(itkBSplineTransformInitializerBSTD33IUS3)
itkBSplineTransformInitializerBSTD33IUS3___New_orig__ = _itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IUS3___New_orig__
itkBSplineTransformInitializerBSTD33IUS3_cast = _itkBSplineTransformInitializerPython.itkBSplineTransformInitializerBSTD33IUS3_cast



