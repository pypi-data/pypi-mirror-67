# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkScaleLogarithmicTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkScaleLogarithmicTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkScaleLogarithmicTransformPython
            return _itkScaleLogarithmicTransformPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkScaleLogarithmicTransformPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkScaleLogarithmicTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkScaleLogarithmicTransformPython
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
import itkOptimizerParametersPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import itkArrayPython
import itkPointPython
import vnl_vector_refPython
import itkVectorPython
import itkFixedArrayPython
import itkScaleTransformPython
import itkTransformBasePython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkVariableLengthVectorPython
import itkArray2DPython
import itkMatrixOffsetTransformBasePython

def itkScaleLogarithmicTransformD3_New():
  return itkScaleLogarithmicTransformD3.New()


def itkScaleLogarithmicTransformD2_New():
  return itkScaleLogarithmicTransformD2.New()

class itkScaleLogarithmicTransformD2(itkScaleTransformPython.itkScaleTransformD2):
    """


    Logarithmic Scale transformation of a vector space (e.g. space
    coordinates)

    The only difference between this class and its superclass the
    ScaleTransform is that here the parameters of the transformation are
    the logarithms of the scales. This facilitates to linearize the
    expressions used for optimization.

    C++ includes: itkScaleLogarithmicTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkScaleLogarithmicTransformD2_Pointer":
        """__New_orig__() -> itkScaleLogarithmicTransformD2_Pointer"""
        return _itkScaleLogarithmicTransformPython.itkScaleLogarithmicTransformD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkScaleLogarithmicTransformD2_Pointer":
        """Clone(itkScaleLogarithmicTransformD2 self) -> itkScaleLogarithmicTransformD2_Pointer"""
        return _itkScaleLogarithmicTransformPython.itkScaleLogarithmicTransformD2_Clone(self)

    __swig_destroy__ = _itkScaleLogarithmicTransformPython.delete_itkScaleLogarithmicTransformD2

    def cast(obj: 'itkLightObject') -> "itkScaleLogarithmicTransformD2 *":
        """cast(itkLightObject obj) -> itkScaleLogarithmicTransformD2"""
        return _itkScaleLogarithmicTransformPython.itkScaleLogarithmicTransformD2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkScaleLogarithmicTransformD2

        Create a new object of the class itkScaleLogarithmicTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkScaleLogarithmicTransformD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkScaleLogarithmicTransformD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkScaleLogarithmicTransformD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkScaleLogarithmicTransformD2.Clone = new_instancemethod(_itkScaleLogarithmicTransformPython.itkScaleLogarithmicTransformD2_Clone, None, itkScaleLogarithmicTransformD2)
itkScaleLogarithmicTransformD2_swigregister = _itkScaleLogarithmicTransformPython.itkScaleLogarithmicTransformD2_swigregister
itkScaleLogarithmicTransformD2_swigregister(itkScaleLogarithmicTransformD2)

def itkScaleLogarithmicTransformD2___New_orig__() -> "itkScaleLogarithmicTransformD2_Pointer":
    """itkScaleLogarithmicTransformD2___New_orig__() -> itkScaleLogarithmicTransformD2_Pointer"""
    return _itkScaleLogarithmicTransformPython.itkScaleLogarithmicTransformD2___New_orig__()

def itkScaleLogarithmicTransformD2_cast(obj: 'itkLightObject') -> "itkScaleLogarithmicTransformD2 *":
    """itkScaleLogarithmicTransformD2_cast(itkLightObject obj) -> itkScaleLogarithmicTransformD2"""
    return _itkScaleLogarithmicTransformPython.itkScaleLogarithmicTransformD2_cast(obj)

class itkScaleLogarithmicTransformD3(itkScaleTransformPython.itkScaleTransformD3):
    """


    Logarithmic Scale transformation of a vector space (e.g. space
    coordinates)

    The only difference between this class and its superclass the
    ScaleTransform is that here the parameters of the transformation are
    the logarithms of the scales. This facilitates to linearize the
    expressions used for optimization.

    C++ includes: itkScaleLogarithmicTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkScaleLogarithmicTransformD3_Pointer":
        """__New_orig__() -> itkScaleLogarithmicTransformD3_Pointer"""
        return _itkScaleLogarithmicTransformPython.itkScaleLogarithmicTransformD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkScaleLogarithmicTransformD3_Pointer":
        """Clone(itkScaleLogarithmicTransformD3 self) -> itkScaleLogarithmicTransformD3_Pointer"""
        return _itkScaleLogarithmicTransformPython.itkScaleLogarithmicTransformD3_Clone(self)

    __swig_destroy__ = _itkScaleLogarithmicTransformPython.delete_itkScaleLogarithmicTransformD3

    def cast(obj: 'itkLightObject') -> "itkScaleLogarithmicTransformD3 *":
        """cast(itkLightObject obj) -> itkScaleLogarithmicTransformD3"""
        return _itkScaleLogarithmicTransformPython.itkScaleLogarithmicTransformD3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkScaleLogarithmicTransformD3

        Create a new object of the class itkScaleLogarithmicTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkScaleLogarithmicTransformD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkScaleLogarithmicTransformD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkScaleLogarithmicTransformD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkScaleLogarithmicTransformD3.Clone = new_instancemethod(_itkScaleLogarithmicTransformPython.itkScaleLogarithmicTransformD3_Clone, None, itkScaleLogarithmicTransformD3)
itkScaleLogarithmicTransformD3_swigregister = _itkScaleLogarithmicTransformPython.itkScaleLogarithmicTransformD3_swigregister
itkScaleLogarithmicTransformD3_swigregister(itkScaleLogarithmicTransformD3)

def itkScaleLogarithmicTransformD3___New_orig__() -> "itkScaleLogarithmicTransformD3_Pointer":
    """itkScaleLogarithmicTransformD3___New_orig__() -> itkScaleLogarithmicTransformD3_Pointer"""
    return _itkScaleLogarithmicTransformPython.itkScaleLogarithmicTransformD3___New_orig__()

def itkScaleLogarithmicTransformD3_cast(obj: 'itkLightObject') -> "itkScaleLogarithmicTransformD3 *":
    """itkScaleLogarithmicTransformD3_cast(itkLightObject obj) -> itkScaleLogarithmicTransformD3"""
    return _itkScaleLogarithmicTransformPython.itkScaleLogarithmicTransformD3_cast(obj)



