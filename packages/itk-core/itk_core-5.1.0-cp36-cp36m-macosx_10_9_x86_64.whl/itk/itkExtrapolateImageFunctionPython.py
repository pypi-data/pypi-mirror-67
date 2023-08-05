# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkExtrapolateImageFunctionPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkExtrapolateImageFunctionPython', [dirname(__file__)])
        except ImportError:
            import _itkExtrapolateImageFunctionPython
            return _itkExtrapolateImageFunctionPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkExtrapolateImageFunctionPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkExtrapolateImageFunctionPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkExtrapolateImageFunctionPython
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
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkPointPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkVectorPython
import itkContinuousIndexPython
import itkImageFunctionBasePython
import itkFunctionBasePython
import itkRGBAPixelPython
import itkArrayPython
import itkCovariantVectorPython
import itkRGBPixelPython
import itkImagePython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkImageRegionPython

def itkExtrapolateImageFunctionID3D_New():
  return itkExtrapolateImageFunctionID3D.New()


def itkExtrapolateImageFunctionIF3D_New():
  return itkExtrapolateImageFunctionIF3D.New()


def itkExtrapolateImageFunctionIUS3D_New():
  return itkExtrapolateImageFunctionIUS3D.New()


def itkExtrapolateImageFunctionIUC3D_New():
  return itkExtrapolateImageFunctionIUC3D.New()


def itkExtrapolateImageFunctionISS3D_New():
  return itkExtrapolateImageFunctionISS3D.New()


def itkExtrapolateImageFunctionID2D_New():
  return itkExtrapolateImageFunctionID2D.New()


def itkExtrapolateImageFunctionIF2D_New():
  return itkExtrapolateImageFunctionIF2D.New()


def itkExtrapolateImageFunctionIUS2D_New():
  return itkExtrapolateImageFunctionIUS2D.New()


def itkExtrapolateImageFunctionIUC2D_New():
  return itkExtrapolateImageFunctionIUC2D.New()


def itkExtrapolateImageFunctionISS2D_New():
  return itkExtrapolateImageFunctionISS2D.New()

class itkExtrapolateImageFunctionID2D(itkImageFunctionBasePython.itkImageFunctionID2DD):
    """


    Base class for all image extrapolaters.

    ExtrapolateImageFunction is the base for all ImageFunctions that
    extrapolates image intensity at a non-integer pixel position outside
    the image buffer. This class is templated over the input image type
    and the coordinate representation type (e.g. float or double ).

    WARNING:  This hierarchy of functions work only for images with scalar
    pixel types.

    C++ includes: itkExtrapolateImageFunction.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkExtrapolateImageFunctionPython.delete_itkExtrapolateImageFunctionID2D

    def cast(obj: 'itkLightObject') -> "itkExtrapolateImageFunctionID2D *":
        """cast(itkLightObject obj) -> itkExtrapolateImageFunctionID2D"""
        return _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionID2D_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkExtrapolateImageFunctionID2D

        Create a new object of the class itkExtrapolateImageFunctionID2D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExtrapolateImageFunctionID2D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkExtrapolateImageFunctionID2D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkExtrapolateImageFunctionID2D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkExtrapolateImageFunctionID2D_swigregister = _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionID2D_swigregister
itkExtrapolateImageFunctionID2D_swigregister(itkExtrapolateImageFunctionID2D)

def itkExtrapolateImageFunctionID2D_cast(obj: 'itkLightObject') -> "itkExtrapolateImageFunctionID2D *":
    """itkExtrapolateImageFunctionID2D_cast(itkLightObject obj) -> itkExtrapolateImageFunctionID2D"""
    return _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionID2D_cast(obj)

class itkExtrapolateImageFunctionID3D(itkImageFunctionBasePython.itkImageFunctionID3DD):
    """


    Base class for all image extrapolaters.

    ExtrapolateImageFunction is the base for all ImageFunctions that
    extrapolates image intensity at a non-integer pixel position outside
    the image buffer. This class is templated over the input image type
    and the coordinate representation type (e.g. float or double ).

    WARNING:  This hierarchy of functions work only for images with scalar
    pixel types.

    C++ includes: itkExtrapolateImageFunction.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkExtrapolateImageFunctionPython.delete_itkExtrapolateImageFunctionID3D

    def cast(obj: 'itkLightObject') -> "itkExtrapolateImageFunctionID3D *":
        """cast(itkLightObject obj) -> itkExtrapolateImageFunctionID3D"""
        return _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionID3D_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkExtrapolateImageFunctionID3D

        Create a new object of the class itkExtrapolateImageFunctionID3D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExtrapolateImageFunctionID3D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkExtrapolateImageFunctionID3D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkExtrapolateImageFunctionID3D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkExtrapolateImageFunctionID3D_swigregister = _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionID3D_swigregister
itkExtrapolateImageFunctionID3D_swigregister(itkExtrapolateImageFunctionID3D)

def itkExtrapolateImageFunctionID3D_cast(obj: 'itkLightObject') -> "itkExtrapolateImageFunctionID3D *":
    """itkExtrapolateImageFunctionID3D_cast(itkLightObject obj) -> itkExtrapolateImageFunctionID3D"""
    return _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionID3D_cast(obj)

class itkExtrapolateImageFunctionIF2D(itkImageFunctionBasePython.itkImageFunctionIF2DD):
    """


    Base class for all image extrapolaters.

    ExtrapolateImageFunction is the base for all ImageFunctions that
    extrapolates image intensity at a non-integer pixel position outside
    the image buffer. This class is templated over the input image type
    and the coordinate representation type (e.g. float or double ).

    WARNING:  This hierarchy of functions work only for images with scalar
    pixel types.

    C++ includes: itkExtrapolateImageFunction.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkExtrapolateImageFunctionPython.delete_itkExtrapolateImageFunctionIF2D

    def cast(obj: 'itkLightObject') -> "itkExtrapolateImageFunctionIF2D *":
        """cast(itkLightObject obj) -> itkExtrapolateImageFunctionIF2D"""
        return _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIF2D_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkExtrapolateImageFunctionIF2D

        Create a new object of the class itkExtrapolateImageFunctionIF2D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExtrapolateImageFunctionIF2D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkExtrapolateImageFunctionIF2D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkExtrapolateImageFunctionIF2D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkExtrapolateImageFunctionIF2D_swigregister = _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIF2D_swigregister
itkExtrapolateImageFunctionIF2D_swigregister(itkExtrapolateImageFunctionIF2D)

def itkExtrapolateImageFunctionIF2D_cast(obj: 'itkLightObject') -> "itkExtrapolateImageFunctionIF2D *":
    """itkExtrapolateImageFunctionIF2D_cast(itkLightObject obj) -> itkExtrapolateImageFunctionIF2D"""
    return _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIF2D_cast(obj)

class itkExtrapolateImageFunctionIF3D(itkImageFunctionBasePython.itkImageFunctionIF3DD):
    """


    Base class for all image extrapolaters.

    ExtrapolateImageFunction is the base for all ImageFunctions that
    extrapolates image intensity at a non-integer pixel position outside
    the image buffer. This class is templated over the input image type
    and the coordinate representation type (e.g. float or double ).

    WARNING:  This hierarchy of functions work only for images with scalar
    pixel types.

    C++ includes: itkExtrapolateImageFunction.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkExtrapolateImageFunctionPython.delete_itkExtrapolateImageFunctionIF3D

    def cast(obj: 'itkLightObject') -> "itkExtrapolateImageFunctionIF3D *":
        """cast(itkLightObject obj) -> itkExtrapolateImageFunctionIF3D"""
        return _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIF3D_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkExtrapolateImageFunctionIF3D

        Create a new object of the class itkExtrapolateImageFunctionIF3D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExtrapolateImageFunctionIF3D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkExtrapolateImageFunctionIF3D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkExtrapolateImageFunctionIF3D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkExtrapolateImageFunctionIF3D_swigregister = _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIF3D_swigregister
itkExtrapolateImageFunctionIF3D_swigregister(itkExtrapolateImageFunctionIF3D)

def itkExtrapolateImageFunctionIF3D_cast(obj: 'itkLightObject') -> "itkExtrapolateImageFunctionIF3D *":
    """itkExtrapolateImageFunctionIF3D_cast(itkLightObject obj) -> itkExtrapolateImageFunctionIF3D"""
    return _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIF3D_cast(obj)

class itkExtrapolateImageFunctionISS2D(itkImageFunctionBasePython.itkImageFunctionISS2DD):
    """


    Base class for all image extrapolaters.

    ExtrapolateImageFunction is the base for all ImageFunctions that
    extrapolates image intensity at a non-integer pixel position outside
    the image buffer. This class is templated over the input image type
    and the coordinate representation type (e.g. float or double ).

    WARNING:  This hierarchy of functions work only for images with scalar
    pixel types.

    C++ includes: itkExtrapolateImageFunction.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkExtrapolateImageFunctionPython.delete_itkExtrapolateImageFunctionISS2D

    def cast(obj: 'itkLightObject') -> "itkExtrapolateImageFunctionISS2D *":
        """cast(itkLightObject obj) -> itkExtrapolateImageFunctionISS2D"""
        return _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionISS2D_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkExtrapolateImageFunctionISS2D

        Create a new object of the class itkExtrapolateImageFunctionISS2D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExtrapolateImageFunctionISS2D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkExtrapolateImageFunctionISS2D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkExtrapolateImageFunctionISS2D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkExtrapolateImageFunctionISS2D_swigregister = _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionISS2D_swigregister
itkExtrapolateImageFunctionISS2D_swigregister(itkExtrapolateImageFunctionISS2D)

def itkExtrapolateImageFunctionISS2D_cast(obj: 'itkLightObject') -> "itkExtrapolateImageFunctionISS2D *":
    """itkExtrapolateImageFunctionISS2D_cast(itkLightObject obj) -> itkExtrapolateImageFunctionISS2D"""
    return _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionISS2D_cast(obj)

class itkExtrapolateImageFunctionISS3D(itkImageFunctionBasePython.itkImageFunctionISS3DD):
    """


    Base class for all image extrapolaters.

    ExtrapolateImageFunction is the base for all ImageFunctions that
    extrapolates image intensity at a non-integer pixel position outside
    the image buffer. This class is templated over the input image type
    and the coordinate representation type (e.g. float or double ).

    WARNING:  This hierarchy of functions work only for images with scalar
    pixel types.

    C++ includes: itkExtrapolateImageFunction.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkExtrapolateImageFunctionPython.delete_itkExtrapolateImageFunctionISS3D

    def cast(obj: 'itkLightObject') -> "itkExtrapolateImageFunctionISS3D *":
        """cast(itkLightObject obj) -> itkExtrapolateImageFunctionISS3D"""
        return _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionISS3D_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkExtrapolateImageFunctionISS3D

        Create a new object of the class itkExtrapolateImageFunctionISS3D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExtrapolateImageFunctionISS3D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkExtrapolateImageFunctionISS3D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkExtrapolateImageFunctionISS3D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkExtrapolateImageFunctionISS3D_swigregister = _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionISS3D_swigregister
itkExtrapolateImageFunctionISS3D_swigregister(itkExtrapolateImageFunctionISS3D)

def itkExtrapolateImageFunctionISS3D_cast(obj: 'itkLightObject') -> "itkExtrapolateImageFunctionISS3D *":
    """itkExtrapolateImageFunctionISS3D_cast(itkLightObject obj) -> itkExtrapolateImageFunctionISS3D"""
    return _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionISS3D_cast(obj)

class itkExtrapolateImageFunctionIUC2D(itkImageFunctionBasePython.itkImageFunctionIUC2DD):
    """


    Base class for all image extrapolaters.

    ExtrapolateImageFunction is the base for all ImageFunctions that
    extrapolates image intensity at a non-integer pixel position outside
    the image buffer. This class is templated over the input image type
    and the coordinate representation type (e.g. float or double ).

    WARNING:  This hierarchy of functions work only for images with scalar
    pixel types.

    C++ includes: itkExtrapolateImageFunction.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkExtrapolateImageFunctionPython.delete_itkExtrapolateImageFunctionIUC2D

    def cast(obj: 'itkLightObject') -> "itkExtrapolateImageFunctionIUC2D *":
        """cast(itkLightObject obj) -> itkExtrapolateImageFunctionIUC2D"""
        return _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIUC2D_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkExtrapolateImageFunctionIUC2D

        Create a new object of the class itkExtrapolateImageFunctionIUC2D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExtrapolateImageFunctionIUC2D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkExtrapolateImageFunctionIUC2D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkExtrapolateImageFunctionIUC2D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkExtrapolateImageFunctionIUC2D_swigregister = _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIUC2D_swigregister
itkExtrapolateImageFunctionIUC2D_swigregister(itkExtrapolateImageFunctionIUC2D)

def itkExtrapolateImageFunctionIUC2D_cast(obj: 'itkLightObject') -> "itkExtrapolateImageFunctionIUC2D *":
    """itkExtrapolateImageFunctionIUC2D_cast(itkLightObject obj) -> itkExtrapolateImageFunctionIUC2D"""
    return _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIUC2D_cast(obj)

class itkExtrapolateImageFunctionIUC3D(itkImageFunctionBasePython.itkImageFunctionIUC3DD):
    """


    Base class for all image extrapolaters.

    ExtrapolateImageFunction is the base for all ImageFunctions that
    extrapolates image intensity at a non-integer pixel position outside
    the image buffer. This class is templated over the input image type
    and the coordinate representation type (e.g. float or double ).

    WARNING:  This hierarchy of functions work only for images with scalar
    pixel types.

    C++ includes: itkExtrapolateImageFunction.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkExtrapolateImageFunctionPython.delete_itkExtrapolateImageFunctionIUC3D

    def cast(obj: 'itkLightObject') -> "itkExtrapolateImageFunctionIUC3D *":
        """cast(itkLightObject obj) -> itkExtrapolateImageFunctionIUC3D"""
        return _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIUC3D_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkExtrapolateImageFunctionIUC3D

        Create a new object of the class itkExtrapolateImageFunctionIUC3D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExtrapolateImageFunctionIUC3D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkExtrapolateImageFunctionIUC3D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkExtrapolateImageFunctionIUC3D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkExtrapolateImageFunctionIUC3D_swigregister = _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIUC3D_swigregister
itkExtrapolateImageFunctionIUC3D_swigregister(itkExtrapolateImageFunctionIUC3D)

def itkExtrapolateImageFunctionIUC3D_cast(obj: 'itkLightObject') -> "itkExtrapolateImageFunctionIUC3D *":
    """itkExtrapolateImageFunctionIUC3D_cast(itkLightObject obj) -> itkExtrapolateImageFunctionIUC3D"""
    return _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIUC3D_cast(obj)

class itkExtrapolateImageFunctionIUS2D(itkImageFunctionBasePython.itkImageFunctionIUS2DD):
    """


    Base class for all image extrapolaters.

    ExtrapolateImageFunction is the base for all ImageFunctions that
    extrapolates image intensity at a non-integer pixel position outside
    the image buffer. This class is templated over the input image type
    and the coordinate representation type (e.g. float or double ).

    WARNING:  This hierarchy of functions work only for images with scalar
    pixel types.

    C++ includes: itkExtrapolateImageFunction.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkExtrapolateImageFunctionPython.delete_itkExtrapolateImageFunctionIUS2D

    def cast(obj: 'itkLightObject') -> "itkExtrapolateImageFunctionIUS2D *":
        """cast(itkLightObject obj) -> itkExtrapolateImageFunctionIUS2D"""
        return _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIUS2D_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkExtrapolateImageFunctionIUS2D

        Create a new object of the class itkExtrapolateImageFunctionIUS2D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExtrapolateImageFunctionIUS2D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkExtrapolateImageFunctionIUS2D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkExtrapolateImageFunctionIUS2D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkExtrapolateImageFunctionIUS2D_swigregister = _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIUS2D_swigregister
itkExtrapolateImageFunctionIUS2D_swigregister(itkExtrapolateImageFunctionIUS2D)

def itkExtrapolateImageFunctionIUS2D_cast(obj: 'itkLightObject') -> "itkExtrapolateImageFunctionIUS2D *":
    """itkExtrapolateImageFunctionIUS2D_cast(itkLightObject obj) -> itkExtrapolateImageFunctionIUS2D"""
    return _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIUS2D_cast(obj)

class itkExtrapolateImageFunctionIUS3D(itkImageFunctionBasePython.itkImageFunctionIUS3DD):
    """


    Base class for all image extrapolaters.

    ExtrapolateImageFunction is the base for all ImageFunctions that
    extrapolates image intensity at a non-integer pixel position outside
    the image buffer. This class is templated over the input image type
    and the coordinate representation type (e.g. float or double ).

    WARNING:  This hierarchy of functions work only for images with scalar
    pixel types.

    C++ includes: itkExtrapolateImageFunction.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkExtrapolateImageFunctionPython.delete_itkExtrapolateImageFunctionIUS3D

    def cast(obj: 'itkLightObject') -> "itkExtrapolateImageFunctionIUS3D *":
        """cast(itkLightObject obj) -> itkExtrapolateImageFunctionIUS3D"""
        return _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIUS3D_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkExtrapolateImageFunctionIUS3D

        Create a new object of the class itkExtrapolateImageFunctionIUS3D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExtrapolateImageFunctionIUS3D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkExtrapolateImageFunctionIUS3D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkExtrapolateImageFunctionIUS3D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkExtrapolateImageFunctionIUS3D_swigregister = _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIUS3D_swigregister
itkExtrapolateImageFunctionIUS3D_swigregister(itkExtrapolateImageFunctionIUS3D)

def itkExtrapolateImageFunctionIUS3D_cast(obj: 'itkLightObject') -> "itkExtrapolateImageFunctionIUS3D *":
    """itkExtrapolateImageFunctionIUS3D_cast(itkLightObject obj) -> itkExtrapolateImageFunctionIUS3D"""
    return _itkExtrapolateImageFunctionPython.itkExtrapolateImageFunctionIUS3D_cast(obj)



