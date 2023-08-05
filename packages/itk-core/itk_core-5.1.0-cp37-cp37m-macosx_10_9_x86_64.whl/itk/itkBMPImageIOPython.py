# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkBMPImageIOPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkBMPImageIOPython', [dirname(__file__)])
        except ImportError:
            import _itkBMPImageIOPython
            return _itkBMPImageIOPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkBMPImageIOPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkBMPImageIOPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkBMPImageIOPython
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
import itkRGBPixelPython
import itkFixedArrayPython
import ITKIOImageBaseBasePython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython

def itkBMPImageIOFactory_New():
  return itkBMPImageIOFactory.New()


def itkBMPImageIO_New():
  return itkBMPImageIO.New()

class itkBMPImageIO(ITKIOImageBaseBasePython.itkImageIOBase):
    """


    Read BMPImage file format.

    C++ includes: itkBMPImageIO.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBMPImageIO_Pointer":
        """__New_orig__() -> itkBMPImageIO_Pointer"""
        return _itkBMPImageIOPython.itkBMPImageIO___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBMPImageIO_Pointer":
        """Clone(itkBMPImageIO self) -> itkBMPImageIO_Pointer"""
        return _itkBMPImageIOPython.itkBMPImageIO_Clone(self)


    def GetFileLowerLeft(self) -> "bool":
        """
        GetFileLowerLeft(itkBMPImageIO self) -> bool

        Getter for the
        FileLowerLeft attribute. 
        """
        return _itkBMPImageIOPython.itkBMPImageIO_GetFileLowerLeft(self)


    def GetBMPCompression(self) -> "long":
        """
        GetBMPCompression(itkBMPImageIO self) -> long

        Getter for the
        BMPCompression attribute. 
        """
        return _itkBMPImageIOPython.itkBMPImageIO_GetBMPCompression(self)


    def GetColorPalette(self) -> "std::vector< itkRGBPixelUC,std::allocator< itkRGBPixelUC > > const &":
        """
        GetColorPalette(itkBMPImageIO self) -> std::vector< itkRGBPixelUC,std::allocator< itkRGBPixelUC > > const &

        Getter for the
        ColorPalette attribute. 
        """
        return _itkBMPImageIOPython.itkBMPImageIO_GetColorPalette(self)


    def __init__(self):
        """
        __init__(itkBMPImageIO self) -> itkBMPImageIO



        Read BMPImage file format.

        C++ includes: itkBMPImageIO.h 
        """
        _itkBMPImageIOPython.itkBMPImageIO_swiginit(self, _itkBMPImageIOPython.new_itkBMPImageIO())

    def PrintSelf(self, os: 'ostream', indent: 'itkIndent') -> "void":
        """PrintSelf(itkBMPImageIO self, ostream os, itkIndent indent)"""
        return _itkBMPImageIOPython.itkBMPImageIO_PrintSelf(self, os, indent)

    __swig_destroy__ = _itkBMPImageIOPython.delete_itkBMPImageIO

    def cast(obj: 'itkLightObject') -> "itkBMPImageIO *":
        """cast(itkLightObject obj) -> itkBMPImageIO"""
        return _itkBMPImageIOPython.itkBMPImageIO_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkBMPImageIO

        Create a new object of the class itkBMPImageIO and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBMPImageIO.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBMPImageIO.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBMPImageIO.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBMPImageIO.Clone = new_instancemethod(_itkBMPImageIOPython.itkBMPImageIO_Clone, None, itkBMPImageIO)
itkBMPImageIO.GetFileLowerLeft = new_instancemethod(_itkBMPImageIOPython.itkBMPImageIO_GetFileLowerLeft, None, itkBMPImageIO)
itkBMPImageIO.GetBMPCompression = new_instancemethod(_itkBMPImageIOPython.itkBMPImageIO_GetBMPCompression, None, itkBMPImageIO)
itkBMPImageIO.GetColorPalette = new_instancemethod(_itkBMPImageIOPython.itkBMPImageIO_GetColorPalette, None, itkBMPImageIO)
itkBMPImageIO.PrintSelf = new_instancemethod(_itkBMPImageIOPython.itkBMPImageIO_PrintSelf, None, itkBMPImageIO)
itkBMPImageIO_swigregister = _itkBMPImageIOPython.itkBMPImageIO_swigregister
itkBMPImageIO_swigregister(itkBMPImageIO)

def itkBMPImageIO___New_orig__() -> "itkBMPImageIO_Pointer":
    """itkBMPImageIO___New_orig__() -> itkBMPImageIO_Pointer"""
    return _itkBMPImageIOPython.itkBMPImageIO___New_orig__()

def itkBMPImageIO_cast(obj: 'itkLightObject') -> "itkBMPImageIO *":
    """itkBMPImageIO_cast(itkLightObject obj) -> itkBMPImageIO"""
    return _itkBMPImageIOPython.itkBMPImageIO_cast(obj)

class itkBMPImageIOFactory(ITKCommonBasePython.itkObjectFactoryBase):
    """


    Create instances of BMPImageIO objects using an object factory.

    C++ includes: itkBMPImageIOFactory.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBMPImageIOFactory_Pointer":
        """__New_orig__() -> itkBMPImageIOFactory_Pointer"""
        return _itkBMPImageIOPython.itkBMPImageIOFactory___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def RegisterOneFactory() -> "void":
        """RegisterOneFactory()"""
        return _itkBMPImageIOPython.itkBMPImageIOFactory_RegisterOneFactory()

    RegisterOneFactory = staticmethod(RegisterOneFactory)
    __swig_destroy__ = _itkBMPImageIOPython.delete_itkBMPImageIOFactory

    def cast(obj: 'itkLightObject') -> "itkBMPImageIOFactory *":
        """cast(itkLightObject obj) -> itkBMPImageIOFactory"""
        return _itkBMPImageIOPython.itkBMPImageIOFactory_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkBMPImageIOFactory

        Create a new object of the class itkBMPImageIOFactory and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBMPImageIOFactory.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBMPImageIOFactory.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBMPImageIOFactory.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBMPImageIOFactory_swigregister = _itkBMPImageIOPython.itkBMPImageIOFactory_swigregister
itkBMPImageIOFactory_swigregister(itkBMPImageIOFactory)

def itkBMPImageIOFactory___New_orig__() -> "itkBMPImageIOFactory_Pointer":
    """itkBMPImageIOFactory___New_orig__() -> itkBMPImageIOFactory_Pointer"""
    return _itkBMPImageIOPython.itkBMPImageIOFactory___New_orig__()

def itkBMPImageIOFactory_RegisterOneFactory() -> "void":
    """itkBMPImageIOFactory_RegisterOneFactory()"""
    return _itkBMPImageIOPython.itkBMPImageIOFactory_RegisterOneFactory()

def itkBMPImageIOFactory_cast(obj: 'itkLightObject') -> "itkBMPImageIOFactory *":
    """itkBMPImageIOFactory_cast(itkLightObject obj) -> itkBMPImageIOFactory"""
    return _itkBMPImageIOPython.itkBMPImageIOFactory_cast(obj)



