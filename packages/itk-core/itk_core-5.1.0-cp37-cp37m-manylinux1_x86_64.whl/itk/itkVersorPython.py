# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkVersorPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkVersorPython', [dirname(__file__)])
        except ImportError:
            import _itkVersorPython
            return _itkVersorPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkVersorPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkVersorPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkVersorPython
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
import itkMatrixPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
class itkVersorD(object):
    """


    A templated class holding a unit quaternion.

    Versor is a templated class that holds a unit quaternion. The
    difference between versors and quaternions is that quaternions can
    represent rotations and scale changes while versors are limited to
    rotations.

    This class only implements the operations that maintain versors as a
    group, that is, any operations between versors result in another
    versor. For this reason, addition is not defined in this class, even
    though it is a valid operation between quaternions.

    See:   Vector

    See:   Point

    See:   CovariantVector

    See:   Matrix

    C++ includes: itkVersor.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def GetVnlQuaternion(self) -> "vnl_quaternion< double >":
        """
        GetVnlQuaternion(itkVersorD self) -> vnl_quaternion< double >

        Get a
        vnl_quaternion with a copy of the internal memory block. 
        """
        return _itkVersorPython.itkVersorD_GetVnlQuaternion(self)


    def __init__(self, *args):
        """
        __init__(itkVersorD self) -> itkVersorD
        __init__(itkVersorD self, itkVersorD v) -> itkVersorD



        A templated class holding a unit quaternion.

        Versor is a templated class that holds a unit quaternion. The
        difference between versors and quaternions is that quaternions can
        represent rotations and scale changes while versors are limited to
        rotations.

        This class only implements the operations that maintain versors as a
        group, that is, any operations between versors result in another
        versor. For this reason, addition is not defined in this class, even
        though it is a valid operation between quaternions.

        See:   Vector

        See:   Point

        See:   CovariantVector

        See:   Matrix

        C++ includes: itkVersor.h 
        """
        _itkVersorPython.itkVersorD_swiginit(self, _itkVersorPython.new_itkVersorD(*args))

    def __imul__(self, v: 'itkVersorD') -> "itkVersorD const &":
        """__imul__(itkVersorD self, itkVersorD v) -> itkVersorD"""
        return _itkVersorPython.itkVersorD___imul__(self, v)


    def __idiv__(self, v: 'itkVersorD') -> "itkVersorD const &":
        """__idiv__(itkVersorD self, itkVersorD v) -> itkVersorD"""
        return _itkVersorPython.itkVersorD___idiv__(self, v)


    def GetTensor(self) -> "double":
        """
        GetTensor(itkVersorD self) -> double

        Get Tensor part of the
        Versor. Given that Versors are normalized quaternions this value is
        expected to be 1.0 always 
        """
        return _itkVersorPython.itkVersorD_GetTensor(self)


    def Normalize(self) -> "void":
        """
        Normalize(itkVersorD self)

        Normalize the Versor.
        Given that Versors are normalized quaternions this method is provided
        only for convenience when it is suspected that a versor could be out
        of the unit sphere. 
        """
        return _itkVersorPython.itkVersorD_Normalize(self)


    def GetConjugate(self) -> "itkVersorD":
        """
        GetConjugate(itkVersorD self) -> itkVersorD

        Get Conjugate versor.
        Returns the versor that produce a rotation by the same angle but in
        opposite direction. 
        """
        return _itkVersorPython.itkVersorD_GetConjugate(self)


    def GetReciprocal(self) -> "itkVersorD":
        """
        GetReciprocal(itkVersorD self) -> itkVersorD

        Get Reciprocal
        versor. Returns the versor that composed with this one will result in
        a scalar operator equals to 1. It is also equivalent to 1/this. 
        """
        return _itkVersorPython.itkVersorD_GetReciprocal(self)


    def __mul__(self, vec: 'itkVersorD') -> "itkVersorD":
        """__mul__(itkVersorD self, itkVersorD vec) -> itkVersorD"""
        return _itkVersorPython.itkVersorD___mul__(self, vec)


    def __div__(self, vec: 'itkVersorD') -> "itkVersorD":
        """__div__(itkVersorD self, itkVersorD vec) -> itkVersorD"""
        return _itkVersorPython.itkVersorD___div__(self, vec)


    def __eq__(self, vec: 'itkVersorD') -> "bool":
        """__eq__(itkVersorD self, itkVersorD vec) -> bool"""
        return _itkVersorPython.itkVersorD___eq__(self, vec)


    def __ne__(self, vec: 'itkVersorD') -> "bool":
        """__ne__(itkVersorD self, itkVersorD vec) -> bool"""
        return _itkVersorPython.itkVersorD___ne__(self, vec)


    def GetScalar(self) -> "double":
        """
        GetScalar(itkVersorD self) -> double

        Returns the Scalar part.

        """
        return _itkVersorPython.itkVersorD_GetScalar(self)


    def GetX(self) -> "double":
        """
        GetX(itkVersorD self) -> double

        Returns the X component. 
        """
        return _itkVersorPython.itkVersorD_GetX(self)


    def GetY(self) -> "double":
        """
        GetY(itkVersorD self) -> double

        Returns the Y component. 
        """
        return _itkVersorPython.itkVersorD_GetY(self)


    def GetZ(self) -> "double":
        """
        GetZ(itkVersorD self) -> double

        Returns the Z component. 
        """
        return _itkVersorPython.itkVersorD_GetZ(self)


    def GetW(self) -> "double":
        """
        GetW(itkVersorD self) -> double

        Returns the W component. 
        """
        return _itkVersorPython.itkVersorD_GetW(self)


    def GetAngle(self) -> "double":
        """
        GetAngle(itkVersorD self) -> double

        Returns the rotation angle
        in radians. 
        """
        return _itkVersorPython.itkVersorD_GetAngle(self)


    def GetAxis(self) -> "itkVectorD3":
        """
        GetAxis(itkVersorD self) -> itkVectorD3

        Returns the axis of the
        rotation. It is a unit vector parallel to the axis. 
        """
        return _itkVersorPython.itkVersorD_GetAxis(self)


    def GetRight(self) -> "itkVectorD3":
        """
        GetRight(itkVersorD self) -> itkVectorD3

        Returns the Right part It
        is a vector part of the Versor. It is called Right because it is
        equivalent to a right angle rotation. 
        """
        return _itkVersorPython.itkVersorD_GetRight(self)


    def Set(self, *args) -> "void":
        """
        Set(itkVersorD self, vnl_quaternion< double > const & arg0)
        Set(itkVersorD self, double x, double y, double z, double w)
        Set(itkVersorD self, itkVectorD3 axis, double angle)
        Set(itkVersorD self, itkMatrixD33 m)
        Set(itkVersorD self, itkVectorD3 axis)

        Set the versor using the right
        part. the magnitude of the vector given is assumed to be equal to
        std::sin(angle/2). This method will compute internally the scalar part
        that preserve the Versor as a unit quaternion. 
        """
        return _itkVersorPython.itkVersorD_Set(self, *args)


    def SetRotationAroundX(self, angle: 'double') -> "void":
        """
        SetRotationAroundX(itkVersorD self, double angle)

        Sets a rotation
        around the X axis using the parameter as angle in radians. This is a
        method provided for convenience to initialize a rotation. The effect
        of this methods is not cumulative with any value previously stored in
        the Versor. See:   Set

        See:   SetRotationAroundY

        See:   SetRotationAroundZ 
        """
        return _itkVersorPython.itkVersorD_SetRotationAroundX(self, angle)


    def SetRotationAroundY(self, angle: 'double') -> "void":
        """
        SetRotationAroundY(itkVersorD self, double angle)

        Sets a rotation
        around the Y axis using the parameter as angle in radians. This is a
        method provided for convenience to initialize a rotation. The effect
        of this methods is not cumulative with any value previously stored in
        the Versor. See:   Set

        See:   SetRotationAroundX

        See:   SetRotationAroundZ 
        """
        return _itkVersorPython.itkVersorD_SetRotationAroundY(self, angle)


    def SetRotationAroundZ(self, angle: 'double') -> "void":
        """
        SetRotationAroundZ(itkVersorD self, double angle)

        Sets a rotation
        around the Y axis using the parameter as angle in radians. This is a
        method provided for convenience to initialize a rotation. The effect
        of this methods is not cumulative with any value previously stored in
        the Versor. See:   Set

        See:   SetRotationAroundX

        See:   SetRotationAroundY 
        """
        return _itkVersorPython.itkVersorD_SetRotationAroundZ(self, angle)


    def SetIdentity(self) -> "void":
        """
        SetIdentity(itkVersorD self)

        Reset the values so the
        versor is equivalent to an identity transformation. This is equivalent
        to set a zero angle 
        """
        return _itkVersorPython.itkVersorD_SetIdentity(self)


    def Transform(self, *args) -> "vnl_vector_fixed< double,3 >":
        """
        Transform(itkVersorD self, itkVectorD3 v) -> itkVectorD3
        Transform(itkVersorD self, itkCovariantVectorD3 v) -> itkCovariantVectorD3
        Transform(itkVersorD self, itkPointD3 v) -> itkPointD3
        Transform(itkVersorD self, vnl_vector_fixed< double,3 > const & v) -> vnl_vector_fixed< double,3 >

        Transform a vnl_vector.

        """
        return _itkVersorPython.itkVersorD_Transform(self, *args)


    def GetMatrix(self) -> "itkMatrixD33":
        """
        GetMatrix(itkVersorD self) -> itkMatrixD33

        Get the matrix
        representation. 
        """
        return _itkVersorPython.itkVersorD_GetMatrix(self)


    def SquareRoot(self) -> "itkVersorD":
        """
        SquareRoot(itkVersorD self) -> itkVersorD

        Get the Square root of
        the unit quaternion. 
        """
        return _itkVersorPython.itkVersorD_SquareRoot(self)


    def Exponential(self, exponent: 'double') -> "itkVersorD":
        """
        Exponential(itkVersorD self, double exponent) -> itkVersorD

        Compute the Exponential
        of the unit quaternion Exponentiation by a factor is equivalent to
        multiplication of the rotation angle of the quaternion. 
        """
        return _itkVersorPython.itkVersorD_Exponential(self, exponent)

    __swig_destroy__ = _itkVersorPython.delete_itkVersorD
itkVersorD.GetVnlQuaternion = new_instancemethod(_itkVersorPython.itkVersorD_GetVnlQuaternion, None, itkVersorD)
itkVersorD.__imul__ = new_instancemethod(_itkVersorPython.itkVersorD___imul__, None, itkVersorD)
itkVersorD.__idiv__ = new_instancemethod(_itkVersorPython.itkVersorD___idiv__, None, itkVersorD)
itkVersorD.GetTensor = new_instancemethod(_itkVersorPython.itkVersorD_GetTensor, None, itkVersorD)
itkVersorD.Normalize = new_instancemethod(_itkVersorPython.itkVersorD_Normalize, None, itkVersorD)
itkVersorD.GetConjugate = new_instancemethod(_itkVersorPython.itkVersorD_GetConjugate, None, itkVersorD)
itkVersorD.GetReciprocal = new_instancemethod(_itkVersorPython.itkVersorD_GetReciprocal, None, itkVersorD)
itkVersorD.__mul__ = new_instancemethod(_itkVersorPython.itkVersorD___mul__, None, itkVersorD)
itkVersorD.__div__ = new_instancemethod(_itkVersorPython.itkVersorD___div__, None, itkVersorD)
itkVersorD.__eq__ = new_instancemethod(_itkVersorPython.itkVersorD___eq__, None, itkVersorD)
itkVersorD.__ne__ = new_instancemethod(_itkVersorPython.itkVersorD___ne__, None, itkVersorD)
itkVersorD.GetScalar = new_instancemethod(_itkVersorPython.itkVersorD_GetScalar, None, itkVersorD)
itkVersorD.GetX = new_instancemethod(_itkVersorPython.itkVersorD_GetX, None, itkVersorD)
itkVersorD.GetY = new_instancemethod(_itkVersorPython.itkVersorD_GetY, None, itkVersorD)
itkVersorD.GetZ = new_instancemethod(_itkVersorPython.itkVersorD_GetZ, None, itkVersorD)
itkVersorD.GetW = new_instancemethod(_itkVersorPython.itkVersorD_GetW, None, itkVersorD)
itkVersorD.GetAngle = new_instancemethod(_itkVersorPython.itkVersorD_GetAngle, None, itkVersorD)
itkVersorD.GetAxis = new_instancemethod(_itkVersorPython.itkVersorD_GetAxis, None, itkVersorD)
itkVersorD.GetRight = new_instancemethod(_itkVersorPython.itkVersorD_GetRight, None, itkVersorD)
itkVersorD.Set = new_instancemethod(_itkVersorPython.itkVersorD_Set, None, itkVersorD)
itkVersorD.SetRotationAroundX = new_instancemethod(_itkVersorPython.itkVersorD_SetRotationAroundX, None, itkVersorD)
itkVersorD.SetRotationAroundY = new_instancemethod(_itkVersorPython.itkVersorD_SetRotationAroundY, None, itkVersorD)
itkVersorD.SetRotationAroundZ = new_instancemethod(_itkVersorPython.itkVersorD_SetRotationAroundZ, None, itkVersorD)
itkVersorD.SetIdentity = new_instancemethod(_itkVersorPython.itkVersorD_SetIdentity, None, itkVersorD)
itkVersorD.Transform = new_instancemethod(_itkVersorPython.itkVersorD_Transform, None, itkVersorD)
itkVersorD.GetMatrix = new_instancemethod(_itkVersorPython.itkVersorD_GetMatrix, None, itkVersorD)
itkVersorD.SquareRoot = new_instancemethod(_itkVersorPython.itkVersorD_SquareRoot, None, itkVersorD)
itkVersorD.Exponential = new_instancemethod(_itkVersorPython.itkVersorD_Exponential, None, itkVersorD)
itkVersorD_swigregister = _itkVersorPython.itkVersorD_swigregister
itkVersorD_swigregister(itkVersorD)



