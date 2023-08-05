# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkVolumeSplineKernelTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkVolumeSplineKernelTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkVolumeSplineKernelTransformPython
            return _itkVolumeSplineKernelTransformPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkVolumeSplineKernelTransformPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkVolumeSplineKernelTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkVolumeSplineKernelTransformPython
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


import vnl_matrix_fixedPython
import vnl_matrixPython
import vnl_vectorPython
import stdcomplexPython
import pyBasePython
import itkPointPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkVectorPython
import itkKernelTransformPython
import itkTransformBasePython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import itkCovariantVectorPython
import itkArray2DPython
import itkVariableLengthVectorPython
import itkOptimizerParametersPython
import itkArrayPython
import ITKCommonBasePython
import itkPointSetPython
import itkVectorContainerPython
import itkOffsetPython
import itkSizePython
import itkContinuousIndexPython
import itkIndexPython

def itkVolumeSplineKernelTransformD3_New():
  return itkVolumeSplineKernelTransformD3.New()


def itkVolumeSplineKernelTransformD2_New():
  return itkVolumeSplineKernelTransformD2.New()

class itkVolumeSplineKernelTransformD2(itkKernelTransformPython.itkKernelTransformD2):
    """


    This class defines the thin plate spline (TPS) transformation. It is
    implemented in as straightforward a manner as possible from the IEEE
    TMI paper by Davis, Khotanzad, Flamig, and Harms, Vol. 16 No. 3 June
    1997

    C++ includes: itkVolumeSplineKernelTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkVolumeSplineKernelTransformD2_Pointer":
        """__New_orig__() -> itkVolumeSplineKernelTransformD2_Pointer"""
        return _itkVolumeSplineKernelTransformPython.itkVolumeSplineKernelTransformD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkVolumeSplineKernelTransformD2_Pointer":
        """Clone(itkVolumeSplineKernelTransformD2 self) -> itkVolumeSplineKernelTransformD2_Pointer"""
        return _itkVolumeSplineKernelTransformPython.itkVolumeSplineKernelTransformD2_Clone(self)

    __swig_destroy__ = _itkVolumeSplineKernelTransformPython.delete_itkVolumeSplineKernelTransformD2

    def cast(obj: 'itkLightObject') -> "itkVolumeSplineKernelTransformD2 *":
        """cast(itkLightObject obj) -> itkVolumeSplineKernelTransformD2"""
        return _itkVolumeSplineKernelTransformPython.itkVolumeSplineKernelTransformD2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkVolumeSplineKernelTransformD2

        Create a new object of the class itkVolumeSplineKernelTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVolumeSplineKernelTransformD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkVolumeSplineKernelTransformD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkVolumeSplineKernelTransformD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkVolumeSplineKernelTransformD2.Clone = new_instancemethod(_itkVolumeSplineKernelTransformPython.itkVolumeSplineKernelTransformD2_Clone, None, itkVolumeSplineKernelTransformD2)
itkVolumeSplineKernelTransformD2_swigregister = _itkVolumeSplineKernelTransformPython.itkVolumeSplineKernelTransformD2_swigregister
itkVolumeSplineKernelTransformD2_swigregister(itkVolumeSplineKernelTransformD2)

def itkVolumeSplineKernelTransformD2___New_orig__() -> "itkVolumeSplineKernelTransformD2_Pointer":
    """itkVolumeSplineKernelTransformD2___New_orig__() -> itkVolumeSplineKernelTransformD2_Pointer"""
    return _itkVolumeSplineKernelTransformPython.itkVolumeSplineKernelTransformD2___New_orig__()

def itkVolumeSplineKernelTransformD2_cast(obj: 'itkLightObject') -> "itkVolumeSplineKernelTransformD2 *":
    """itkVolumeSplineKernelTransformD2_cast(itkLightObject obj) -> itkVolumeSplineKernelTransformD2"""
    return _itkVolumeSplineKernelTransformPython.itkVolumeSplineKernelTransformD2_cast(obj)

class itkVolumeSplineKernelTransformD3(itkKernelTransformPython.itkKernelTransformD3):
    """


    This class defines the thin plate spline (TPS) transformation. It is
    implemented in as straightforward a manner as possible from the IEEE
    TMI paper by Davis, Khotanzad, Flamig, and Harms, Vol. 16 No. 3 June
    1997

    C++ includes: itkVolumeSplineKernelTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkVolumeSplineKernelTransformD3_Pointer":
        """__New_orig__() -> itkVolumeSplineKernelTransformD3_Pointer"""
        return _itkVolumeSplineKernelTransformPython.itkVolumeSplineKernelTransformD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkVolumeSplineKernelTransformD3_Pointer":
        """Clone(itkVolumeSplineKernelTransformD3 self) -> itkVolumeSplineKernelTransformD3_Pointer"""
        return _itkVolumeSplineKernelTransformPython.itkVolumeSplineKernelTransformD3_Clone(self)

    __swig_destroy__ = _itkVolumeSplineKernelTransformPython.delete_itkVolumeSplineKernelTransformD3

    def cast(obj: 'itkLightObject') -> "itkVolumeSplineKernelTransformD3 *":
        """cast(itkLightObject obj) -> itkVolumeSplineKernelTransformD3"""
        return _itkVolumeSplineKernelTransformPython.itkVolumeSplineKernelTransformD3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkVolumeSplineKernelTransformD3

        Create a new object of the class itkVolumeSplineKernelTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVolumeSplineKernelTransformD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkVolumeSplineKernelTransformD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkVolumeSplineKernelTransformD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkVolumeSplineKernelTransformD3.Clone = new_instancemethod(_itkVolumeSplineKernelTransformPython.itkVolumeSplineKernelTransformD3_Clone, None, itkVolumeSplineKernelTransformD3)
itkVolumeSplineKernelTransformD3_swigregister = _itkVolumeSplineKernelTransformPython.itkVolumeSplineKernelTransformD3_swigregister
itkVolumeSplineKernelTransformD3_swigregister(itkVolumeSplineKernelTransformD3)

def itkVolumeSplineKernelTransformD3___New_orig__() -> "itkVolumeSplineKernelTransformD3_Pointer":
    """itkVolumeSplineKernelTransformD3___New_orig__() -> itkVolumeSplineKernelTransformD3_Pointer"""
    return _itkVolumeSplineKernelTransformPython.itkVolumeSplineKernelTransformD3___New_orig__()

def itkVolumeSplineKernelTransformD3_cast(obj: 'itkLightObject') -> "itkVolumeSplineKernelTransformD3 *":
    """itkVolumeSplineKernelTransformD3_cast(itkLightObject obj) -> itkVolumeSplineKernelTransformD3"""
    return _itkVolumeSplineKernelTransformPython.itkVolumeSplineKernelTransformD3_cast(obj)



