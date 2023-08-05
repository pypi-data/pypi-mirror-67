# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkScaleTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkScaleTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkScaleTransformPython
            return _itkScaleTransformPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkScaleTransformPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkScaleTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkScaleTransformPython
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


import itkCovariantVectorPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import pyBasePython
import vnl_vector_refPython
import itkVectorPython
import itkFixedArrayPython
import ITKCommonBasePython
import itkPointPython
import itkArray2DPython
import itkOptimizerParametersPython
import itkArrayPython
import vnl_matrix_fixedPython
import itkMatrixOffsetTransformBasePython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import itkDiffusionTensor3DPython
import itkVariableLengthVectorPython
import itkTransformBasePython

def itkScaleTransformD3_New():
  return itkScaleTransformD3.New()


def itkScaleTransformD2_New():
  return itkScaleTransformD2.New()

class itkScaleTransformD2(itkMatrixOffsetTransformBasePython.itkMatrixOffsetTransformBaseD22):
    """


    Scale transformation of a vector space (e.g. space coordinates)

    The same functionality could be obtained by using the Affine
    transform, but with a large difference in performance since the affine
    transform will use a matrix multiplication using a diagonal matrix.

    \\sphinx \\sphinxexample{Core/Transform/ScaleAnImage,Scale An
    Image} \\endsphinx

    C++ includes: itkScaleTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkScaleTransformD2_Pointer":
        """__New_orig__() -> itkScaleTransformD2_Pointer"""
        return _itkScaleTransformPython.itkScaleTransformD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkScaleTransformD2_Pointer":
        """Clone(itkScaleTransformD2 self) -> itkScaleTransformD2_Pointer"""
        return _itkScaleTransformPython.itkScaleTransformD2_Clone(self)


    def SetScale(self, scale: 'itkFixedArrayD2') -> "void":
        """
        SetScale(itkScaleTransformD2 self, itkFixedArrayD2 scale)

        Set the factors of an
        Scale Transform This method sets the factors of an ScaleTransform to a
        value specified by the user. This method cannot be done with SetMacro
        because itk::Array has not an operator== defined. The array of scales
        correspond in order to the factors to be applied to each one of the
        coordinates. For example, in 3D, scale[0] corresponds to X, scale[1]
        corresponds to Y and scale[2] corresponds to Z. 
        """
        return _itkScaleTransformPython.itkScaleTransformD2_SetScale(self, scale)


    def ComputeMatrix(self) -> "void":
        """ComputeMatrix(itkScaleTransformD2 self)"""
        return _itkScaleTransformPython.itkScaleTransformD2_ComputeMatrix(self)


    def Compose(self, other: 'itkScaleTransformD2', pre: 'bool'=False) -> "void":
        """
        Compose(itkScaleTransformD2 self, itkScaleTransformD2 other, bool pre=False)
        Compose(itkScaleTransformD2 self, itkScaleTransformD2 other)

        Compose with another
        ScaleTransform. 
        """
        return _itkScaleTransformPython.itkScaleTransformD2_Compose(self, other, pre)


    def Scale(self, scale: 'itkFixedArrayD2', pre: 'bool'=False) -> "void":
        """
        Scale(itkScaleTransformD2 self, itkFixedArrayD2 scale, bool pre=False)
        Scale(itkScaleTransformD2 self, itkFixedArrayD2 scale)

        Compose this transform
        transformation with another scaling. The pre argument is irrelevant
        here since scale transforms are commutative, pre and postcomposition
        are therefore equivalent. 
        """
        return _itkScaleTransformPython.itkScaleTransformD2_Scale(self, scale, pre)


    def TransformVector(self, *args) -> "vnl_vector_fixed< double,2 >":
        """
        TransformVector(itkScaleTransformD2 self, itkVectorD2 vector) -> itkVectorD2
        TransformVector(itkScaleTransformD2 self, vnl_vector_fixed< double,2 > const & vector) -> vnl_vector_fixed< double,2 >

        Method to transform
        a vector stored in a VectorImage, at a point. For global transforms,
        point is ignored and TransformVector( vector ) is called. Local
        transforms (e.g. deformation field transform) must override and
        provide required behavior. 
        """
        return _itkScaleTransformPython.itkScaleTransformD2_TransformVector(self, *args)


    def BackTransform(self, *args) -> "itkCovariantVectorD2":
        """
        BackTransform(itkScaleTransformD2 self, itkPointD2 point) -> itkPointD2
        BackTransform(itkScaleTransformD2 self, itkVectorD2 vector) -> itkVectorD2
        BackTransform(itkScaleTransformD2 self, vnl_vector_fixed< double,2 > const & vector) -> vnl_vector_fixed< double,2 >
        BackTransform(itkScaleTransformD2 self, itkCovariantVectorD2 vector) -> itkCovariantVectorD2

        Back transform by a
        scale transformation This method finds the point or vector that maps
        to a given point or vector under the scale transformation defined by
        self. If no such point exists, an exception is thrown. 
        """
        return _itkScaleTransformPython.itkScaleTransformD2_BackTransform(self, *args)


    def GetInverse(self, inverse: 'itkScaleTransformD2') -> "bool":
        """
        GetInverse(itkScaleTransformD2 self, itkScaleTransformD2 inverse) -> bool

        Find inverse of a scale
        transformation This method creates and returns a new ScaleTransform
        object which is the inverse of self. If self is not invertible, false
        is returned. 
        """
        return _itkScaleTransformPython.itkScaleTransformD2_GetInverse(self, inverse)


    def GetScale(self) -> "itkFixedArrayD2 const &":
        """
        GetScale(itkScaleTransformD2 self) -> itkFixedArrayD2

        Get access to scale values

        """
        return _itkScaleTransformPython.itkScaleTransformD2_GetScale(self)

    __swig_destroy__ = _itkScaleTransformPython.delete_itkScaleTransformD2

    def cast(obj: 'itkLightObject') -> "itkScaleTransformD2 *":
        """cast(itkLightObject obj) -> itkScaleTransformD2"""
        return _itkScaleTransformPython.itkScaleTransformD2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkScaleTransformD2

        Create a new object of the class itkScaleTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkScaleTransformD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkScaleTransformD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkScaleTransformD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkScaleTransformD2.Clone = new_instancemethod(_itkScaleTransformPython.itkScaleTransformD2_Clone, None, itkScaleTransformD2)
itkScaleTransformD2.SetScale = new_instancemethod(_itkScaleTransformPython.itkScaleTransformD2_SetScale, None, itkScaleTransformD2)
itkScaleTransformD2.ComputeMatrix = new_instancemethod(_itkScaleTransformPython.itkScaleTransformD2_ComputeMatrix, None, itkScaleTransformD2)
itkScaleTransformD2.Compose = new_instancemethod(_itkScaleTransformPython.itkScaleTransformD2_Compose, None, itkScaleTransformD2)
itkScaleTransformD2.Scale = new_instancemethod(_itkScaleTransformPython.itkScaleTransformD2_Scale, None, itkScaleTransformD2)
itkScaleTransformD2.TransformVector = new_instancemethod(_itkScaleTransformPython.itkScaleTransformD2_TransformVector, None, itkScaleTransformD2)
itkScaleTransformD2.BackTransform = new_instancemethod(_itkScaleTransformPython.itkScaleTransformD2_BackTransform, None, itkScaleTransformD2)
itkScaleTransformD2.GetInverse = new_instancemethod(_itkScaleTransformPython.itkScaleTransformD2_GetInverse, None, itkScaleTransformD2)
itkScaleTransformD2.GetScale = new_instancemethod(_itkScaleTransformPython.itkScaleTransformD2_GetScale, None, itkScaleTransformD2)
itkScaleTransformD2_swigregister = _itkScaleTransformPython.itkScaleTransformD2_swigregister
itkScaleTransformD2_swigregister(itkScaleTransformD2)

def itkScaleTransformD2___New_orig__() -> "itkScaleTransformD2_Pointer":
    """itkScaleTransformD2___New_orig__() -> itkScaleTransformD2_Pointer"""
    return _itkScaleTransformPython.itkScaleTransformD2___New_orig__()

def itkScaleTransformD2_cast(obj: 'itkLightObject') -> "itkScaleTransformD2 *":
    """itkScaleTransformD2_cast(itkLightObject obj) -> itkScaleTransformD2"""
    return _itkScaleTransformPython.itkScaleTransformD2_cast(obj)

class itkScaleTransformD3(itkMatrixOffsetTransformBasePython.itkMatrixOffsetTransformBaseD33):
    """


    Scale transformation of a vector space (e.g. space coordinates)

    The same functionality could be obtained by using the Affine
    transform, but with a large difference in performance since the affine
    transform will use a matrix multiplication using a diagonal matrix.

    \\sphinx \\sphinxexample{Core/Transform/ScaleAnImage,Scale An
    Image} \\endsphinx

    C++ includes: itkScaleTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkScaleTransformD3_Pointer":
        """__New_orig__() -> itkScaleTransformD3_Pointer"""
        return _itkScaleTransformPython.itkScaleTransformD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkScaleTransformD3_Pointer":
        """Clone(itkScaleTransformD3 self) -> itkScaleTransformD3_Pointer"""
        return _itkScaleTransformPython.itkScaleTransformD3_Clone(self)


    def SetScale(self, scale: 'itkFixedArrayD3') -> "void":
        """
        SetScale(itkScaleTransformD3 self, itkFixedArrayD3 scale)

        Set the factors of an
        Scale Transform This method sets the factors of an ScaleTransform to a
        value specified by the user. This method cannot be done with SetMacro
        because itk::Array has not an operator== defined. The array of scales
        correspond in order to the factors to be applied to each one of the
        coordinates. For example, in 3D, scale[0] corresponds to X, scale[1]
        corresponds to Y and scale[2] corresponds to Z. 
        """
        return _itkScaleTransformPython.itkScaleTransformD3_SetScale(self, scale)


    def ComputeMatrix(self) -> "void":
        """ComputeMatrix(itkScaleTransformD3 self)"""
        return _itkScaleTransformPython.itkScaleTransformD3_ComputeMatrix(self)


    def Compose(self, other: 'itkScaleTransformD3', pre: 'bool'=False) -> "void":
        """
        Compose(itkScaleTransformD3 self, itkScaleTransformD3 other, bool pre=False)
        Compose(itkScaleTransformD3 self, itkScaleTransformD3 other)

        Compose with another
        ScaleTransform. 
        """
        return _itkScaleTransformPython.itkScaleTransformD3_Compose(self, other, pre)


    def Scale(self, scale: 'itkFixedArrayD3', pre: 'bool'=False) -> "void":
        """
        Scale(itkScaleTransformD3 self, itkFixedArrayD3 scale, bool pre=False)
        Scale(itkScaleTransformD3 self, itkFixedArrayD3 scale)

        Compose this transform
        transformation with another scaling. The pre argument is irrelevant
        here since scale transforms are commutative, pre and postcomposition
        are therefore equivalent. 
        """
        return _itkScaleTransformPython.itkScaleTransformD3_Scale(self, scale, pre)


    def TransformVector(self, *args) -> "vnl_vector_fixed< double,3 >":
        """
        TransformVector(itkScaleTransformD3 self, itkVectorD3 vector) -> itkVectorD3
        TransformVector(itkScaleTransformD3 self, vnl_vector_fixed< double,3 > const & vector) -> vnl_vector_fixed< double,3 >

        Method to transform
        a vector stored in a VectorImage, at a point. For global transforms,
        point is ignored and TransformVector( vector ) is called. Local
        transforms (e.g. deformation field transform) must override and
        provide required behavior. 
        """
        return _itkScaleTransformPython.itkScaleTransformD3_TransformVector(self, *args)


    def BackTransform(self, *args) -> "itkCovariantVectorD3":
        """
        BackTransform(itkScaleTransformD3 self, itkPointD3 point) -> itkPointD3
        BackTransform(itkScaleTransformD3 self, itkVectorD3 vector) -> itkVectorD3
        BackTransform(itkScaleTransformD3 self, vnl_vector_fixed< double,3 > const & vector) -> vnl_vector_fixed< double,3 >
        BackTransform(itkScaleTransformD3 self, itkCovariantVectorD3 vector) -> itkCovariantVectorD3

        Back transform by a
        scale transformation This method finds the point or vector that maps
        to a given point or vector under the scale transformation defined by
        self. If no such point exists, an exception is thrown. 
        """
        return _itkScaleTransformPython.itkScaleTransformD3_BackTransform(self, *args)


    def GetInverse(self, inverse: 'itkScaleTransformD3') -> "bool":
        """
        GetInverse(itkScaleTransformD3 self, itkScaleTransformD3 inverse) -> bool

        Find inverse of a scale
        transformation This method creates and returns a new ScaleTransform
        object which is the inverse of self. If self is not invertible, false
        is returned. 
        """
        return _itkScaleTransformPython.itkScaleTransformD3_GetInverse(self, inverse)


    def GetScale(self) -> "itkFixedArrayD3 const &":
        """
        GetScale(itkScaleTransformD3 self) -> itkFixedArrayD3

        Get access to scale values

        """
        return _itkScaleTransformPython.itkScaleTransformD3_GetScale(self)

    __swig_destroy__ = _itkScaleTransformPython.delete_itkScaleTransformD3

    def cast(obj: 'itkLightObject') -> "itkScaleTransformD3 *":
        """cast(itkLightObject obj) -> itkScaleTransformD3"""
        return _itkScaleTransformPython.itkScaleTransformD3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkScaleTransformD3

        Create a new object of the class itkScaleTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkScaleTransformD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkScaleTransformD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkScaleTransformD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkScaleTransformD3.Clone = new_instancemethod(_itkScaleTransformPython.itkScaleTransformD3_Clone, None, itkScaleTransformD3)
itkScaleTransformD3.SetScale = new_instancemethod(_itkScaleTransformPython.itkScaleTransformD3_SetScale, None, itkScaleTransformD3)
itkScaleTransformD3.ComputeMatrix = new_instancemethod(_itkScaleTransformPython.itkScaleTransformD3_ComputeMatrix, None, itkScaleTransformD3)
itkScaleTransformD3.Compose = new_instancemethod(_itkScaleTransformPython.itkScaleTransformD3_Compose, None, itkScaleTransformD3)
itkScaleTransformD3.Scale = new_instancemethod(_itkScaleTransformPython.itkScaleTransformD3_Scale, None, itkScaleTransformD3)
itkScaleTransformD3.TransformVector = new_instancemethod(_itkScaleTransformPython.itkScaleTransformD3_TransformVector, None, itkScaleTransformD3)
itkScaleTransformD3.BackTransform = new_instancemethod(_itkScaleTransformPython.itkScaleTransformD3_BackTransform, None, itkScaleTransformD3)
itkScaleTransformD3.GetInverse = new_instancemethod(_itkScaleTransformPython.itkScaleTransformD3_GetInverse, None, itkScaleTransformD3)
itkScaleTransformD3.GetScale = new_instancemethod(_itkScaleTransformPython.itkScaleTransformD3_GetScale, None, itkScaleTransformD3)
itkScaleTransformD3_swigregister = _itkScaleTransformPython.itkScaleTransformD3_swigregister
itkScaleTransformD3_swigregister(itkScaleTransformD3)

def itkScaleTransformD3___New_orig__() -> "itkScaleTransformD3_Pointer":
    """itkScaleTransformD3___New_orig__() -> itkScaleTransformD3_Pointer"""
    return _itkScaleTransformPython.itkScaleTransformD3___New_orig__()

def itkScaleTransformD3_cast(obj: 'itkLightObject') -> "itkScaleTransformD3 *":
    """itkScaleTransformD3_cast(itkLightObject obj) -> itkScaleTransformD3"""
    return _itkScaleTransformPython.itkScaleTransformD3_cast(obj)



