# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkIdentityTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkIdentityTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkIdentityTransformPython
            return _itkIdentityTransformPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkIdentityTransformPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkIdentityTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkIdentityTransformPython
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


import itkPointPython
import vnl_vector_refPython
import stdcomplexPython
import pyBasePython
import vnl_vectorPython
import vnl_matrixPython
import itkFixedArrayPython
import itkVectorPython
import itkCovariantVectorPython
import ITKCommonBasePython
import vnl_matrix_fixedPython
import itkOptimizerParametersPython
import itkArrayPython
import itkTransformBasePython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import itkVariableLengthVectorPython
import itkArray2DPython

def itkIdentityTransformD3_New():
  return itkIdentityTransformD3.New()


def itkIdentityTransformD2_New():
  return itkIdentityTransformD2.New()

class itkIdentityTransformD2(itkTransformBasePython.itkTransformD22):
    """


    Implementation of an Identity Transform.

    This class defines the generic interface for an Identity Transform.

    It will map every point to itself, every vector to itself and every
    covariant vector to itself.

    This class is intended to be used primarily as a default Transform for
    initializing those classes supporting a generic Transform.

    This class is templated over the Representation type for coordinates
    (that is the type used for representing the components of points and
    vectors) and over the dimension of the space. In this case the Input
    and Output spaces are the same so only one dimension is required.

    C++ includes: itkIdentityTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkIdentityTransformD2_Pointer":
        """__New_orig__() -> itkIdentityTransformD2_Pointer"""
        return _itkIdentityTransformPython.itkIdentityTransformD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkIdentityTransformD2_Pointer":
        """Clone(itkIdentityTransformD2 self) -> itkIdentityTransformD2_Pointer"""
        return _itkIdentityTransformPython.itkIdentityTransformD2_Clone(self)


    def TransformVector(self, *args) -> "vnl_vector_fixed< double,2 >":
        """
        TransformVector(itkIdentityTransformD2 self, itkVectorD2 vector) -> itkVectorD2
        TransformVector(itkIdentityTransformD2 self, vnl_vector_fixed< double,2 > const & vector) -> vnl_vector_fixed< double,2 >

        Method to transform
        a vnl_vector. 
        """
        return _itkIdentityTransformPython.itkIdentityTransformD2_TransformVector(self, *args)


    def SetIdentity(self) -> "void":
        """
        SetIdentity(itkIdentityTransformD2 self)

        Set the transformation
        to an Identity

        This is a nullptr operation in the case of this particular transform.
        The method is provided only to comply with the interface of other
        transforms. 
        """
        return _itkIdentityTransformPython.itkIdentityTransformD2_SetIdentity(self)


    def GetInverse(self, inverseTransform: 'itkIdentityTransformD2') -> "bool":
        """
        GetInverse(itkIdentityTransformD2 self, itkIdentityTransformD2 inverseTransform) -> bool

        Returns a boolean
        indicating whether it is possible or not to compute the inverse of
        this current Transform. If it is possible, then the inverse of the
        transform is returned in the inverseTransform variable passed by the
        user. The inverse is recomputed if this current transform has been
        modified. This method is intended to be overriden as needed by derived
        classes. 
        """
        return _itkIdentityTransformPython.itkIdentityTransformD2_GetInverse(self, inverseTransform)

    __swig_destroy__ = _itkIdentityTransformPython.delete_itkIdentityTransformD2

    def cast(obj: 'itkLightObject') -> "itkIdentityTransformD2 *":
        """cast(itkLightObject obj) -> itkIdentityTransformD2"""
        return _itkIdentityTransformPython.itkIdentityTransformD2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkIdentityTransformD2

        Create a new object of the class itkIdentityTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIdentityTransformD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIdentityTransformD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIdentityTransformD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkIdentityTransformD2.Clone = new_instancemethod(_itkIdentityTransformPython.itkIdentityTransformD2_Clone, None, itkIdentityTransformD2)
itkIdentityTransformD2.TransformVector = new_instancemethod(_itkIdentityTransformPython.itkIdentityTransformD2_TransformVector, None, itkIdentityTransformD2)
itkIdentityTransformD2.SetIdentity = new_instancemethod(_itkIdentityTransformPython.itkIdentityTransformD2_SetIdentity, None, itkIdentityTransformD2)
itkIdentityTransformD2.GetInverse = new_instancemethod(_itkIdentityTransformPython.itkIdentityTransformD2_GetInverse, None, itkIdentityTransformD2)
itkIdentityTransformD2_swigregister = _itkIdentityTransformPython.itkIdentityTransformD2_swigregister
itkIdentityTransformD2_swigregister(itkIdentityTransformD2)

def itkIdentityTransformD2___New_orig__() -> "itkIdentityTransformD2_Pointer":
    """itkIdentityTransformD2___New_orig__() -> itkIdentityTransformD2_Pointer"""
    return _itkIdentityTransformPython.itkIdentityTransformD2___New_orig__()

def itkIdentityTransformD2_cast(obj: 'itkLightObject') -> "itkIdentityTransformD2 *":
    """itkIdentityTransformD2_cast(itkLightObject obj) -> itkIdentityTransformD2"""
    return _itkIdentityTransformPython.itkIdentityTransformD2_cast(obj)

class itkIdentityTransformD3(itkTransformBasePython.itkTransformD33):
    """


    Implementation of an Identity Transform.

    This class defines the generic interface for an Identity Transform.

    It will map every point to itself, every vector to itself and every
    covariant vector to itself.

    This class is intended to be used primarily as a default Transform for
    initializing those classes supporting a generic Transform.

    This class is templated over the Representation type for coordinates
    (that is the type used for representing the components of points and
    vectors) and over the dimension of the space. In this case the Input
    and Output spaces are the same so only one dimension is required.

    C++ includes: itkIdentityTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkIdentityTransformD3_Pointer":
        """__New_orig__() -> itkIdentityTransformD3_Pointer"""
        return _itkIdentityTransformPython.itkIdentityTransformD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkIdentityTransformD3_Pointer":
        """Clone(itkIdentityTransformD3 self) -> itkIdentityTransformD3_Pointer"""
        return _itkIdentityTransformPython.itkIdentityTransformD3_Clone(self)


    def TransformVector(self, *args) -> "vnl_vector_fixed< double,3 >":
        """
        TransformVector(itkIdentityTransformD3 self, itkVectorD3 vector) -> itkVectorD3
        TransformVector(itkIdentityTransformD3 self, vnl_vector_fixed< double,3 > const & vector) -> vnl_vector_fixed< double,3 >

        Method to transform
        a vnl_vector. 
        """
        return _itkIdentityTransformPython.itkIdentityTransformD3_TransformVector(self, *args)


    def SetIdentity(self) -> "void":
        """
        SetIdentity(itkIdentityTransformD3 self)

        Set the transformation
        to an Identity

        This is a nullptr operation in the case of this particular transform.
        The method is provided only to comply with the interface of other
        transforms. 
        """
        return _itkIdentityTransformPython.itkIdentityTransformD3_SetIdentity(self)


    def GetInverse(self, inverseTransform: 'itkIdentityTransformD3') -> "bool":
        """
        GetInverse(itkIdentityTransformD3 self, itkIdentityTransformD3 inverseTransform) -> bool

        Returns a boolean
        indicating whether it is possible or not to compute the inverse of
        this current Transform. If it is possible, then the inverse of the
        transform is returned in the inverseTransform variable passed by the
        user. The inverse is recomputed if this current transform has been
        modified. This method is intended to be overriden as needed by derived
        classes. 
        """
        return _itkIdentityTransformPython.itkIdentityTransformD3_GetInverse(self, inverseTransform)

    __swig_destroy__ = _itkIdentityTransformPython.delete_itkIdentityTransformD3

    def cast(obj: 'itkLightObject') -> "itkIdentityTransformD3 *":
        """cast(itkLightObject obj) -> itkIdentityTransformD3"""
        return _itkIdentityTransformPython.itkIdentityTransformD3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkIdentityTransformD3

        Create a new object of the class itkIdentityTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkIdentityTransformD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkIdentityTransformD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkIdentityTransformD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkIdentityTransformD3.Clone = new_instancemethod(_itkIdentityTransformPython.itkIdentityTransformD3_Clone, None, itkIdentityTransformD3)
itkIdentityTransformD3.TransformVector = new_instancemethod(_itkIdentityTransformPython.itkIdentityTransformD3_TransformVector, None, itkIdentityTransformD3)
itkIdentityTransformD3.SetIdentity = new_instancemethod(_itkIdentityTransformPython.itkIdentityTransformD3_SetIdentity, None, itkIdentityTransformD3)
itkIdentityTransformD3.GetInverse = new_instancemethod(_itkIdentityTransformPython.itkIdentityTransformD3_GetInverse, None, itkIdentityTransformD3)
itkIdentityTransformD3_swigregister = _itkIdentityTransformPython.itkIdentityTransformD3_swigregister
itkIdentityTransformD3_swigregister(itkIdentityTransformD3)

def itkIdentityTransformD3___New_orig__() -> "itkIdentityTransformD3_Pointer":
    """itkIdentityTransformD3___New_orig__() -> itkIdentityTransformD3_Pointer"""
    return _itkIdentityTransformPython.itkIdentityTransformD3___New_orig__()

def itkIdentityTransformD3_cast(obj: 'itkLightObject') -> "itkIdentityTransformD3 *":
    """itkIdentityTransformD3_cast(itkLightObject obj) -> itkIdentityTransformD3"""
    return _itkIdentityTransformPython.itkIdentityTransformD3_cast(obj)



