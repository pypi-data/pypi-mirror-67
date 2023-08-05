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
    from . import _itkJPEGImageIOPython
else:
    import _itkJPEGImageIOPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkJPEGImageIOPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkJPEGImageIOPython.SWIG_PyStaticMethod_New

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


import ITKIOImageBaseBasePython
import ITKCommonBasePython
import pyBasePython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython

def itkJPEGImageIOFactory_New():
  return itkJPEGImageIOFactory.New()


def itkJPEGImageIO_New():
  return itkJPEGImageIO.New()

class itkJPEGImageIO(ITKIOImageBaseBasePython.itkImageIOBase):
    r"""Proxy of C++ itkJPEGImageIO class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkJPEGImageIOPython.itkJPEGImageIO___New_orig__)
    Clone = _swig_new_instance_method(_itkJPEGImageIOPython.itkJPEGImageIO_Clone)
    SetQuality = _swig_new_instance_method(_itkJPEGImageIOPython.itkJPEGImageIO_SetQuality)
    GetQuality = _swig_new_instance_method(_itkJPEGImageIOPython.itkJPEGImageIO_GetQuality)
    SetProgressive = _swig_new_instance_method(_itkJPEGImageIOPython.itkJPEGImageIO_SetProgressive)
    GetProgressive = _swig_new_instance_method(_itkJPEGImageIOPython.itkJPEGImageIO_GetProgressive)
    ReadVolume = _swig_new_instance_method(_itkJPEGImageIOPython.itkJPEGImageIO_ReadVolume)
    __swig_destroy__ = _itkJPEGImageIOPython.delete_itkJPEGImageIO
    cast = _swig_new_static_method(_itkJPEGImageIOPython.itkJPEGImageIO_cast)

    def New(*args, **kargs):
        """New() -> itkJPEGImageIO

        Create a new object of the class itkJPEGImageIO and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkJPEGImageIO.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkJPEGImageIO.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkJPEGImageIO.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkJPEGImageIO in _itkJPEGImageIOPython:
_itkJPEGImageIOPython.itkJPEGImageIO_swigregister(itkJPEGImageIO)
itkJPEGImageIO___New_orig__ = _itkJPEGImageIOPython.itkJPEGImageIO___New_orig__
itkJPEGImageIO_cast = _itkJPEGImageIOPython.itkJPEGImageIO_cast

class itkJPEGImageIOFactory(ITKCommonBasePython.itkObjectFactoryBase):
    r"""Proxy of C++ itkJPEGImageIOFactory class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkJPEGImageIOPython.itkJPEGImageIOFactory___New_orig__)
    FactoryNew = _swig_new_static_method(_itkJPEGImageIOPython.itkJPEGImageIOFactory_FactoryNew)
    RegisterOneFactory = _swig_new_static_method(_itkJPEGImageIOPython.itkJPEGImageIOFactory_RegisterOneFactory)
    __swig_destroy__ = _itkJPEGImageIOPython.delete_itkJPEGImageIOFactory
    cast = _swig_new_static_method(_itkJPEGImageIOPython.itkJPEGImageIOFactory_cast)

    def New(*args, **kargs):
        """New() -> itkJPEGImageIOFactory

        Create a new object of the class itkJPEGImageIOFactory and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkJPEGImageIOFactory.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkJPEGImageIOFactory.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkJPEGImageIOFactory.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkJPEGImageIOFactory in _itkJPEGImageIOPython:
_itkJPEGImageIOPython.itkJPEGImageIOFactory_swigregister(itkJPEGImageIOFactory)
itkJPEGImageIOFactory___New_orig__ = _itkJPEGImageIOPython.itkJPEGImageIOFactory___New_orig__
itkJPEGImageIOFactory_FactoryNew = _itkJPEGImageIOPython.itkJPEGImageIOFactory_FactoryNew
itkJPEGImageIOFactory_RegisterOneFactory = _itkJPEGImageIOPython.itkJPEGImageIOFactory_RegisterOneFactory
itkJPEGImageIOFactory_cast = _itkJPEGImageIOPython.itkJPEGImageIOFactory_cast



