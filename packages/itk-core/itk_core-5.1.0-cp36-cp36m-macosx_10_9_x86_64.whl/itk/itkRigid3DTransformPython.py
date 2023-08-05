# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkRigid3DTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkRigid3DTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkRigid3DTransformPython
            return _itkRigid3DTransformPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkRigid3DTransformPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkRigid3DTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkRigid3DTransformPython
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
import itkMatrixOffsetTransformBasePython
import itkCovariantVectorPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkVectorPython
import vnl_matrix_fixedPython
import itkPointPython
import itkOptimizerParametersPython
import itkArrayPython
import itkMatrixPython
import itkSymmetricSecondRankTensorPython
import itkArray2DPython
import itkVariableLengthVectorPython
import itkDiffusionTensor3DPython
import itkTransformBasePython

def itkRigid3DTransformD_New():
  return itkRigid3DTransformD.New()

class itkRigid3DTransformD(itkMatrixOffsetTransformBasePython.itkMatrixOffsetTransformBaseD33):
    """


    Rigid3DTransform of a vector space (e.g. space coordinates)

    This transform applies a rotation and translation in 3D space. The
    transform is specified as a rotation matrix around a arbitrary center
    and is followed by a translation.

    The parameters for this transform can be set either using individual
    Set methods or in serialized form using SetParameters() and
    SetFixedParameters().

    The serialization of the optimizable parameters is an array of 12
    elements. The first 9 parameters represents the rotation matrix in
    row-major order (where the column index varies the fastest). The last
    3 parameters defines the translation in each dimension.

    The serialization of the fixed parameters is an array of 3 elements
    defining the center of rotation in each dimension.

    The Rigid3DTransform is intended to be a base class that defines a
    consistent family of transform types that respect rigid
    transformations. Only classes that derive from Rigid3DTransform should
    be used.

    See:   Euler3DTransform

    See:   QuaternionRigidTransform

    See:   VersorTransform

    C++ includes: itkRigid3DTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkRigid3DTransformD_Pointer":
        """__New_orig__() -> itkRigid3DTransformD_Pointer"""
        return _itkRigid3DTransformPython.itkRigid3DTransformD___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkRigid3DTransformD_Pointer":
        """Clone(itkRigid3DTransformD self) -> itkRigid3DTransformD_Pointer"""
        return _itkRigid3DTransformPython.itkRigid3DTransformD_Clone(self)


    def SetMatrix(self, *args) -> "void":
        """
        SetMatrix(itkRigid3DTransformD self, itkMatrixD33 matrix)
        SetMatrix(itkRigid3DTransformD self, itkMatrixD33 matrix, double const tolerance)

        Directly set the rotation
        matrix of the transform. WARNING:  The input matrix must be orthogonal
        to within the specified tolerance, else an exception is thrown.

        See:   MatrixOffsetTransformBase::SetMatrix() 
        """
        return _itkRigid3DTransformPython.itkRigid3DTransformD_SetMatrix(self, *args)


    def Translate(self, offset: 'itkVectorD3', pre: 'bool'=False) -> "void":
        """
        Translate(itkRigid3DTransformD self, itkVectorD3 offset, bool pre=False)
        Translate(itkRigid3DTransformD self, itkVectorD3 offset)

        Compose the
        transformation with a translation

        This method modifies self to include a translation of the origin. The
        translation is precomposed with self if pre is true, and postcomposed
        otherwise. 
        """
        return _itkRigid3DTransformPython.itkRigid3DTransformD_Translate(self, offset, pre)


    def MatrixIsOrthogonal(self, *args) -> "bool":
        """
        MatrixIsOrthogonal(itkRigid3DTransformD self, itkMatrixD33 matrix, double const tolerance) -> bool
        MatrixIsOrthogonal(itkRigid3DTransformD self, itkMatrixD33 matrix) -> bool

        Utility function
        to test if a matrix is orthogonal within a specified tolerance 
        """
        return _itkRigid3DTransformPython.itkRigid3DTransformD_MatrixIsOrthogonal(self, *args)

    __swig_destroy__ = _itkRigid3DTransformPython.delete_itkRigid3DTransformD

    def cast(obj: 'itkLightObject') -> "itkRigid3DTransformD *":
        """cast(itkLightObject obj) -> itkRigid3DTransformD"""
        return _itkRigid3DTransformPython.itkRigid3DTransformD_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkRigid3DTransformD

        Create a new object of the class itkRigid3DTransformD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRigid3DTransformD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRigid3DTransformD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRigid3DTransformD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRigid3DTransformD.Clone = new_instancemethod(_itkRigid3DTransformPython.itkRigid3DTransformD_Clone, None, itkRigid3DTransformD)
itkRigid3DTransformD.SetMatrix = new_instancemethod(_itkRigid3DTransformPython.itkRigid3DTransformD_SetMatrix, None, itkRigid3DTransformD)
itkRigid3DTransformD.Translate = new_instancemethod(_itkRigid3DTransformPython.itkRigid3DTransformD_Translate, None, itkRigid3DTransformD)
itkRigid3DTransformD.MatrixIsOrthogonal = new_instancemethod(_itkRigid3DTransformPython.itkRigid3DTransformD_MatrixIsOrthogonal, None, itkRigid3DTransformD)
itkRigid3DTransformD_swigregister = _itkRigid3DTransformPython.itkRigid3DTransformD_swigregister
itkRigid3DTransformD_swigregister(itkRigid3DTransformD)

def itkRigid3DTransformD___New_orig__() -> "itkRigid3DTransformD_Pointer":
    """itkRigid3DTransformD___New_orig__() -> itkRigid3DTransformD_Pointer"""
    return _itkRigid3DTransformPython.itkRigid3DTransformD___New_orig__()

def itkRigid3DTransformD_cast(obj: 'itkLightObject') -> "itkRigid3DTransformD *":
    """itkRigid3DTransformD_cast(itkLightObject obj) -> itkRigid3DTransformD"""
    return _itkRigid3DTransformPython.itkRigid3DTransformD_cast(obj)



