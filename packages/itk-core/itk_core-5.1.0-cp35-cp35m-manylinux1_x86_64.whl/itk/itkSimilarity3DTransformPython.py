# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkSimilarity3DTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkSimilarity3DTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkSimilarity3DTransformPython
            return _itkSimilarity3DTransformPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkSimilarity3DTransformPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkSimilarity3DTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkSimilarity3DTransformPython
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


import itkMatrixPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import pyBasePython
import itkPointPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkVectorPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkArray2DPython
import ITKCommonBasePython
import itkVersorRigid3DTransformPython
import itkVersorTransformPython
import itkRigid3DTransformPython
import itkMatrixOffsetTransformBasePython
import itkSymmetricSecondRankTensorPython
import itkDiffusionTensor3DPython
import itkVariableLengthVectorPython
import itkTransformBasePython
import itkArrayPython
import itkOptimizerParametersPython
import itkVersorPython

def itkSimilarity3DTransformD_New():
  return itkSimilarity3DTransformD.New()

class itkSimilarity3DTransformD(itkVersorRigid3DTransformPython.itkVersorRigid3DTransformD):
    """


    Similarity3DTransform of a vector space (e.g. space coordinates)

    This transform applies a rotation, translation and isotropic scaling
    to the space.

    The parameters for this transform can be set either using individual
    Set methods or in serialized form using SetParameters() and
    SetFixedParameters().

    The serialization of the optimizable parameters is an array of 7
    elements. The first 3 elements are the components of the versor
    representation of 3D rotation. The next 3 parameters defines the
    translation in each dimension. The last parameter defines the
    isotropic scaling.

    The serialization of the fixed parameters is an array of 3 elements
    defining the center of rotation.

    See:   VersorRigid3DTransform

    C++ includes: itkSimilarity3DTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSimilarity3DTransformD_Pointer":
        """__New_orig__() -> itkSimilarity3DTransformD_Pointer"""
        return _itkSimilarity3DTransformPython.itkSimilarity3DTransformD___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSimilarity3DTransformD_Pointer":
        """Clone(itkSimilarity3DTransformD self) -> itkSimilarity3DTransformD_Pointer"""
        return _itkSimilarity3DTransformPython.itkSimilarity3DTransformD_Clone(self)


    def SetMatrix(self, *args) -> "void":
        """
        SetMatrix(itkSimilarity3DTransformD self, itkMatrixD33 matrix)
        SetMatrix(itkSimilarity3DTransformD self, itkMatrixD33 matrix, double const tolerance)

        Directly set the rotation
        matrix of the transform.

        WARNING:  The input matrix must be orthogonal with isotropic scaling
        to within the specified tolerance, else an exception is thrown.

        See:   MatrixOffsetTransformBase::SetMatrix() 
        """
        return _itkSimilarity3DTransformPython.itkSimilarity3DTransformD_SetMatrix(self, *args)


    def SetScale(self, scale: 'double') -> "void":
        """
        SetScale(itkSimilarity3DTransformD self, double scale)

        Set/Get the value of the
        isotropic scaling factor 
        """
        return _itkSimilarity3DTransformPython.itkSimilarity3DTransformD_SetScale(self, scale)


    def GetScale(self) -> "double const &":
        """GetScale(itkSimilarity3DTransformD self) -> double const &"""
        return _itkSimilarity3DTransformPython.itkSimilarity3DTransformD_GetScale(self)

    __swig_destroy__ = _itkSimilarity3DTransformPython.delete_itkSimilarity3DTransformD

    def cast(obj: 'itkLightObject') -> "itkSimilarity3DTransformD *":
        """cast(itkLightObject obj) -> itkSimilarity3DTransformD"""
        return _itkSimilarity3DTransformPython.itkSimilarity3DTransformD_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkSimilarity3DTransformD

        Create a new object of the class itkSimilarity3DTransformD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSimilarity3DTransformD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSimilarity3DTransformD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSimilarity3DTransformD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSimilarity3DTransformD.Clone = new_instancemethod(_itkSimilarity3DTransformPython.itkSimilarity3DTransformD_Clone, None, itkSimilarity3DTransformD)
itkSimilarity3DTransformD.SetMatrix = new_instancemethod(_itkSimilarity3DTransformPython.itkSimilarity3DTransformD_SetMatrix, None, itkSimilarity3DTransformD)
itkSimilarity3DTransformD.SetScale = new_instancemethod(_itkSimilarity3DTransformPython.itkSimilarity3DTransformD_SetScale, None, itkSimilarity3DTransformD)
itkSimilarity3DTransformD.GetScale = new_instancemethod(_itkSimilarity3DTransformPython.itkSimilarity3DTransformD_GetScale, None, itkSimilarity3DTransformD)
itkSimilarity3DTransformD_swigregister = _itkSimilarity3DTransformPython.itkSimilarity3DTransformD_swigregister
itkSimilarity3DTransformD_swigregister(itkSimilarity3DTransformD)

def itkSimilarity3DTransformD___New_orig__() -> "itkSimilarity3DTransformD_Pointer":
    """itkSimilarity3DTransformD___New_orig__() -> itkSimilarity3DTransformD_Pointer"""
    return _itkSimilarity3DTransformPython.itkSimilarity3DTransformD___New_orig__()

def itkSimilarity3DTransformD_cast(obj: 'itkLightObject') -> "itkSimilarity3DTransformD *":
    """itkSimilarity3DTransformD_cast(itkLightObject obj) -> itkSimilarity3DTransformD"""
    return _itkSimilarity3DTransformPython.itkSimilarity3DTransformD_cast(obj)



