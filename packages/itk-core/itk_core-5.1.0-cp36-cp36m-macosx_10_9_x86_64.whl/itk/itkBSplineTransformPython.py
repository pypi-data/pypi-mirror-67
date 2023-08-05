# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkBSplineTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkBSplineTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkBSplineTransformPython
            return _itkBSplineTransformPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkBSplineTransformPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkBSplineTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkBSplineTransformPython
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
import itkContinuousIndexPython
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
import itkOptimizerParametersPython
import itkArrayPython
import itkMatrixPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import itkArray2DPython
import itkBSplineBaseTransformPython
import itkBSplineInterpolationWeightFunctionPython
import itkFunctionBasePython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkImagePython
import itkSymmetricSecondRankTensorPython
import itkImageRegionPython
import itkTransformBasePython
import itkVariableLengthVectorPython
import itkDiffusionTensor3DPython

def itkBSplineTransformD33_New():
  return itkBSplineTransformD33.New()


def itkBSplineTransformD23_New():
  return itkBSplineTransformD23.New()

class itkBSplineTransformD23(itkBSplineBaseTransformPython.itkBSplineBaseTransformD23):
    """


    Deformable transform using a BSpline representation.

    This class encapsulates a deformable transform of points from one
    N-dimensional space to another N-dimensional space. The deformation
    field is modelled using B-splines. A deformation is defined on a
    sparse regular grid of control points $ \\vec{\\lambda}_j $ and is
    varied by defining a deformation $ \\vec{g}(\\vec{\\lambda}_j) $
    of each control point. The deformation $ D(\\vec{x}) $ at any point
    $ \\vec{x} $ is obtained by using a B-spline interpolation kernel.

    The deformation field grid is defined by a user specified transform
    domain (origin, physical dimensions, direction) and B-spline mesh size
    where the mesh size is the number of polynomial patches comprising the
    finite domain of support. The relationship between the mesh size (
    number of polynomial pieces) and the number of control points in any
    given dimension is

    mesh size = number of control points - spline order

    Each grid/control point has associated with it N deformation
    coefficients $ \\vec{\\delta}_j $, representing the N directional
    components of the deformation. Deformation outside the grid plus
    support region for the BSpline interpolation is assumed to be zero.

    The parameters for this transform is N x N-D grid of spline
    coefficients. The user specifies the parameters as one flat array:
    each N-D grid is represented by an array in the same way an N-D image
    is represented in the buffer; the N arrays are then concatenated
    together to form a single array.

    The following illustrates the typical usage of this class:

    An alternative way to set the B-spline coefficients is via array of
    images. The fixed parameters of the transform are taken directly from
    the first image. It is assumed that the subsequent images are the same
    buffered region. The following illustrates the API:

    WARNING:  Use either the SetParameters() or SetCoefficientImages()
    API. Mixing the two modes may results in unexpected results.  The
    class is templated coordinate representation type (float or double),
    the space dimension and the spline order.

    C++ includes: itkBSplineTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBSplineTransformD23_Pointer":
        """__New_orig__() -> itkBSplineTransformD23_Pointer"""
        return _itkBSplineTransformPython.itkBSplineTransformD23___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBSplineTransformD23_Pointer":
        """Clone(itkBSplineTransformD23 self) -> itkBSplineTransformD23_Pointer"""
        return _itkBSplineTransformPython.itkBSplineTransformD23_Clone(self)


    def SetTransformDomainOrigin(self, arg0: 'itkPointD2') -> "void":
        """
        SetTransformDomainOrigin(itkBSplineTransformD23 self, itkPointD2 arg0)

        Function
        to specify the transform domain origin. 
        """
        return _itkBSplineTransformPython.itkBSplineTransformD23_SetTransformDomainOrigin(self, arg0)


    def GetTransformDomainOrigin(self) -> "itkPointD2":
        """
        GetTransformDomainOrigin(itkBSplineTransformD23 self) -> itkPointD2

        Function
        to retrieve the transform domain origin. 
        """
        return _itkBSplineTransformPython.itkBSplineTransformD23_GetTransformDomainOrigin(self)


    def SetTransformDomainPhysicalDimensions(self, arg0: 'itkVectorD2') -> "void":
        """
        SetTransformDomainPhysicalDimensions(itkBSplineTransformD23 self, itkVectorD2 arg0)

        Function to specify the transform domain physical dimensions. 
        """
        return _itkBSplineTransformPython.itkBSplineTransformD23_SetTransformDomainPhysicalDimensions(self, arg0)


    def GetTransformDomainPhysicalDimensions(self) -> "itkVectorD2":
        """
        GetTransformDomainPhysicalDimensions(itkBSplineTransformD23 self) -> itkVectorD2

        Function to retrieve the transform domain physical dimensions. 
        """
        return _itkBSplineTransformPython.itkBSplineTransformD23_GetTransformDomainPhysicalDimensions(self)


    def SetTransformDomainDirection(self, arg0: 'itkMatrixD22') -> "void":
        """
        SetTransformDomainDirection(itkBSplineTransformD23 self, itkMatrixD22 arg0)

        Function to specify the transform domain direction. 
        """
        return _itkBSplineTransformPython.itkBSplineTransformD23_SetTransformDomainDirection(self, arg0)


    def GetTransformDomainDirection(self) -> "itkMatrixD22":
        """
        GetTransformDomainDirection(itkBSplineTransformD23 self) -> itkMatrixD22

        Function to retrieve the transform domain direction. 
        """
        return _itkBSplineTransformPython.itkBSplineTransformD23_GetTransformDomainDirection(self)


    def SetTransformDomainMeshSize(self, arg0: 'itkSize2') -> "void":
        """
        SetTransformDomainMeshSize(itkBSplineTransformD23 self, itkSize2 arg0)

        Function
        to specify the transform domain mesh size. 
        """
        return _itkBSplineTransformPython.itkBSplineTransformD23_SetTransformDomainMeshSize(self, arg0)


    def GetTransformDomainMeshSize(self) -> "itkSize2":
        """
        GetTransformDomainMeshSize(itkBSplineTransformD23 self) -> itkSize2

        Function
        to retrieve the transform domain mesh size. 
        """
        return _itkBSplineTransformPython.itkBSplineTransformD23_GetTransformDomainMeshSize(self)

    __swig_destroy__ = _itkBSplineTransformPython.delete_itkBSplineTransformD23

    def cast(obj: 'itkLightObject') -> "itkBSplineTransformD23 *":
        """cast(itkLightObject obj) -> itkBSplineTransformD23"""
        return _itkBSplineTransformPython.itkBSplineTransformD23_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkBSplineTransformD23

        Create a new object of the class itkBSplineTransformD23 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineTransformD23.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineTransformD23.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineTransformD23.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBSplineTransformD23.Clone = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD23_Clone, None, itkBSplineTransformD23)
itkBSplineTransformD23.SetTransformDomainOrigin = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD23_SetTransformDomainOrigin, None, itkBSplineTransformD23)
itkBSplineTransformD23.GetTransformDomainOrigin = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD23_GetTransformDomainOrigin, None, itkBSplineTransformD23)
itkBSplineTransformD23.SetTransformDomainPhysicalDimensions = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD23_SetTransformDomainPhysicalDimensions, None, itkBSplineTransformD23)
itkBSplineTransformD23.GetTransformDomainPhysicalDimensions = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD23_GetTransformDomainPhysicalDimensions, None, itkBSplineTransformD23)
itkBSplineTransformD23.SetTransformDomainDirection = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD23_SetTransformDomainDirection, None, itkBSplineTransformD23)
itkBSplineTransformD23.GetTransformDomainDirection = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD23_GetTransformDomainDirection, None, itkBSplineTransformD23)
itkBSplineTransformD23.SetTransformDomainMeshSize = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD23_SetTransformDomainMeshSize, None, itkBSplineTransformD23)
itkBSplineTransformD23.GetTransformDomainMeshSize = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD23_GetTransformDomainMeshSize, None, itkBSplineTransformD23)
itkBSplineTransformD23_swigregister = _itkBSplineTransformPython.itkBSplineTransformD23_swigregister
itkBSplineTransformD23_swigregister(itkBSplineTransformD23)

def itkBSplineTransformD23___New_orig__() -> "itkBSplineTransformD23_Pointer":
    """itkBSplineTransformD23___New_orig__() -> itkBSplineTransformD23_Pointer"""
    return _itkBSplineTransformPython.itkBSplineTransformD23___New_orig__()

def itkBSplineTransformD23_cast(obj: 'itkLightObject') -> "itkBSplineTransformD23 *":
    """itkBSplineTransformD23_cast(itkLightObject obj) -> itkBSplineTransformD23"""
    return _itkBSplineTransformPython.itkBSplineTransformD23_cast(obj)

class itkBSplineTransformD33(itkBSplineBaseTransformPython.itkBSplineBaseTransformD33):
    """


    Deformable transform using a BSpline representation.

    This class encapsulates a deformable transform of points from one
    N-dimensional space to another N-dimensional space. The deformation
    field is modelled using B-splines. A deformation is defined on a
    sparse regular grid of control points $ \\vec{\\lambda}_j $ and is
    varied by defining a deformation $ \\vec{g}(\\vec{\\lambda}_j) $
    of each control point. The deformation $ D(\\vec{x}) $ at any point
    $ \\vec{x} $ is obtained by using a B-spline interpolation kernel.

    The deformation field grid is defined by a user specified transform
    domain (origin, physical dimensions, direction) and B-spline mesh size
    where the mesh size is the number of polynomial patches comprising the
    finite domain of support. The relationship between the mesh size (
    number of polynomial pieces) and the number of control points in any
    given dimension is

    mesh size = number of control points - spline order

    Each grid/control point has associated with it N deformation
    coefficients $ \\vec{\\delta}_j $, representing the N directional
    components of the deformation. Deformation outside the grid plus
    support region for the BSpline interpolation is assumed to be zero.

    The parameters for this transform is N x N-D grid of spline
    coefficients. The user specifies the parameters as one flat array:
    each N-D grid is represented by an array in the same way an N-D image
    is represented in the buffer; the N arrays are then concatenated
    together to form a single array.

    The following illustrates the typical usage of this class:

    An alternative way to set the B-spline coefficients is via array of
    images. The fixed parameters of the transform are taken directly from
    the first image. It is assumed that the subsequent images are the same
    buffered region. The following illustrates the API:

    WARNING:  Use either the SetParameters() or SetCoefficientImages()
    API. Mixing the two modes may results in unexpected results.  The
    class is templated coordinate representation type (float or double),
    the space dimension and the spline order.

    C++ includes: itkBSplineTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBSplineTransformD33_Pointer":
        """__New_orig__() -> itkBSplineTransformD33_Pointer"""
        return _itkBSplineTransformPython.itkBSplineTransformD33___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBSplineTransformD33_Pointer":
        """Clone(itkBSplineTransformD33 self) -> itkBSplineTransformD33_Pointer"""
        return _itkBSplineTransformPython.itkBSplineTransformD33_Clone(self)


    def SetTransformDomainOrigin(self, arg0: 'itkPointD3') -> "void":
        """
        SetTransformDomainOrigin(itkBSplineTransformD33 self, itkPointD3 arg0)

        Function
        to specify the transform domain origin. 
        """
        return _itkBSplineTransformPython.itkBSplineTransformD33_SetTransformDomainOrigin(self, arg0)


    def GetTransformDomainOrigin(self) -> "itkPointD3":
        """
        GetTransformDomainOrigin(itkBSplineTransformD33 self) -> itkPointD3

        Function
        to retrieve the transform domain origin. 
        """
        return _itkBSplineTransformPython.itkBSplineTransformD33_GetTransformDomainOrigin(self)


    def SetTransformDomainPhysicalDimensions(self, arg0: 'itkVectorD3') -> "void":
        """
        SetTransformDomainPhysicalDimensions(itkBSplineTransformD33 self, itkVectorD3 arg0)

        Function to specify the transform domain physical dimensions. 
        """
        return _itkBSplineTransformPython.itkBSplineTransformD33_SetTransformDomainPhysicalDimensions(self, arg0)


    def GetTransformDomainPhysicalDimensions(self) -> "itkVectorD3":
        """
        GetTransformDomainPhysicalDimensions(itkBSplineTransformD33 self) -> itkVectorD3

        Function to retrieve the transform domain physical dimensions. 
        """
        return _itkBSplineTransformPython.itkBSplineTransformD33_GetTransformDomainPhysicalDimensions(self)


    def SetTransformDomainDirection(self, arg0: 'itkMatrixD33') -> "void":
        """
        SetTransformDomainDirection(itkBSplineTransformD33 self, itkMatrixD33 arg0)

        Function to specify the transform domain direction. 
        """
        return _itkBSplineTransformPython.itkBSplineTransformD33_SetTransformDomainDirection(self, arg0)


    def GetTransformDomainDirection(self) -> "itkMatrixD33":
        """
        GetTransformDomainDirection(itkBSplineTransformD33 self) -> itkMatrixD33

        Function to retrieve the transform domain direction. 
        """
        return _itkBSplineTransformPython.itkBSplineTransformD33_GetTransformDomainDirection(self)


    def SetTransformDomainMeshSize(self, arg0: 'itkSize3') -> "void":
        """
        SetTransformDomainMeshSize(itkBSplineTransformD33 self, itkSize3 arg0)

        Function
        to specify the transform domain mesh size. 
        """
        return _itkBSplineTransformPython.itkBSplineTransformD33_SetTransformDomainMeshSize(self, arg0)


    def GetTransformDomainMeshSize(self) -> "itkSize3":
        """
        GetTransformDomainMeshSize(itkBSplineTransformD33 self) -> itkSize3

        Function
        to retrieve the transform domain mesh size. 
        """
        return _itkBSplineTransformPython.itkBSplineTransformD33_GetTransformDomainMeshSize(self)

    __swig_destroy__ = _itkBSplineTransformPython.delete_itkBSplineTransformD33

    def cast(obj: 'itkLightObject') -> "itkBSplineTransformD33 *":
        """cast(itkLightObject obj) -> itkBSplineTransformD33"""
        return _itkBSplineTransformPython.itkBSplineTransformD33_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkBSplineTransformD33

        Create a new object of the class itkBSplineTransformD33 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineTransformD33.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineTransformD33.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineTransformD33.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBSplineTransformD33.Clone = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD33_Clone, None, itkBSplineTransformD33)
itkBSplineTransformD33.SetTransformDomainOrigin = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD33_SetTransformDomainOrigin, None, itkBSplineTransformD33)
itkBSplineTransformD33.GetTransformDomainOrigin = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD33_GetTransformDomainOrigin, None, itkBSplineTransformD33)
itkBSplineTransformD33.SetTransformDomainPhysicalDimensions = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD33_SetTransformDomainPhysicalDimensions, None, itkBSplineTransformD33)
itkBSplineTransformD33.GetTransformDomainPhysicalDimensions = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD33_GetTransformDomainPhysicalDimensions, None, itkBSplineTransformD33)
itkBSplineTransformD33.SetTransformDomainDirection = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD33_SetTransformDomainDirection, None, itkBSplineTransformD33)
itkBSplineTransformD33.GetTransformDomainDirection = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD33_GetTransformDomainDirection, None, itkBSplineTransformD33)
itkBSplineTransformD33.SetTransformDomainMeshSize = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD33_SetTransformDomainMeshSize, None, itkBSplineTransformD33)
itkBSplineTransformD33.GetTransformDomainMeshSize = new_instancemethod(_itkBSplineTransformPython.itkBSplineTransformD33_GetTransformDomainMeshSize, None, itkBSplineTransformD33)
itkBSplineTransformD33_swigregister = _itkBSplineTransformPython.itkBSplineTransformD33_swigregister
itkBSplineTransformD33_swigregister(itkBSplineTransformD33)

def itkBSplineTransformD33___New_orig__() -> "itkBSplineTransformD33_Pointer":
    """itkBSplineTransformD33___New_orig__() -> itkBSplineTransformD33_Pointer"""
    return _itkBSplineTransformPython.itkBSplineTransformD33___New_orig__()

def itkBSplineTransformD33_cast(obj: 'itkLightObject') -> "itkBSplineTransformD33 *":
    """itkBSplineTransformD33_cast(itkLightObject obj) -> itkBSplineTransformD33"""
    return _itkBSplineTransformPython.itkBSplineTransformD33_cast(obj)



