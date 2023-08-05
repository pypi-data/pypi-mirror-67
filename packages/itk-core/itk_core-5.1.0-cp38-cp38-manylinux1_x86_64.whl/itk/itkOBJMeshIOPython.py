# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkOBJMeshIOPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkOBJMeshIOPython', [dirname(__file__)])
        except ImportError:
            import _itkOBJMeshIOPython
            return _itkOBJMeshIOPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkOBJMeshIOPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkOBJMeshIOPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkOBJMeshIOPython
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

def itkOBJMeshIOFactory_New():
  return itkOBJMeshIOFactory.New()


def itkOBJMeshIO_New():
  return itkOBJMeshIO.New()

class itkOBJMeshIO(itkMeshIOBasePython.itkMeshIOBase):
    """


    This class defines how to read and write Object file format.

    C++ includes: itkOBJMeshIO.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkOBJMeshIO_Pointer":
        """__New_orig__() -> itkOBJMeshIO_Pointer"""
        return _itkOBJMeshIOPython.itkOBJMeshIO___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkOBJMeshIO_Pointer":
        """Clone(itkOBJMeshIO self) -> itkOBJMeshIO_Pointer"""
        return _itkOBJMeshIOPython.itkOBJMeshIO_Clone(self)

    __swig_destroy__ = _itkOBJMeshIOPython.delete_itkOBJMeshIO

    def cast(obj: 'itkLightObject') -> "itkOBJMeshIO *":
        """cast(itkLightObject obj) -> itkOBJMeshIO"""
        return _itkOBJMeshIOPython.itkOBJMeshIO_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkOBJMeshIO

        Create a new object of the class itkOBJMeshIO and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkOBJMeshIO.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkOBJMeshIO.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkOBJMeshIO.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkOBJMeshIO.Clone = new_instancemethod(_itkOBJMeshIOPython.itkOBJMeshIO_Clone, None, itkOBJMeshIO)
itkOBJMeshIO_swigregister = _itkOBJMeshIOPython.itkOBJMeshIO_swigregister
itkOBJMeshIO_swigregister(itkOBJMeshIO)

def itkOBJMeshIO___New_orig__() -> "itkOBJMeshIO_Pointer":
    """itkOBJMeshIO___New_orig__() -> itkOBJMeshIO_Pointer"""
    return _itkOBJMeshIOPython.itkOBJMeshIO___New_orig__()

def itkOBJMeshIO_cast(obj: 'itkLightObject') -> "itkOBJMeshIO *":
    """itkOBJMeshIO_cast(itkLightObject obj) -> itkOBJMeshIO"""
    return _itkOBJMeshIOPython.itkOBJMeshIO_cast(obj)

class itkOBJMeshIOFactory(ITKCommonBasePython.itkObjectFactoryBase):
    """


    Create instances of OBJMeshIO objects using an object factory.

    C++ includes: itkOBJMeshIOFactory.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkOBJMeshIOFactory_Pointer":
        """__New_orig__() -> itkOBJMeshIOFactory_Pointer"""
        return _itkOBJMeshIOPython.itkOBJMeshIOFactory___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def RegisterOneFactory() -> "void":
        """RegisterOneFactory()"""
        return _itkOBJMeshIOPython.itkOBJMeshIOFactory_RegisterOneFactory()

    RegisterOneFactory = staticmethod(RegisterOneFactory)
    __swig_destroy__ = _itkOBJMeshIOPython.delete_itkOBJMeshIOFactory

    def cast(obj: 'itkLightObject') -> "itkOBJMeshIOFactory *":
        """cast(itkLightObject obj) -> itkOBJMeshIOFactory"""
        return _itkOBJMeshIOPython.itkOBJMeshIOFactory_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkOBJMeshIOFactory

        Create a new object of the class itkOBJMeshIOFactory and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkOBJMeshIOFactory.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkOBJMeshIOFactory.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkOBJMeshIOFactory.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkOBJMeshIOFactory_swigregister = _itkOBJMeshIOPython.itkOBJMeshIOFactory_swigregister
itkOBJMeshIOFactory_swigregister(itkOBJMeshIOFactory)

def itkOBJMeshIOFactory___New_orig__() -> "itkOBJMeshIOFactory_Pointer":
    """itkOBJMeshIOFactory___New_orig__() -> itkOBJMeshIOFactory_Pointer"""
    return _itkOBJMeshIOPython.itkOBJMeshIOFactory___New_orig__()

def itkOBJMeshIOFactory_RegisterOneFactory() -> "void":
    """itkOBJMeshIOFactory_RegisterOneFactory()"""
    return _itkOBJMeshIOPython.itkOBJMeshIOFactory_RegisterOneFactory()

def itkOBJMeshIOFactory_cast(obj: 'itkLightObject') -> "itkOBJMeshIOFactory *":
    """itkOBJMeshIOFactory_cast(itkLightObject obj) -> itkOBJMeshIOFactory"""
    return _itkOBJMeshIOPython.itkOBJMeshIOFactory_cast(obj)



