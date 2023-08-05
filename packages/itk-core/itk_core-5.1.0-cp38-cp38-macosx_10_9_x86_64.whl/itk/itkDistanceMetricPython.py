# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkDistanceMetricPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkDistanceMetricPython', [dirname(__file__)])
        except ImportError:
            import _itkDistanceMetricPython
            return _itkDistanceMetricPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkDistanceMetricPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkDistanceMetricPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkDistanceMetricPython
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


import itkVectorPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import pyBasePython
import vnl_vector_refPython
import itkFixedArrayPython
import itkArrayPython
import ITKCommonBasePython
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

def itkDistanceMetricVF3_New():
  return itkDistanceMetricVF3.New()


def itkDistanceMetricVF2_New():
  return itkDistanceMetricVF2.New()

class itkDistanceMetricVF2(itkFunctionBasePython.itkFunctionBaseVF2D):
    """


    this class declares common interfaces for distance functions.

    As a function derived from FunctionBase, users use Evaluate method to
    get result.

    To use this function users should first set the origin by calling
    SetOrigin() function, then call Evaluate() method with a point to get
    the distance between the origin point and the evaluation point.

    See:  EuclideanSquareDistanceMetric

    See:   EuclideanDistanceMetric

    See:  ManhattanDistanceMetric

    C++ includes: itkDistanceMetric.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def SetOrigin(self, x: 'itkArrayD') -> "void":
        """
        SetOrigin(itkDistanceMetricVF2 self, itkArrayD x)

        Sets the origin point
        that will be used for the single point version Evaluate() function.
        This function is necessary part of implementing the Evaluate()
        interface. The argument of SetOrigin() must be of type
        DistanceMetric::OriginType, which in most cases will be different from
        the TVector type. This is necessary because often times the origin
        would be a mean, or a vector representative of a collection of
        vectors. 
        """
        return _itkDistanceMetricPython.itkDistanceMetricVF2_SetOrigin(self, x)


    def GetOrigin(self) -> "itkArrayD const &":
        """GetOrigin(itkDistanceMetricVF2 self) -> itkArrayD"""
        return _itkDistanceMetricPython.itkDistanceMetricVF2_GetOrigin(self)


    def Evaluate(self, *args) -> "double":
        """
        Evaluate(itkDistanceMetricVF2 self, itkVectorF2 x) -> double
        Evaluate(itkDistanceMetricVF2 self, itkVectorF2 x1, itkVectorF2 x2) -> double

        Gets the distance between
        x1 and x2. This method is used by KdTreeKMeans estimators. When the
        estimator is refactored, this method should be removed. Distance
        between two measurement vectors can be computed by setting one of them
        as an origin of the distane and using the Evaluate method with a
        single argument 
        """
        return _itkDistanceMetricPython.itkDistanceMetricVF2_Evaluate(self, *args)


    def SetMeasurementVectorSize(self, s: 'unsigned int') -> "void":
        """
        SetMeasurementVectorSize(itkDistanceMetricVF2 self, unsigned int s)

        Set method
        for the length of the measurement vector 
        """
        return _itkDistanceMetricPython.itkDistanceMetricVF2_SetMeasurementVectorSize(self, s)


    def GetMeasurementVectorSize(self) -> "unsigned int":
        """
        GetMeasurementVectorSize(itkDistanceMetricVF2 self) -> unsigned int

        Get method
        for the length of the measurement vector 
        """
        return _itkDistanceMetricPython.itkDistanceMetricVF2_GetMeasurementVectorSize(self)

    __swig_destroy__ = _itkDistanceMetricPython.delete_itkDistanceMetricVF2

    def cast(obj: 'itkLightObject') -> "itkDistanceMetricVF2 *":
        """cast(itkLightObject obj) -> itkDistanceMetricVF2"""
        return _itkDistanceMetricPython.itkDistanceMetricVF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkDistanceMetricVF2

        Create a new object of the class itkDistanceMetricVF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDistanceMetricVF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDistanceMetricVF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDistanceMetricVF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkDistanceMetricVF2.SetOrigin = new_instancemethod(_itkDistanceMetricPython.itkDistanceMetricVF2_SetOrigin, None, itkDistanceMetricVF2)
itkDistanceMetricVF2.GetOrigin = new_instancemethod(_itkDistanceMetricPython.itkDistanceMetricVF2_GetOrigin, None, itkDistanceMetricVF2)
itkDistanceMetricVF2.Evaluate = new_instancemethod(_itkDistanceMetricPython.itkDistanceMetricVF2_Evaluate, None, itkDistanceMetricVF2)
itkDistanceMetricVF2.SetMeasurementVectorSize = new_instancemethod(_itkDistanceMetricPython.itkDistanceMetricVF2_SetMeasurementVectorSize, None, itkDistanceMetricVF2)
itkDistanceMetricVF2.GetMeasurementVectorSize = new_instancemethod(_itkDistanceMetricPython.itkDistanceMetricVF2_GetMeasurementVectorSize, None, itkDistanceMetricVF2)
itkDistanceMetricVF2_swigregister = _itkDistanceMetricPython.itkDistanceMetricVF2_swigregister
itkDistanceMetricVF2_swigregister(itkDistanceMetricVF2)

def itkDistanceMetricVF2_cast(obj: 'itkLightObject') -> "itkDistanceMetricVF2 *":
    """itkDistanceMetricVF2_cast(itkLightObject obj) -> itkDistanceMetricVF2"""
    return _itkDistanceMetricPython.itkDistanceMetricVF2_cast(obj)

class itkDistanceMetricVF3(itkFunctionBasePython.itkFunctionBaseVF3D):
    """


    this class declares common interfaces for distance functions.

    As a function derived from FunctionBase, users use Evaluate method to
    get result.

    To use this function users should first set the origin by calling
    SetOrigin() function, then call Evaluate() method with a point to get
    the distance between the origin point and the evaluation point.

    See:  EuclideanSquareDistanceMetric

    See:   EuclideanDistanceMetric

    See:  ManhattanDistanceMetric

    C++ includes: itkDistanceMetric.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def SetOrigin(self, x: 'itkArrayD') -> "void":
        """
        SetOrigin(itkDistanceMetricVF3 self, itkArrayD x)

        Sets the origin point
        that will be used for the single point version Evaluate() function.
        This function is necessary part of implementing the Evaluate()
        interface. The argument of SetOrigin() must be of type
        DistanceMetric::OriginType, which in most cases will be different from
        the TVector type. This is necessary because often times the origin
        would be a mean, or a vector representative of a collection of
        vectors. 
        """
        return _itkDistanceMetricPython.itkDistanceMetricVF3_SetOrigin(self, x)


    def GetOrigin(self) -> "itkArrayD const &":
        """GetOrigin(itkDistanceMetricVF3 self) -> itkArrayD"""
        return _itkDistanceMetricPython.itkDistanceMetricVF3_GetOrigin(self)


    def Evaluate(self, *args) -> "double":
        """
        Evaluate(itkDistanceMetricVF3 self, itkVectorF3 x) -> double
        Evaluate(itkDistanceMetricVF3 self, itkVectorF3 x1, itkVectorF3 x2) -> double

        Gets the distance between
        x1 and x2. This method is used by KdTreeKMeans estimators. When the
        estimator is refactored, this method should be removed. Distance
        between two measurement vectors can be computed by setting one of them
        as an origin of the distane and using the Evaluate method with a
        single argument 
        """
        return _itkDistanceMetricPython.itkDistanceMetricVF3_Evaluate(self, *args)


    def SetMeasurementVectorSize(self, s: 'unsigned int') -> "void":
        """
        SetMeasurementVectorSize(itkDistanceMetricVF3 self, unsigned int s)

        Set method
        for the length of the measurement vector 
        """
        return _itkDistanceMetricPython.itkDistanceMetricVF3_SetMeasurementVectorSize(self, s)


    def GetMeasurementVectorSize(self) -> "unsigned int":
        """
        GetMeasurementVectorSize(itkDistanceMetricVF3 self) -> unsigned int

        Get method
        for the length of the measurement vector 
        """
        return _itkDistanceMetricPython.itkDistanceMetricVF3_GetMeasurementVectorSize(self)

    __swig_destroy__ = _itkDistanceMetricPython.delete_itkDistanceMetricVF3

    def cast(obj: 'itkLightObject') -> "itkDistanceMetricVF3 *":
        """cast(itkLightObject obj) -> itkDistanceMetricVF3"""
        return _itkDistanceMetricPython.itkDistanceMetricVF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkDistanceMetricVF3

        Create a new object of the class itkDistanceMetricVF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDistanceMetricVF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkDistanceMetricVF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkDistanceMetricVF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkDistanceMetricVF3.SetOrigin = new_instancemethod(_itkDistanceMetricPython.itkDistanceMetricVF3_SetOrigin, None, itkDistanceMetricVF3)
itkDistanceMetricVF3.GetOrigin = new_instancemethod(_itkDistanceMetricPython.itkDistanceMetricVF3_GetOrigin, None, itkDistanceMetricVF3)
itkDistanceMetricVF3.Evaluate = new_instancemethod(_itkDistanceMetricPython.itkDistanceMetricVF3_Evaluate, None, itkDistanceMetricVF3)
itkDistanceMetricVF3.SetMeasurementVectorSize = new_instancemethod(_itkDistanceMetricPython.itkDistanceMetricVF3_SetMeasurementVectorSize, None, itkDistanceMetricVF3)
itkDistanceMetricVF3.GetMeasurementVectorSize = new_instancemethod(_itkDistanceMetricPython.itkDistanceMetricVF3_GetMeasurementVectorSize, None, itkDistanceMetricVF3)
itkDistanceMetricVF3_swigregister = _itkDistanceMetricPython.itkDistanceMetricVF3_swigregister
itkDistanceMetricVF3_swigregister(itkDistanceMetricVF3)

def itkDistanceMetricVF3_cast(obj: 'itkLightObject') -> "itkDistanceMetricVF3 *":
    """itkDistanceMetricVF3_cast(itkLightObject obj) -> itkDistanceMetricVF3"""
    return _itkDistanceMetricPython.itkDistanceMetricVF3_cast(obj)



