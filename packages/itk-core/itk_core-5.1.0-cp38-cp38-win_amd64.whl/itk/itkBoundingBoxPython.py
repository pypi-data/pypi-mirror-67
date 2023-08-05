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
    from . import _itkBoundingBoxPython
else:
    import _itkBoundingBoxPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkBoundingBoxPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkBoundingBoxPython.SWIG_PyStaticMethod_New

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
import itkPointPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import itkFixedArrayPython
import itkVectorPython
import vnl_vector_refPython
import itkMapContainerPython
import itkVectorContainerPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkContinuousIndexPython
import itkIndexPython
import itkOffsetPython
import itkSizePython

def itkBoundingBoxULL3DMCULLPD3_New():
  return itkBoundingBoxULL3DMCULLPD3.New()


def itkBoundingBoxULL3DVCULLPD3_New():
  return itkBoundingBoxULL3DVCULLPD3.New()


def itkBoundingBoxULL3FMCULLPF3_New():
  return itkBoundingBoxULL3FMCULLPF3.New()


def itkBoundingBoxULL3FVCULLPF3_New():
  return itkBoundingBoxULL3FVCULLPF3.New()


def itkBoundingBoxULL2DMCULLPD2_New():
  return itkBoundingBoxULL2DMCULLPD2.New()


def itkBoundingBoxULL2DVCULLPD2_New():
  return itkBoundingBoxULL2DVCULLPD2.New()


def itkBoundingBoxULL2FMCULLPF2_New():
  return itkBoundingBoxULL2FMCULLPF2.New()


def itkBoundingBoxULL2FVCULLPF2_New():
  return itkBoundingBoxULL2FVCULLPF2.New()

class itkBoundingBoxULL2DMCULLPD2(ITKCommonBasePython.itkObject):
    r"""Proxy of C++ itkBoundingBoxULL2DMCULLPD2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBoundingBoxPython.itkBoundingBoxULL2DMCULLPD2___New_orig__)
    Clone = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2DMCULLPD2_Clone)
    SetPoints = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2DMCULLPD2_SetPoints)
    GetPoints = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2DMCULLPD2_GetPoints)
    ComputeCorners = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2DMCULLPD2_ComputeCorners)
    ComputeBoundingBox = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2DMCULLPD2_ComputeBoundingBox)
    GetBounds = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2DMCULLPD2_GetBounds)
    GetCenter = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2DMCULLPD2_GetCenter)
    GetMinimum = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2DMCULLPD2_GetMinimum)
    SetMinimum = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2DMCULLPD2_SetMinimum)
    GetMaximum = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2DMCULLPD2_GetMaximum)
    SetMaximum = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2DMCULLPD2_SetMaximum)
    ConsiderPoint = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2DMCULLPD2_ConsiderPoint)
    GetDiagonalLength2 = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2DMCULLPD2_GetDiagonalLength2)
    IsInside = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2DMCULLPD2_IsInside)
    DeepCopy = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2DMCULLPD2_DeepCopy)
    __swig_destroy__ = _itkBoundingBoxPython.delete_itkBoundingBoxULL2DMCULLPD2
    cast = _swig_new_static_method(_itkBoundingBoxPython.itkBoundingBoxULL2DMCULLPD2_cast)

    def New(*args, **kargs):
        """New() -> itkBoundingBoxULL2DMCULLPD2

        Create a new object of the class itkBoundingBoxULL2DMCULLPD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBoundingBoxULL2DMCULLPD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBoundingBoxULL2DMCULLPD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBoundingBoxULL2DMCULLPD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBoundingBoxULL2DMCULLPD2 in _itkBoundingBoxPython:
_itkBoundingBoxPython.itkBoundingBoxULL2DMCULLPD2_swigregister(itkBoundingBoxULL2DMCULLPD2)
itkBoundingBoxULL2DMCULLPD2___New_orig__ = _itkBoundingBoxPython.itkBoundingBoxULL2DMCULLPD2___New_orig__
itkBoundingBoxULL2DMCULLPD2_cast = _itkBoundingBoxPython.itkBoundingBoxULL2DMCULLPD2_cast

class itkBoundingBoxULL2DVCULLPD2(ITKCommonBasePython.itkObject):
    r"""Proxy of C++ itkBoundingBoxULL2DVCULLPD2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBoundingBoxPython.itkBoundingBoxULL2DVCULLPD2___New_orig__)
    Clone = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2DVCULLPD2_Clone)
    SetPoints = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2DVCULLPD2_SetPoints)
    GetPoints = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2DVCULLPD2_GetPoints)
    ComputeCorners = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2DVCULLPD2_ComputeCorners)
    ComputeBoundingBox = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2DVCULLPD2_ComputeBoundingBox)
    GetBounds = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2DVCULLPD2_GetBounds)
    GetCenter = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2DVCULLPD2_GetCenter)
    GetMinimum = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2DVCULLPD2_GetMinimum)
    SetMinimum = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2DVCULLPD2_SetMinimum)
    GetMaximum = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2DVCULLPD2_GetMaximum)
    SetMaximum = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2DVCULLPD2_SetMaximum)
    ConsiderPoint = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2DVCULLPD2_ConsiderPoint)
    GetDiagonalLength2 = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2DVCULLPD2_GetDiagonalLength2)
    IsInside = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2DVCULLPD2_IsInside)
    DeepCopy = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2DVCULLPD2_DeepCopy)
    __swig_destroy__ = _itkBoundingBoxPython.delete_itkBoundingBoxULL2DVCULLPD2
    cast = _swig_new_static_method(_itkBoundingBoxPython.itkBoundingBoxULL2DVCULLPD2_cast)

    def New(*args, **kargs):
        """New() -> itkBoundingBoxULL2DVCULLPD2

        Create a new object of the class itkBoundingBoxULL2DVCULLPD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBoundingBoxULL2DVCULLPD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBoundingBoxULL2DVCULLPD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBoundingBoxULL2DVCULLPD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBoundingBoxULL2DVCULLPD2 in _itkBoundingBoxPython:
_itkBoundingBoxPython.itkBoundingBoxULL2DVCULLPD2_swigregister(itkBoundingBoxULL2DVCULLPD2)
itkBoundingBoxULL2DVCULLPD2___New_orig__ = _itkBoundingBoxPython.itkBoundingBoxULL2DVCULLPD2___New_orig__
itkBoundingBoxULL2DVCULLPD2_cast = _itkBoundingBoxPython.itkBoundingBoxULL2DVCULLPD2_cast

class itkBoundingBoxULL2FMCULLPF2(ITKCommonBasePython.itkObject):
    r"""Proxy of C++ itkBoundingBoxULL2FMCULLPF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBoundingBoxPython.itkBoundingBoxULL2FMCULLPF2___New_orig__)
    Clone = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2FMCULLPF2_Clone)
    SetPoints = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2FMCULLPF2_SetPoints)
    GetPoints = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2FMCULLPF2_GetPoints)
    ComputeCorners = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2FMCULLPF2_ComputeCorners)
    ComputeBoundingBox = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2FMCULLPF2_ComputeBoundingBox)
    GetBounds = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2FMCULLPF2_GetBounds)
    GetCenter = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2FMCULLPF2_GetCenter)
    GetMinimum = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2FMCULLPF2_GetMinimum)
    SetMinimum = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2FMCULLPF2_SetMinimum)
    GetMaximum = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2FMCULLPF2_GetMaximum)
    SetMaximum = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2FMCULLPF2_SetMaximum)
    ConsiderPoint = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2FMCULLPF2_ConsiderPoint)
    GetDiagonalLength2 = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2FMCULLPF2_GetDiagonalLength2)
    IsInside = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2FMCULLPF2_IsInside)
    DeepCopy = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2FMCULLPF2_DeepCopy)
    __swig_destroy__ = _itkBoundingBoxPython.delete_itkBoundingBoxULL2FMCULLPF2
    cast = _swig_new_static_method(_itkBoundingBoxPython.itkBoundingBoxULL2FMCULLPF2_cast)

    def New(*args, **kargs):
        """New() -> itkBoundingBoxULL2FMCULLPF2

        Create a new object of the class itkBoundingBoxULL2FMCULLPF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBoundingBoxULL2FMCULLPF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBoundingBoxULL2FMCULLPF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBoundingBoxULL2FMCULLPF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBoundingBoxULL2FMCULLPF2 in _itkBoundingBoxPython:
_itkBoundingBoxPython.itkBoundingBoxULL2FMCULLPF2_swigregister(itkBoundingBoxULL2FMCULLPF2)
itkBoundingBoxULL2FMCULLPF2___New_orig__ = _itkBoundingBoxPython.itkBoundingBoxULL2FMCULLPF2___New_orig__
itkBoundingBoxULL2FMCULLPF2_cast = _itkBoundingBoxPython.itkBoundingBoxULL2FMCULLPF2_cast

class itkBoundingBoxULL2FVCULLPF2(ITKCommonBasePython.itkObject):
    r"""Proxy of C++ itkBoundingBoxULL2FVCULLPF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBoundingBoxPython.itkBoundingBoxULL2FVCULLPF2___New_orig__)
    Clone = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2FVCULLPF2_Clone)
    SetPoints = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2FVCULLPF2_SetPoints)
    GetPoints = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2FVCULLPF2_GetPoints)
    ComputeCorners = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2FVCULLPF2_ComputeCorners)
    ComputeBoundingBox = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2FVCULLPF2_ComputeBoundingBox)
    GetBounds = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2FVCULLPF2_GetBounds)
    GetCenter = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2FVCULLPF2_GetCenter)
    GetMinimum = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2FVCULLPF2_GetMinimum)
    SetMinimum = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2FVCULLPF2_SetMinimum)
    GetMaximum = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2FVCULLPF2_GetMaximum)
    SetMaximum = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2FVCULLPF2_SetMaximum)
    ConsiderPoint = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2FVCULLPF2_ConsiderPoint)
    GetDiagonalLength2 = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2FVCULLPF2_GetDiagonalLength2)
    IsInside = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2FVCULLPF2_IsInside)
    DeepCopy = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL2FVCULLPF2_DeepCopy)
    __swig_destroy__ = _itkBoundingBoxPython.delete_itkBoundingBoxULL2FVCULLPF2
    cast = _swig_new_static_method(_itkBoundingBoxPython.itkBoundingBoxULL2FVCULLPF2_cast)

    def New(*args, **kargs):
        """New() -> itkBoundingBoxULL2FVCULLPF2

        Create a new object of the class itkBoundingBoxULL2FVCULLPF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBoundingBoxULL2FVCULLPF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBoundingBoxULL2FVCULLPF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBoundingBoxULL2FVCULLPF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBoundingBoxULL2FVCULLPF2 in _itkBoundingBoxPython:
_itkBoundingBoxPython.itkBoundingBoxULL2FVCULLPF2_swigregister(itkBoundingBoxULL2FVCULLPF2)
itkBoundingBoxULL2FVCULLPF2___New_orig__ = _itkBoundingBoxPython.itkBoundingBoxULL2FVCULLPF2___New_orig__
itkBoundingBoxULL2FVCULLPF2_cast = _itkBoundingBoxPython.itkBoundingBoxULL2FVCULLPF2_cast

class itkBoundingBoxULL3DMCULLPD3(ITKCommonBasePython.itkObject):
    r"""Proxy of C++ itkBoundingBoxULL3DMCULLPD3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBoundingBoxPython.itkBoundingBoxULL3DMCULLPD3___New_orig__)
    Clone = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3DMCULLPD3_Clone)
    SetPoints = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3DMCULLPD3_SetPoints)
    GetPoints = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3DMCULLPD3_GetPoints)
    ComputeCorners = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3DMCULLPD3_ComputeCorners)
    ComputeBoundingBox = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3DMCULLPD3_ComputeBoundingBox)
    GetBounds = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3DMCULLPD3_GetBounds)
    GetCenter = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3DMCULLPD3_GetCenter)
    GetMinimum = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3DMCULLPD3_GetMinimum)
    SetMinimum = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3DMCULLPD3_SetMinimum)
    GetMaximum = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3DMCULLPD3_GetMaximum)
    SetMaximum = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3DMCULLPD3_SetMaximum)
    ConsiderPoint = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3DMCULLPD3_ConsiderPoint)
    GetDiagonalLength2 = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3DMCULLPD3_GetDiagonalLength2)
    IsInside = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3DMCULLPD3_IsInside)
    DeepCopy = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3DMCULLPD3_DeepCopy)
    __swig_destroy__ = _itkBoundingBoxPython.delete_itkBoundingBoxULL3DMCULLPD3
    cast = _swig_new_static_method(_itkBoundingBoxPython.itkBoundingBoxULL3DMCULLPD3_cast)

    def New(*args, **kargs):
        """New() -> itkBoundingBoxULL3DMCULLPD3

        Create a new object of the class itkBoundingBoxULL3DMCULLPD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBoundingBoxULL3DMCULLPD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBoundingBoxULL3DMCULLPD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBoundingBoxULL3DMCULLPD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBoundingBoxULL3DMCULLPD3 in _itkBoundingBoxPython:
_itkBoundingBoxPython.itkBoundingBoxULL3DMCULLPD3_swigregister(itkBoundingBoxULL3DMCULLPD3)
itkBoundingBoxULL3DMCULLPD3___New_orig__ = _itkBoundingBoxPython.itkBoundingBoxULL3DMCULLPD3___New_orig__
itkBoundingBoxULL3DMCULLPD3_cast = _itkBoundingBoxPython.itkBoundingBoxULL3DMCULLPD3_cast

class itkBoundingBoxULL3DVCULLPD3(ITKCommonBasePython.itkObject):
    r"""Proxy of C++ itkBoundingBoxULL3DVCULLPD3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBoundingBoxPython.itkBoundingBoxULL3DVCULLPD3___New_orig__)
    Clone = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3DVCULLPD3_Clone)
    SetPoints = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3DVCULLPD3_SetPoints)
    GetPoints = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3DVCULLPD3_GetPoints)
    ComputeCorners = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3DVCULLPD3_ComputeCorners)
    ComputeBoundingBox = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3DVCULLPD3_ComputeBoundingBox)
    GetBounds = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3DVCULLPD3_GetBounds)
    GetCenter = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3DVCULLPD3_GetCenter)
    GetMinimum = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3DVCULLPD3_GetMinimum)
    SetMinimum = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3DVCULLPD3_SetMinimum)
    GetMaximum = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3DVCULLPD3_GetMaximum)
    SetMaximum = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3DVCULLPD3_SetMaximum)
    ConsiderPoint = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3DVCULLPD3_ConsiderPoint)
    GetDiagonalLength2 = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3DVCULLPD3_GetDiagonalLength2)
    IsInside = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3DVCULLPD3_IsInside)
    DeepCopy = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3DVCULLPD3_DeepCopy)
    __swig_destroy__ = _itkBoundingBoxPython.delete_itkBoundingBoxULL3DVCULLPD3
    cast = _swig_new_static_method(_itkBoundingBoxPython.itkBoundingBoxULL3DVCULLPD3_cast)

    def New(*args, **kargs):
        """New() -> itkBoundingBoxULL3DVCULLPD3

        Create a new object of the class itkBoundingBoxULL3DVCULLPD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBoundingBoxULL3DVCULLPD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBoundingBoxULL3DVCULLPD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBoundingBoxULL3DVCULLPD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBoundingBoxULL3DVCULLPD3 in _itkBoundingBoxPython:
_itkBoundingBoxPython.itkBoundingBoxULL3DVCULLPD3_swigregister(itkBoundingBoxULL3DVCULLPD3)
itkBoundingBoxULL3DVCULLPD3___New_orig__ = _itkBoundingBoxPython.itkBoundingBoxULL3DVCULLPD3___New_orig__
itkBoundingBoxULL3DVCULLPD3_cast = _itkBoundingBoxPython.itkBoundingBoxULL3DVCULLPD3_cast

class itkBoundingBoxULL3FMCULLPF3(ITKCommonBasePython.itkObject):
    r"""Proxy of C++ itkBoundingBoxULL3FMCULLPF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBoundingBoxPython.itkBoundingBoxULL3FMCULLPF3___New_orig__)
    Clone = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3FMCULLPF3_Clone)
    SetPoints = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3FMCULLPF3_SetPoints)
    GetPoints = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3FMCULLPF3_GetPoints)
    ComputeCorners = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3FMCULLPF3_ComputeCorners)
    ComputeBoundingBox = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3FMCULLPF3_ComputeBoundingBox)
    GetBounds = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3FMCULLPF3_GetBounds)
    GetCenter = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3FMCULLPF3_GetCenter)
    GetMinimum = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3FMCULLPF3_GetMinimum)
    SetMinimum = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3FMCULLPF3_SetMinimum)
    GetMaximum = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3FMCULLPF3_GetMaximum)
    SetMaximum = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3FMCULLPF3_SetMaximum)
    ConsiderPoint = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3FMCULLPF3_ConsiderPoint)
    GetDiagonalLength2 = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3FMCULLPF3_GetDiagonalLength2)
    IsInside = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3FMCULLPF3_IsInside)
    DeepCopy = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3FMCULLPF3_DeepCopy)
    __swig_destroy__ = _itkBoundingBoxPython.delete_itkBoundingBoxULL3FMCULLPF3
    cast = _swig_new_static_method(_itkBoundingBoxPython.itkBoundingBoxULL3FMCULLPF3_cast)

    def New(*args, **kargs):
        """New() -> itkBoundingBoxULL3FMCULLPF3

        Create a new object of the class itkBoundingBoxULL3FMCULLPF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBoundingBoxULL3FMCULLPF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBoundingBoxULL3FMCULLPF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBoundingBoxULL3FMCULLPF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBoundingBoxULL3FMCULLPF3 in _itkBoundingBoxPython:
_itkBoundingBoxPython.itkBoundingBoxULL3FMCULLPF3_swigregister(itkBoundingBoxULL3FMCULLPF3)
itkBoundingBoxULL3FMCULLPF3___New_orig__ = _itkBoundingBoxPython.itkBoundingBoxULL3FMCULLPF3___New_orig__
itkBoundingBoxULL3FMCULLPF3_cast = _itkBoundingBoxPython.itkBoundingBoxULL3FMCULLPF3_cast

class itkBoundingBoxULL3FVCULLPF3(ITKCommonBasePython.itkObject):
    r"""Proxy of C++ itkBoundingBoxULL3FVCULLPF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBoundingBoxPython.itkBoundingBoxULL3FVCULLPF3___New_orig__)
    Clone = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3FVCULLPF3_Clone)
    SetPoints = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3FVCULLPF3_SetPoints)
    GetPoints = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3FVCULLPF3_GetPoints)
    ComputeCorners = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3FVCULLPF3_ComputeCorners)
    ComputeBoundingBox = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3FVCULLPF3_ComputeBoundingBox)
    GetBounds = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3FVCULLPF3_GetBounds)
    GetCenter = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3FVCULLPF3_GetCenter)
    GetMinimum = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3FVCULLPF3_GetMinimum)
    SetMinimum = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3FVCULLPF3_SetMinimum)
    GetMaximum = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3FVCULLPF3_GetMaximum)
    SetMaximum = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3FVCULLPF3_SetMaximum)
    ConsiderPoint = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3FVCULLPF3_ConsiderPoint)
    GetDiagonalLength2 = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3FVCULLPF3_GetDiagonalLength2)
    IsInside = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3FVCULLPF3_IsInside)
    DeepCopy = _swig_new_instance_method(_itkBoundingBoxPython.itkBoundingBoxULL3FVCULLPF3_DeepCopy)
    __swig_destroy__ = _itkBoundingBoxPython.delete_itkBoundingBoxULL3FVCULLPF3
    cast = _swig_new_static_method(_itkBoundingBoxPython.itkBoundingBoxULL3FVCULLPF3_cast)

    def New(*args, **kargs):
        """New() -> itkBoundingBoxULL3FVCULLPF3

        Create a new object of the class itkBoundingBoxULL3FVCULLPF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBoundingBoxULL3FVCULLPF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBoundingBoxULL3FVCULLPF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBoundingBoxULL3FVCULLPF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBoundingBoxULL3FVCULLPF3 in _itkBoundingBoxPython:
_itkBoundingBoxPython.itkBoundingBoxULL3FVCULLPF3_swigregister(itkBoundingBoxULL3FVCULLPF3)
itkBoundingBoxULL3FVCULLPF3___New_orig__ = _itkBoundingBoxPython.itkBoundingBoxULL3FVCULLPF3___New_orig__
itkBoundingBoxULL3FVCULLPF3_cast = _itkBoundingBoxPython.itkBoundingBoxULL3FVCULLPF3_cast



