# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkNiftiImageIOPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkNiftiImageIOPython', [dirname(__file__)])
        except ImportError:
            import _itkNiftiImageIOPython
            return _itkNiftiImageIOPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkNiftiImageIOPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkNiftiImageIOPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkNiftiImageIOPython
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


import ITKIOImageBaseBasePython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import pyBasePython
import ITKCommonBasePython

def itkNiftiImageIOFactory_New():
  return itkNiftiImageIOFactory.New()


def itkNiftiImageIO_New():
  return itkNiftiImageIO.New()


_itkNiftiImageIOPython.itkAnalyze75Flavor_AnalyzeITK4_swigconstant(_itkNiftiImageIOPython)
itkAnalyze75Flavor_AnalyzeITK4 = _itkNiftiImageIOPython.itkAnalyze75Flavor_AnalyzeITK4

_itkNiftiImageIOPython.itkAnalyze75Flavor_AnalyzeFSL_swigconstant(_itkNiftiImageIOPython)
itkAnalyze75Flavor_AnalyzeFSL = _itkNiftiImageIOPython.itkAnalyze75Flavor_AnalyzeFSL

_itkNiftiImageIOPython.itkAnalyze75Flavor_AnalyzeSPM_swigconstant(_itkNiftiImageIOPython)
itkAnalyze75Flavor_AnalyzeSPM = _itkNiftiImageIOPython.itkAnalyze75Flavor_AnalyzeSPM

_itkNiftiImageIOPython.itkAnalyze75Flavor_AnalyzeITK4Warning_swigconstant(_itkNiftiImageIOPython)
itkAnalyze75Flavor_AnalyzeITK4Warning = _itkNiftiImageIOPython.itkAnalyze75Flavor_AnalyzeITK4Warning

_itkNiftiImageIOPython.itkAnalyze75Flavor_AnalyzeReject_swigconstant(_itkNiftiImageIOPython)
itkAnalyze75Flavor_AnalyzeReject = _itkNiftiImageIOPython.itkAnalyze75Flavor_AnalyzeReject
class itkNiftiImageIO(ITKIOImageBaseBasePython.itkImageIOBase):
    """


    Class that defines how to read Nifti file format. Nifti IMAGE FILE
    FORMAT - As much information as I can determine from
    sourceforge.net/projects/Niftilib.

    Hans J. Johnson, The University of Iowa 2002 The specification for
    this file format is taken from the web sitehttp://analyzedirect.com/su
    pport/10.0Documents/Analyze_Resource_01.pdf

    C++ includes: itkNiftiImageIO.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkNiftiImageIO_Pointer":
        """__New_orig__() -> itkNiftiImageIO_Pointer"""
        return _itkNiftiImageIOPython.itkNiftiImageIO___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkNiftiImageIO_Pointer":
        """Clone(itkNiftiImageIO self) -> itkNiftiImageIO_Pointer"""
        return _itkNiftiImageIOPython.itkNiftiImageIO_Clone(self)

    FileType_TwoFileNifti = _itkNiftiImageIOPython.itkNiftiImageIO_FileType_TwoFileNifti
    FileType_OneFileNifti = _itkNiftiImageIOPython.itkNiftiImageIO_FileType_OneFileNifti
    FileType_Analyze75 = _itkNiftiImageIOPython.itkNiftiImageIO_FileType_Analyze75
    FileType_OtherOrError = _itkNiftiImageIOPython.itkNiftiImageIO_FileType_OtherOrError

    def DetermineFileType(self, FileNameToRead: 'char const *') -> "itkNiftiImageIO::FileType":
        """
        DetermineFileType(itkNiftiImageIO self, char const * FileNameToRead) -> itkNiftiImageIO::FileType

        Reads the file to
        determine if it can be read with this ImageIO implementation, and to
        determine what kind of file it is (Analyze vs NIfTI). Note that the
        value of LegacyAnalyze75Mode is ignored by this method.

        Parameters:
        -----------

        FileNameToRead:  The name of the file to test for reading.

        Returns one of the IOFileEnum enumerations. 
        """
        return _itkNiftiImageIOPython.itkNiftiImageIO_DetermineFileType(self, FileNameToRead)


    def SetRescaleSlope(self, _arg: 'double const') -> "void":
        """
        SetRescaleSlope(itkNiftiImageIO self, double const _arg)

        Set the slope and
        intercept for voxel value rescaling. 
        """
        return _itkNiftiImageIOPython.itkNiftiImageIO_SetRescaleSlope(self, _arg)


    def SetRescaleIntercept(self, _arg: 'double const') -> "void":
        """SetRescaleIntercept(itkNiftiImageIO self, double const _arg)"""
        return _itkNiftiImageIOPython.itkNiftiImageIO_SetRescaleIntercept(self, _arg)


    def SetLegacyAnalyze75Mode(self, _arg: 'itkAnalyze75Flavor const') -> "void":
        """
        SetLegacyAnalyze75Mode(itkNiftiImageIO self, itkAnalyze75Flavor const _arg)

        A mode to
        allow the Nifti filter to read and write to the LegacyAnalyze75 format
        as interpreted by the nifti library maintainers. This format does not
        properly respect the file orientation fields. By default this is set
        by configuration option ITK_NIFTI_IO_ANALYZE_FLAVOR 
        """
        return _itkNiftiImageIOPython.itkNiftiImageIO_SetLegacyAnalyze75Mode(self, _arg)


    def GetLegacyAnalyze75Mode(self) -> "itkAnalyze75Flavor":
        """GetLegacyAnalyze75Mode(itkNiftiImageIO self) -> itkAnalyze75Flavor"""
        return _itkNiftiImageIOPython.itkNiftiImageIO_GetLegacyAnalyze75Mode(self)

    __swig_destroy__ = _itkNiftiImageIOPython.delete_itkNiftiImageIO

    def cast(obj: 'itkLightObject') -> "itkNiftiImageIO *":
        """cast(itkLightObject obj) -> itkNiftiImageIO"""
        return _itkNiftiImageIOPython.itkNiftiImageIO_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkNiftiImageIO

        Create a new object of the class itkNiftiImageIO and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNiftiImageIO.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNiftiImageIO.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNiftiImageIO.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkNiftiImageIO.Clone = new_instancemethod(_itkNiftiImageIOPython.itkNiftiImageIO_Clone, None, itkNiftiImageIO)
itkNiftiImageIO.DetermineFileType = new_instancemethod(_itkNiftiImageIOPython.itkNiftiImageIO_DetermineFileType, None, itkNiftiImageIO)
itkNiftiImageIO.SetRescaleSlope = new_instancemethod(_itkNiftiImageIOPython.itkNiftiImageIO_SetRescaleSlope, None, itkNiftiImageIO)
itkNiftiImageIO.SetRescaleIntercept = new_instancemethod(_itkNiftiImageIOPython.itkNiftiImageIO_SetRescaleIntercept, None, itkNiftiImageIO)
itkNiftiImageIO.SetLegacyAnalyze75Mode = new_instancemethod(_itkNiftiImageIOPython.itkNiftiImageIO_SetLegacyAnalyze75Mode, None, itkNiftiImageIO)
itkNiftiImageIO.GetLegacyAnalyze75Mode = new_instancemethod(_itkNiftiImageIOPython.itkNiftiImageIO_GetLegacyAnalyze75Mode, None, itkNiftiImageIO)
itkNiftiImageIO_swigregister = _itkNiftiImageIOPython.itkNiftiImageIO_swigregister
itkNiftiImageIO_swigregister(itkNiftiImageIO)

def itkNiftiImageIO___New_orig__() -> "itkNiftiImageIO_Pointer":
    """itkNiftiImageIO___New_orig__() -> itkNiftiImageIO_Pointer"""
    return _itkNiftiImageIOPython.itkNiftiImageIO___New_orig__()

def itkNiftiImageIO_cast(obj: 'itkLightObject') -> "itkNiftiImageIO *":
    """itkNiftiImageIO_cast(itkLightObject obj) -> itkNiftiImageIO"""
    return _itkNiftiImageIOPython.itkNiftiImageIO_cast(obj)

class itkNiftiImageIOFactory(ITKCommonBasePython.itkObjectFactoryBase):
    """


    Create instances of NiftiImageIO objects using an object factory.

    C++ includes: itkNiftiImageIOFactory.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkNiftiImageIOFactory_Pointer":
        """__New_orig__() -> itkNiftiImageIOFactory_Pointer"""
        return _itkNiftiImageIOPython.itkNiftiImageIOFactory___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def RegisterOneFactory() -> "void":
        """RegisterOneFactory()"""
        return _itkNiftiImageIOPython.itkNiftiImageIOFactory_RegisterOneFactory()

    RegisterOneFactory = staticmethod(RegisterOneFactory)
    __swig_destroy__ = _itkNiftiImageIOPython.delete_itkNiftiImageIOFactory

    def cast(obj: 'itkLightObject') -> "itkNiftiImageIOFactory *":
        """cast(itkLightObject obj) -> itkNiftiImageIOFactory"""
        return _itkNiftiImageIOPython.itkNiftiImageIOFactory_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkNiftiImageIOFactory

        Create a new object of the class itkNiftiImageIOFactory and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkNiftiImageIOFactory.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkNiftiImageIOFactory.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkNiftiImageIOFactory.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkNiftiImageIOFactory_swigregister = _itkNiftiImageIOPython.itkNiftiImageIOFactory_swigregister
itkNiftiImageIOFactory_swigregister(itkNiftiImageIOFactory)

def itkNiftiImageIOFactory___New_orig__() -> "itkNiftiImageIOFactory_Pointer":
    """itkNiftiImageIOFactory___New_orig__() -> itkNiftiImageIOFactory_Pointer"""
    return _itkNiftiImageIOPython.itkNiftiImageIOFactory___New_orig__()

def itkNiftiImageIOFactory_RegisterOneFactory() -> "void":
    """itkNiftiImageIOFactory_RegisterOneFactory()"""
    return _itkNiftiImageIOPython.itkNiftiImageIOFactory_RegisterOneFactory()

def itkNiftiImageIOFactory_cast(obj: 'itkLightObject') -> "itkNiftiImageIOFactory *":
    """itkNiftiImageIOFactory_cast(itkLightObject obj) -> itkNiftiImageIOFactory"""
    return _itkNiftiImageIOPython.itkNiftiImageIOFactory_cast(obj)



