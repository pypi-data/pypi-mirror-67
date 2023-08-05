# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkTranslationTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkTranslationTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkTranslationTransformPython
            return _itkTranslationTransformPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkTranslationTransformPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkTranslationTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkTranslationTransformPython
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
import itkTransformBasePython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import itkDiffusionTensor3DPython
import itkVariableLengthVectorPython

def itkTranslationTransformD3_New():
  return itkTranslationTransformD3.New()


def itkTranslationTransformD2_New():
  return itkTranslationTransformD2.New()

class itkTranslationTransformD2(itkTransformBasePython.itkTransformD22):
    """


    Translation transformation of a vector space (e.g. space coordinates)

    The same functionality could be obtained by using the Affine
    transform, but with a large difference in performance.

    \\sphinx
    \\sphinxexample{Core/Transform/TranslateAVectorImage,Translate
    Vector Image} \\sphinxexample{Registration/Common/GlobalRegistration
    OfTwoImages,Global Registration Of Two Images}
    \\sphinxexample{Registration/Common/MutualInformation,Mutual
    Information} \\endsphinx

    C++ includes: itkTranslationTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkTranslationTransformD2_Pointer":
        """__New_orig__() -> itkTranslationTransformD2_Pointer"""
        return _itkTranslationTransformPython.itkTranslationTransformD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkTranslationTransformD2_Pointer":
        """Clone(itkTranslationTransformD2 self) -> itkTranslationTransformD2_Pointer"""
        return _itkTranslationTransformPython.itkTranslationTransformD2_Clone(self)


    def GetOffset(self) -> "itkVectorD2 const &":
        """
        GetOffset(itkTranslationTransformD2 self) -> itkVectorD2

        This method returns the
        value of the offset of the TranslationTransform. 
        """
        return _itkTranslationTransformPython.itkTranslationTransformD2_GetOffset(self)


    def SetOffset(self, offset: 'itkVectorD2') -> "void":
        """
        SetOffset(itkTranslationTransformD2 self, itkVectorD2 offset)

        Set offset of an
        Translation Transform. This method sets the offset of an
        TranslationTransform to a value specified by the user. 
        """
        return _itkTranslationTransformPython.itkTranslationTransformD2_SetOffset(self, offset)


    def Compose(self, other: 'itkTranslationTransformD2', pre: 'bool'=False) -> "void":
        """
        Compose(itkTranslationTransformD2 self, itkTranslationTransformD2 other, bool pre=False)
        Compose(itkTranslationTransformD2 self, itkTranslationTransformD2 other)

        Compose with another
        TranslationTransform. 
        """
        return _itkTranslationTransformPython.itkTranslationTransformD2_Compose(self, other, pre)


    def Translate(self, offset: 'itkVectorD2', pre: 'bool'=False) -> "void":
        """
        Translate(itkTranslationTransformD2 self, itkVectorD2 offset, bool pre=False)
        Translate(itkTranslationTransformD2 self, itkVectorD2 offset)

        Compose affine
        transformation with a translation. This method modifies self to
        include a translation of the origin. The translation is precomposed
        with self if pre is true, and postcomposed otherwise. 
        """
        return _itkTranslationTransformPython.itkTranslationTransformD2_Translate(self, offset, pre)


    def TransformVector(self, *args) -> "vnl_vector_fixed< double,2 >":
        """
        TransformVector(itkTranslationTransformD2 self, itkVectorD2 vector) -> itkVectorD2
        TransformVector(itkTranslationTransformD2 self, vnl_vector_fixed< double,2 > const & vector) -> vnl_vector_fixed< double,2 >

        Method to transform
        a vector stored in a VectorImage, at a point. For global transforms,
        point is ignored and TransformVector( vector ) is called. Local
        transforms (e.g. deformation field transform) must override and
        provide required behavior. 
        """
        return _itkTranslationTransformPython.itkTranslationTransformD2_TransformVector(self, *args)


    def BackTransform(self, *args) -> "itkCovariantVectorD2":
        """
        BackTransform(itkTranslationTransformD2 self, itkPointD2 point) -> itkPointD2
        BackTransform(itkTranslationTransformD2 self, itkVectorD2 vector) -> itkVectorD2
        BackTransform(itkTranslationTransformD2 self, vnl_vector_fixed< double,2 > const & vector) -> vnl_vector_fixed< double,2 >
        BackTransform(itkTranslationTransformD2 self, itkCovariantVectorD2 vector) -> itkCovariantVectorD2

        This method finds the
        point or vector that maps to a given point or vector under the affine
        transformation defined by self. If no such point exists, an exception
        is thrown. 
        """
        return _itkTranslationTransformPython.itkTranslationTransformD2_BackTransform(self, *args)


    def GetInverse(self, inverse: 'itkTranslationTransformD2') -> "bool":
        """
        GetInverse(itkTranslationTransformD2 self, itkTranslationTransformD2 inverse) -> bool

        Find inverse of an
        affine transformation. This method creates and returns a new
        TranslationTransform object which is the inverse of self. If self is
        not invertible, false is returned. 
        """
        return _itkTranslationTransformPython.itkTranslationTransformD2_GetInverse(self, inverse)


    def SetIdentity(self) -> "void":
        """
        SetIdentity(itkTranslationTransformD2 self)

        Set the parameters to
        the IdentityTransform 
        """
        return _itkTranslationTransformPython.itkTranslationTransformD2_SetIdentity(self)

    __swig_destroy__ = _itkTranslationTransformPython.delete_itkTranslationTransformD2

    def cast(obj: 'itkLightObject') -> "itkTranslationTransformD2 *":
        """cast(itkLightObject obj) -> itkTranslationTransformD2"""
        return _itkTranslationTransformPython.itkTranslationTransformD2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkTranslationTransformD2

        Create a new object of the class itkTranslationTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTranslationTransformD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTranslationTransformD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTranslationTransformD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkTranslationTransformD2.Clone = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD2_Clone, None, itkTranslationTransformD2)
itkTranslationTransformD2.GetOffset = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD2_GetOffset, None, itkTranslationTransformD2)
itkTranslationTransformD2.SetOffset = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD2_SetOffset, None, itkTranslationTransformD2)
itkTranslationTransformD2.Compose = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD2_Compose, None, itkTranslationTransformD2)
itkTranslationTransformD2.Translate = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD2_Translate, None, itkTranslationTransformD2)
itkTranslationTransformD2.TransformVector = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD2_TransformVector, None, itkTranslationTransformD2)
itkTranslationTransformD2.BackTransform = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD2_BackTransform, None, itkTranslationTransformD2)
itkTranslationTransformD2.GetInverse = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD2_GetInverse, None, itkTranslationTransformD2)
itkTranslationTransformD2.SetIdentity = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD2_SetIdentity, None, itkTranslationTransformD2)
itkTranslationTransformD2_swigregister = _itkTranslationTransformPython.itkTranslationTransformD2_swigregister
itkTranslationTransformD2_swigregister(itkTranslationTransformD2)

def itkTranslationTransformD2___New_orig__() -> "itkTranslationTransformD2_Pointer":
    """itkTranslationTransformD2___New_orig__() -> itkTranslationTransformD2_Pointer"""
    return _itkTranslationTransformPython.itkTranslationTransformD2___New_orig__()

def itkTranslationTransformD2_cast(obj: 'itkLightObject') -> "itkTranslationTransformD2 *":
    """itkTranslationTransformD2_cast(itkLightObject obj) -> itkTranslationTransformD2"""
    return _itkTranslationTransformPython.itkTranslationTransformD2_cast(obj)

class itkTranslationTransformD3(itkTransformBasePython.itkTransformD33):
    """


    Translation transformation of a vector space (e.g. space coordinates)

    The same functionality could be obtained by using the Affine
    transform, but with a large difference in performance.

    \\sphinx
    \\sphinxexample{Core/Transform/TranslateAVectorImage,Translate
    Vector Image} \\sphinxexample{Registration/Common/GlobalRegistration
    OfTwoImages,Global Registration Of Two Images}
    \\sphinxexample{Registration/Common/MutualInformation,Mutual
    Information} \\endsphinx

    C++ includes: itkTranslationTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkTranslationTransformD3_Pointer":
        """__New_orig__() -> itkTranslationTransformD3_Pointer"""
        return _itkTranslationTransformPython.itkTranslationTransformD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkTranslationTransformD3_Pointer":
        """Clone(itkTranslationTransformD3 self) -> itkTranslationTransformD3_Pointer"""
        return _itkTranslationTransformPython.itkTranslationTransformD3_Clone(self)


    def GetOffset(self) -> "itkVectorD3 const &":
        """
        GetOffset(itkTranslationTransformD3 self) -> itkVectorD3

        This method returns the
        value of the offset of the TranslationTransform. 
        """
        return _itkTranslationTransformPython.itkTranslationTransformD3_GetOffset(self)


    def SetOffset(self, offset: 'itkVectorD3') -> "void":
        """
        SetOffset(itkTranslationTransformD3 self, itkVectorD3 offset)

        Set offset of an
        Translation Transform. This method sets the offset of an
        TranslationTransform to a value specified by the user. 
        """
        return _itkTranslationTransformPython.itkTranslationTransformD3_SetOffset(self, offset)


    def Compose(self, other: 'itkTranslationTransformD3', pre: 'bool'=False) -> "void":
        """
        Compose(itkTranslationTransformD3 self, itkTranslationTransformD3 other, bool pre=False)
        Compose(itkTranslationTransformD3 self, itkTranslationTransformD3 other)

        Compose with another
        TranslationTransform. 
        """
        return _itkTranslationTransformPython.itkTranslationTransformD3_Compose(self, other, pre)


    def Translate(self, offset: 'itkVectorD3', pre: 'bool'=False) -> "void":
        """
        Translate(itkTranslationTransformD3 self, itkVectorD3 offset, bool pre=False)
        Translate(itkTranslationTransformD3 self, itkVectorD3 offset)

        Compose affine
        transformation with a translation. This method modifies self to
        include a translation of the origin. The translation is precomposed
        with self if pre is true, and postcomposed otherwise. 
        """
        return _itkTranslationTransformPython.itkTranslationTransformD3_Translate(self, offset, pre)


    def TransformVector(self, *args) -> "vnl_vector_fixed< double,3 >":
        """
        TransformVector(itkTranslationTransformD3 self, itkVectorD3 vector) -> itkVectorD3
        TransformVector(itkTranslationTransformD3 self, vnl_vector_fixed< double,3 > const & vector) -> vnl_vector_fixed< double,3 >

        Method to transform
        a vector stored in a VectorImage, at a point. For global transforms,
        point is ignored and TransformVector( vector ) is called. Local
        transforms (e.g. deformation field transform) must override and
        provide required behavior. 
        """
        return _itkTranslationTransformPython.itkTranslationTransformD3_TransformVector(self, *args)


    def BackTransform(self, *args) -> "itkCovariantVectorD3":
        """
        BackTransform(itkTranslationTransformD3 self, itkPointD3 point) -> itkPointD3
        BackTransform(itkTranslationTransformD3 self, itkVectorD3 vector) -> itkVectorD3
        BackTransform(itkTranslationTransformD3 self, vnl_vector_fixed< double,3 > const & vector) -> vnl_vector_fixed< double,3 >
        BackTransform(itkTranslationTransformD3 self, itkCovariantVectorD3 vector) -> itkCovariantVectorD3

        This method finds the
        point or vector that maps to a given point or vector under the affine
        transformation defined by self. If no such point exists, an exception
        is thrown. 
        """
        return _itkTranslationTransformPython.itkTranslationTransformD3_BackTransform(self, *args)


    def GetInverse(self, inverse: 'itkTranslationTransformD3') -> "bool":
        """
        GetInverse(itkTranslationTransformD3 self, itkTranslationTransformD3 inverse) -> bool

        Find inverse of an
        affine transformation. This method creates and returns a new
        TranslationTransform object which is the inverse of self. If self is
        not invertible, false is returned. 
        """
        return _itkTranslationTransformPython.itkTranslationTransformD3_GetInverse(self, inverse)


    def SetIdentity(self) -> "void":
        """
        SetIdentity(itkTranslationTransformD3 self)

        Set the parameters to
        the IdentityTransform 
        """
        return _itkTranslationTransformPython.itkTranslationTransformD3_SetIdentity(self)

    __swig_destroy__ = _itkTranslationTransformPython.delete_itkTranslationTransformD3

    def cast(obj: 'itkLightObject') -> "itkTranslationTransformD3 *":
        """cast(itkLightObject obj) -> itkTranslationTransformD3"""
        return _itkTranslationTransformPython.itkTranslationTransformD3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkTranslationTransformD3

        Create a new object of the class itkTranslationTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTranslationTransformD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTranslationTransformD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTranslationTransformD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkTranslationTransformD3.Clone = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD3_Clone, None, itkTranslationTransformD3)
itkTranslationTransformD3.GetOffset = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD3_GetOffset, None, itkTranslationTransformD3)
itkTranslationTransformD3.SetOffset = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD3_SetOffset, None, itkTranslationTransformD3)
itkTranslationTransformD3.Compose = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD3_Compose, None, itkTranslationTransformD3)
itkTranslationTransformD3.Translate = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD3_Translate, None, itkTranslationTransformD3)
itkTranslationTransformD3.TransformVector = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD3_TransformVector, None, itkTranslationTransformD3)
itkTranslationTransformD3.BackTransform = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD3_BackTransform, None, itkTranslationTransformD3)
itkTranslationTransformD3.GetInverse = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD3_GetInverse, None, itkTranslationTransformD3)
itkTranslationTransformD3.SetIdentity = new_instancemethod(_itkTranslationTransformPython.itkTranslationTransformD3_SetIdentity, None, itkTranslationTransformD3)
itkTranslationTransformD3_swigregister = _itkTranslationTransformPython.itkTranslationTransformD3_swigregister
itkTranslationTransformD3_swigregister(itkTranslationTransformD3)

def itkTranslationTransformD3___New_orig__() -> "itkTranslationTransformD3_Pointer":
    """itkTranslationTransformD3___New_orig__() -> itkTranslationTransformD3_Pointer"""
    return _itkTranslationTransformPython.itkTranslationTransformD3___New_orig__()

def itkTranslationTransformD3_cast(obj: 'itkLightObject') -> "itkTranslationTransformD3 *":
    """itkTranslationTransformD3_cast(itkLightObject obj) -> itkTranslationTransformD3"""
    return _itkTranslationTransformPython.itkTranslationTransformD3_cast(obj)



