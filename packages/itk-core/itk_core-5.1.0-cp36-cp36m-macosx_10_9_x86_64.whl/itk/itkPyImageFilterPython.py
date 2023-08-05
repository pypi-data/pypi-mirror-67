# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkPyImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkPyImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkPyImageFilterPython
            return _itkPyImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkPyImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkPyImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkPyImageFilterPython
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


import itkImageToImageFilterAPython
import ITKCommonBasePython
import pyBasePython
import itkImageSourcePython
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkImageSourceCommonPython
import itkVectorImagePython
import stdcomplexPython
import itkVariableLengthVectorPython
import itkImagePython
import itkSymmetricSecondRankTensorPython
import itkFixedArrayPython
import itkMatrixPython
import vnl_matrixPython
import vnl_vectorPython
import itkPointPython
import vnl_vector_refPython
import itkVectorPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkImageToImageFilterCommonPython

def itkPyImageFilterIUS3IUS3_New():
  return itkPyImageFilterIUS3IUS3.New()


def itkPyImageFilterIUS2IUS2_New():
  return itkPyImageFilterIUS2IUS2.New()


def itkPyImageFilterIUC3IUC3_New():
  return itkPyImageFilterIUC3IUC3.New()


def itkPyImageFilterIUC2IUC2_New():
  return itkPyImageFilterIUC2IUC2.New()

class itkPyImageFilterIUC2IUC2(itkImageToImageFilterAPython.itkImageToImageFilterIUC2IUC2):
    """


    ImageToImageFilter subclass that calls a Python callable object, e.g.
    a Python function.

    C++ includes: itkPyImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkPyImageFilterIUC2IUC2_Pointer":
        """__New_orig__() -> itkPyImageFilterIUC2IUC2_Pointer"""
        return _itkPyImageFilterPython.itkPyImageFilterIUC2IUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkPyImageFilterIUC2IUC2_Pointer":
        """Clone(itkPyImageFilterIUC2IUC2 self) -> itkPyImageFilterIUC2IUC2_Pointer"""
        return _itkPyImageFilterPython.itkPyImageFilterIUC2IUC2_Clone(self)


    def SetPyGenerateData(self, obj: 'PyObject *') -> "void":
        """SetPyGenerateData(itkPyImageFilterIUC2IUC2 self, PyObject * obj)"""
        return _itkPyImageFilterPython.itkPyImageFilterIUC2IUC2_SetPyGenerateData(self, obj)

    __swig_destroy__ = _itkPyImageFilterPython.delete_itkPyImageFilterIUC2IUC2

    def cast(obj: 'itkLightObject') -> "itkPyImageFilterIUC2IUC2 *":
        """cast(itkLightObject obj) -> itkPyImageFilterIUC2IUC2"""
        return _itkPyImageFilterPython.itkPyImageFilterIUC2IUC2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkPyImageFilterIUC2IUC2

        Create a new object of the class itkPyImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPyImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkPyImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkPyImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkPyImageFilterIUC2IUC2.Clone = new_instancemethod(_itkPyImageFilterPython.itkPyImageFilterIUC2IUC2_Clone, None, itkPyImageFilterIUC2IUC2)
itkPyImageFilterIUC2IUC2.SetPyGenerateData = new_instancemethod(_itkPyImageFilterPython.itkPyImageFilterIUC2IUC2_SetPyGenerateData, None, itkPyImageFilterIUC2IUC2)
itkPyImageFilterIUC2IUC2_swigregister = _itkPyImageFilterPython.itkPyImageFilterIUC2IUC2_swigregister
itkPyImageFilterIUC2IUC2_swigregister(itkPyImageFilterIUC2IUC2)

def itkPyImageFilterIUC2IUC2___New_orig__() -> "itkPyImageFilterIUC2IUC2_Pointer":
    """itkPyImageFilterIUC2IUC2___New_orig__() -> itkPyImageFilterIUC2IUC2_Pointer"""
    return _itkPyImageFilterPython.itkPyImageFilterIUC2IUC2___New_orig__()

def itkPyImageFilterIUC2IUC2_cast(obj: 'itkLightObject') -> "itkPyImageFilterIUC2IUC2 *":
    """itkPyImageFilterIUC2IUC2_cast(itkLightObject obj) -> itkPyImageFilterIUC2IUC2"""
    return _itkPyImageFilterPython.itkPyImageFilterIUC2IUC2_cast(obj)

class itkPyImageFilterIUC3IUC3(itkImageToImageFilterAPython.itkImageToImageFilterIUC3IUC3):
    """


    ImageToImageFilter subclass that calls a Python callable object, e.g.
    a Python function.

    C++ includes: itkPyImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkPyImageFilterIUC3IUC3_Pointer":
        """__New_orig__() -> itkPyImageFilterIUC3IUC3_Pointer"""
        return _itkPyImageFilterPython.itkPyImageFilterIUC3IUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkPyImageFilterIUC3IUC3_Pointer":
        """Clone(itkPyImageFilterIUC3IUC3 self) -> itkPyImageFilterIUC3IUC3_Pointer"""
        return _itkPyImageFilterPython.itkPyImageFilterIUC3IUC3_Clone(self)


    def SetPyGenerateData(self, obj: 'PyObject *') -> "void":
        """SetPyGenerateData(itkPyImageFilterIUC3IUC3 self, PyObject * obj)"""
        return _itkPyImageFilterPython.itkPyImageFilterIUC3IUC3_SetPyGenerateData(self, obj)

    __swig_destroy__ = _itkPyImageFilterPython.delete_itkPyImageFilterIUC3IUC3

    def cast(obj: 'itkLightObject') -> "itkPyImageFilterIUC3IUC3 *":
        """cast(itkLightObject obj) -> itkPyImageFilterIUC3IUC3"""
        return _itkPyImageFilterPython.itkPyImageFilterIUC3IUC3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkPyImageFilterIUC3IUC3

        Create a new object of the class itkPyImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPyImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkPyImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkPyImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkPyImageFilterIUC3IUC3.Clone = new_instancemethod(_itkPyImageFilterPython.itkPyImageFilterIUC3IUC3_Clone, None, itkPyImageFilterIUC3IUC3)
itkPyImageFilterIUC3IUC3.SetPyGenerateData = new_instancemethod(_itkPyImageFilterPython.itkPyImageFilterIUC3IUC3_SetPyGenerateData, None, itkPyImageFilterIUC3IUC3)
itkPyImageFilterIUC3IUC3_swigregister = _itkPyImageFilterPython.itkPyImageFilterIUC3IUC3_swigregister
itkPyImageFilterIUC3IUC3_swigregister(itkPyImageFilterIUC3IUC3)

def itkPyImageFilterIUC3IUC3___New_orig__() -> "itkPyImageFilterIUC3IUC3_Pointer":
    """itkPyImageFilterIUC3IUC3___New_orig__() -> itkPyImageFilterIUC3IUC3_Pointer"""
    return _itkPyImageFilterPython.itkPyImageFilterIUC3IUC3___New_orig__()

def itkPyImageFilterIUC3IUC3_cast(obj: 'itkLightObject') -> "itkPyImageFilterIUC3IUC3 *":
    """itkPyImageFilterIUC3IUC3_cast(itkLightObject obj) -> itkPyImageFilterIUC3IUC3"""
    return _itkPyImageFilterPython.itkPyImageFilterIUC3IUC3_cast(obj)

class itkPyImageFilterIUS2IUS2(itkImageToImageFilterAPython.itkImageToImageFilterIUS2IUS2):
    """


    ImageToImageFilter subclass that calls a Python callable object, e.g.
    a Python function.

    C++ includes: itkPyImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkPyImageFilterIUS2IUS2_Pointer":
        """__New_orig__() -> itkPyImageFilterIUS2IUS2_Pointer"""
        return _itkPyImageFilterPython.itkPyImageFilterIUS2IUS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkPyImageFilterIUS2IUS2_Pointer":
        """Clone(itkPyImageFilterIUS2IUS2 self) -> itkPyImageFilterIUS2IUS2_Pointer"""
        return _itkPyImageFilterPython.itkPyImageFilterIUS2IUS2_Clone(self)


    def SetPyGenerateData(self, obj: 'PyObject *') -> "void":
        """SetPyGenerateData(itkPyImageFilterIUS2IUS2 self, PyObject * obj)"""
        return _itkPyImageFilterPython.itkPyImageFilterIUS2IUS2_SetPyGenerateData(self, obj)

    __swig_destroy__ = _itkPyImageFilterPython.delete_itkPyImageFilterIUS2IUS2

    def cast(obj: 'itkLightObject') -> "itkPyImageFilterIUS2IUS2 *":
        """cast(itkLightObject obj) -> itkPyImageFilterIUS2IUS2"""
        return _itkPyImageFilterPython.itkPyImageFilterIUS2IUS2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkPyImageFilterIUS2IUS2

        Create a new object of the class itkPyImageFilterIUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPyImageFilterIUS2IUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkPyImageFilterIUS2IUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkPyImageFilterIUS2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkPyImageFilterIUS2IUS2.Clone = new_instancemethod(_itkPyImageFilterPython.itkPyImageFilterIUS2IUS2_Clone, None, itkPyImageFilterIUS2IUS2)
itkPyImageFilterIUS2IUS2.SetPyGenerateData = new_instancemethod(_itkPyImageFilterPython.itkPyImageFilterIUS2IUS2_SetPyGenerateData, None, itkPyImageFilterIUS2IUS2)
itkPyImageFilterIUS2IUS2_swigregister = _itkPyImageFilterPython.itkPyImageFilterIUS2IUS2_swigregister
itkPyImageFilterIUS2IUS2_swigregister(itkPyImageFilterIUS2IUS2)

def itkPyImageFilterIUS2IUS2___New_orig__() -> "itkPyImageFilterIUS2IUS2_Pointer":
    """itkPyImageFilterIUS2IUS2___New_orig__() -> itkPyImageFilterIUS2IUS2_Pointer"""
    return _itkPyImageFilterPython.itkPyImageFilterIUS2IUS2___New_orig__()

def itkPyImageFilterIUS2IUS2_cast(obj: 'itkLightObject') -> "itkPyImageFilterIUS2IUS2 *":
    """itkPyImageFilterIUS2IUS2_cast(itkLightObject obj) -> itkPyImageFilterIUS2IUS2"""
    return _itkPyImageFilterPython.itkPyImageFilterIUS2IUS2_cast(obj)

class itkPyImageFilterIUS3IUS3(itkImageToImageFilterAPython.itkImageToImageFilterIUS3IUS3):
    """


    ImageToImageFilter subclass that calls a Python callable object, e.g.
    a Python function.

    C++ includes: itkPyImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkPyImageFilterIUS3IUS3_Pointer":
        """__New_orig__() -> itkPyImageFilterIUS3IUS3_Pointer"""
        return _itkPyImageFilterPython.itkPyImageFilterIUS3IUS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkPyImageFilterIUS3IUS3_Pointer":
        """Clone(itkPyImageFilterIUS3IUS3 self) -> itkPyImageFilterIUS3IUS3_Pointer"""
        return _itkPyImageFilterPython.itkPyImageFilterIUS3IUS3_Clone(self)


    def SetPyGenerateData(self, obj: 'PyObject *') -> "void":
        """SetPyGenerateData(itkPyImageFilterIUS3IUS3 self, PyObject * obj)"""
        return _itkPyImageFilterPython.itkPyImageFilterIUS3IUS3_SetPyGenerateData(self, obj)

    __swig_destroy__ = _itkPyImageFilterPython.delete_itkPyImageFilterIUS3IUS3

    def cast(obj: 'itkLightObject') -> "itkPyImageFilterIUS3IUS3 *":
        """cast(itkLightObject obj) -> itkPyImageFilterIUS3IUS3"""
        return _itkPyImageFilterPython.itkPyImageFilterIUS3IUS3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkPyImageFilterIUS3IUS3

        Create a new object of the class itkPyImageFilterIUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPyImageFilterIUS3IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkPyImageFilterIUS3IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkPyImageFilterIUS3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkPyImageFilterIUS3IUS3.Clone = new_instancemethod(_itkPyImageFilterPython.itkPyImageFilterIUS3IUS3_Clone, None, itkPyImageFilterIUS3IUS3)
itkPyImageFilterIUS3IUS3.SetPyGenerateData = new_instancemethod(_itkPyImageFilterPython.itkPyImageFilterIUS3IUS3_SetPyGenerateData, None, itkPyImageFilterIUS3IUS3)
itkPyImageFilterIUS3IUS3_swigregister = _itkPyImageFilterPython.itkPyImageFilterIUS3IUS3_swigregister
itkPyImageFilterIUS3IUS3_swigregister(itkPyImageFilterIUS3IUS3)

def itkPyImageFilterIUS3IUS3___New_orig__() -> "itkPyImageFilterIUS3IUS3_Pointer":
    """itkPyImageFilterIUS3IUS3___New_orig__() -> itkPyImageFilterIUS3IUS3_Pointer"""
    return _itkPyImageFilterPython.itkPyImageFilterIUS3IUS3___New_orig__()

def itkPyImageFilterIUS3IUS3_cast(obj: 'itkLightObject') -> "itkPyImageFilterIUS3IUS3 *":
    """itkPyImageFilterIUS3IUS3_cast(itkLightObject obj) -> itkPyImageFilterIUS3IUS3"""
    return _itkPyImageFilterPython.itkPyImageFilterIUS3IUS3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def py_image_filter(*args, **kwargs):
    """Procedural interface for PyImageFilter"""
    import itk
    instance = itk.PyImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def py_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.PyImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.PyImageFilter.values()[0]
    else:
        filter_object = itk.PyImageFilter

    py_image_filter.__doc__ = filter_object.__doc__
    py_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    py_image_filter.__doc__ += "Available Keyword Arguments:\n"
    py_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



