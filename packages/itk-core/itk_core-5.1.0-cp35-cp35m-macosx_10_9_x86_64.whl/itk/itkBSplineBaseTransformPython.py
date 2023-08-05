# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkBSplineBaseTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkBSplineBaseTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkBSplineBaseTransformPython
            return _itkBSplineBaseTransformPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkBSplineBaseTransformPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkBSplineBaseTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkBSplineBaseTransformPython
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


import itkTransformBasePython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkFixedArrayPython
import pyBasePython
import itkMatrixPython
import vnl_matrix_fixedPython
import vnl_matrixPython
import vnl_vectorPython
import stdcomplexPython
import itkVectorPython
import vnl_vector_refPython
import itkCovariantVectorPython
import itkPointPython
import itkArray2DPython
import itkVariableLengthVectorPython
import itkOptimizerParametersPython
import itkArrayPython
import ITKCommonBasePython
import itkContinuousIndexPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkBSplineInterpolationWeightFunctionPython
import itkFunctionBasePython
import itkImagePython
import itkImageRegionPython
import itkRGBAPixelPython
import itkRGBPixelPython

def itkBSplineBaseTransformD33_New():
  return itkBSplineBaseTransformD33.New()


def itkBSplineBaseTransformD23_New():
  return itkBSplineBaseTransformD23.New()

class itkBSplineBaseTransformD23(itkTransformBasePython.itkTransformD22):
    """


    A base class with common elements of BSplineTransform and
    BSplineDeformableTransform.

    C++ includes: itkBSplineBaseTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def Clone(self) -> "itkBSplineBaseTransformD23_Pointer":
        """Clone(itkBSplineBaseTransformD23 self) -> itkBSplineBaseTransformD23_Pointer"""
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD23_Clone(self)


    def SetIdentity(self) -> "void":
        """
        SetIdentity(itkBSplineBaseTransformD23 self)

        This method can ONLY be
        invoked AFTER calling SetParameters(). This restriction is due to the
        fact that the BSplineBaseTransform does not copy the array of
        parameters internally, instead it keeps a pointer to the user-provided
        array of parameters. This method is also in violation of the const-
        correctness of the parameters since the parameter array has been
        passed to the transform on a 'const' basis but the values get modified
        when the user invokes SetIdentity(). 
        """
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD23_SetIdentity(self)


    def SetCoefficientImages(self, images: 'itk::FixedArray< itk::SmartPointer< itk::Image< double,2 > >,2 > const &') -> "void":
        """
        SetCoefficientImages(itkBSplineBaseTransformD23 self, itk::FixedArray< itk::SmartPointer< itk::Image< double,2 > >,2 > const & images)

        Set the array
        of coefficient images.

        This is an alternative API for setting the BSpline coefficients as an
        array of SpaceDimension images. The fixed parameters are taken from
        the first image. It is assumed that the buffered region of all the
        subsequent images are the same as the first image. Note that no error
        checking is done.

        Warning: use either the SetParameters() or SetCoefficientImages() API.
        Mixing the two modes may results in unexpected results. 
        """
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD23_SetCoefficientImages(self, images)


    def GetCoefficientImages(self) -> "itk::FixedArray< itk::SmartPointer< itk::Image< double,2 > >,2 > const":
        """
        GetCoefficientImages(itkBSplineBaseTransformD23 self) -> itk::FixedArray< itk::SmartPointer< itk::Image< double,2 > >,2 > const

        Get the array
        of coefficient images. 
        """
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD23_GetCoefficientImages(self)


    def UpdateTransformParameters(self, update: 'itkArrayD', factor: 'double'=1.) -> "void":
        """
        UpdateTransformParameters(itkBSplineBaseTransformD23 self, itkArrayD update, double factor=1.)
        UpdateTransformParameters(itkBSplineBaseTransformD23 self, itkArrayD update)

        Update
        the transform's parameters by the adding values in update to current
        parameter values. We assume update is of the same length as
        Parameters. Throw exception otherwise. factor is a scalar multiplier
        for each value in update. SetParameters is called at the end of this
        method, to allow transforms to perform any required operations on the
        update parameters, typically a conversion to member variables for use
        in TransformPoint. Derived classes should override to provide
        specialized behavior. 
        """
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD23_UpdateTransformParameters(self, update, factor)


    def TransformPoint(self, *args) -> "void":
        """
        TransformPoint(itkBSplineBaseTransformD23 self, itkPointD2 point) -> itkPointD2
        TransformPoint(itkBSplineBaseTransformD23 self, itkPointD2 inputPoint, itkPointD2 outputPoint, itkArrayD weights, itkArrayUL indices, bool & inside)

        Transform points by
        a BSpline deformable transformation. On return, weights contains the
        interpolation weights used to compute the deformation and indices of
        the x (zeroth) dimension coefficient parameters in the support region
        used to compute the deformation. Parameter indices for the i-th
        dimension can be obtained by adding ( i * this->
        GetNumberOfParametersPerDimension() ) to the indices array. 
        """
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD23_TransformPoint(self, *args)


    def GetNumberOfWeights(self) -> "unsigned long":
        """
        GetNumberOfWeights(itkBSplineBaseTransformD23 self) -> unsigned long

        Get number of
        weights. 
        """
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD23_GetNumberOfWeights(self)


    def TransformVector(self, *args) -> "vnl_vector_fixed< double,2 >":
        """
        TransformVector(itkBSplineBaseTransformD23 self, itkVectorD2 arg0) -> itkVectorD2
        TransformVector(itkBSplineBaseTransformD23 self, vnl_vector_fixed< double,2 > const & arg0) -> vnl_vector_fixed< double,2 >

        Method to transform
        a vnl_vector - not applicable for this type of transform 
        """
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD23_TransformVector(self, *args)


    def ComputeJacobianFromBSplineWeightsWithRespectToPosition(self, arg0: 'itkPointD2', arg1: 'itkArrayD', arg2: 'itkArrayUL') -> "void":
        """
        ComputeJacobianFromBSplineWeightsWithRespectToPosition(itkBSplineBaseTransformD23 self, itkPointD2 arg0, itkArrayD arg1, itkArrayUL arg2)

        Get
        Jacobian at a point. A very specialized function just for BSplines 
        """
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD23_ComputeJacobianFromBSplineWeightsWithRespectToPosition(self, arg0, arg1, arg2)


    def GetNumberOfParametersPerDimension(self) -> "unsigned long":
        """
        GetNumberOfParametersPerDimension(itkBSplineBaseTransformD23 self) -> unsigned long

        Return the number of parameters per dimension 
        """
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD23_GetNumberOfParametersPerDimension(self)


    def GetNumberOfAffectedWeights(self) -> "unsigned int":
        """GetNumberOfAffectedWeights(itkBSplineBaseTransformD23 self) -> unsigned int"""
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD23_GetNumberOfAffectedWeights(self)

    __swig_destroy__ = _itkBSplineBaseTransformPython.delete_itkBSplineBaseTransformD23

    def cast(obj: 'itkLightObject') -> "itkBSplineBaseTransformD23 *":
        """cast(itkLightObject obj) -> itkBSplineBaseTransformD23"""
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD23_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkBSplineBaseTransformD23

        Create a new object of the class itkBSplineBaseTransformD23 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineBaseTransformD23.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineBaseTransformD23.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineBaseTransformD23.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBSplineBaseTransformD23.Clone = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD23_Clone, None, itkBSplineBaseTransformD23)
itkBSplineBaseTransformD23.SetIdentity = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD23_SetIdentity, None, itkBSplineBaseTransformD23)
itkBSplineBaseTransformD23.SetCoefficientImages = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD23_SetCoefficientImages, None, itkBSplineBaseTransformD23)
itkBSplineBaseTransformD23.GetCoefficientImages = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD23_GetCoefficientImages, None, itkBSplineBaseTransformD23)
itkBSplineBaseTransformD23.UpdateTransformParameters = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD23_UpdateTransformParameters, None, itkBSplineBaseTransformD23)
itkBSplineBaseTransformD23.TransformPoint = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD23_TransformPoint, None, itkBSplineBaseTransformD23)
itkBSplineBaseTransformD23.GetNumberOfWeights = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD23_GetNumberOfWeights, None, itkBSplineBaseTransformD23)
itkBSplineBaseTransformD23.TransformVector = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD23_TransformVector, None, itkBSplineBaseTransformD23)
itkBSplineBaseTransformD23.ComputeJacobianFromBSplineWeightsWithRespectToPosition = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD23_ComputeJacobianFromBSplineWeightsWithRespectToPosition, None, itkBSplineBaseTransformD23)
itkBSplineBaseTransformD23.GetNumberOfParametersPerDimension = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD23_GetNumberOfParametersPerDimension, None, itkBSplineBaseTransformD23)
itkBSplineBaseTransformD23.GetNumberOfAffectedWeights = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD23_GetNumberOfAffectedWeights, None, itkBSplineBaseTransformD23)
itkBSplineBaseTransformD23_swigregister = _itkBSplineBaseTransformPython.itkBSplineBaseTransformD23_swigregister
itkBSplineBaseTransformD23_swigregister(itkBSplineBaseTransformD23)

def itkBSplineBaseTransformD23_cast(obj: 'itkLightObject') -> "itkBSplineBaseTransformD23 *":
    """itkBSplineBaseTransformD23_cast(itkLightObject obj) -> itkBSplineBaseTransformD23"""
    return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD23_cast(obj)

class itkBSplineBaseTransformD33(itkTransformBasePython.itkTransformD33):
    """


    A base class with common elements of BSplineTransform and
    BSplineDeformableTransform.

    C++ includes: itkBSplineBaseTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def Clone(self) -> "itkBSplineBaseTransformD33_Pointer":
        """Clone(itkBSplineBaseTransformD33 self) -> itkBSplineBaseTransformD33_Pointer"""
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_Clone(self)


    def SetIdentity(self) -> "void":
        """
        SetIdentity(itkBSplineBaseTransformD33 self)

        This method can ONLY be
        invoked AFTER calling SetParameters(). This restriction is due to the
        fact that the BSplineBaseTransform does not copy the array of
        parameters internally, instead it keeps a pointer to the user-provided
        array of parameters. This method is also in violation of the const-
        correctness of the parameters since the parameter array has been
        passed to the transform on a 'const' basis but the values get modified
        when the user invokes SetIdentity(). 
        """
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_SetIdentity(self)


    def SetCoefficientImages(self, images: 'itk::FixedArray< itk::SmartPointer< itk::Image< double,3 > >,3 > const &') -> "void":
        """
        SetCoefficientImages(itkBSplineBaseTransformD33 self, itk::FixedArray< itk::SmartPointer< itk::Image< double,3 > >,3 > const & images)

        Set the array
        of coefficient images.

        This is an alternative API for setting the BSpline coefficients as an
        array of SpaceDimension images. The fixed parameters are taken from
        the first image. It is assumed that the buffered region of all the
        subsequent images are the same as the first image. Note that no error
        checking is done.

        Warning: use either the SetParameters() or SetCoefficientImages() API.
        Mixing the two modes may results in unexpected results. 
        """
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_SetCoefficientImages(self, images)


    def GetCoefficientImages(self) -> "itk::FixedArray< itk::SmartPointer< itk::Image< double,3 > >,3 > const":
        """
        GetCoefficientImages(itkBSplineBaseTransformD33 self) -> itk::FixedArray< itk::SmartPointer< itk::Image< double,3 > >,3 > const

        Get the array
        of coefficient images. 
        """
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_GetCoefficientImages(self)


    def UpdateTransformParameters(self, update: 'itkArrayD', factor: 'double'=1.) -> "void":
        """
        UpdateTransformParameters(itkBSplineBaseTransformD33 self, itkArrayD update, double factor=1.)
        UpdateTransformParameters(itkBSplineBaseTransformD33 self, itkArrayD update)

        Update
        the transform's parameters by the adding values in update to current
        parameter values. We assume update is of the same length as
        Parameters. Throw exception otherwise. factor is a scalar multiplier
        for each value in update. SetParameters is called at the end of this
        method, to allow transforms to perform any required operations on the
        update parameters, typically a conversion to member variables for use
        in TransformPoint. Derived classes should override to provide
        specialized behavior. 
        """
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_UpdateTransformParameters(self, update, factor)


    def TransformPoint(self, *args) -> "void":
        """
        TransformPoint(itkBSplineBaseTransformD33 self, itkPointD3 point) -> itkPointD3
        TransformPoint(itkBSplineBaseTransformD33 self, itkPointD3 inputPoint, itkPointD3 outputPoint, itkArrayD weights, itkArrayUL indices, bool & inside)

        Transform points by
        a BSpline deformable transformation. On return, weights contains the
        interpolation weights used to compute the deformation and indices of
        the x (zeroth) dimension coefficient parameters in the support region
        used to compute the deformation. Parameter indices for the i-th
        dimension can be obtained by adding ( i * this->
        GetNumberOfParametersPerDimension() ) to the indices array. 
        """
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_TransformPoint(self, *args)


    def GetNumberOfWeights(self) -> "unsigned long":
        """
        GetNumberOfWeights(itkBSplineBaseTransformD33 self) -> unsigned long

        Get number of
        weights. 
        """
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_GetNumberOfWeights(self)


    def TransformVector(self, *args) -> "vnl_vector_fixed< double,3 >":
        """
        TransformVector(itkBSplineBaseTransformD33 self, itkVectorD3 arg0) -> itkVectorD3
        TransformVector(itkBSplineBaseTransformD33 self, vnl_vector_fixed< double,3 > const & arg0) -> vnl_vector_fixed< double,3 >

        Method to transform
        a vnl_vector - not applicable for this type of transform 
        """
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_TransformVector(self, *args)


    def ComputeJacobianFromBSplineWeightsWithRespectToPosition(self, arg0: 'itkPointD3', arg1: 'itkArrayD', arg2: 'itkArrayUL') -> "void":
        """
        ComputeJacobianFromBSplineWeightsWithRespectToPosition(itkBSplineBaseTransformD33 self, itkPointD3 arg0, itkArrayD arg1, itkArrayUL arg2)

        Get
        Jacobian at a point. A very specialized function just for BSplines 
        """
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_ComputeJacobianFromBSplineWeightsWithRespectToPosition(self, arg0, arg1, arg2)


    def GetNumberOfParametersPerDimension(self) -> "unsigned long":
        """
        GetNumberOfParametersPerDimension(itkBSplineBaseTransformD33 self) -> unsigned long

        Return the number of parameters per dimension 
        """
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_GetNumberOfParametersPerDimension(self)


    def GetNumberOfAffectedWeights(self) -> "unsigned int":
        """GetNumberOfAffectedWeights(itkBSplineBaseTransformD33 self) -> unsigned int"""
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_GetNumberOfAffectedWeights(self)

    __swig_destroy__ = _itkBSplineBaseTransformPython.delete_itkBSplineBaseTransformD33

    def cast(obj: 'itkLightObject') -> "itkBSplineBaseTransformD33 *":
        """cast(itkLightObject obj) -> itkBSplineBaseTransformD33"""
        return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkBSplineBaseTransformD33

        Create a new object of the class itkBSplineBaseTransformD33 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineBaseTransformD33.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineBaseTransformD33.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineBaseTransformD33.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBSplineBaseTransformD33.Clone = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_Clone, None, itkBSplineBaseTransformD33)
itkBSplineBaseTransformD33.SetIdentity = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_SetIdentity, None, itkBSplineBaseTransformD33)
itkBSplineBaseTransformD33.SetCoefficientImages = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_SetCoefficientImages, None, itkBSplineBaseTransformD33)
itkBSplineBaseTransformD33.GetCoefficientImages = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_GetCoefficientImages, None, itkBSplineBaseTransformD33)
itkBSplineBaseTransformD33.UpdateTransformParameters = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_UpdateTransformParameters, None, itkBSplineBaseTransformD33)
itkBSplineBaseTransformD33.TransformPoint = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_TransformPoint, None, itkBSplineBaseTransformD33)
itkBSplineBaseTransformD33.GetNumberOfWeights = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_GetNumberOfWeights, None, itkBSplineBaseTransformD33)
itkBSplineBaseTransformD33.TransformVector = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_TransformVector, None, itkBSplineBaseTransformD33)
itkBSplineBaseTransformD33.ComputeJacobianFromBSplineWeightsWithRespectToPosition = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_ComputeJacobianFromBSplineWeightsWithRespectToPosition, None, itkBSplineBaseTransformD33)
itkBSplineBaseTransformD33.GetNumberOfParametersPerDimension = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_GetNumberOfParametersPerDimension, None, itkBSplineBaseTransformD33)
itkBSplineBaseTransformD33.GetNumberOfAffectedWeights = new_instancemethod(_itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_GetNumberOfAffectedWeights, None, itkBSplineBaseTransformD33)
itkBSplineBaseTransformD33_swigregister = _itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_swigregister
itkBSplineBaseTransformD33_swigregister(itkBSplineBaseTransformD33)

def itkBSplineBaseTransformD33_cast(obj: 'itkLightObject') -> "itkBSplineBaseTransformD33 *":
    """itkBSplineBaseTransformD33_cast(itkLightObject obj) -> itkBSplineBaseTransformD33"""
    return _itkBSplineBaseTransformPython.itkBSplineBaseTransformD33_cast(obj)



