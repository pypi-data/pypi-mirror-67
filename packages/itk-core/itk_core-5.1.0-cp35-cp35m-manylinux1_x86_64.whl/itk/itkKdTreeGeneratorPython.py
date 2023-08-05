# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkKdTreeGeneratorPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkKdTreeGeneratorPython', [dirname(__file__)])
        except ImportError:
            import _itkKdTreeGeneratorPython
            return _itkKdTreeGeneratorPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkKdTreeGeneratorPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkKdTreeGeneratorPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkKdTreeGeneratorPython
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


import itkKdTreePython
import itkListSamplePython
import ITKCommonBasePython
import pyBasePython
import itkVectorPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkSamplePython
import itkArrayPython
import itkEuclideanDistanceMetricPython
import itkDistanceMetricPython
import itkFunctionBasePython
import itkRGBPixelPython
import itkPointPython
import itkCovariantVectorPython
import itkImagePython
import itkImageRegionPython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkRGBAPixelPython
import itkContinuousIndexPython

def itkKdTreeGeneratorLSVF3_New():
  return itkKdTreeGeneratorLSVF3.New()


def itkKdTreeGeneratorLSVF2_New():
  return itkKdTreeGeneratorLSVF2.New()

class itkKdTreeGeneratorLSVF2(ITKCommonBasePython.itkObject):
    """


    This class generates a KdTree object without centroid information.

    The KdTree object stores measurement vectors in a k-d tree structure
    that is a binary tree. The partition value is the median value of one
    of the k dimension (partition dimension). The partition dimension is
    determined by the spread of measurement values in each dimension. The
    partition dimension is the dimension has the widest spread. Our
    implementation of k-d tree doesn't have any construction or insertion
    logic. Users should use this class or the
    WeightedCentroidKdTreeGenerator class.

    The number of the measurement vectors in a terminal node is set by the
    SetBucketSize method. If we use too small number for this, it might
    cause computational overhead to calculate bound conditions. However,
    too large number will cause more distance calculation between the
    measurement vectors in a terminal node and the query point.

    To run this generator, users should provides the bucket size
    (SetBucketSize method) and the input sample (SetSample method). The
    Update method will run this generator. To get the resulting KdTree
    object, call the GetOutput method.

    Recent API changes: The static const macro to get the length of a
    measurement vector, 'MeasurementVectorSize' has been removed to allow
    the length of a measurement vector to be specified at run time. It is
    now obtained from the sample set as input. You may query this length
    using the function GetMeasurementVectorSize().

    See:   KdTree, KdTreeNode, KdTreeNonterminalNode, KdTreeTerminalNode,
    WeightedCentroidKdTreeGenerator

    C++ includes: itkKdTreeGenerator.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkKdTreeGeneratorLSVF2_Pointer":
        """__New_orig__() -> itkKdTreeGeneratorLSVF2_Pointer"""
        return _itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkKdTreeGeneratorLSVF2_Pointer":
        """Clone(itkKdTreeGeneratorLSVF2 self) -> itkKdTreeGeneratorLSVF2_Pointer"""
        return _itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF2_Clone(self)


    def SetSample(self, sample: 'itkListSampleVF2') -> "void":
        """
        SetSample(itkKdTreeGeneratorLSVF2 self, itkListSampleVF2 sample)

        Sets the input sample
        that provides the measurement vectors. 
        """
        return _itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF2_SetSample(self, sample)


    def SetBucketSize(self, size: 'unsigned int') -> "void":
        """
        SetBucketSize(itkKdTreeGeneratorLSVF2 self, unsigned int size)

        Sets the number of
        measurement vectors that can be stored in a terminal node. 
        """
        return _itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF2_SetBucketSize(self, size)


    def GetOutput(self) -> "itkKdTreeLSVF2_Pointer":
        """
        GetOutput(itkKdTreeGeneratorLSVF2 self) -> itkKdTreeLSVF2_Pointer

        Returns the pointer to
        the generated k-d tree. 
        """
        return _itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF2_GetOutput(self)


    def Update(self) -> "void":
        """
        Update(itkKdTreeGeneratorLSVF2 self)

        Runs this k-d tree
        construction algorithm. 
        """
        return _itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF2_Update(self)


    def GenerateData(self) -> "void":
        """
        GenerateData(itkKdTreeGeneratorLSVF2 self)

        Runs this k-d tree
        construction algorithm. 
        """
        return _itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF2_GenerateData(self)


    def GetMeasurementVectorSize(self) -> "unsigned int":
        """
        GetMeasurementVectorSize(itkKdTreeGeneratorLSVF2 self) -> unsigned int

        Get macro
        to get the length of the measurement vectors that are being held in
        the 'sample' that is passed to this class 
        """
        return _itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF2_GetMeasurementVectorSize(self)

    __swig_destroy__ = _itkKdTreeGeneratorPython.delete_itkKdTreeGeneratorLSVF2

    def cast(obj: 'itkLightObject') -> "itkKdTreeGeneratorLSVF2 *":
        """cast(itkLightObject obj) -> itkKdTreeGeneratorLSVF2"""
        return _itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkKdTreeGeneratorLSVF2

        Create a new object of the class itkKdTreeGeneratorLSVF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkKdTreeGeneratorLSVF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkKdTreeGeneratorLSVF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkKdTreeGeneratorLSVF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkKdTreeGeneratorLSVF2.Clone = new_instancemethod(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF2_Clone, None, itkKdTreeGeneratorLSVF2)
itkKdTreeGeneratorLSVF2.SetSample = new_instancemethod(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF2_SetSample, None, itkKdTreeGeneratorLSVF2)
itkKdTreeGeneratorLSVF2.SetBucketSize = new_instancemethod(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF2_SetBucketSize, None, itkKdTreeGeneratorLSVF2)
itkKdTreeGeneratorLSVF2.GetOutput = new_instancemethod(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF2_GetOutput, None, itkKdTreeGeneratorLSVF2)
itkKdTreeGeneratorLSVF2.Update = new_instancemethod(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF2_Update, None, itkKdTreeGeneratorLSVF2)
itkKdTreeGeneratorLSVF2.GenerateData = new_instancemethod(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF2_GenerateData, None, itkKdTreeGeneratorLSVF2)
itkKdTreeGeneratorLSVF2.GetMeasurementVectorSize = new_instancemethod(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF2_GetMeasurementVectorSize, None, itkKdTreeGeneratorLSVF2)
itkKdTreeGeneratorLSVF2_swigregister = _itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF2_swigregister
itkKdTreeGeneratorLSVF2_swigregister(itkKdTreeGeneratorLSVF2)

def itkKdTreeGeneratorLSVF2___New_orig__() -> "itkKdTreeGeneratorLSVF2_Pointer":
    """itkKdTreeGeneratorLSVF2___New_orig__() -> itkKdTreeGeneratorLSVF2_Pointer"""
    return _itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF2___New_orig__()

def itkKdTreeGeneratorLSVF2_cast(obj: 'itkLightObject') -> "itkKdTreeGeneratorLSVF2 *":
    """itkKdTreeGeneratorLSVF2_cast(itkLightObject obj) -> itkKdTreeGeneratorLSVF2"""
    return _itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF2_cast(obj)

class itkKdTreeGeneratorLSVF3(ITKCommonBasePython.itkObject):
    """


    This class generates a KdTree object without centroid information.

    The KdTree object stores measurement vectors in a k-d tree structure
    that is a binary tree. The partition value is the median value of one
    of the k dimension (partition dimension). The partition dimension is
    determined by the spread of measurement values in each dimension. The
    partition dimension is the dimension has the widest spread. Our
    implementation of k-d tree doesn't have any construction or insertion
    logic. Users should use this class or the
    WeightedCentroidKdTreeGenerator class.

    The number of the measurement vectors in a terminal node is set by the
    SetBucketSize method. If we use too small number for this, it might
    cause computational overhead to calculate bound conditions. However,
    too large number will cause more distance calculation between the
    measurement vectors in a terminal node and the query point.

    To run this generator, users should provides the bucket size
    (SetBucketSize method) and the input sample (SetSample method). The
    Update method will run this generator. To get the resulting KdTree
    object, call the GetOutput method.

    Recent API changes: The static const macro to get the length of a
    measurement vector, 'MeasurementVectorSize' has been removed to allow
    the length of a measurement vector to be specified at run time. It is
    now obtained from the sample set as input. You may query this length
    using the function GetMeasurementVectorSize().

    See:   KdTree, KdTreeNode, KdTreeNonterminalNode, KdTreeTerminalNode,
    WeightedCentroidKdTreeGenerator

    C++ includes: itkKdTreeGenerator.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkKdTreeGeneratorLSVF3_Pointer":
        """__New_orig__() -> itkKdTreeGeneratorLSVF3_Pointer"""
        return _itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkKdTreeGeneratorLSVF3_Pointer":
        """Clone(itkKdTreeGeneratorLSVF3 self) -> itkKdTreeGeneratorLSVF3_Pointer"""
        return _itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF3_Clone(self)


    def SetSample(self, sample: 'itkListSampleVF3') -> "void":
        """
        SetSample(itkKdTreeGeneratorLSVF3 self, itkListSampleVF3 sample)

        Sets the input sample
        that provides the measurement vectors. 
        """
        return _itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF3_SetSample(self, sample)


    def SetBucketSize(self, size: 'unsigned int') -> "void":
        """
        SetBucketSize(itkKdTreeGeneratorLSVF3 self, unsigned int size)

        Sets the number of
        measurement vectors that can be stored in a terminal node. 
        """
        return _itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF3_SetBucketSize(self, size)


    def GetOutput(self) -> "itkKdTreeLSVF3_Pointer":
        """
        GetOutput(itkKdTreeGeneratorLSVF3 self) -> itkKdTreeLSVF3_Pointer

        Returns the pointer to
        the generated k-d tree. 
        """
        return _itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF3_GetOutput(self)


    def Update(self) -> "void":
        """
        Update(itkKdTreeGeneratorLSVF3 self)

        Runs this k-d tree
        construction algorithm. 
        """
        return _itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF3_Update(self)


    def GenerateData(self) -> "void":
        """
        GenerateData(itkKdTreeGeneratorLSVF3 self)

        Runs this k-d tree
        construction algorithm. 
        """
        return _itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF3_GenerateData(self)


    def GetMeasurementVectorSize(self) -> "unsigned int":
        """
        GetMeasurementVectorSize(itkKdTreeGeneratorLSVF3 self) -> unsigned int

        Get macro
        to get the length of the measurement vectors that are being held in
        the 'sample' that is passed to this class 
        """
        return _itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF3_GetMeasurementVectorSize(self)

    __swig_destroy__ = _itkKdTreeGeneratorPython.delete_itkKdTreeGeneratorLSVF3

    def cast(obj: 'itkLightObject') -> "itkKdTreeGeneratorLSVF3 *":
        """cast(itkLightObject obj) -> itkKdTreeGeneratorLSVF3"""
        return _itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkKdTreeGeneratorLSVF3

        Create a new object of the class itkKdTreeGeneratorLSVF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkKdTreeGeneratorLSVF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkKdTreeGeneratorLSVF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkKdTreeGeneratorLSVF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkKdTreeGeneratorLSVF3.Clone = new_instancemethod(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF3_Clone, None, itkKdTreeGeneratorLSVF3)
itkKdTreeGeneratorLSVF3.SetSample = new_instancemethod(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF3_SetSample, None, itkKdTreeGeneratorLSVF3)
itkKdTreeGeneratorLSVF3.SetBucketSize = new_instancemethod(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF3_SetBucketSize, None, itkKdTreeGeneratorLSVF3)
itkKdTreeGeneratorLSVF3.GetOutput = new_instancemethod(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF3_GetOutput, None, itkKdTreeGeneratorLSVF3)
itkKdTreeGeneratorLSVF3.Update = new_instancemethod(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF3_Update, None, itkKdTreeGeneratorLSVF3)
itkKdTreeGeneratorLSVF3.GenerateData = new_instancemethod(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF3_GenerateData, None, itkKdTreeGeneratorLSVF3)
itkKdTreeGeneratorLSVF3.GetMeasurementVectorSize = new_instancemethod(_itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF3_GetMeasurementVectorSize, None, itkKdTreeGeneratorLSVF3)
itkKdTreeGeneratorLSVF3_swigregister = _itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF3_swigregister
itkKdTreeGeneratorLSVF3_swigregister(itkKdTreeGeneratorLSVF3)

def itkKdTreeGeneratorLSVF3___New_orig__() -> "itkKdTreeGeneratorLSVF3_Pointer":
    """itkKdTreeGeneratorLSVF3___New_orig__() -> itkKdTreeGeneratorLSVF3_Pointer"""
    return _itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF3___New_orig__()

def itkKdTreeGeneratorLSVF3_cast(obj: 'itkLightObject') -> "itkKdTreeGeneratorLSVF3 *":
    """itkKdTreeGeneratorLSVF3_cast(itkLightObject obj) -> itkKdTreeGeneratorLSVF3"""
    return _itkKdTreeGeneratorPython.itkKdTreeGeneratorLSVF3_cast(obj)



