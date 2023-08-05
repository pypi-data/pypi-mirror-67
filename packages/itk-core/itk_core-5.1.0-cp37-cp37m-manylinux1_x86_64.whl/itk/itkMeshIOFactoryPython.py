# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkMeshIOFactoryPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkMeshIOFactoryPython', [dirname(__file__)])
        except ImportError:
            import _itkMeshIOFactoryPython
            return _itkMeshIOFactoryPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkMeshIOFactoryPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkMeshIOFactoryPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkMeshIOFactoryPython
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


import itkMeshIOBasePython
import ITKCommonBasePython
import pyBasePython

def itkMeshIOFactory_New():
  return itkMeshIOFactory.New()

class itkMeshIOFactory(ITKCommonBasePython.itkObject):
    """


    Create instances of MeshIO objects using an object factory.

    Below are the supported mesh file format: BYU Geometry File
    Format(*.byu) Freesurfer curvature file format (*.fcv) Freesurfer
    surface file format (ASCII *.fia and BINARY *.fsb) Geometry format
    under the neuroimaging informatics technology initiative (*.gii)
    Object file format (*.obj) VTK legacy file format (*.vtk)

    C++ includes: itkMeshIOFactory.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMeshIOFactory_Pointer":
        """__New_orig__() -> itkMeshIOFactory_Pointer"""
        return _itkMeshIOFactoryPython.itkMeshIOFactory___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMeshIOFactory_Pointer":
        """Clone(itkMeshIOFactory self) -> itkMeshIOFactory_Pointer"""
        return _itkMeshIOFactoryPython.itkMeshIOFactory_Clone(self)


    def CreateMeshIO(path: 'char const *', mode: 'itkCommonEnums::IOFileMode') -> "itkMeshIOBase_Pointer":
        """CreateMeshIO(char const * path, itkCommonEnums::IOFileMode mode) -> itkMeshIOBase_Pointer"""
        return _itkMeshIOFactoryPython.itkMeshIOFactory_CreateMeshIO(path, mode)

    CreateMeshIO = staticmethod(CreateMeshIO)
    __swig_destroy__ = _itkMeshIOFactoryPython.delete_itkMeshIOFactory

    def cast(obj: 'itkLightObject') -> "itkMeshIOFactory *":
        """cast(itkLightObject obj) -> itkMeshIOFactory"""
        return _itkMeshIOFactoryPython.itkMeshIOFactory_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkMeshIOFactory

        Create a new object of the class itkMeshIOFactory and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeshIOFactory.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeshIOFactory.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeshIOFactory.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMeshIOFactory.Clone = new_instancemethod(_itkMeshIOFactoryPython.itkMeshIOFactory_Clone, None, itkMeshIOFactory)
itkMeshIOFactory_swigregister = _itkMeshIOFactoryPython.itkMeshIOFactory_swigregister
itkMeshIOFactory_swigregister(itkMeshIOFactory)

def itkMeshIOFactory___New_orig__() -> "itkMeshIOFactory_Pointer":
    """itkMeshIOFactory___New_orig__() -> itkMeshIOFactory_Pointer"""
    return _itkMeshIOFactoryPython.itkMeshIOFactory___New_orig__()

def itkMeshIOFactory_CreateMeshIO(path: 'char const *', mode: 'itkCommonEnums::IOFileMode') -> "itkMeshIOBase_Pointer":
    """itkMeshIOFactory_CreateMeshIO(char const * path, itkCommonEnums::IOFileMode mode) -> itkMeshIOBase_Pointer"""
    return _itkMeshIOFactoryPython.itkMeshIOFactory_CreateMeshIO(path, mode)

def itkMeshIOFactory_cast(obj: 'itkLightObject') -> "itkMeshIOFactory *":
    """itkMeshIOFactory_cast(itkLightObject obj) -> itkMeshIOFactory"""
    return _itkMeshIOFactoryPython.itkMeshIOFactory_cast(obj)



