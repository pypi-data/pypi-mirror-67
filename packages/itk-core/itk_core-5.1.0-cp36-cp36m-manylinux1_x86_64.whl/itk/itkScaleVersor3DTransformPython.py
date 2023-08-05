# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkScaleVersor3DTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkScaleVersor3DTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkScaleVersor3DTransformPython
            return _itkScaleVersor3DTransformPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkScaleVersor3DTransformPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkScaleVersor3DTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkScaleVersor3DTransformPython
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
import itkVectorPython
import itkFixedArrayPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import vnl_vector_refPython
import itkOptimizerParametersPython
import itkArrayPython
import itkPointPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkVersorRigid3DTransformPython
import itkVersorTransformPython
import itkVersorPython
import itkRigid3DTransformPython
import itkMatrixOffsetTransformBasePython
import itkTransformBasePython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkVariableLengthVectorPython
import itkArray2DPython

def itkScaleVersor3DTransformD_New():
  return itkScaleVersor3DTransformD.New()

class itkScaleVersor3DTransformD(itkVersorRigid3DTransformPython.itkVersorRigid3DTransformD):
    """


    This transform applies a Versor rotation, translation and anisotropic
    scale to the space.

    The transform can be described as: $ (\\textbf{R}_v +
    \\textbf{S})\\textbf{x} $ where $\\textbf{R}_v$ is the rotation
    matrix given the versor, and $S=\\left( \\begin{array}{ccc}s_0-1 &
    0 & 0 \\\\ 0 & s_1-1 & 0 \\\\ 0 & 0 & s_2-1 \\end{array}
    \\right)\\ $

    This transform's scale parameters are not related to the uniform
    scaling parameter of the Similarity3DTransform.

    Johnson H.J., Harris G., Williams K. University of Iowa Carver College
    of Medicine, Department of Psychiatry NeuroImaging Center  This
    implementation was taken from the Insight Journal
    paper:https://hdl.handle.net/1926/1291 orhttp://www.insight-
    journal.org/browse/publication/180

    C++ includes: itkScaleVersor3DTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkScaleVersor3DTransformD_Pointer":
        """__New_orig__() -> itkScaleVersor3DTransformD_Pointer"""
        return _itkScaleVersor3DTransformPython.itkScaleVersor3DTransformD___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkScaleVersor3DTransformD_Pointer":
        """Clone(itkScaleVersor3DTransformD self) -> itkScaleVersor3DTransformD_Pointer"""
        return _itkScaleVersor3DTransformPython.itkScaleVersor3DTransformD_Clone(self)


    def SetMatrix(self, *args) -> "void":
        """
        SetMatrix(itkScaleVersor3DTransformD self, itkMatrixD33 matrix)
        SetMatrix(itkScaleVersor3DTransformD self, itkMatrixD33 matrix, double const tolerance)

        Directly set the matrix
        of the transform.

        Orthogonality testing is bypassed in this case.

        See:   MatrixOffsetTransformBase::SetMatrix() 
        """
        return _itkScaleVersor3DTransformPython.itkScaleVersor3DTransformD_SetMatrix(self, *args)


    def SetScale(self, scale: 'itkVectorD3') -> "void":
        """
        SetScale(itkScaleVersor3DTransformD self, itkVectorD3 scale)

        Set/Get the scale vector.
        These scale factors are associated to the axis of coordinates. 
        """
        return _itkScaleVersor3DTransformPython.itkScaleVersor3DTransformD_SetScale(self, scale)


    def GetScale(self) -> "itkVectorD3 const &":
        """GetScale(itkScaleVersor3DTransformD self) -> itkVectorD3"""
        return _itkScaleVersor3DTransformPython.itkScaleVersor3DTransformD_GetScale(self)

    __swig_destroy__ = _itkScaleVersor3DTransformPython.delete_itkScaleVersor3DTransformD

    def cast(obj: 'itkLightObject') -> "itkScaleVersor3DTransformD *":
        """cast(itkLightObject obj) -> itkScaleVersor3DTransformD"""
        return _itkScaleVersor3DTransformPython.itkScaleVersor3DTransformD_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkScaleVersor3DTransformD

        Create a new object of the class itkScaleVersor3DTransformD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkScaleVersor3DTransformD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkScaleVersor3DTransformD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkScaleVersor3DTransformD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkScaleVersor3DTransformD.Clone = new_instancemethod(_itkScaleVersor3DTransformPython.itkScaleVersor3DTransformD_Clone, None, itkScaleVersor3DTransformD)
itkScaleVersor3DTransformD.SetMatrix = new_instancemethod(_itkScaleVersor3DTransformPython.itkScaleVersor3DTransformD_SetMatrix, None, itkScaleVersor3DTransformD)
itkScaleVersor3DTransformD.SetScale = new_instancemethod(_itkScaleVersor3DTransformPython.itkScaleVersor3DTransformD_SetScale, None, itkScaleVersor3DTransformD)
itkScaleVersor3DTransformD.GetScale = new_instancemethod(_itkScaleVersor3DTransformPython.itkScaleVersor3DTransformD_GetScale, None, itkScaleVersor3DTransformD)
itkScaleVersor3DTransformD_swigregister = _itkScaleVersor3DTransformPython.itkScaleVersor3DTransformD_swigregister
itkScaleVersor3DTransformD_swigregister(itkScaleVersor3DTransformD)

def itkScaleVersor3DTransformD___New_orig__() -> "itkScaleVersor3DTransformD_Pointer":
    """itkScaleVersor3DTransformD___New_orig__() -> itkScaleVersor3DTransformD_Pointer"""
    return _itkScaleVersor3DTransformPython.itkScaleVersor3DTransformD___New_orig__()

def itkScaleVersor3DTransformD_cast(obj: 'itkLightObject') -> "itkScaleVersor3DTransformD *":
    """itkScaleVersor3DTransformD_cast(itkLightObject obj) -> itkScaleVersor3DTransformD"""
    return _itkScaleVersor3DTransformPython.itkScaleVersor3DTransformD_cast(obj)



