# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkScaleSkewVersor3DTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkScaleSkewVersor3DTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkScaleSkewVersor3DTransformPython
            return _itkScaleSkewVersor3DTransformPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkScaleSkewVersor3DTransformPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkScaleSkewVersor3DTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkScaleSkewVersor3DTransformPython
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
import itkMatrixPython
import vnl_matrixPython
import stdcomplexPython
import vnl_vectorPython
import itkPointPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkVectorPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkVersorRigid3DTransformPython
import itkArrayPython
import itkVersorTransformPython
import itkVersorPython
import itkOptimizerParametersPython
import itkArray2DPython
import itkRigid3DTransformPython
import itkMatrixOffsetTransformBasePython
import itkTransformBasePython
import itkSymmetricSecondRankTensorPython
import itkVariableLengthVectorPython
import itkDiffusionTensor3DPython

def itkScaleSkewVersor3DTransformD_New():
  return itkScaleSkewVersor3DTransformD.New()

class itkScaleSkewVersor3DTransformD(itkVersorRigid3DTransformPython.itkVersorRigid3DTransformD):
    """


    ScaleSkewVersor3DTransform of a vector space (e.g. space coordinates)

    This transform applies a versor rotation and translation & scale/skew
    to the space

    The parameters for this transform can be set either using individual
    Set methods or in serialized form using SetParameters() and
    SetFixedParameters().

    The serialization of the optimizable parameters is an array of 15
    elements. The first 3 elements are the components of the versor
    representation of 3D rotation. The next 3 parameters defines the
    translation in each dimension. The next 3 parameters defines scaling
    in each dimension. The last 6 parameters defines the skew.

    The serialization of the fixed parameters is an array of 3 elements
    defining the center of rotation.

    The transform can be described as: $ (\\textbf{R}_v + \\textbf{S}
    + \\textbf{K})\\textbf{x} $ where $\\textbf{R}_v$ is the
    rotation matrix given the versor, $S=\\left(
    \\begin{array}{ccc}s_0-1 & 0 & 0 \\\\ 0 & s_1-1 & 0 \\\\ 0 &
    0 & s_2-1 \\end{array} \\right) $ , and $K=\\left(
    \\begin{array}{ccc}0 & k_0 & k_1 \\\\ k_2 & 0 & k_3 \\\\ k_4
    & k_5 & 0 \\end{array} \\right)\\ $.

    C++ includes: itkScaleSkewVersor3DTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkScaleSkewVersor3DTransformD_Pointer":
        """__New_orig__() -> itkScaleSkewVersor3DTransformD_Pointer"""
        return _itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkScaleSkewVersor3DTransformD_Pointer":
        """Clone(itkScaleSkewVersor3DTransformD self) -> itkScaleSkewVersor3DTransformD_Pointer"""
        return _itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD_Clone(self)


    def SetMatrix(self, *args) -> "void":
        """
        SetMatrix(itkScaleSkewVersor3DTransformD self, itkMatrixD33 matrix)
        SetMatrix(itkScaleSkewVersor3DTransformD self, itkMatrixD33 matrix, double const tolerance)

        Directly set the matrix
        of the transform.

        Orthogonality testing is bypassed in this case.

        See:   MatrixOffsetTransformBase::SetMatrix() 
        """
        return _itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD_SetMatrix(self, *args)


    def SetScale(self, scale: 'itkVectorD3') -> "void":
        """SetScale(itkScaleSkewVersor3DTransformD self, itkVectorD3 scale)"""
        return _itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD_SetScale(self, scale)


    def GetScale(self) -> "itkVectorD3 const &":
        """GetScale(itkScaleSkewVersor3DTransformD self) -> itkVectorD3"""
        return _itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD_GetScale(self)


    def SetSkew(self, skew: 'itkVectorD6') -> "void":
        """SetSkew(itkScaleSkewVersor3DTransformD self, itkVectorD6 skew)"""
        return _itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD_SetSkew(self, skew)


    def GetSkew(self) -> "itkVectorD6 const &":
        """GetSkew(itkScaleSkewVersor3DTransformD self) -> itkVectorD6"""
        return _itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD_GetSkew(self)

    __swig_destroy__ = _itkScaleSkewVersor3DTransformPython.delete_itkScaleSkewVersor3DTransformD

    def cast(obj: 'itkLightObject') -> "itkScaleSkewVersor3DTransformD *":
        """cast(itkLightObject obj) -> itkScaleSkewVersor3DTransformD"""
        return _itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkScaleSkewVersor3DTransformD

        Create a new object of the class itkScaleSkewVersor3DTransformD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkScaleSkewVersor3DTransformD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkScaleSkewVersor3DTransformD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkScaleSkewVersor3DTransformD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkScaleSkewVersor3DTransformD.Clone = new_instancemethod(_itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD_Clone, None, itkScaleSkewVersor3DTransformD)
itkScaleSkewVersor3DTransformD.SetMatrix = new_instancemethod(_itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD_SetMatrix, None, itkScaleSkewVersor3DTransformD)
itkScaleSkewVersor3DTransformD.SetScale = new_instancemethod(_itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD_SetScale, None, itkScaleSkewVersor3DTransformD)
itkScaleSkewVersor3DTransformD.GetScale = new_instancemethod(_itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD_GetScale, None, itkScaleSkewVersor3DTransformD)
itkScaleSkewVersor3DTransformD.SetSkew = new_instancemethod(_itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD_SetSkew, None, itkScaleSkewVersor3DTransformD)
itkScaleSkewVersor3DTransformD.GetSkew = new_instancemethod(_itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD_GetSkew, None, itkScaleSkewVersor3DTransformD)
itkScaleSkewVersor3DTransformD_swigregister = _itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD_swigregister
itkScaleSkewVersor3DTransformD_swigregister(itkScaleSkewVersor3DTransformD)

def itkScaleSkewVersor3DTransformD___New_orig__() -> "itkScaleSkewVersor3DTransformD_Pointer":
    """itkScaleSkewVersor3DTransformD___New_orig__() -> itkScaleSkewVersor3DTransformD_Pointer"""
    return _itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD___New_orig__()

def itkScaleSkewVersor3DTransformD_cast(obj: 'itkLightObject') -> "itkScaleSkewVersor3DTransformD *":
    """itkScaleSkewVersor3DTransformD_cast(itkLightObject obj) -> itkScaleSkewVersor3DTransformD"""
    return _itkScaleSkewVersor3DTransformPython.itkScaleSkewVersor3DTransformD_cast(obj)



