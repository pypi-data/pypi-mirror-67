# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkListSamplePython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkListSamplePython', [dirname(__file__)])
        except ImportError:
            import _itkListSamplePython
            return _itkListSamplePython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkListSamplePython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkListSamplePython = swig_import_helper()
    del swig_import_helper
else:
    import _itkListSamplePython
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


import itkVectorPython
import itkFixedArrayPython
import pyBasePython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkSamplePython
import ITKCommonBasePython
import itkArrayPython

def itkListSampleVF3_New():
  return itkListSampleVF3.New()


def itkListSampleVF2_New():
  return itkListSampleVF2.New()

class itkListSampleVF2(itkSamplePython.itkSampleVF2):
    """


    This class is the native implementation of the a Sample with an STL
    container.

    ListSample stores measurements in a list type structure (as opposed to
    a Histogram, etc.). ListSample allows duplicate measurements.
    ListSample is not sorted.

    ListSample does not allow the user to specify the frequency of a
    measurement directly. The GetFrequency() methods returns 1 if the
    measurement exists in the list, 0 otherwise.

    See:   Sample, Histogram

    C++ includes: itkListSample.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkListSampleVF2_Pointer":
        """__New_orig__() -> itkListSampleVF2_Pointer"""
        return _itkListSamplePython.itkListSampleVF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkListSampleVF2_Pointer":
        """Clone(itkListSampleVF2 self) -> itkListSampleVF2_Pointer"""
        return _itkListSamplePython.itkListSampleVF2_Clone(self)


    def Resize(self, newsize: 'unsigned long') -> "void":
        """
        Resize(itkListSampleVF2 self, unsigned long newsize)

        Resize the container. Using
        Resize() and then SetMeasurementVector() is about nine times faster
        than usign PushBack() continuously. Which means that whenever the
        total number of Measurement vectors is known, the users should prefer
        calling Resize() first and then set the values by calling
        SetMeasurementVector(). On the other hand, if the number of
        measurement vectors is not known from the beginning, then calling
        PushBack() sequentially is a convenient option. 
        """
        return _itkListSamplePython.itkListSampleVF2_Resize(self, newsize)


    def Clear(self) -> "void":
        """
        Clear(itkListSampleVF2 self)

        Removes all the elements in
        the Sample 
        """
        return _itkListSamplePython.itkListSampleVF2_Clear(self)


    def PushBack(self, mv: 'itkVectorF2') -> "void":
        """
        PushBack(itkListSampleVF2 self, itkVectorF2 mv)

        Inserts a measurement at
        the end of the list 
        """
        return _itkListSamplePython.itkListSampleVF2_PushBack(self, mv)


    def SetMeasurement(self, id: 'unsigned long', dim: 'unsigned int', value: 'float const &') -> "void":
        """
        SetMeasurement(itkListSampleVF2 self, unsigned long id, unsigned int dim, float const & value)

        Set a component a
        measurement to a particular value. 
        """
        return _itkListSamplePython.itkListSampleVF2_SetMeasurement(self, id, dim, value)


    def SetMeasurementVector(self, id: 'unsigned long', mv: 'itkVectorF2') -> "void":
        """
        SetMeasurementVector(itkListSampleVF2 self, unsigned long id, itkVectorF2 mv)

        Replace a
        measurement with a different measurement 
        """
        return _itkListSamplePython.itkListSampleVF2_SetMeasurementVector(self, id, mv)

    __swig_destroy__ = _itkListSamplePython.delete_itkListSampleVF2

    def cast(obj: 'itkLightObject') -> "itkListSampleVF2 *":
        """cast(itkLightObject obj) -> itkListSampleVF2"""
        return _itkListSamplePython.itkListSampleVF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkListSampleVF2

        Create a new object of the class itkListSampleVF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkListSampleVF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkListSampleVF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkListSampleVF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkListSampleVF2.Clone = new_instancemethod(_itkListSamplePython.itkListSampleVF2_Clone, None, itkListSampleVF2)
itkListSampleVF2.Resize = new_instancemethod(_itkListSamplePython.itkListSampleVF2_Resize, None, itkListSampleVF2)
itkListSampleVF2.Clear = new_instancemethod(_itkListSamplePython.itkListSampleVF2_Clear, None, itkListSampleVF2)
itkListSampleVF2.PushBack = new_instancemethod(_itkListSamplePython.itkListSampleVF2_PushBack, None, itkListSampleVF2)
itkListSampleVF2.SetMeasurement = new_instancemethod(_itkListSamplePython.itkListSampleVF2_SetMeasurement, None, itkListSampleVF2)
itkListSampleVF2.SetMeasurementVector = new_instancemethod(_itkListSamplePython.itkListSampleVF2_SetMeasurementVector, None, itkListSampleVF2)
itkListSampleVF2_swigregister = _itkListSamplePython.itkListSampleVF2_swigregister
itkListSampleVF2_swigregister(itkListSampleVF2)

def itkListSampleVF2___New_orig__() -> "itkListSampleVF2_Pointer":
    """itkListSampleVF2___New_orig__() -> itkListSampleVF2_Pointer"""
    return _itkListSamplePython.itkListSampleVF2___New_orig__()

def itkListSampleVF2_cast(obj: 'itkLightObject') -> "itkListSampleVF2 *":
    """itkListSampleVF2_cast(itkLightObject obj) -> itkListSampleVF2"""
    return _itkListSamplePython.itkListSampleVF2_cast(obj)

class itkListSampleVF3(itkSamplePython.itkSampleVF3):
    """


    This class is the native implementation of the a Sample with an STL
    container.

    ListSample stores measurements in a list type structure (as opposed to
    a Histogram, etc.). ListSample allows duplicate measurements.
    ListSample is not sorted.

    ListSample does not allow the user to specify the frequency of a
    measurement directly. The GetFrequency() methods returns 1 if the
    measurement exists in the list, 0 otherwise.

    See:   Sample, Histogram

    C++ includes: itkListSample.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkListSampleVF3_Pointer":
        """__New_orig__() -> itkListSampleVF3_Pointer"""
        return _itkListSamplePython.itkListSampleVF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkListSampleVF3_Pointer":
        """Clone(itkListSampleVF3 self) -> itkListSampleVF3_Pointer"""
        return _itkListSamplePython.itkListSampleVF3_Clone(self)


    def Resize(self, newsize: 'unsigned long') -> "void":
        """
        Resize(itkListSampleVF3 self, unsigned long newsize)

        Resize the container. Using
        Resize() and then SetMeasurementVector() is about nine times faster
        than usign PushBack() continuously. Which means that whenever the
        total number of Measurement vectors is known, the users should prefer
        calling Resize() first and then set the values by calling
        SetMeasurementVector(). On the other hand, if the number of
        measurement vectors is not known from the beginning, then calling
        PushBack() sequentially is a convenient option. 
        """
        return _itkListSamplePython.itkListSampleVF3_Resize(self, newsize)


    def Clear(self) -> "void":
        """
        Clear(itkListSampleVF3 self)

        Removes all the elements in
        the Sample 
        """
        return _itkListSamplePython.itkListSampleVF3_Clear(self)


    def PushBack(self, mv: 'itkVectorF3') -> "void":
        """
        PushBack(itkListSampleVF3 self, itkVectorF3 mv)

        Inserts a measurement at
        the end of the list 
        """
        return _itkListSamplePython.itkListSampleVF3_PushBack(self, mv)


    def SetMeasurement(self, id: 'unsigned long', dim: 'unsigned int', value: 'float const &') -> "void":
        """
        SetMeasurement(itkListSampleVF3 self, unsigned long id, unsigned int dim, float const & value)

        Set a component a
        measurement to a particular value. 
        """
        return _itkListSamplePython.itkListSampleVF3_SetMeasurement(self, id, dim, value)


    def SetMeasurementVector(self, id: 'unsigned long', mv: 'itkVectorF3') -> "void":
        """
        SetMeasurementVector(itkListSampleVF3 self, unsigned long id, itkVectorF3 mv)

        Replace a
        measurement with a different measurement 
        """
        return _itkListSamplePython.itkListSampleVF3_SetMeasurementVector(self, id, mv)

    __swig_destroy__ = _itkListSamplePython.delete_itkListSampleVF3

    def cast(obj: 'itkLightObject') -> "itkListSampleVF3 *":
        """cast(itkLightObject obj) -> itkListSampleVF3"""
        return _itkListSamplePython.itkListSampleVF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkListSampleVF3

        Create a new object of the class itkListSampleVF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkListSampleVF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkListSampleVF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkListSampleVF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkListSampleVF3.Clone = new_instancemethod(_itkListSamplePython.itkListSampleVF3_Clone, None, itkListSampleVF3)
itkListSampleVF3.Resize = new_instancemethod(_itkListSamplePython.itkListSampleVF3_Resize, None, itkListSampleVF3)
itkListSampleVF3.Clear = new_instancemethod(_itkListSamplePython.itkListSampleVF3_Clear, None, itkListSampleVF3)
itkListSampleVF3.PushBack = new_instancemethod(_itkListSamplePython.itkListSampleVF3_PushBack, None, itkListSampleVF3)
itkListSampleVF3.SetMeasurement = new_instancemethod(_itkListSamplePython.itkListSampleVF3_SetMeasurement, None, itkListSampleVF3)
itkListSampleVF3.SetMeasurementVector = new_instancemethod(_itkListSamplePython.itkListSampleVF3_SetMeasurementVector, None, itkListSampleVF3)
itkListSampleVF3_swigregister = _itkListSamplePython.itkListSampleVF3_swigregister
itkListSampleVF3_swigregister(itkListSampleVF3)

def itkListSampleVF3___New_orig__() -> "itkListSampleVF3_Pointer":
    """itkListSampleVF3___New_orig__() -> itkListSampleVF3_Pointer"""
    return _itkListSamplePython.itkListSampleVF3___New_orig__()

def itkListSampleVF3_cast(obj: 'itkLightObject') -> "itkListSampleVF3 *":
    """itkListSampleVF3_cast(itkLightObject obj) -> itkListSampleVF3"""
    return _itkListSamplePython.itkListSampleVF3_cast(obj)



