# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkTIFFImageIOPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkTIFFImageIOPython', [dirname(__file__)])
        except ImportError:
            import _itkTIFFImageIOPython
            return _itkTIFFImageIOPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkTIFFImageIOPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkTIFFImageIOPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkTIFFImageIOPython
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


import itkRGBPixelPython
import itkFixedArrayPython
import pyBasePython
import ITKIOImageBaseBasePython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import ITKCommonBasePython

def itkTIFFImageIOFactory_New():
  return itkTIFFImageIOFactory.New()


def itkTIFFImageIO_New():
  return itkTIFFImageIO.New()

class itkTIFFImageIO(ITKIOImageBaseBasePython.itkImageIOBase):
    """


    ImageIO object for reading and writing TIFF images.

    The compressors supported include "PackBits" (default), "JPEG",
    "DEFLATE" and may also include "LZW". Only the "JPEG" compressor
    supports the compression level for JPEG quality parameter in the range
    0-100.

    C++ includes: itkTIFFImageIO.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkTIFFImageIO_Pointer":
        """__New_orig__() -> itkTIFFImageIO_Pointer"""
        return _itkTIFFImageIOPython.itkTIFFImageIO___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkTIFFImageIO_Pointer":
        """Clone(itkTIFFImageIO self) -> itkTIFFImageIO_Pointer"""
        return _itkTIFFImageIOPython.itkTIFFImageIO_Clone(self)


    def ReadVolume(self, buffer: 'void *') -> "void":
        """
        ReadVolume(itkTIFFImageIO self, void * buffer)

        Reads 3D data from
        multi-pages tiff. 
        """
        return _itkTIFFImageIOPython.itkTIFFImageIO_ReadVolume(self, buffer)

    NOFORMAT = _itkTIFFImageIOPython.itkTIFFImageIO_NOFORMAT
    RGB_ = _itkTIFFImageIOPython.itkTIFFImageIO_RGB_
    GRAYSCALE = _itkTIFFImageIOPython.itkTIFFImageIO_GRAYSCALE
    PALETTE_RGB = _itkTIFFImageIOPython.itkTIFFImageIO_PALETTE_RGB
    PALETTE_GRAYSCALE = _itkTIFFImageIOPython.itkTIFFImageIO_PALETTE_GRAYSCALE
    OTHER = _itkTIFFImageIOPython.itkTIFFImageIO_OTHER
    NoCompression = _itkTIFFImageIOPython.itkTIFFImageIO_NoCompression
    PackBits = _itkTIFFImageIOPython.itkTIFFImageIO_PackBits
    JPEG = _itkTIFFImageIOPython.itkTIFFImageIO_JPEG
    Deflate = _itkTIFFImageIOPython.itkTIFFImageIO_Deflate
    LZW = _itkTIFFImageIOPython.itkTIFFImageIO_LZW

    def SetCompressionToNoCompression(self) -> "void":
        """
        SetCompressionToNoCompression(itkTIFFImageIO self)

        Set
        type and automatically enable/disable compression.

        Since LZW compression is patented outside US, the additional work
        steps have to be taken in order to use that compression. 
        """
        return _itkTIFFImageIOPython.itkTIFFImageIO_SetCompressionToNoCompression(self)


    def SetCompressionToPackBits(self) -> "void":
        """SetCompressionToPackBits(itkTIFFImageIO self)"""
        return _itkTIFFImageIOPython.itkTIFFImageIO_SetCompressionToPackBits(self)


    def SetCompressionToJPEG(self) -> "void":
        """SetCompressionToJPEG(itkTIFFImageIO self)"""
        return _itkTIFFImageIOPython.itkTIFFImageIO_SetCompressionToJPEG(self)


    def SetCompressionToDeflate(self) -> "void":
        """SetCompressionToDeflate(itkTIFFImageIO self)"""
        return _itkTIFFImageIOPython.itkTIFFImageIO_SetCompressionToDeflate(self)


    def SetCompressionToLZW(self) -> "void":
        """SetCompressionToLZW(itkTIFFImageIO self)"""
        return _itkTIFFImageIOPython.itkTIFFImageIO_SetCompressionToLZW(self)


    def SetJPEGQuality(self, _JPEGQuality: 'int') -> "void":
        """
        SetJPEGQuality(itkTIFFImageIO self, int _JPEGQuality)

        Set/Get the level of
        quality for the output images if Compression is JPEG. Settings vary
        from 1 to 100. 100 is the highest quality. Default is 75 
        """
        return _itkTIFFImageIOPython.itkTIFFImageIO_SetJPEGQuality(self, _JPEGQuality)


    def GetJPEGQuality(self) -> "int":
        """GetJPEGQuality(itkTIFFImageIO self) -> int"""
        return _itkTIFFImageIOPython.itkTIFFImageIO_GetJPEGQuality(self)


    def GetColorPalette(self) -> "std::vector< itkRGBPixelUS,std::allocator< itkRGBPixelUS > > const &":
        """
        GetColorPalette(itkTIFFImageIO self) -> std::vector< itkRGBPixelUS,std::allocator< itkRGBPixelUS > > const &

        Get a const ref to
        the palette of the image. In the case of non palette image or
        ExpandRGBPalette set to true, a vector of size 0 is returned. For
        multipage Images, only the palette of the first page is read 
        """
        return _itkTIFFImageIOPython.itkTIFFImageIO_GetColorPalette(self)


    def SetColorPalette(self, _arg: 'std::vector< itkRGBPixelUS,std::allocator< itkRGBPixelUS > > const') -> "void":
        """
        SetColorPalette(itkTIFFImageIO self, std::vector< itkRGBPixelUS,std::allocator< itkRGBPixelUS > > const _arg)

        Set the palette of
        the image. For multipage images, the same palette is going to be used
        for all pages 
        """
        return _itkTIFFImageIOPython.itkTIFFImageIO_SetColorPalette(self, _arg)

    __swig_destroy__ = _itkTIFFImageIOPython.delete_itkTIFFImageIO

    def cast(obj: 'itkLightObject') -> "itkTIFFImageIO *":
        """cast(itkLightObject obj) -> itkTIFFImageIO"""
        return _itkTIFFImageIOPython.itkTIFFImageIO_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkTIFFImageIO

        Create a new object of the class itkTIFFImageIO and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTIFFImageIO.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTIFFImageIO.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTIFFImageIO.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkTIFFImageIO.Clone = new_instancemethod(_itkTIFFImageIOPython.itkTIFFImageIO_Clone, None, itkTIFFImageIO)
itkTIFFImageIO.ReadVolume = new_instancemethod(_itkTIFFImageIOPython.itkTIFFImageIO_ReadVolume, None, itkTIFFImageIO)
itkTIFFImageIO.SetCompressionToNoCompression = new_instancemethod(_itkTIFFImageIOPython.itkTIFFImageIO_SetCompressionToNoCompression, None, itkTIFFImageIO)
itkTIFFImageIO.SetCompressionToPackBits = new_instancemethod(_itkTIFFImageIOPython.itkTIFFImageIO_SetCompressionToPackBits, None, itkTIFFImageIO)
itkTIFFImageIO.SetCompressionToJPEG = new_instancemethod(_itkTIFFImageIOPython.itkTIFFImageIO_SetCompressionToJPEG, None, itkTIFFImageIO)
itkTIFFImageIO.SetCompressionToDeflate = new_instancemethod(_itkTIFFImageIOPython.itkTIFFImageIO_SetCompressionToDeflate, None, itkTIFFImageIO)
itkTIFFImageIO.SetCompressionToLZW = new_instancemethod(_itkTIFFImageIOPython.itkTIFFImageIO_SetCompressionToLZW, None, itkTIFFImageIO)
itkTIFFImageIO.SetJPEGQuality = new_instancemethod(_itkTIFFImageIOPython.itkTIFFImageIO_SetJPEGQuality, None, itkTIFFImageIO)
itkTIFFImageIO.GetJPEGQuality = new_instancemethod(_itkTIFFImageIOPython.itkTIFFImageIO_GetJPEGQuality, None, itkTIFFImageIO)
itkTIFFImageIO.GetColorPalette = new_instancemethod(_itkTIFFImageIOPython.itkTIFFImageIO_GetColorPalette, None, itkTIFFImageIO)
itkTIFFImageIO.SetColorPalette = new_instancemethod(_itkTIFFImageIOPython.itkTIFFImageIO_SetColorPalette, None, itkTIFFImageIO)
itkTIFFImageIO_swigregister = _itkTIFFImageIOPython.itkTIFFImageIO_swigregister
itkTIFFImageIO_swigregister(itkTIFFImageIO)

def itkTIFFImageIO___New_orig__() -> "itkTIFFImageIO_Pointer":
    """itkTIFFImageIO___New_orig__() -> itkTIFFImageIO_Pointer"""
    return _itkTIFFImageIOPython.itkTIFFImageIO___New_orig__()

def itkTIFFImageIO_cast(obj: 'itkLightObject') -> "itkTIFFImageIO *":
    """itkTIFFImageIO_cast(itkLightObject obj) -> itkTIFFImageIO"""
    return _itkTIFFImageIOPython.itkTIFFImageIO_cast(obj)

class itkTIFFImageIOFactory(ITKCommonBasePython.itkObjectFactoryBase):
    """


    Create instances of TIFFImageIO objects using an object factory.

    C++ includes: itkTIFFImageIOFactory.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkTIFFImageIOFactory_Pointer":
        """__New_orig__() -> itkTIFFImageIOFactory_Pointer"""
        return _itkTIFFImageIOPython.itkTIFFImageIOFactory___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def FactoryNew() -> "itkTIFFImageIOFactory *":
        """FactoryNew() -> itkTIFFImageIOFactory"""
        return _itkTIFFImageIOPython.itkTIFFImageIOFactory_FactoryNew()

    FactoryNew = staticmethod(FactoryNew)

    def RegisterOneFactory() -> "void":
        """RegisterOneFactory()"""
        return _itkTIFFImageIOPython.itkTIFFImageIOFactory_RegisterOneFactory()

    RegisterOneFactory = staticmethod(RegisterOneFactory)
    __swig_destroy__ = _itkTIFFImageIOPython.delete_itkTIFFImageIOFactory

    def cast(obj: 'itkLightObject') -> "itkTIFFImageIOFactory *":
        """cast(itkLightObject obj) -> itkTIFFImageIOFactory"""
        return _itkTIFFImageIOPython.itkTIFFImageIOFactory_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkTIFFImageIOFactory

        Create a new object of the class itkTIFFImageIOFactory and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTIFFImageIOFactory.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTIFFImageIOFactory.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTIFFImageIOFactory.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkTIFFImageIOFactory_swigregister = _itkTIFFImageIOPython.itkTIFFImageIOFactory_swigregister
itkTIFFImageIOFactory_swigregister(itkTIFFImageIOFactory)

def itkTIFFImageIOFactory___New_orig__() -> "itkTIFFImageIOFactory_Pointer":
    """itkTIFFImageIOFactory___New_orig__() -> itkTIFFImageIOFactory_Pointer"""
    return _itkTIFFImageIOPython.itkTIFFImageIOFactory___New_orig__()

def itkTIFFImageIOFactory_FactoryNew() -> "itkTIFFImageIOFactory *":
    """itkTIFFImageIOFactory_FactoryNew() -> itkTIFFImageIOFactory"""
    return _itkTIFFImageIOPython.itkTIFFImageIOFactory_FactoryNew()

def itkTIFFImageIOFactory_RegisterOneFactory() -> "void":
    """itkTIFFImageIOFactory_RegisterOneFactory()"""
    return _itkTIFFImageIOPython.itkTIFFImageIOFactory_RegisterOneFactory()

def itkTIFFImageIOFactory_cast(obj: 'itkLightObject') -> "itkTIFFImageIOFactory *":
    """itkTIFFImageIOFactory_cast(itkLightObject obj) -> itkTIFFImageIOFactory"""
    return _itkTIFFImageIOPython.itkTIFFImageIOFactory_cast(obj)



