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
    from . import _itkVTKPolyDataReaderPython
else:
    import _itkVTKPolyDataReaderPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkVTKPolyDataReaderPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkVTKPolyDataReaderPython.SWIG_PyStaticMethod_New

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


import itkMeshBasePython
import itkVectorContainerPython
import itkPointPython
import itkFixedArrayPython
import pyBasePython
import itkVectorPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import vnl_vector_refPython
import ITKCommonBasePython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkOffsetPython
import itkSizePython
import itkContinuousIndexPython
import itkIndexPython
import itkBoundingBoxPython
import itkMapContainerPython
import itkArrayPython
import itkPointSetPython

def itkVTKPolyDataReaderMD3_New():
  return itkVTKPolyDataReaderMD3.New()


def itkVTKPolyDataReaderMD3_Superclass_New():
  return itkVTKPolyDataReaderMD3_Superclass.New()


def itkVTKPolyDataReaderMF3_New():
  return itkVTKPolyDataReaderMF3.New()


def itkVTKPolyDataReaderMF3_Superclass_New():
  return itkVTKPolyDataReaderMF3_Superclass.New()


def itkVTKPolyDataReaderMD2_New():
  return itkVTKPolyDataReaderMD2.New()


def itkVTKPolyDataReaderMD2_Superclass_New():
  return itkVTKPolyDataReaderMD2_Superclass.New()


def itkVTKPolyDataReaderMF2_New():
  return itkVTKPolyDataReaderMF2.New()


def itkVTKPolyDataReaderMF2_Superclass_New():
  return itkVTKPolyDataReaderMF2_Superclass.New()

class itkVTKPolyDataReaderMD2_Superclass(ITKCommonBasePython.itkProcessObject):
    r"""Proxy of C++ itkVTKPolyDataReaderMD2_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD2_Superclass___New_orig__)
    Clone = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD2_Superclass_Clone)
    GetOutput = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD2_Superclass_GetOutput)
    SetOutput = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD2_Superclass_SetOutput)
    GraftOutput = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD2_Superclass_GraftOutput)
    GraftNthOutput = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD2_Superclass_GraftNthOutput)
    __swig_destroy__ = _itkVTKPolyDataReaderPython.delete_itkVTKPolyDataReaderMD2_Superclass
    cast = _swig_new_static_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD2_Superclass_cast)

    def New(*args, **kargs):
        """New() -> itkVTKPolyDataReaderMD2_Superclass

        Create a new object of the class itkVTKPolyDataReaderMD2_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVTKPolyDataReaderMD2_Superclass.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkVTKPolyDataReaderMD2_Superclass.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkVTKPolyDataReaderMD2_Superclass.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVTKPolyDataReaderMD2_Superclass in _itkVTKPolyDataReaderPython:
_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD2_Superclass_swigregister(itkVTKPolyDataReaderMD2_Superclass)
itkVTKPolyDataReaderMD2_Superclass___New_orig__ = _itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD2_Superclass___New_orig__
itkVTKPolyDataReaderMD2_Superclass_cast = _itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD2_Superclass_cast

class itkVTKPolyDataReaderMD3_Superclass(ITKCommonBasePython.itkProcessObject):
    r"""Proxy of C++ itkVTKPolyDataReaderMD3_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD3_Superclass___New_orig__)
    Clone = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD3_Superclass_Clone)
    GetOutput = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD3_Superclass_GetOutput)
    SetOutput = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD3_Superclass_SetOutput)
    GraftOutput = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD3_Superclass_GraftOutput)
    GraftNthOutput = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD3_Superclass_GraftNthOutput)
    __swig_destroy__ = _itkVTKPolyDataReaderPython.delete_itkVTKPolyDataReaderMD3_Superclass
    cast = _swig_new_static_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD3_Superclass_cast)

    def New(*args, **kargs):
        """New() -> itkVTKPolyDataReaderMD3_Superclass

        Create a new object of the class itkVTKPolyDataReaderMD3_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVTKPolyDataReaderMD3_Superclass.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkVTKPolyDataReaderMD3_Superclass.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkVTKPolyDataReaderMD3_Superclass.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVTKPolyDataReaderMD3_Superclass in _itkVTKPolyDataReaderPython:
_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD3_Superclass_swigregister(itkVTKPolyDataReaderMD3_Superclass)
itkVTKPolyDataReaderMD3_Superclass___New_orig__ = _itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD3_Superclass___New_orig__
itkVTKPolyDataReaderMD3_Superclass_cast = _itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD3_Superclass_cast

class itkVTKPolyDataReaderMF2_Superclass(ITKCommonBasePython.itkProcessObject):
    r"""Proxy of C++ itkVTKPolyDataReaderMF2_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF2_Superclass___New_orig__)
    Clone = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF2_Superclass_Clone)
    GetOutput = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF2_Superclass_GetOutput)
    SetOutput = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF2_Superclass_SetOutput)
    GraftOutput = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF2_Superclass_GraftOutput)
    GraftNthOutput = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF2_Superclass_GraftNthOutput)
    __swig_destroy__ = _itkVTKPolyDataReaderPython.delete_itkVTKPolyDataReaderMF2_Superclass
    cast = _swig_new_static_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF2_Superclass_cast)

    def New(*args, **kargs):
        """New() -> itkVTKPolyDataReaderMF2_Superclass

        Create a new object of the class itkVTKPolyDataReaderMF2_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVTKPolyDataReaderMF2_Superclass.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkVTKPolyDataReaderMF2_Superclass.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkVTKPolyDataReaderMF2_Superclass.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVTKPolyDataReaderMF2_Superclass in _itkVTKPolyDataReaderPython:
_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF2_Superclass_swigregister(itkVTKPolyDataReaderMF2_Superclass)
itkVTKPolyDataReaderMF2_Superclass___New_orig__ = _itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF2_Superclass___New_orig__
itkVTKPolyDataReaderMF2_Superclass_cast = _itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF2_Superclass_cast

class itkVTKPolyDataReaderMF3_Superclass(ITKCommonBasePython.itkProcessObject):
    r"""Proxy of C++ itkVTKPolyDataReaderMF3_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF3_Superclass___New_orig__)
    Clone = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF3_Superclass_Clone)
    GetOutput = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF3_Superclass_GetOutput)
    SetOutput = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF3_Superclass_SetOutput)
    GraftOutput = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF3_Superclass_GraftOutput)
    GraftNthOutput = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF3_Superclass_GraftNthOutput)
    __swig_destroy__ = _itkVTKPolyDataReaderPython.delete_itkVTKPolyDataReaderMF3_Superclass
    cast = _swig_new_static_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF3_Superclass_cast)

    def New(*args, **kargs):
        """New() -> itkVTKPolyDataReaderMF3_Superclass

        Create a new object of the class itkVTKPolyDataReaderMF3_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVTKPolyDataReaderMF3_Superclass.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkVTKPolyDataReaderMF3_Superclass.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkVTKPolyDataReaderMF3_Superclass.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVTKPolyDataReaderMF3_Superclass in _itkVTKPolyDataReaderPython:
_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF3_Superclass_swigregister(itkVTKPolyDataReaderMF3_Superclass)
itkVTKPolyDataReaderMF3_Superclass___New_orig__ = _itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF3_Superclass___New_orig__
itkVTKPolyDataReaderMF3_Superclass_cast = _itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF3_Superclass_cast

class itkVTKPolyDataReaderMD2(itkVTKPolyDataReaderMD2_Superclass):
    r"""Proxy of C++ itkVTKPolyDataReaderMD2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD2___New_orig__)
    Clone = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD2_Clone)
    SetFileName = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD2_SetFileName)
    GetFileName = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD2_GetFileName)
    GetVersion = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD2_GetVersion)
    GetHeader = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD2_GetHeader)
    __swig_destroy__ = _itkVTKPolyDataReaderPython.delete_itkVTKPolyDataReaderMD2
    cast = _swig_new_static_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD2_cast)

    def New(*args, **kargs):
        """New() -> itkVTKPolyDataReaderMD2

        Create a new object of the class itkVTKPolyDataReaderMD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVTKPolyDataReaderMD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkVTKPolyDataReaderMD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkVTKPolyDataReaderMD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVTKPolyDataReaderMD2 in _itkVTKPolyDataReaderPython:
_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD2_swigregister(itkVTKPolyDataReaderMD2)
itkVTKPolyDataReaderMD2___New_orig__ = _itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD2___New_orig__
itkVTKPolyDataReaderMD2_cast = _itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD2_cast

class itkVTKPolyDataReaderMD3(itkVTKPolyDataReaderMD3_Superclass):
    r"""Proxy of C++ itkVTKPolyDataReaderMD3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD3___New_orig__)
    Clone = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD3_Clone)
    SetFileName = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD3_SetFileName)
    GetFileName = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD3_GetFileName)
    GetVersion = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD3_GetVersion)
    GetHeader = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD3_GetHeader)
    __swig_destroy__ = _itkVTKPolyDataReaderPython.delete_itkVTKPolyDataReaderMD3
    cast = _swig_new_static_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD3_cast)

    def New(*args, **kargs):
        """New() -> itkVTKPolyDataReaderMD3

        Create a new object of the class itkVTKPolyDataReaderMD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVTKPolyDataReaderMD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkVTKPolyDataReaderMD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkVTKPolyDataReaderMD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVTKPolyDataReaderMD3 in _itkVTKPolyDataReaderPython:
_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD3_swigregister(itkVTKPolyDataReaderMD3)
itkVTKPolyDataReaderMD3___New_orig__ = _itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD3___New_orig__
itkVTKPolyDataReaderMD3_cast = _itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMD3_cast

class itkVTKPolyDataReaderMF2(itkVTKPolyDataReaderMF2_Superclass):
    r"""Proxy of C++ itkVTKPolyDataReaderMF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF2___New_orig__)
    Clone = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF2_Clone)
    SetFileName = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF2_SetFileName)
    GetFileName = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF2_GetFileName)
    GetVersion = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF2_GetVersion)
    GetHeader = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF2_GetHeader)
    __swig_destroy__ = _itkVTKPolyDataReaderPython.delete_itkVTKPolyDataReaderMF2
    cast = _swig_new_static_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF2_cast)

    def New(*args, **kargs):
        """New() -> itkVTKPolyDataReaderMF2

        Create a new object of the class itkVTKPolyDataReaderMF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVTKPolyDataReaderMF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkVTKPolyDataReaderMF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkVTKPolyDataReaderMF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVTKPolyDataReaderMF2 in _itkVTKPolyDataReaderPython:
_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF2_swigregister(itkVTKPolyDataReaderMF2)
itkVTKPolyDataReaderMF2___New_orig__ = _itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF2___New_orig__
itkVTKPolyDataReaderMF2_cast = _itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF2_cast

class itkVTKPolyDataReaderMF3(itkVTKPolyDataReaderMF3_Superclass):
    r"""Proxy of C++ itkVTKPolyDataReaderMF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF3___New_orig__)
    Clone = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF3_Clone)
    SetFileName = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF3_SetFileName)
    GetFileName = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF3_GetFileName)
    GetVersion = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF3_GetVersion)
    GetHeader = _swig_new_instance_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF3_GetHeader)
    __swig_destroy__ = _itkVTKPolyDataReaderPython.delete_itkVTKPolyDataReaderMF3
    cast = _swig_new_static_method(_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF3_cast)

    def New(*args, **kargs):
        """New() -> itkVTKPolyDataReaderMF3

        Create a new object of the class itkVTKPolyDataReaderMF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVTKPolyDataReaderMF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkVTKPolyDataReaderMF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkVTKPolyDataReaderMF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkVTKPolyDataReaderMF3 in _itkVTKPolyDataReaderPython:
_itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF3_swigregister(itkVTKPolyDataReaderMF3)
itkVTKPolyDataReaderMF3___New_orig__ = _itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF3___New_orig__
itkVTKPolyDataReaderMF3_cast = _itkVTKPolyDataReaderPython.itkVTKPolyDataReaderMF3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def vtk_poly_data_reader(*args, **kwargs):
    """Procedural interface for VTKPolyDataReader"""
    import itk
    instance = itk.VTKPolyDataReader.New(*args, **kwargs)
    return instance.__internal_call__()

def vtk_poly_data_reader_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.VTKPolyDataReader, itkTemplate.itkTemplate):
        filter_object = itk.VTKPolyDataReader.values()[0]
    else:
        filter_object = itk.VTKPolyDataReader

    vtk_poly_data_reader.__doc__ = filter_object.__doc__
    vtk_poly_data_reader.__doc__ += "\n Args are Input(s) to the filter.\n"
    vtk_poly_data_reader.__doc__ += "Available Keyword Arguments:\n"
    vtk_poly_data_reader.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])
import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def mesh_source(*args, **kwargs):
    """Procedural interface for MeshSource"""
    import itk
    instance = itk.MeshSource.New(*args, **kwargs)
    return instance.__internal_call__()

def mesh_source_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.MeshSource, itkTemplate.itkTemplate):
        filter_object = itk.MeshSource.values()[0]
    else:
        filter_object = itk.MeshSource

    mesh_source.__doc__ = filter_object.__doc__
    mesh_source.__doc__ += "\n Args are Input(s) to the filter.\n"
    mesh_source.__doc__ += "Available Keyword Arguments:\n"
    mesh_source.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



