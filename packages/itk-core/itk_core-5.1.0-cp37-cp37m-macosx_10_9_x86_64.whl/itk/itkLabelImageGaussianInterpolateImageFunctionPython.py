# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkLabelImageGaussianInterpolateImageFunctionPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkLabelImageGaussianInterpolateImageFunctionPython', [dirname(__file__)])
        except ImportError:
            import _itkLabelImageGaussianInterpolateImageFunctionPython
            return _itkLabelImageGaussianInterpolateImageFunctionPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkLabelImageGaussianInterpolateImageFunctionPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkLabelImageGaussianInterpolateImageFunctionPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkLabelImageGaussianInterpolateImageFunctionPython
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


import itkContinuousIndexPython
import itkIndexPython
import itkSizePython
import pyBasePython
import itkOffsetPython
import itkPointPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import vnl_vector_refPython
import itkVectorPython
import itkFixedArrayPython
import ITKCommonBasePython
import itkGaussianInterpolateImageFunctionPython
import itkImageRegionPython
import itkImagePython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkInterpolateImageFunctionPython
import itkImageFunctionBasePython
import itkFunctionBasePython
import itkArrayPython

def itkLabelImageGaussianInterpolateImageFunctionIUS3D_New():
  return itkLabelImageGaussianInterpolateImageFunctionIUS3D.New()


def itkLabelImageGaussianInterpolateImageFunctionIUC3D_New():
  return itkLabelImageGaussianInterpolateImageFunctionIUC3D.New()


def itkLabelImageGaussianInterpolateImageFunctionISS3D_New():
  return itkLabelImageGaussianInterpolateImageFunctionISS3D.New()


def itkLabelImageGaussianInterpolateImageFunctionIUS2D_New():
  return itkLabelImageGaussianInterpolateImageFunctionIUS2D.New()


def itkLabelImageGaussianInterpolateImageFunctionIUC2D_New():
  return itkLabelImageGaussianInterpolateImageFunctionIUC2D.New()


def itkLabelImageGaussianInterpolateImageFunctionISS2D_New():
  return itkLabelImageGaussianInterpolateImageFunctionISS2D.New()

class itkLabelImageGaussianInterpolateImageFunctionISS2D(itkGaussianInterpolateImageFunctionPython.itkGaussianInterpolateImageFunctionISS2D):
    """


    Interpolation function for multi-label images that implicitly smooths
    each unique value in the image corresponding to each label set element
    and returns the corresponding label set element with the largest
    weight.

    This filter is an alternative to nearest neighbor interpolation for
    multi-label images. Given a multi-label image I with label set L, this
    function returns a label at the non-voxel position I(x), based on the
    following rule

    \\[ I(x) = \\arg\\max_{l \\in L} (G_\\sigma * I_l)(x) \\]

    Where $ I_l $ is the l-th binary component of the multilabel image. In
    other words, each label in the multi-label image is convolved with a
    Gaussian, and the label for which the response is largest is returned.
    For sigma=0, this is just nearest neighbor interpolation.

    This class defines an N-dimensional Gaussian interpolation function
    for label using the vnl error function. The two parameters associated
    with this function are:  Sigma - a scalar array of size ImageDimension
    determining the width of the interpolation function.

    Alpha - a scalar specifying the cutoff distance over which the
    function is calculated.

    The input image can be of any type, but the number of unique intensity
    values in the image will determine the amount of memory needed to
    complete each interpolation.

    Paul Yushkevich

    Nick Tustison  \\sphinx
    \\sphinxexample{Core/ImageFunction/ResampleSegmentedImage,Resample
    Segmented Image} \\endsphinx

    C++ includes: itkLabelImageGaussianInterpolateImageFunction.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLabelImageGaussianInterpolateImageFunctionISS2D_Pointer":
        """__New_orig__() -> itkLabelImageGaussianInterpolateImageFunctionISS2D_Pointer"""
        return _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionISS2D___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLabelImageGaussianInterpolateImageFunctionISS2D_Pointer":
        """Clone(itkLabelImageGaussianInterpolateImageFunctionISS2D self) -> itkLabelImageGaussianInterpolateImageFunctionISS2D_Pointer"""
        return _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionISS2D_Clone(self)

    __swig_destroy__ = _itkLabelImageGaussianInterpolateImageFunctionPython.delete_itkLabelImageGaussianInterpolateImageFunctionISS2D

    def cast(obj: 'itkLightObject') -> "itkLabelImageGaussianInterpolateImageFunctionISS2D *":
        """cast(itkLightObject obj) -> itkLabelImageGaussianInterpolateImageFunctionISS2D"""
        return _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionISS2D_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLabelImageGaussianInterpolateImageFunctionISS2D

        Create a new object of the class itkLabelImageGaussianInterpolateImageFunctionISS2D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelImageGaussianInterpolateImageFunctionISS2D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelImageGaussianInterpolateImageFunctionISS2D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelImageGaussianInterpolateImageFunctionISS2D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLabelImageGaussianInterpolateImageFunctionISS2D.Clone = new_instancemethod(_itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionISS2D_Clone, None, itkLabelImageGaussianInterpolateImageFunctionISS2D)
itkLabelImageGaussianInterpolateImageFunctionISS2D_swigregister = _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionISS2D_swigregister
itkLabelImageGaussianInterpolateImageFunctionISS2D_swigregister(itkLabelImageGaussianInterpolateImageFunctionISS2D)

def itkLabelImageGaussianInterpolateImageFunctionISS2D___New_orig__() -> "itkLabelImageGaussianInterpolateImageFunctionISS2D_Pointer":
    """itkLabelImageGaussianInterpolateImageFunctionISS2D___New_orig__() -> itkLabelImageGaussianInterpolateImageFunctionISS2D_Pointer"""
    return _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionISS2D___New_orig__()

def itkLabelImageGaussianInterpolateImageFunctionISS2D_cast(obj: 'itkLightObject') -> "itkLabelImageGaussianInterpolateImageFunctionISS2D *":
    """itkLabelImageGaussianInterpolateImageFunctionISS2D_cast(itkLightObject obj) -> itkLabelImageGaussianInterpolateImageFunctionISS2D"""
    return _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionISS2D_cast(obj)

class itkLabelImageGaussianInterpolateImageFunctionISS3D(itkGaussianInterpolateImageFunctionPython.itkGaussianInterpolateImageFunctionISS3D):
    """


    Interpolation function for multi-label images that implicitly smooths
    each unique value in the image corresponding to each label set element
    and returns the corresponding label set element with the largest
    weight.

    This filter is an alternative to nearest neighbor interpolation for
    multi-label images. Given a multi-label image I with label set L, this
    function returns a label at the non-voxel position I(x), based on the
    following rule

    \\[ I(x) = \\arg\\max_{l \\in L} (G_\\sigma * I_l)(x) \\]

    Where $ I_l $ is the l-th binary component of the multilabel image. In
    other words, each label in the multi-label image is convolved with a
    Gaussian, and the label for which the response is largest is returned.
    For sigma=0, this is just nearest neighbor interpolation.

    This class defines an N-dimensional Gaussian interpolation function
    for label using the vnl error function. The two parameters associated
    with this function are:  Sigma - a scalar array of size ImageDimension
    determining the width of the interpolation function.

    Alpha - a scalar specifying the cutoff distance over which the
    function is calculated.

    The input image can be of any type, but the number of unique intensity
    values in the image will determine the amount of memory needed to
    complete each interpolation.

    Paul Yushkevich

    Nick Tustison  \\sphinx
    \\sphinxexample{Core/ImageFunction/ResampleSegmentedImage,Resample
    Segmented Image} \\endsphinx

    C++ includes: itkLabelImageGaussianInterpolateImageFunction.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLabelImageGaussianInterpolateImageFunctionISS3D_Pointer":
        """__New_orig__() -> itkLabelImageGaussianInterpolateImageFunctionISS3D_Pointer"""
        return _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionISS3D___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLabelImageGaussianInterpolateImageFunctionISS3D_Pointer":
        """Clone(itkLabelImageGaussianInterpolateImageFunctionISS3D self) -> itkLabelImageGaussianInterpolateImageFunctionISS3D_Pointer"""
        return _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionISS3D_Clone(self)

    __swig_destroy__ = _itkLabelImageGaussianInterpolateImageFunctionPython.delete_itkLabelImageGaussianInterpolateImageFunctionISS3D

    def cast(obj: 'itkLightObject') -> "itkLabelImageGaussianInterpolateImageFunctionISS3D *":
        """cast(itkLightObject obj) -> itkLabelImageGaussianInterpolateImageFunctionISS3D"""
        return _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionISS3D_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLabelImageGaussianInterpolateImageFunctionISS3D

        Create a new object of the class itkLabelImageGaussianInterpolateImageFunctionISS3D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelImageGaussianInterpolateImageFunctionISS3D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelImageGaussianInterpolateImageFunctionISS3D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelImageGaussianInterpolateImageFunctionISS3D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLabelImageGaussianInterpolateImageFunctionISS3D.Clone = new_instancemethod(_itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionISS3D_Clone, None, itkLabelImageGaussianInterpolateImageFunctionISS3D)
itkLabelImageGaussianInterpolateImageFunctionISS3D_swigregister = _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionISS3D_swigregister
itkLabelImageGaussianInterpolateImageFunctionISS3D_swigregister(itkLabelImageGaussianInterpolateImageFunctionISS3D)

def itkLabelImageGaussianInterpolateImageFunctionISS3D___New_orig__() -> "itkLabelImageGaussianInterpolateImageFunctionISS3D_Pointer":
    """itkLabelImageGaussianInterpolateImageFunctionISS3D___New_orig__() -> itkLabelImageGaussianInterpolateImageFunctionISS3D_Pointer"""
    return _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionISS3D___New_orig__()

def itkLabelImageGaussianInterpolateImageFunctionISS3D_cast(obj: 'itkLightObject') -> "itkLabelImageGaussianInterpolateImageFunctionISS3D *":
    """itkLabelImageGaussianInterpolateImageFunctionISS3D_cast(itkLightObject obj) -> itkLabelImageGaussianInterpolateImageFunctionISS3D"""
    return _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionISS3D_cast(obj)

class itkLabelImageGaussianInterpolateImageFunctionIUC2D(itkGaussianInterpolateImageFunctionPython.itkGaussianInterpolateImageFunctionIUC2D):
    """


    Interpolation function for multi-label images that implicitly smooths
    each unique value in the image corresponding to each label set element
    and returns the corresponding label set element with the largest
    weight.

    This filter is an alternative to nearest neighbor interpolation for
    multi-label images. Given a multi-label image I with label set L, this
    function returns a label at the non-voxel position I(x), based on the
    following rule

    \\[ I(x) = \\arg\\max_{l \\in L} (G_\\sigma * I_l)(x) \\]

    Where $ I_l $ is the l-th binary component of the multilabel image. In
    other words, each label in the multi-label image is convolved with a
    Gaussian, and the label for which the response is largest is returned.
    For sigma=0, this is just nearest neighbor interpolation.

    This class defines an N-dimensional Gaussian interpolation function
    for label using the vnl error function. The two parameters associated
    with this function are:  Sigma - a scalar array of size ImageDimension
    determining the width of the interpolation function.

    Alpha - a scalar specifying the cutoff distance over which the
    function is calculated.

    The input image can be of any type, but the number of unique intensity
    values in the image will determine the amount of memory needed to
    complete each interpolation.

    Paul Yushkevich

    Nick Tustison  \\sphinx
    \\sphinxexample{Core/ImageFunction/ResampleSegmentedImage,Resample
    Segmented Image} \\endsphinx

    C++ includes: itkLabelImageGaussianInterpolateImageFunction.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLabelImageGaussianInterpolateImageFunctionIUC2D_Pointer":
        """__New_orig__() -> itkLabelImageGaussianInterpolateImageFunctionIUC2D_Pointer"""
        return _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUC2D___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLabelImageGaussianInterpolateImageFunctionIUC2D_Pointer":
        """Clone(itkLabelImageGaussianInterpolateImageFunctionIUC2D self) -> itkLabelImageGaussianInterpolateImageFunctionIUC2D_Pointer"""
        return _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUC2D_Clone(self)

    __swig_destroy__ = _itkLabelImageGaussianInterpolateImageFunctionPython.delete_itkLabelImageGaussianInterpolateImageFunctionIUC2D

    def cast(obj: 'itkLightObject') -> "itkLabelImageGaussianInterpolateImageFunctionIUC2D *":
        """cast(itkLightObject obj) -> itkLabelImageGaussianInterpolateImageFunctionIUC2D"""
        return _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUC2D_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLabelImageGaussianInterpolateImageFunctionIUC2D

        Create a new object of the class itkLabelImageGaussianInterpolateImageFunctionIUC2D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelImageGaussianInterpolateImageFunctionIUC2D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelImageGaussianInterpolateImageFunctionIUC2D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelImageGaussianInterpolateImageFunctionIUC2D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLabelImageGaussianInterpolateImageFunctionIUC2D.Clone = new_instancemethod(_itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUC2D_Clone, None, itkLabelImageGaussianInterpolateImageFunctionIUC2D)
itkLabelImageGaussianInterpolateImageFunctionIUC2D_swigregister = _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUC2D_swigregister
itkLabelImageGaussianInterpolateImageFunctionIUC2D_swigregister(itkLabelImageGaussianInterpolateImageFunctionIUC2D)

def itkLabelImageGaussianInterpolateImageFunctionIUC2D___New_orig__() -> "itkLabelImageGaussianInterpolateImageFunctionIUC2D_Pointer":
    """itkLabelImageGaussianInterpolateImageFunctionIUC2D___New_orig__() -> itkLabelImageGaussianInterpolateImageFunctionIUC2D_Pointer"""
    return _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUC2D___New_orig__()

def itkLabelImageGaussianInterpolateImageFunctionIUC2D_cast(obj: 'itkLightObject') -> "itkLabelImageGaussianInterpolateImageFunctionIUC2D *":
    """itkLabelImageGaussianInterpolateImageFunctionIUC2D_cast(itkLightObject obj) -> itkLabelImageGaussianInterpolateImageFunctionIUC2D"""
    return _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUC2D_cast(obj)

class itkLabelImageGaussianInterpolateImageFunctionIUC3D(itkGaussianInterpolateImageFunctionPython.itkGaussianInterpolateImageFunctionIUC3D):
    """


    Interpolation function for multi-label images that implicitly smooths
    each unique value in the image corresponding to each label set element
    and returns the corresponding label set element with the largest
    weight.

    This filter is an alternative to nearest neighbor interpolation for
    multi-label images. Given a multi-label image I with label set L, this
    function returns a label at the non-voxel position I(x), based on the
    following rule

    \\[ I(x) = \\arg\\max_{l \\in L} (G_\\sigma * I_l)(x) \\]

    Where $ I_l $ is the l-th binary component of the multilabel image. In
    other words, each label in the multi-label image is convolved with a
    Gaussian, and the label for which the response is largest is returned.
    For sigma=0, this is just nearest neighbor interpolation.

    This class defines an N-dimensional Gaussian interpolation function
    for label using the vnl error function. The two parameters associated
    with this function are:  Sigma - a scalar array of size ImageDimension
    determining the width of the interpolation function.

    Alpha - a scalar specifying the cutoff distance over which the
    function is calculated.

    The input image can be of any type, but the number of unique intensity
    values in the image will determine the amount of memory needed to
    complete each interpolation.

    Paul Yushkevich

    Nick Tustison  \\sphinx
    \\sphinxexample{Core/ImageFunction/ResampleSegmentedImage,Resample
    Segmented Image} \\endsphinx

    C++ includes: itkLabelImageGaussianInterpolateImageFunction.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLabelImageGaussianInterpolateImageFunctionIUC3D_Pointer":
        """__New_orig__() -> itkLabelImageGaussianInterpolateImageFunctionIUC3D_Pointer"""
        return _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUC3D___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLabelImageGaussianInterpolateImageFunctionIUC3D_Pointer":
        """Clone(itkLabelImageGaussianInterpolateImageFunctionIUC3D self) -> itkLabelImageGaussianInterpolateImageFunctionIUC3D_Pointer"""
        return _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUC3D_Clone(self)

    __swig_destroy__ = _itkLabelImageGaussianInterpolateImageFunctionPython.delete_itkLabelImageGaussianInterpolateImageFunctionIUC3D

    def cast(obj: 'itkLightObject') -> "itkLabelImageGaussianInterpolateImageFunctionIUC3D *":
        """cast(itkLightObject obj) -> itkLabelImageGaussianInterpolateImageFunctionIUC3D"""
        return _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUC3D_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLabelImageGaussianInterpolateImageFunctionIUC3D

        Create a new object of the class itkLabelImageGaussianInterpolateImageFunctionIUC3D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelImageGaussianInterpolateImageFunctionIUC3D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelImageGaussianInterpolateImageFunctionIUC3D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelImageGaussianInterpolateImageFunctionIUC3D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLabelImageGaussianInterpolateImageFunctionIUC3D.Clone = new_instancemethod(_itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUC3D_Clone, None, itkLabelImageGaussianInterpolateImageFunctionIUC3D)
itkLabelImageGaussianInterpolateImageFunctionIUC3D_swigregister = _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUC3D_swigregister
itkLabelImageGaussianInterpolateImageFunctionIUC3D_swigregister(itkLabelImageGaussianInterpolateImageFunctionIUC3D)

def itkLabelImageGaussianInterpolateImageFunctionIUC3D___New_orig__() -> "itkLabelImageGaussianInterpolateImageFunctionIUC3D_Pointer":
    """itkLabelImageGaussianInterpolateImageFunctionIUC3D___New_orig__() -> itkLabelImageGaussianInterpolateImageFunctionIUC3D_Pointer"""
    return _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUC3D___New_orig__()

def itkLabelImageGaussianInterpolateImageFunctionIUC3D_cast(obj: 'itkLightObject') -> "itkLabelImageGaussianInterpolateImageFunctionIUC3D *":
    """itkLabelImageGaussianInterpolateImageFunctionIUC3D_cast(itkLightObject obj) -> itkLabelImageGaussianInterpolateImageFunctionIUC3D"""
    return _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUC3D_cast(obj)

class itkLabelImageGaussianInterpolateImageFunctionIUS2D(itkGaussianInterpolateImageFunctionPython.itkGaussianInterpolateImageFunctionIUS2D):
    """


    Interpolation function for multi-label images that implicitly smooths
    each unique value in the image corresponding to each label set element
    and returns the corresponding label set element with the largest
    weight.

    This filter is an alternative to nearest neighbor interpolation for
    multi-label images. Given a multi-label image I with label set L, this
    function returns a label at the non-voxel position I(x), based on the
    following rule

    \\[ I(x) = \\arg\\max_{l \\in L} (G_\\sigma * I_l)(x) \\]

    Where $ I_l $ is the l-th binary component of the multilabel image. In
    other words, each label in the multi-label image is convolved with a
    Gaussian, and the label for which the response is largest is returned.
    For sigma=0, this is just nearest neighbor interpolation.

    This class defines an N-dimensional Gaussian interpolation function
    for label using the vnl error function. The two parameters associated
    with this function are:  Sigma - a scalar array of size ImageDimension
    determining the width of the interpolation function.

    Alpha - a scalar specifying the cutoff distance over which the
    function is calculated.

    The input image can be of any type, but the number of unique intensity
    values in the image will determine the amount of memory needed to
    complete each interpolation.

    Paul Yushkevich

    Nick Tustison  \\sphinx
    \\sphinxexample{Core/ImageFunction/ResampleSegmentedImage,Resample
    Segmented Image} \\endsphinx

    C++ includes: itkLabelImageGaussianInterpolateImageFunction.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLabelImageGaussianInterpolateImageFunctionIUS2D_Pointer":
        """__New_orig__() -> itkLabelImageGaussianInterpolateImageFunctionIUS2D_Pointer"""
        return _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUS2D___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLabelImageGaussianInterpolateImageFunctionIUS2D_Pointer":
        """Clone(itkLabelImageGaussianInterpolateImageFunctionIUS2D self) -> itkLabelImageGaussianInterpolateImageFunctionIUS2D_Pointer"""
        return _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUS2D_Clone(self)

    __swig_destroy__ = _itkLabelImageGaussianInterpolateImageFunctionPython.delete_itkLabelImageGaussianInterpolateImageFunctionIUS2D

    def cast(obj: 'itkLightObject') -> "itkLabelImageGaussianInterpolateImageFunctionIUS2D *":
        """cast(itkLightObject obj) -> itkLabelImageGaussianInterpolateImageFunctionIUS2D"""
        return _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUS2D_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLabelImageGaussianInterpolateImageFunctionIUS2D

        Create a new object of the class itkLabelImageGaussianInterpolateImageFunctionIUS2D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelImageGaussianInterpolateImageFunctionIUS2D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelImageGaussianInterpolateImageFunctionIUS2D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelImageGaussianInterpolateImageFunctionIUS2D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLabelImageGaussianInterpolateImageFunctionIUS2D.Clone = new_instancemethod(_itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUS2D_Clone, None, itkLabelImageGaussianInterpolateImageFunctionIUS2D)
itkLabelImageGaussianInterpolateImageFunctionIUS2D_swigregister = _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUS2D_swigregister
itkLabelImageGaussianInterpolateImageFunctionIUS2D_swigregister(itkLabelImageGaussianInterpolateImageFunctionIUS2D)

def itkLabelImageGaussianInterpolateImageFunctionIUS2D___New_orig__() -> "itkLabelImageGaussianInterpolateImageFunctionIUS2D_Pointer":
    """itkLabelImageGaussianInterpolateImageFunctionIUS2D___New_orig__() -> itkLabelImageGaussianInterpolateImageFunctionIUS2D_Pointer"""
    return _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUS2D___New_orig__()

def itkLabelImageGaussianInterpolateImageFunctionIUS2D_cast(obj: 'itkLightObject') -> "itkLabelImageGaussianInterpolateImageFunctionIUS2D *":
    """itkLabelImageGaussianInterpolateImageFunctionIUS2D_cast(itkLightObject obj) -> itkLabelImageGaussianInterpolateImageFunctionIUS2D"""
    return _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUS2D_cast(obj)

class itkLabelImageGaussianInterpolateImageFunctionIUS3D(itkGaussianInterpolateImageFunctionPython.itkGaussianInterpolateImageFunctionIUS3D):
    """


    Interpolation function for multi-label images that implicitly smooths
    each unique value in the image corresponding to each label set element
    and returns the corresponding label set element with the largest
    weight.

    This filter is an alternative to nearest neighbor interpolation for
    multi-label images. Given a multi-label image I with label set L, this
    function returns a label at the non-voxel position I(x), based on the
    following rule

    \\[ I(x) = \\arg\\max_{l \\in L} (G_\\sigma * I_l)(x) \\]

    Where $ I_l $ is the l-th binary component of the multilabel image. In
    other words, each label in the multi-label image is convolved with a
    Gaussian, and the label for which the response is largest is returned.
    For sigma=0, this is just nearest neighbor interpolation.

    This class defines an N-dimensional Gaussian interpolation function
    for label using the vnl error function. The two parameters associated
    with this function are:  Sigma - a scalar array of size ImageDimension
    determining the width of the interpolation function.

    Alpha - a scalar specifying the cutoff distance over which the
    function is calculated.

    The input image can be of any type, but the number of unique intensity
    values in the image will determine the amount of memory needed to
    complete each interpolation.

    Paul Yushkevich

    Nick Tustison  \\sphinx
    \\sphinxexample{Core/ImageFunction/ResampleSegmentedImage,Resample
    Segmented Image} \\endsphinx

    C++ includes: itkLabelImageGaussianInterpolateImageFunction.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLabelImageGaussianInterpolateImageFunctionIUS3D_Pointer":
        """__New_orig__() -> itkLabelImageGaussianInterpolateImageFunctionIUS3D_Pointer"""
        return _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUS3D___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLabelImageGaussianInterpolateImageFunctionIUS3D_Pointer":
        """Clone(itkLabelImageGaussianInterpolateImageFunctionIUS3D self) -> itkLabelImageGaussianInterpolateImageFunctionIUS3D_Pointer"""
        return _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUS3D_Clone(self)

    __swig_destroy__ = _itkLabelImageGaussianInterpolateImageFunctionPython.delete_itkLabelImageGaussianInterpolateImageFunctionIUS3D

    def cast(obj: 'itkLightObject') -> "itkLabelImageGaussianInterpolateImageFunctionIUS3D *":
        """cast(itkLightObject obj) -> itkLabelImageGaussianInterpolateImageFunctionIUS3D"""
        return _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUS3D_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLabelImageGaussianInterpolateImageFunctionIUS3D

        Create a new object of the class itkLabelImageGaussianInterpolateImageFunctionIUS3D and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLabelImageGaussianInterpolateImageFunctionIUS3D.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLabelImageGaussianInterpolateImageFunctionIUS3D.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLabelImageGaussianInterpolateImageFunctionIUS3D.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLabelImageGaussianInterpolateImageFunctionIUS3D.Clone = new_instancemethod(_itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUS3D_Clone, None, itkLabelImageGaussianInterpolateImageFunctionIUS3D)
itkLabelImageGaussianInterpolateImageFunctionIUS3D_swigregister = _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUS3D_swigregister
itkLabelImageGaussianInterpolateImageFunctionIUS3D_swigregister(itkLabelImageGaussianInterpolateImageFunctionIUS3D)

def itkLabelImageGaussianInterpolateImageFunctionIUS3D___New_orig__() -> "itkLabelImageGaussianInterpolateImageFunctionIUS3D_Pointer":
    """itkLabelImageGaussianInterpolateImageFunctionIUS3D___New_orig__() -> itkLabelImageGaussianInterpolateImageFunctionIUS3D_Pointer"""
    return _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUS3D___New_orig__()

def itkLabelImageGaussianInterpolateImageFunctionIUS3D_cast(obj: 'itkLightObject') -> "itkLabelImageGaussianInterpolateImageFunctionIUS3D *":
    """itkLabelImageGaussianInterpolateImageFunctionIUS3D_cast(itkLightObject obj) -> itkLabelImageGaussianInterpolateImageFunctionIUS3D"""
    return _itkLabelImageGaussianInterpolateImageFunctionPython.itkLabelImageGaussianInterpolateImageFunctionIUS3D_cast(obj)



