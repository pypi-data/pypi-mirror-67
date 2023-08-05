# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkRigid2DTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkRigid2DTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkRigid2DTransformPython
            return _itkRigid2DTransformPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkRigid2DTransformPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkRigid2DTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkRigid2DTransformPython
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
import itkMatrixOffsetTransformBasePython

def itkRigid2DTransformD_New():
  return itkRigid2DTransformD.New()

class itkRigid2DTransformD(itkMatrixOffsetTransformBasePython.itkMatrixOffsetTransformBaseD22):
    """


    Rigid2DTransform of a vector space (e.g. space coordinates)

    This transform applies a rigid transformation in 2D space. The
    transform is specified as a rotation around a arbitrary center and is
    followed by a translation.

    The parameters for this transform can be set either using individual
    Set methods or in serialized form using SetParameters() and
    SetFixedParameters().

    The serialization of the optimizable parameters is an array of 3
    elements ordered as follows: p[0] = angle p[1] = x component of the
    translation p[2] = y component of the translation

    The serialization of the fixed parameters is an array of 2 elements
    ordered as follows: p[0] = x coordinate of the center p[1] = y
    coordinate of the center

    Access methods for the center, translation and underlying matrix
    offset vectors are documented in the superclass
    MatrixOffsetTransformBase.

    See:  Transfrom

    See:   MatrixOffsetTransformBase

    C++ includes: itkRigid2DTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkRigid2DTransformD_Pointer":
        """__New_orig__() -> itkRigid2DTransformD_Pointer"""
        return _itkRigid2DTransformPython.itkRigid2DTransformD___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkRigid2DTransformD_Pointer":
        """Clone(itkRigid2DTransformD self) -> itkRigid2DTransformD_Pointer"""
        return _itkRigid2DTransformPython.itkRigid2DTransformD_Clone(self)


    def SetMatrix(self, *args) -> "void":
        """
        SetMatrix(itkRigid2DTransformD self, itkMatrixD22 matrix)
        SetMatrix(itkRigid2DTransformD self, itkMatrixD22 matrix, double const tolerance)

        Set the rotation Matrix
        of a Rigid2D Transform

        This method sets the 2x2 matrix representing the rotation in the
        transform. The Matrix is expected to be orthogonal with a certain
        tolerance.

        WARNING:  This method will throw an exception is the matrix provided
        as argument is not orthogonal within the given tolerance.

        See:   MatrixOffsetTransformBase::SetMatrix() 
        """
        return _itkRigid2DTransformPython.itkRigid2DTransformD_SetMatrix(self, *args)


    def Translate(self, offset: 'itkVectorD2', pre: 'bool'=False) -> "void":
        """
        Translate(itkRigid2DTransformD self, itkVectorD2 offset, bool pre=False)
        Translate(itkRigid2DTransformD self, itkVectorD2 offset)

        Compose the
        transformation with a translation

        This method modifies self to include a translation of the origin. The
        translation is precomposed with self if pre is true, and postcomposed
        otherwise. 
        """
        return _itkRigid2DTransformPython.itkRigid2DTransformD_Translate(self, offset, pre)


    def BackTransform(self, *args) -> "itkCovariantVectorD2":
        """
        BackTransform(itkRigid2DTransformD self, itkPointD2 point) -> itkPointD2
        BackTransform(itkRigid2DTransformD self, itkVectorD2 vector) -> itkVectorD2
        BackTransform(itkRigid2DTransformD self, vnl_vector_fixed< double,2 > const & vector) -> vnl_vector_fixed< double,2 >
        BackTransform(itkRigid2DTransformD self, itkCovariantVectorD2 vector) -> itkCovariantVectorD2

        Back transform by an
        rigid transformation.

        The BackTransform() methods are slated to be removed from ITK.
        Instead, please use GetInverse() or CloneInverseTo() to generate an
        inverse transform and then perform the transform using that inverted
        transform. 
        """
        return _itkRigid2DTransformPython.itkRigid2DTransformD_BackTransform(self, *args)


    def SetAngle(self, angle: 'double') -> "void":
        """
        SetAngle(itkRigid2DTransformD self, double angle)

        Set/Get the angle of
        rotation in radians 
        """
        return _itkRigid2DTransformPython.itkRigid2DTransformD_SetAngle(self, angle)


    def GetAngle(self) -> "double const &":
        """GetAngle(itkRigid2DTransformD self) -> double const &"""
        return _itkRigid2DTransformPython.itkRigid2DTransformD_GetAngle(self)


    def SetAngleInDegrees(self, angle: 'double') -> "void":
        """
        SetAngleInDegrees(itkRigid2DTransformD self, double angle)

        Set the angle of
        rotation in degrees. 
        """
        return _itkRigid2DTransformPython.itkRigid2DTransformD_SetAngleInDegrees(self, angle)


    def SetRotation(self, angle: 'double') -> "void":
        """
        SetRotation(itkRigid2DTransformD self, double angle)

        Set/Get the angle of
        rotation in radians. These methods are old and are retained for
        backward compatibility. Instead, use SetAngle() and GetAngle(). 
        """
        return _itkRigid2DTransformPython.itkRigid2DTransformD_SetRotation(self, angle)


    def GetRotation(self) -> "double const &":
        """GetRotation(itkRigid2DTransformD self) -> double const &"""
        return _itkRigid2DTransformPython.itkRigid2DTransformD_GetRotation(self)


    def CloneInverseTo(self, newinverse: 'itkRigid2DTransformD_Pointer &') -> "void":
        """
        CloneInverseTo(itkRigid2DTransformD self, itkRigid2DTransformD_Pointer & newinverse)

        This method creates
        and returns a new Rigid2DTransform object which is the inverse of
        self. 
        """
        return _itkRigid2DTransformPython.itkRigid2DTransformD_CloneInverseTo(self, newinverse)


    def GetInverse(self, inverse: 'itkRigid2DTransformD') -> "bool":
        """
        GetInverse(itkRigid2DTransformD self, itkRigid2DTransformD inverse) -> bool

        Get an inverse of this
        transform. 
        """
        return _itkRigid2DTransformPython.itkRigid2DTransformD_GetInverse(self, inverse)


    def CloneTo(self, clone: 'itkRigid2DTransformD_Pointer &') -> "void":
        """
        CloneTo(itkRigid2DTransformD self, itkRigid2DTransformD_Pointer & clone)

        This method creates and
        returns a new Rigid2DTransform object which has the same parameters.

        """
        return _itkRigid2DTransformPython.itkRigid2DTransformD_CloneTo(self, clone)

    __swig_destroy__ = _itkRigid2DTransformPython.delete_itkRigid2DTransformD

    def cast(obj: 'itkLightObject') -> "itkRigid2DTransformD *":
        """cast(itkLightObject obj) -> itkRigid2DTransformD"""
        return _itkRigid2DTransformPython.itkRigid2DTransformD_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkRigid2DTransformD

        Create a new object of the class itkRigid2DTransformD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRigid2DTransformD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRigid2DTransformD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRigid2DTransformD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRigid2DTransformD.Clone = new_instancemethod(_itkRigid2DTransformPython.itkRigid2DTransformD_Clone, None, itkRigid2DTransformD)
itkRigid2DTransformD.SetMatrix = new_instancemethod(_itkRigid2DTransformPython.itkRigid2DTransformD_SetMatrix, None, itkRigid2DTransformD)
itkRigid2DTransformD.Translate = new_instancemethod(_itkRigid2DTransformPython.itkRigid2DTransformD_Translate, None, itkRigid2DTransformD)
itkRigid2DTransformD.BackTransform = new_instancemethod(_itkRigid2DTransformPython.itkRigid2DTransformD_BackTransform, None, itkRigid2DTransformD)
itkRigid2DTransformD.SetAngle = new_instancemethod(_itkRigid2DTransformPython.itkRigid2DTransformD_SetAngle, None, itkRigid2DTransformD)
itkRigid2DTransformD.GetAngle = new_instancemethod(_itkRigid2DTransformPython.itkRigid2DTransformD_GetAngle, None, itkRigid2DTransformD)
itkRigid2DTransformD.SetAngleInDegrees = new_instancemethod(_itkRigid2DTransformPython.itkRigid2DTransformD_SetAngleInDegrees, None, itkRigid2DTransformD)
itkRigid2DTransformD.SetRotation = new_instancemethod(_itkRigid2DTransformPython.itkRigid2DTransformD_SetRotation, None, itkRigid2DTransformD)
itkRigid2DTransformD.GetRotation = new_instancemethod(_itkRigid2DTransformPython.itkRigid2DTransformD_GetRotation, None, itkRigid2DTransformD)
itkRigid2DTransformD.CloneInverseTo = new_instancemethod(_itkRigid2DTransformPython.itkRigid2DTransformD_CloneInverseTo, None, itkRigid2DTransformD)
itkRigid2DTransformD.GetInverse = new_instancemethod(_itkRigid2DTransformPython.itkRigid2DTransformD_GetInverse, None, itkRigid2DTransformD)
itkRigid2DTransformD.CloneTo = new_instancemethod(_itkRigid2DTransformPython.itkRigid2DTransformD_CloneTo, None, itkRigid2DTransformD)
itkRigid2DTransformD_swigregister = _itkRigid2DTransformPython.itkRigid2DTransformD_swigregister
itkRigid2DTransformD_swigregister(itkRigid2DTransformD)

def itkRigid2DTransformD___New_orig__() -> "itkRigid2DTransformD_Pointer":
    """itkRigid2DTransformD___New_orig__() -> itkRigid2DTransformD_Pointer"""
    return _itkRigid2DTransformPython.itkRigid2DTransformD___New_orig__()

def itkRigid2DTransformD_cast(obj: 'itkLightObject') -> "itkRigid2DTransformD *":
    """itkRigid2DTransformD_cast(itkLightObject obj) -> itkRigid2DTransformD"""
    return _itkRigid2DTransformPython.itkRigid2DTransformD_cast(obj)



