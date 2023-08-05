# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkVTKImageIOPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkVTKImageIOPython', [dirname(__file__)])
        except ImportError:
            import _itkVTKImageIOPython
            return _itkVTKImageIOPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkVTKImageIOPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkVTKImageIOPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkVTKImageIOPython
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


import ITKCommonBasePython
import pyBasePython
import ITKIOImageBaseBasePython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython

def itkVTKImageIOFactory_New():
  return itkVTKImageIOFactory.New()


def itkVTKImageIO_New():
  return itkVTKImageIO.New()

class itkVTKImageIO(ITKIOImageBaseBasePython.itkStreamingImageIOBase):
    """


    ImageIO class for reading VTK images.

    This implementation was taken fron the Insight
    Joural:https://hdl.handle.net/10380/3171

    C++ includes: itkVTKImageIO.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkVTKImageIO_Pointer":
        """__New_orig__() -> itkVTKImageIO_Pointer"""
        return _itkVTKImageIOPython.itkVTKImageIO___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkVTKImageIO_Pointer":
        """Clone(itkVTKImageIO self) -> itkVTKImageIO_Pointer"""
        return _itkVTKImageIOPython.itkVTKImageIO_Clone(self)


    def GetHeaderSize(self) -> "long":
        """
        GetHeaderSize(itkVTKImageIO self) -> long

        returns the header
        size, if it is unknown it will return 0 
        """
        return _itkVTKImageIOPython.itkVTKImageIO_GetHeaderSize(self)

    __swig_destroy__ = _itkVTKImageIOPython.delete_itkVTKImageIO

    def cast(obj: 'itkLightObject') -> "itkVTKImageIO *":
        """cast(itkLightObject obj) -> itkVTKImageIO"""
        return _itkVTKImageIOPython.itkVTKImageIO_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkVTKImageIO

        Create a new object of the class itkVTKImageIO and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVTKImageIO.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkVTKImageIO.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkVTKImageIO.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkVTKImageIO.Clone = new_instancemethod(_itkVTKImageIOPython.itkVTKImageIO_Clone, None, itkVTKImageIO)
itkVTKImageIO.GetHeaderSize = new_instancemethod(_itkVTKImageIOPython.itkVTKImageIO_GetHeaderSize, None, itkVTKImageIO)
itkVTKImageIO_swigregister = _itkVTKImageIOPython.itkVTKImageIO_swigregister
itkVTKImageIO_swigregister(itkVTKImageIO)

def itkVTKImageIO___New_orig__() -> "itkVTKImageIO_Pointer":
    """itkVTKImageIO___New_orig__() -> itkVTKImageIO_Pointer"""
    return _itkVTKImageIOPython.itkVTKImageIO___New_orig__()

def itkVTKImageIO_cast(obj: 'itkLightObject') -> "itkVTKImageIO *":
    """itkVTKImageIO_cast(itkLightObject obj) -> itkVTKImageIO"""
    return _itkVTKImageIOPython.itkVTKImageIO_cast(obj)

class itkVTKImageIOFactory(ITKCommonBasePython.itkObjectFactoryBase):
    """


    Create instances of VTKImageIO objects using an object factory.

    C++ includes: itkVTKImageIOFactory.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkVTKImageIOFactory_Pointer":
        """__New_orig__() -> itkVTKImageIOFactory_Pointer"""
        return _itkVTKImageIOPython.itkVTKImageIOFactory___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def RegisterOneFactory() -> "void":
        """RegisterOneFactory()"""
        return _itkVTKImageIOPython.itkVTKImageIOFactory_RegisterOneFactory()

    RegisterOneFactory = staticmethod(RegisterOneFactory)
    __swig_destroy__ = _itkVTKImageIOPython.delete_itkVTKImageIOFactory

    def cast(obj: 'itkLightObject') -> "itkVTKImageIOFactory *":
        """cast(itkLightObject obj) -> itkVTKImageIOFactory"""
        return _itkVTKImageIOPython.itkVTKImageIOFactory_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkVTKImageIOFactory

        Create a new object of the class itkVTKImageIOFactory and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVTKImageIOFactory.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkVTKImageIOFactory.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkVTKImageIOFactory.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkVTKImageIOFactory_swigregister = _itkVTKImageIOPython.itkVTKImageIOFactory_swigregister
itkVTKImageIOFactory_swigregister(itkVTKImageIOFactory)

def itkVTKImageIOFactory___New_orig__() -> "itkVTKImageIOFactory_Pointer":
    """itkVTKImageIOFactory___New_orig__() -> itkVTKImageIOFactory_Pointer"""
    return _itkVTKImageIOPython.itkVTKImageIOFactory___New_orig__()

def itkVTKImageIOFactory_RegisterOneFactory() -> "void":
    """itkVTKImageIOFactory_RegisterOneFactory()"""
    return _itkVTKImageIOPython.itkVTKImageIOFactory_RegisterOneFactory()

def itkVTKImageIOFactory_cast(obj: 'itkLightObject') -> "itkVTKImageIOFactory *":
    """itkVTKImageIOFactory_cast(itkLightObject obj) -> itkVTKImageIOFactory"""
    return _itkVTKImageIOPython.itkVTKImageIOFactory_cast(obj)



