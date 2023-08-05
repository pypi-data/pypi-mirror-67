# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkRigid3DPerspectiveTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkRigid3DPerspectiveTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkRigid3DPerspectiveTransformPython
            return _itkRigid3DPerspectiveTransformPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkRigid3DPerspectiveTransformPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkRigid3DPerspectiveTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkRigid3DPerspectiveTransformPython
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
import itkTransformBasePython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkFixedArrayPython
import itkMatrixPython
import vnl_matrixPython
import vnl_vectorPython
import stdcomplexPython
import itkVectorPython
import vnl_vector_refPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkPointPython
import itkVariableLengthVectorPython
import itkOptimizerParametersPython
import itkArrayPython
import itkArray2DPython
import itkVersorPython

def itkRigid3DPerspectiveTransformD_New():
  return itkRigid3DPerspectiveTransformD.New()

class itkRigid3DPerspectiveTransformD(itkTransformBasePython.itkTransformD32):
    """


    Rigid3DTramsform of a vector space (e.g. space coordinates)

    This transform applies a rotation and translation to the 3D space
    followed by a projection to 2D space along the Z axis.

    C++ includes: itkRigid3DPerspectiveTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkRigid3DPerspectiveTransformD_Pointer":
        """__New_orig__() -> itkRigid3DPerspectiveTransformD_Pointer"""
        return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkRigid3DPerspectiveTransformD_Pointer":
        """Clone(itkRigid3DPerspectiveTransformD self) -> itkRigid3DPerspectiveTransformD_Pointer"""
        return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_Clone(self)


    def GetOffset(self) -> "itkVectorD3 const &":
        """
        GetOffset(itkRigid3DPerspectiveTransformD self) -> itkVectorD3

        Get offset of an
        Rigid3DPerspectiveTransform This method returns the value of the
        offset of the Rigid3DPerspectiveTransform. 
        """
        return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_GetOffset(self)


    def GetRotation(self) -> "itkVersorD const &":
        """
        GetRotation(itkRigid3DPerspectiveTransformD self) -> itkVersorD

        Get rotation from an
        Rigid3DPerspectiveTransform. This method returns the value of the
        rotation of the Rigid3DPerspectiveTransform. 
        """
        return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_GetRotation(self)


    def SetOffset(self, offset: 'itkVectorD3') -> "void":
        """
        SetOffset(itkRigid3DPerspectiveTransformD self, itkVectorD3 offset)

        This method sets the
        offset of an Rigid3DPerspectiveTransform to a value specified by the
        user. 
        """
        return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_SetOffset(self, offset)


    def SetRotation(self, *args) -> "void":
        """
        SetRotation(itkRigid3DPerspectiveTransformD self, itkVersorD rotation)
        SetRotation(itkRigid3DPerspectiveTransformD self, itkVectorD3 axis, double angle)

        Set Rotation of the
        Rigid transform. This method sets the rotation of an Rigid3DTransform
        to a value specified by the user using the axis of rotation an the
        angle. 
        """
        return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_SetRotation(self, *args)


    def SetFocalDistance(self, focalDistance: 'double') -> "void":
        """
        SetFocalDistance(itkRigid3DPerspectiveTransformD self, double focalDistance)

        Set the Focal
        Distance of the projection This method sets the focal distance for the
        perspective projection to a value specified by the user. 
        """
        return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_SetFocalDistance(self, focalDistance)


    def GetFocalDistance(self) -> "double":
        """
        GetFocalDistance(itkRigid3DPerspectiveTransformD self) -> double

        Return the Focal
        Distance 
        """
        return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_GetFocalDistance(self)


    def TransformVector(self, *args) -> "vnl_vector_fixed< double,2 >":
        """
        TransformVector(itkRigid3DPerspectiveTransformD self, itkVectorD3 arg0) -> itkVectorD2
        TransformVector(itkRigid3DPerspectiveTransformD self, vnl_vector_fixed< double,3 > const & arg0) -> vnl_vector_fixed< double,2 >

        Method to transform
        a vector stored in a VectorImage, at a point. For global transforms,
        point is ignored and TransformVector( vector ) is called. Local
        transforms (e.g. deformation field transform) must override and
        provide required behavior. 
        """
        return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_TransformVector(self, *args)


    def GetRotationMatrix(self) -> "itkMatrixD33 const &":
        """
        GetRotationMatrix(itkRigid3DPerspectiveTransformD self) -> itkMatrixD33

        Return the
        rotation matrix 
        """
        return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_GetRotationMatrix(self)


    def ComputeMatrix(self) -> "void":
        """
        ComputeMatrix(itkRigid3DPerspectiveTransformD self)

        Compute the matrix.

        """
        return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_ComputeMatrix(self)


    def GetFixedOffset(self) -> "itkVectorD3 const &":
        """
        GetFixedOffset(itkRigid3DPerspectiveTransformD self) -> itkVectorD3

        Set a fixed offset:
        this allow to center the object to be transformed 
        """
        return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_GetFixedOffset(self)


    def SetFixedOffset(self, _arg: 'itkVectorD3') -> "void":
        """SetFixedOffset(itkRigid3DPerspectiveTransformD self, itkVectorD3 _arg)"""
        return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_SetFixedOffset(self, _arg)


    def SetCenterOfRotation(self, _arg: 'itkPointD3') -> "void":
        """
        SetCenterOfRotation(itkRigid3DPerspectiveTransformD self, itkPointD3 _arg)

        Set the center
        of Rotation 
        """
        return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_SetCenterOfRotation(self, _arg)


    def GetCenterOfRotation(self) -> "itkPointD3 const &":
        """GetCenterOfRotation(itkRigid3DPerspectiveTransformD self) -> itkPointD3"""
        return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_GetCenterOfRotation(self)

    __swig_destroy__ = _itkRigid3DPerspectiveTransformPython.delete_itkRigid3DPerspectiveTransformD

    def cast(obj: 'itkLightObject') -> "itkRigid3DPerspectiveTransformD *":
        """cast(itkLightObject obj) -> itkRigid3DPerspectiveTransformD"""
        return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkRigid3DPerspectiveTransformD

        Create a new object of the class itkRigid3DPerspectiveTransformD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRigid3DPerspectiveTransformD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRigid3DPerspectiveTransformD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRigid3DPerspectiveTransformD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkRigid3DPerspectiveTransformD.Clone = new_instancemethod(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_Clone, None, itkRigid3DPerspectiveTransformD)
itkRigid3DPerspectiveTransformD.GetOffset = new_instancemethod(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_GetOffset, None, itkRigid3DPerspectiveTransformD)
itkRigid3DPerspectiveTransformD.GetRotation = new_instancemethod(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_GetRotation, None, itkRigid3DPerspectiveTransformD)
itkRigid3DPerspectiveTransformD.SetOffset = new_instancemethod(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_SetOffset, None, itkRigid3DPerspectiveTransformD)
itkRigid3DPerspectiveTransformD.SetRotation = new_instancemethod(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_SetRotation, None, itkRigid3DPerspectiveTransformD)
itkRigid3DPerspectiveTransformD.SetFocalDistance = new_instancemethod(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_SetFocalDistance, None, itkRigid3DPerspectiveTransformD)
itkRigid3DPerspectiveTransformD.GetFocalDistance = new_instancemethod(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_GetFocalDistance, None, itkRigid3DPerspectiveTransformD)
itkRigid3DPerspectiveTransformD.TransformVector = new_instancemethod(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_TransformVector, None, itkRigid3DPerspectiveTransformD)
itkRigid3DPerspectiveTransformD.GetRotationMatrix = new_instancemethod(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_GetRotationMatrix, None, itkRigid3DPerspectiveTransformD)
itkRigid3DPerspectiveTransformD.ComputeMatrix = new_instancemethod(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_ComputeMatrix, None, itkRigid3DPerspectiveTransformD)
itkRigid3DPerspectiveTransformD.GetFixedOffset = new_instancemethod(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_GetFixedOffset, None, itkRigid3DPerspectiveTransformD)
itkRigid3DPerspectiveTransformD.SetFixedOffset = new_instancemethod(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_SetFixedOffset, None, itkRigid3DPerspectiveTransformD)
itkRigid3DPerspectiveTransformD.SetCenterOfRotation = new_instancemethod(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_SetCenterOfRotation, None, itkRigid3DPerspectiveTransformD)
itkRigid3DPerspectiveTransformD.GetCenterOfRotation = new_instancemethod(_itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_GetCenterOfRotation, None, itkRigid3DPerspectiveTransformD)
itkRigid3DPerspectiveTransformD_swigregister = _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_swigregister
itkRigid3DPerspectiveTransformD_swigregister(itkRigid3DPerspectiveTransformD)

def itkRigid3DPerspectiveTransformD___New_orig__() -> "itkRigid3DPerspectiveTransformD_Pointer":
    """itkRigid3DPerspectiveTransformD___New_orig__() -> itkRigid3DPerspectiveTransformD_Pointer"""
    return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD___New_orig__()

def itkRigid3DPerspectiveTransformD_cast(obj: 'itkLightObject') -> "itkRigid3DPerspectiveTransformD *":
    """itkRigid3DPerspectiveTransformD_cast(itkLightObject obj) -> itkRigid3DPerspectiveTransformD"""
    return _itkRigid3DPerspectiveTransformPython.itkRigid3DPerspectiveTransformD_cast(obj)



