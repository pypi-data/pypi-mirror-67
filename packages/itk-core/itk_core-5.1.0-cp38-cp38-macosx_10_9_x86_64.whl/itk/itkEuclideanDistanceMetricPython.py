# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkEuclideanDistanceMetricPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkEuclideanDistanceMetricPython', [dirname(__file__)])
        except ImportError:
            import _itkEuclideanDistanceMetricPython
            return _itkEuclideanDistanceMetricPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkEuclideanDistanceMetricPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkEuclideanDistanceMetricPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkEuclideanDistanceMetricPython
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
import itkDistanceMetricPython
import itkVectorPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkArrayPython
import itkFunctionBasePython
import itkContinuousIndexPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkPointPython
import itkImagePython
import itkCovariantVectorPython
import itkRGBPixelPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkRGBAPixelPython
import itkSymmetricSecondRankTensorPython
import itkImageRegionPython

def itkEuclideanDistanceMetricVF3_New():
  return itkEuclideanDistanceMetricVF3.New()


def itkEuclideanDistanceMetricVF2_New():
  return itkEuclideanDistanceMetricVF2.New()

class itkEuclideanDistanceMetricVF2(itkDistanceMetricPython.itkDistanceMetricVF2):
    """


    Euclidean distance function.

    C++ includes: itkEuclideanDistanceMetric.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkEuclideanDistanceMetricVF2_Pointer":
        """__New_orig__() -> itkEuclideanDistanceMetricVF2_Pointer"""
        return _itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkEuclideanDistanceMetricVF2_Pointer":
        """Clone(itkEuclideanDistanceMetricVF2 self) -> itkEuclideanDistanceMetricVF2_Pointer"""
        return _itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF2_Clone(self)


    def Evaluate(self, *args) -> "double":
        """
        Evaluate(itkEuclideanDistanceMetricVF2 self, itkVectorF2 x) -> double
        Evaluate(itkEuclideanDistanceMetricVF2 self, itkVectorF2 x1, itkVectorF2 x2) -> double
        Evaluate(itkEuclideanDistanceMetricVF2 self, float const & a, float const & b) -> double

        Gets the coordinate
        distance between a and b. NOTE: a and b should be type of component.
        This method is used by KdTreeKMeans estimators. When the estimator is
        refactored, this method should be removed. 
        """
        return _itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF2_Evaluate(self, *args)

    __swig_destroy__ = _itkEuclideanDistanceMetricPython.delete_itkEuclideanDistanceMetricVF2

    def cast(obj: 'itkLightObject') -> "itkEuclideanDistanceMetricVF2 *":
        """cast(itkLightObject obj) -> itkEuclideanDistanceMetricVF2"""
        return _itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkEuclideanDistanceMetricVF2

        Create a new object of the class itkEuclideanDistanceMetricVF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkEuclideanDistanceMetricVF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkEuclideanDistanceMetricVF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkEuclideanDistanceMetricVF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkEuclideanDistanceMetricVF2.Clone = new_instancemethod(_itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF2_Clone, None, itkEuclideanDistanceMetricVF2)
itkEuclideanDistanceMetricVF2.Evaluate = new_instancemethod(_itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF2_Evaluate, None, itkEuclideanDistanceMetricVF2)
itkEuclideanDistanceMetricVF2_swigregister = _itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF2_swigregister
itkEuclideanDistanceMetricVF2_swigregister(itkEuclideanDistanceMetricVF2)

def itkEuclideanDistanceMetricVF2___New_orig__() -> "itkEuclideanDistanceMetricVF2_Pointer":
    """itkEuclideanDistanceMetricVF2___New_orig__() -> itkEuclideanDistanceMetricVF2_Pointer"""
    return _itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF2___New_orig__()

def itkEuclideanDistanceMetricVF2_cast(obj: 'itkLightObject') -> "itkEuclideanDistanceMetricVF2 *":
    """itkEuclideanDistanceMetricVF2_cast(itkLightObject obj) -> itkEuclideanDistanceMetricVF2"""
    return _itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF2_cast(obj)

class itkEuclideanDistanceMetricVF3(itkDistanceMetricPython.itkDistanceMetricVF3):
    """


    Euclidean distance function.

    C++ includes: itkEuclideanDistanceMetric.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkEuclideanDistanceMetricVF3_Pointer":
        """__New_orig__() -> itkEuclideanDistanceMetricVF3_Pointer"""
        return _itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkEuclideanDistanceMetricVF3_Pointer":
        """Clone(itkEuclideanDistanceMetricVF3 self) -> itkEuclideanDistanceMetricVF3_Pointer"""
        return _itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF3_Clone(self)


    def Evaluate(self, *args) -> "double":
        """
        Evaluate(itkEuclideanDistanceMetricVF3 self, itkVectorF3 x) -> double
        Evaluate(itkEuclideanDistanceMetricVF3 self, itkVectorF3 x1, itkVectorF3 x2) -> double
        Evaluate(itkEuclideanDistanceMetricVF3 self, float const & a, float const & b) -> double

        Gets the coordinate
        distance between a and b. NOTE: a and b should be type of component.
        This method is used by KdTreeKMeans estimators. When the estimator is
        refactored, this method should be removed. 
        """
        return _itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF3_Evaluate(self, *args)

    __swig_destroy__ = _itkEuclideanDistanceMetricPython.delete_itkEuclideanDistanceMetricVF3

    def cast(obj: 'itkLightObject') -> "itkEuclideanDistanceMetricVF3 *":
        """cast(itkLightObject obj) -> itkEuclideanDistanceMetricVF3"""
        return _itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkEuclideanDistanceMetricVF3

        Create a new object of the class itkEuclideanDistanceMetricVF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkEuclideanDistanceMetricVF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkEuclideanDistanceMetricVF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkEuclideanDistanceMetricVF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkEuclideanDistanceMetricVF3.Clone = new_instancemethod(_itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF3_Clone, None, itkEuclideanDistanceMetricVF3)
itkEuclideanDistanceMetricVF3.Evaluate = new_instancemethod(_itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF3_Evaluate, None, itkEuclideanDistanceMetricVF3)
itkEuclideanDistanceMetricVF3_swigregister = _itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF3_swigregister
itkEuclideanDistanceMetricVF3_swigregister(itkEuclideanDistanceMetricVF3)

def itkEuclideanDistanceMetricVF3___New_orig__() -> "itkEuclideanDistanceMetricVF3_Pointer":
    """itkEuclideanDistanceMetricVF3___New_orig__() -> itkEuclideanDistanceMetricVF3_Pointer"""
    return _itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF3___New_orig__()

def itkEuclideanDistanceMetricVF3_cast(obj: 'itkLightObject') -> "itkEuclideanDistanceMetricVF3 *":
    """itkEuclideanDistanceMetricVF3_cast(itkLightObject obj) -> itkEuclideanDistanceMetricVF3"""
    return _itkEuclideanDistanceMetricPython.itkEuclideanDistanceMetricVF3_cast(obj)



