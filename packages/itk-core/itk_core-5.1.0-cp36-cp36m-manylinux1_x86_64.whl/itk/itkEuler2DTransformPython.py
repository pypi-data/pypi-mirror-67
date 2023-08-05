# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkEuler2DTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkEuler2DTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkEuler2DTransformPython
            return _itkEuler2DTransformPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkEuler2DTransformPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkEuler2DTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkEuler2DTransformPython
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
import itkRigid2DTransformPython
import itkMatrixOffsetTransformBasePython

def itkEuler2DTransformD_New():
  return itkEuler2DTransformD.New()

class itkEuler2DTransformD(itkRigid2DTransformPython.itkRigid2DTransformD):
    """


    Euler2DTransform of a vector space (e.g. space coordinates)

    This transform applies a rigid transformation is 2D space. The
    transform is specified as a rotation around arbitrary center and is
    followed by a translation.

    This transform is basically is a synonym for Rigid2DTransform.

    See:   Rigid2DTransform

    C++ includes: itkEuler2DTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkEuler2DTransformD_Pointer":
        """__New_orig__() -> itkEuler2DTransformD_Pointer"""
        return _itkEuler2DTransformPython.itkEuler2DTransformD___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkEuler2DTransformD_Pointer":
        """Clone(itkEuler2DTransformD self) -> itkEuler2DTransformD_Pointer"""
        return _itkEuler2DTransformPython.itkEuler2DTransformD_Clone(self)


    def CloneInverseTo(self, newinverse: 'itkEuler2DTransformD_Pointer &') -> "void":
        """
        CloneInverseTo(itkEuler2DTransformD self, itkEuler2DTransformD_Pointer & newinverse)

        This method creates
        and returns a new Euler2DTransform object which is the inverse of
        self. 
        """
        return _itkEuler2DTransformPython.itkEuler2DTransformD_CloneInverseTo(self, newinverse)


    def GetInverse(self, inverse: 'itkEuler2DTransformD') -> "bool":
        """
        GetInverse(itkEuler2DTransformD self, itkEuler2DTransformD inverse) -> bool

        Get an inverse of this
        transform. 
        """
        return _itkEuler2DTransformPython.itkEuler2DTransformD_GetInverse(self, inverse)


    def CloneTo(self, clone: 'itkEuler2DTransformD_Pointer &') -> "void":
        """
        CloneTo(itkEuler2DTransformD self, itkEuler2DTransformD_Pointer & clone)

        This method creates and
        returns a new Euler2DTransform object which has the same parameters as
        self. 
        """
        return _itkEuler2DTransformPython.itkEuler2DTransformD_CloneTo(self, clone)


    def ComputeAngleFromMatrix(self) -> "void":
        """
        ComputeAngleFromMatrix(itkEuler2DTransformD self)

        Update the
        angle from the underlying matrix. This method is old and is retained
        for backward compatibility. 
        """
        return _itkEuler2DTransformPython.itkEuler2DTransformD_ComputeAngleFromMatrix(self)

    __swig_destroy__ = _itkEuler2DTransformPython.delete_itkEuler2DTransformD

    def cast(obj: 'itkLightObject') -> "itkEuler2DTransformD *":
        """cast(itkLightObject obj) -> itkEuler2DTransformD"""
        return _itkEuler2DTransformPython.itkEuler2DTransformD_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkEuler2DTransformD

        Create a new object of the class itkEuler2DTransformD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkEuler2DTransformD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkEuler2DTransformD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkEuler2DTransformD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkEuler2DTransformD.Clone = new_instancemethod(_itkEuler2DTransformPython.itkEuler2DTransformD_Clone, None, itkEuler2DTransformD)
itkEuler2DTransformD.CloneInverseTo = new_instancemethod(_itkEuler2DTransformPython.itkEuler2DTransformD_CloneInverseTo, None, itkEuler2DTransformD)
itkEuler2DTransformD.GetInverse = new_instancemethod(_itkEuler2DTransformPython.itkEuler2DTransformD_GetInverse, None, itkEuler2DTransformD)
itkEuler2DTransformD.CloneTo = new_instancemethod(_itkEuler2DTransformPython.itkEuler2DTransformD_CloneTo, None, itkEuler2DTransformD)
itkEuler2DTransformD.ComputeAngleFromMatrix = new_instancemethod(_itkEuler2DTransformPython.itkEuler2DTransformD_ComputeAngleFromMatrix, None, itkEuler2DTransformD)
itkEuler2DTransformD_swigregister = _itkEuler2DTransformPython.itkEuler2DTransformD_swigregister
itkEuler2DTransformD_swigregister(itkEuler2DTransformD)

def itkEuler2DTransformD___New_orig__() -> "itkEuler2DTransformD_Pointer":
    """itkEuler2DTransformD___New_orig__() -> itkEuler2DTransformD_Pointer"""
    return _itkEuler2DTransformPython.itkEuler2DTransformD___New_orig__()

def itkEuler2DTransformD_cast(obj: 'itkLightObject') -> "itkEuler2DTransformD *":
    """itkEuler2DTransformD_cast(itkLightObject obj) -> itkEuler2DTransformD"""
    return _itkEuler2DTransformPython.itkEuler2DTransformD_cast(obj)



