# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkElasticBodySplineKernelTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkElasticBodySplineKernelTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkElasticBodySplineKernelTransformPython
            return _itkElasticBodySplineKernelTransformPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkElasticBodySplineKernelTransformPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkElasticBodySplineKernelTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkElasticBodySplineKernelTransformPython
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
import itkKernelTransformPython
import itkCovariantVectorPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkVectorPython
import vnl_matrix_fixedPython
import itkPointPython
import itkVectorContainerPython
import itkOffsetPython
import itkSizePython
import itkMatrixPython
import itkContinuousIndexPython
import itkIndexPython
import itkPointSetPython
import itkOptimizerParametersPython
import itkArrayPython
import itkArray2DPython
import itkTransformBasePython
import itkSymmetricSecondRankTensorPython
import itkVariableLengthVectorPython
import itkDiffusionTensor3DPython

def itkElasticBodySplineKernelTransformD3_New():
  return itkElasticBodySplineKernelTransformD3.New()


def itkElasticBodySplineKernelTransformD2_New():
  return itkElasticBodySplineKernelTransformD2.New()

class itkElasticBodySplineKernelTransformD2(itkKernelTransformPython.itkKernelTransformD2):
    """


    This class defines the elastic body spline (EBS) transformation.

    This class defines the elastic body spline (EBS) transformation. It is
    implemented in as straightforward a manner as possible from the IEEE
    TMI paper by Davis, Khotanzad, Flamig, and Harms, Vol. 16 No. 3 June
    1997 Taken from the paper: The EBS "is based on a physical model of a
    homogeneous, isotropic, three-dimensional elastic body. The model can
    approximate the way that some physical objects deform".

    C++ includes: itkElasticBodySplineKernelTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkElasticBodySplineKernelTransformD2_Pointer":
        """__New_orig__() -> itkElasticBodySplineKernelTransformD2_Pointer"""
        return _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkElasticBodySplineKernelTransformD2_Pointer":
        """Clone(itkElasticBodySplineKernelTransformD2 self) -> itkElasticBodySplineKernelTransformD2_Pointer"""
        return _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD2_Clone(self)


    def SetAlpha(self, _arg: 'double const') -> "void":
        """
        SetAlpha(itkElasticBodySplineKernelTransformD2 self, double const _arg)

        Set alpha. Alpha is
        related to Poisson's Ratio ( $\\nu$) as $\\alpha = 12 ( 1 - \\nu
        ) - 1$ 
        """
        return _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD2_SetAlpha(self, _arg)


    def GetAlpha(self) -> "double":
        """
        GetAlpha(itkElasticBodySplineKernelTransformD2 self) -> double

        Get alpha 
        """
        return _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD2_GetAlpha(self)

    __swig_destroy__ = _itkElasticBodySplineKernelTransformPython.delete_itkElasticBodySplineKernelTransformD2

    def cast(obj: 'itkLightObject') -> "itkElasticBodySplineKernelTransformD2 *":
        """cast(itkLightObject obj) -> itkElasticBodySplineKernelTransformD2"""
        return _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkElasticBodySplineKernelTransformD2

        Create a new object of the class itkElasticBodySplineKernelTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkElasticBodySplineKernelTransformD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkElasticBodySplineKernelTransformD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkElasticBodySplineKernelTransformD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkElasticBodySplineKernelTransformD2.Clone = new_instancemethod(_itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD2_Clone, None, itkElasticBodySplineKernelTransformD2)
itkElasticBodySplineKernelTransformD2.SetAlpha = new_instancemethod(_itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD2_SetAlpha, None, itkElasticBodySplineKernelTransformD2)
itkElasticBodySplineKernelTransformD2.GetAlpha = new_instancemethod(_itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD2_GetAlpha, None, itkElasticBodySplineKernelTransformD2)
itkElasticBodySplineKernelTransformD2_swigregister = _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD2_swigregister
itkElasticBodySplineKernelTransformD2_swigregister(itkElasticBodySplineKernelTransformD2)

def itkElasticBodySplineKernelTransformD2___New_orig__() -> "itkElasticBodySplineKernelTransformD2_Pointer":
    """itkElasticBodySplineKernelTransformD2___New_orig__() -> itkElasticBodySplineKernelTransformD2_Pointer"""
    return _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD2___New_orig__()

def itkElasticBodySplineKernelTransformD2_cast(obj: 'itkLightObject') -> "itkElasticBodySplineKernelTransformD2 *":
    """itkElasticBodySplineKernelTransformD2_cast(itkLightObject obj) -> itkElasticBodySplineKernelTransformD2"""
    return _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD2_cast(obj)

class itkElasticBodySplineKernelTransformD3(itkKernelTransformPython.itkKernelTransformD3):
    """


    This class defines the elastic body spline (EBS) transformation.

    This class defines the elastic body spline (EBS) transformation. It is
    implemented in as straightforward a manner as possible from the IEEE
    TMI paper by Davis, Khotanzad, Flamig, and Harms, Vol. 16 No. 3 June
    1997 Taken from the paper: The EBS "is based on a physical model of a
    homogeneous, isotropic, three-dimensional elastic body. The model can
    approximate the way that some physical objects deform".

    C++ includes: itkElasticBodySplineKernelTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkElasticBodySplineKernelTransformD3_Pointer":
        """__New_orig__() -> itkElasticBodySplineKernelTransformD3_Pointer"""
        return _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkElasticBodySplineKernelTransformD3_Pointer":
        """Clone(itkElasticBodySplineKernelTransformD3 self) -> itkElasticBodySplineKernelTransformD3_Pointer"""
        return _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD3_Clone(self)


    def SetAlpha(self, _arg: 'double const') -> "void":
        """
        SetAlpha(itkElasticBodySplineKernelTransformD3 self, double const _arg)

        Set alpha. Alpha is
        related to Poisson's Ratio ( $\\nu$) as $\\alpha = 12 ( 1 - \\nu
        ) - 1$ 
        """
        return _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD3_SetAlpha(self, _arg)


    def GetAlpha(self) -> "double":
        """
        GetAlpha(itkElasticBodySplineKernelTransformD3 self) -> double

        Get alpha 
        """
        return _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD3_GetAlpha(self)

    __swig_destroy__ = _itkElasticBodySplineKernelTransformPython.delete_itkElasticBodySplineKernelTransformD3

    def cast(obj: 'itkLightObject') -> "itkElasticBodySplineKernelTransformD3 *":
        """cast(itkLightObject obj) -> itkElasticBodySplineKernelTransformD3"""
        return _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkElasticBodySplineKernelTransformD3

        Create a new object of the class itkElasticBodySplineKernelTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkElasticBodySplineKernelTransformD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkElasticBodySplineKernelTransformD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkElasticBodySplineKernelTransformD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkElasticBodySplineKernelTransformD3.Clone = new_instancemethod(_itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD3_Clone, None, itkElasticBodySplineKernelTransformD3)
itkElasticBodySplineKernelTransformD3.SetAlpha = new_instancemethod(_itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD3_SetAlpha, None, itkElasticBodySplineKernelTransformD3)
itkElasticBodySplineKernelTransformD3.GetAlpha = new_instancemethod(_itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD3_GetAlpha, None, itkElasticBodySplineKernelTransformD3)
itkElasticBodySplineKernelTransformD3_swigregister = _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD3_swigregister
itkElasticBodySplineKernelTransformD3_swigregister(itkElasticBodySplineKernelTransformD3)

def itkElasticBodySplineKernelTransformD3___New_orig__() -> "itkElasticBodySplineKernelTransformD3_Pointer":
    """itkElasticBodySplineKernelTransformD3___New_orig__() -> itkElasticBodySplineKernelTransformD3_Pointer"""
    return _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD3___New_orig__()

def itkElasticBodySplineKernelTransformD3_cast(obj: 'itkLightObject') -> "itkElasticBodySplineKernelTransformD3 *":
    """itkElasticBodySplineKernelTransformD3_cast(itkLightObject obj) -> itkElasticBodySplineKernelTransformD3"""
    return _itkElasticBodySplineKernelTransformPython.itkElasticBodySplineKernelTransformD3_cast(obj)



