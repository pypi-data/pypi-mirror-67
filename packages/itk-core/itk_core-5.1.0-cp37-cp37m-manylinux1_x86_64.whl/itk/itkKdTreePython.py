# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkKdTreePython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkKdTreePython', [dirname(__file__)])
        except ImportError:
            import _itkKdTreePython
            return _itkKdTreePython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkKdTreePython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkKdTreePython = swig_import_helper()
    del swig_import_helper
else:
    import _itkKdTreePython
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


import itkEuclideanDistanceMetricPython
import itkDistanceMetricPython
import ITKCommonBasePython
import pyBasePython
import itkArrayPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkVectorPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkFunctionBasePython
import itkPointPython
import itkRGBAPixelPython
import itkCovariantVectorPython
import itkImagePython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkIndexPython
import itkSizePython
import itkOffsetPython
import itkImageRegionPython
import itkRGBPixelPython
import itkSymmetricSecondRankTensorPython
import itkContinuousIndexPython
import itkListSamplePython
import itkSamplePython

def itkKdTreeLSVF3_New():
  return itkKdTreeLSVF3.New()


def itkKdTreeLSVF2_New():
  return itkKdTreeLSVF2.New()

class itkKdTreeLSVF2(ITKCommonBasePython.itkObject):
    """


    This class provides methods for k-nearest neighbor search and related
    data structures for a k-d tree.

    An object of this class stores instance identifiers in a k-d tree that
    is a binary tree with childrens split along a dimension among
    k-dimensions. The dimension of the split (or partition) is determined
    for each nonterminal node that has two children. The split process is
    terminated when the node has no children (when the number of
    measurement vectors is less than or equal to the size set by the
    SetBucketSize. That is The split process is a recursive process in
    nature and in implementation. This implementation doesn't support
    dynamic insert and delete operations for the tree. Instead, we can use
    the KdTreeGenerator or WeightedCentroidKdTreeGenerator to generate a
    static KdTree object.

    To search k-nearest neighbor, call the Search method with the query
    point in a k-d space and the number of nearest neighbors. The
    GetSearchResult method returns a pointer to a NearestNeighbors object
    with k-nearest neighbors.

    Recent API changes: The static const macro to get the length of a
    measurement vector, 'MeasurementVectorSize' has been removed to allow
    the length of a measurement vector to be specified at run time. Please
    use the function GetMeasurementVectorSize() instead.

    See:   KdTreeNode, KdTreeNonterminalNode,
    KdTreeWeightedCentroidNonterminalNode, KdTreeTerminalNode,
    KdTreeGenerator, WeightedCentroidKdTreeNode

    C++ includes: itkKdTree.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkKdTreeLSVF2_Pointer":
        """__New_orig__() -> itkKdTreeLSVF2_Pointer"""
        return _itkKdTreePython.itkKdTreeLSVF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkKdTreeLSVF2_Pointer":
        """Clone(itkKdTreeLSVF2 self) -> itkKdTreeLSVF2_Pointer"""
        return _itkKdTreePython.itkKdTreeLSVF2_Clone(self)


    def GetMeasurementVectorSize(self) -> "unsigned int":
        """
        GetMeasurementVectorSize(itkKdTreeLSVF2 self) -> unsigned int

        Get Macro
        to get the length of a measurement vector in the KdTree. The length is
        obtained from the input sample. 
        """
        return _itkKdTreePython.itkKdTreeLSVF2_GetMeasurementVectorSize(self)


    def SetBucketSize(self, arg0: 'unsigned int') -> "void":
        """
        SetBucketSize(itkKdTreeLSVF2 self, unsigned int arg0)

        Sets the number of
        measurement vectors that can be stored in a terminal node 
        """
        return _itkKdTreePython.itkKdTreeLSVF2_SetBucketSize(self, arg0)


    def SetSample(self, arg0: 'itkListSampleVF2') -> "void":
        """
        SetSample(itkKdTreeLSVF2 self, itkListSampleVF2 arg0)

        Sets the input sample
        that provides the measurement vectors to the k-d tree 
        """
        return _itkKdTreePython.itkKdTreeLSVF2_SetSample(self, arg0)


    def GetSample(self) -> "itkListSampleVF2 const *":
        """
        GetSample(itkKdTreeLSVF2 self) -> itkListSampleVF2

        Returns the pointer to
        the input sample 
        """
        return _itkKdTreePython.itkKdTreeLSVF2_GetSample(self)


    def Size(self) -> "unsigned long":
        """Size(itkKdTreeLSVF2 self) -> unsigned long"""
        return _itkKdTreePython.itkKdTreeLSVF2_Size(self)


    def GetEmptyTerminalNode(self) -> "itkKdTreeNodeLSVF2 *":
        """
        GetEmptyTerminalNode(itkKdTreeLSVF2 self) -> itkKdTreeNodeLSVF2

        Returns the
        pointer to the empty terminal node. A KdTree object has a single empty
        terminal node in memory. when the split process has to create an empty
        terminal node, the single instance is reused for this case 
        """
        return _itkKdTreePython.itkKdTreeLSVF2_GetEmptyTerminalNode(self)


    def SetRoot(self, root: 'itkKdTreeNodeLSVF2') -> "void":
        """
        SetRoot(itkKdTreeLSVF2 self, itkKdTreeNodeLSVF2 root)

        Sets the root node of the
        KdTree that is a result of KdTreeGenerator or
        WeightedCentroidKdTreeGenerator. 
        """
        return _itkKdTreePython.itkKdTreeLSVF2_SetRoot(self, root)


    def GetRoot(self) -> "itkKdTreeNodeLSVF2 *":
        """
        GetRoot(itkKdTreeLSVF2 self) -> itkKdTreeNodeLSVF2

        Returns the pointer to the
        root node. 
        """
        return _itkKdTreePython.itkKdTreeLSVF2_GetRoot(self)


    def GetMeasurementVector(self, id: 'unsigned long') -> "itkVectorF2 const &":
        """
        GetMeasurementVector(itkKdTreeLSVF2 self, unsigned long id) -> itkVectorF2

        Returns the
        measurement vector identified by the instance identifier that is an
        identifier defiend for the input sample 
        """
        return _itkKdTreePython.itkKdTreeLSVF2_GetMeasurementVector(self, id)


    def GetFrequency(self, id: 'unsigned long') -> "unsigned long":
        """
        GetFrequency(itkKdTreeLSVF2 self, unsigned long id) -> unsigned long

        Returns the frequency
        of the measurement vector identified by the instance identifier 
        """
        return _itkKdTreePython.itkKdTreeLSVF2_GetFrequency(self, id)


    def GetDistanceMetric(self) -> "itkEuclideanDistanceMetricVF2 *":
        """
        GetDistanceMetric(itkKdTreeLSVF2 self) -> itkEuclideanDistanceMetricVF2

        Get the pointer
        to the distance metric. 
        """
        return _itkKdTreePython.itkKdTreeLSVF2_GetDistanceMetric(self)


    def Search(self, *args) -> "void":
        """
        Search(itkKdTreeLSVF2 self, itkVectorF2 arg0, unsigned int arg1, vectorUL arg2)
        Search(itkKdTreeLSVF2 self, itkVectorF2 arg0, unsigned int arg1, vectorUL arg2, vectorD arg3)
        Search(itkKdTreeLSVF2 self, itkVectorF2 arg0, double arg1, vectorUL arg2)

        Searches the neighbors
        fallen into a hypersphere 
        """
        return _itkKdTreePython.itkKdTreeLSVF2_Search(self, *args)


    def BallWithinBounds(self, arg0: 'itkVectorF2', arg1: 'itkVectorF2', arg2: 'itkVectorF2', arg3: 'double') -> "bool":
        """
        BallWithinBounds(itkKdTreeLSVF2 self, itkVectorF2 arg0, itkVectorF2 arg1, itkVectorF2 arg2, double arg3) -> bool

        Returns true if
        the intermediate k-nearest neighbors exist within the the bounding box
        defined by the lowerBound and the upperBound. Otherwise returns false.
        Returns false if the ball defined by the distance between the query
        point and the farthest neighbor touch the surface of the bounding box.

        """
        return _itkKdTreePython.itkKdTreeLSVF2_BallWithinBounds(self, arg0, arg1, arg2, arg3)


    def BoundsOverlapBall(self, arg0: 'itkVectorF2', arg1: 'itkVectorF2', arg2: 'itkVectorF2', arg3: 'double') -> "bool":
        """
        BoundsOverlapBall(itkKdTreeLSVF2 self, itkVectorF2 arg0, itkVectorF2 arg1, itkVectorF2 arg2, double arg3) -> bool

        Returns true if
        the ball defined by the distance between the query point and the
        farthest neighbor overlaps with the bounding box defined by the lower
        and the upper bounds. 
        """
        return _itkKdTreePython.itkKdTreeLSVF2_BoundsOverlapBall(self, arg0, arg1, arg2, arg3)


    def DeleteNode(self, arg0: 'itkKdTreeNodeLSVF2') -> "void":
        """
        DeleteNode(itkKdTreeLSVF2 self, itkKdTreeNodeLSVF2 arg0)

        Deletes the node
        recursively 
        """
        return _itkKdTreePython.itkKdTreeLSVF2_DeleteNode(self, arg0)


    def PrintTree(self, *args) -> "void":
        """
        PrintTree(itkKdTreeLSVF2 self, ostream arg0)
        PrintTree(itkKdTreeLSVF2 self, itkKdTreeNodeLSVF2 arg0, unsigned int arg1, unsigned int arg2, ostream os)
        PrintTree(itkKdTreeLSVF2 self, itkKdTreeNodeLSVF2 arg0, unsigned int arg1, unsigned int arg2)

        Prints out the tree
        information 
        """
        return _itkKdTreePython.itkKdTreeLSVF2_PrintTree(self, *args)


    def PlotTree(self, *args) -> "void":
        """
        PlotTree(itkKdTreeLSVF2 self, ostream os)
        PlotTree(itkKdTreeLSVF2 self, itkKdTreeNodeLSVF2 node, ostream os)
        PlotTree(itkKdTreeLSVF2 self, itkKdTreeNodeLSVF2 node)

        Prints out the tree
        information 
        """
        return _itkKdTreePython.itkKdTreeLSVF2_PlotTree(self, *args)

    __swig_destroy__ = _itkKdTreePython.delete_itkKdTreeLSVF2

    def cast(obj: 'itkLightObject') -> "itkKdTreeLSVF2 *":
        """cast(itkLightObject obj) -> itkKdTreeLSVF2"""
        return _itkKdTreePython.itkKdTreeLSVF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkKdTreeLSVF2

        Create a new object of the class itkKdTreeLSVF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkKdTreeLSVF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkKdTreeLSVF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkKdTreeLSVF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkKdTreeLSVF2.Clone = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_Clone, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.GetMeasurementVectorSize = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_GetMeasurementVectorSize, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.SetBucketSize = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_SetBucketSize, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.SetSample = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_SetSample, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.GetSample = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_GetSample, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.Size = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_Size, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.GetEmptyTerminalNode = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_GetEmptyTerminalNode, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.SetRoot = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_SetRoot, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.GetRoot = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_GetRoot, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.GetMeasurementVector = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_GetMeasurementVector, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.GetFrequency = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_GetFrequency, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.GetDistanceMetric = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_GetDistanceMetric, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.Search = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_Search, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.BallWithinBounds = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_BallWithinBounds, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.BoundsOverlapBall = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_BoundsOverlapBall, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.DeleteNode = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_DeleteNode, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.PrintTree = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_PrintTree, None, itkKdTreeLSVF2)
itkKdTreeLSVF2.PlotTree = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF2_PlotTree, None, itkKdTreeLSVF2)
itkKdTreeLSVF2_swigregister = _itkKdTreePython.itkKdTreeLSVF2_swigregister
itkKdTreeLSVF2_swigregister(itkKdTreeLSVF2)

def itkKdTreeLSVF2___New_orig__() -> "itkKdTreeLSVF2_Pointer":
    """itkKdTreeLSVF2___New_orig__() -> itkKdTreeLSVF2_Pointer"""
    return _itkKdTreePython.itkKdTreeLSVF2___New_orig__()

def itkKdTreeLSVF2_cast(obj: 'itkLightObject') -> "itkKdTreeLSVF2 *":
    """itkKdTreeLSVF2_cast(itkLightObject obj) -> itkKdTreeLSVF2"""
    return _itkKdTreePython.itkKdTreeLSVF2_cast(obj)

class itkKdTreeLSVF3(ITKCommonBasePython.itkObject):
    """


    This class provides methods for k-nearest neighbor search and related
    data structures for a k-d tree.

    An object of this class stores instance identifiers in a k-d tree that
    is a binary tree with childrens split along a dimension among
    k-dimensions. The dimension of the split (or partition) is determined
    for each nonterminal node that has two children. The split process is
    terminated when the node has no children (when the number of
    measurement vectors is less than or equal to the size set by the
    SetBucketSize. That is The split process is a recursive process in
    nature and in implementation. This implementation doesn't support
    dynamic insert and delete operations for the tree. Instead, we can use
    the KdTreeGenerator or WeightedCentroidKdTreeGenerator to generate a
    static KdTree object.

    To search k-nearest neighbor, call the Search method with the query
    point in a k-d space and the number of nearest neighbors. The
    GetSearchResult method returns a pointer to a NearestNeighbors object
    with k-nearest neighbors.

    Recent API changes: The static const macro to get the length of a
    measurement vector, 'MeasurementVectorSize' has been removed to allow
    the length of a measurement vector to be specified at run time. Please
    use the function GetMeasurementVectorSize() instead.

    See:   KdTreeNode, KdTreeNonterminalNode,
    KdTreeWeightedCentroidNonterminalNode, KdTreeTerminalNode,
    KdTreeGenerator, WeightedCentroidKdTreeNode

    C++ includes: itkKdTree.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkKdTreeLSVF3_Pointer":
        """__New_orig__() -> itkKdTreeLSVF3_Pointer"""
        return _itkKdTreePython.itkKdTreeLSVF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkKdTreeLSVF3_Pointer":
        """Clone(itkKdTreeLSVF3 self) -> itkKdTreeLSVF3_Pointer"""
        return _itkKdTreePython.itkKdTreeLSVF3_Clone(self)


    def GetMeasurementVectorSize(self) -> "unsigned int":
        """
        GetMeasurementVectorSize(itkKdTreeLSVF3 self) -> unsigned int

        Get Macro
        to get the length of a measurement vector in the KdTree. The length is
        obtained from the input sample. 
        """
        return _itkKdTreePython.itkKdTreeLSVF3_GetMeasurementVectorSize(self)


    def SetBucketSize(self, arg0: 'unsigned int') -> "void":
        """
        SetBucketSize(itkKdTreeLSVF3 self, unsigned int arg0)

        Sets the number of
        measurement vectors that can be stored in a terminal node 
        """
        return _itkKdTreePython.itkKdTreeLSVF3_SetBucketSize(self, arg0)


    def SetSample(self, arg0: 'itkListSampleVF3') -> "void":
        """
        SetSample(itkKdTreeLSVF3 self, itkListSampleVF3 arg0)

        Sets the input sample
        that provides the measurement vectors to the k-d tree 
        """
        return _itkKdTreePython.itkKdTreeLSVF3_SetSample(self, arg0)


    def GetSample(self) -> "itkListSampleVF3 const *":
        """
        GetSample(itkKdTreeLSVF3 self) -> itkListSampleVF3

        Returns the pointer to
        the input sample 
        """
        return _itkKdTreePython.itkKdTreeLSVF3_GetSample(self)


    def Size(self) -> "unsigned long":
        """Size(itkKdTreeLSVF3 self) -> unsigned long"""
        return _itkKdTreePython.itkKdTreeLSVF3_Size(self)


    def GetEmptyTerminalNode(self) -> "itkKdTreeNodeLSVF3 *":
        """
        GetEmptyTerminalNode(itkKdTreeLSVF3 self) -> itkKdTreeNodeLSVF3

        Returns the
        pointer to the empty terminal node. A KdTree object has a single empty
        terminal node in memory. when the split process has to create an empty
        terminal node, the single instance is reused for this case 
        """
        return _itkKdTreePython.itkKdTreeLSVF3_GetEmptyTerminalNode(self)


    def SetRoot(self, root: 'itkKdTreeNodeLSVF3') -> "void":
        """
        SetRoot(itkKdTreeLSVF3 self, itkKdTreeNodeLSVF3 root)

        Sets the root node of the
        KdTree that is a result of KdTreeGenerator or
        WeightedCentroidKdTreeGenerator. 
        """
        return _itkKdTreePython.itkKdTreeLSVF3_SetRoot(self, root)


    def GetRoot(self) -> "itkKdTreeNodeLSVF3 *":
        """
        GetRoot(itkKdTreeLSVF3 self) -> itkKdTreeNodeLSVF3

        Returns the pointer to the
        root node. 
        """
        return _itkKdTreePython.itkKdTreeLSVF3_GetRoot(self)


    def GetMeasurementVector(self, id: 'unsigned long') -> "itkVectorF3 const &":
        """
        GetMeasurementVector(itkKdTreeLSVF3 self, unsigned long id) -> itkVectorF3

        Returns the
        measurement vector identified by the instance identifier that is an
        identifier defiend for the input sample 
        """
        return _itkKdTreePython.itkKdTreeLSVF3_GetMeasurementVector(self, id)


    def GetFrequency(self, id: 'unsigned long') -> "unsigned long":
        """
        GetFrequency(itkKdTreeLSVF3 self, unsigned long id) -> unsigned long

        Returns the frequency
        of the measurement vector identified by the instance identifier 
        """
        return _itkKdTreePython.itkKdTreeLSVF3_GetFrequency(self, id)


    def GetDistanceMetric(self) -> "itkEuclideanDistanceMetricVF3 *":
        """
        GetDistanceMetric(itkKdTreeLSVF3 self) -> itkEuclideanDistanceMetricVF3

        Get the pointer
        to the distance metric. 
        """
        return _itkKdTreePython.itkKdTreeLSVF3_GetDistanceMetric(self)


    def Search(self, *args) -> "void":
        """
        Search(itkKdTreeLSVF3 self, itkVectorF3 arg0, unsigned int arg1, vectorUL arg2)
        Search(itkKdTreeLSVF3 self, itkVectorF3 arg0, unsigned int arg1, vectorUL arg2, vectorD arg3)
        Search(itkKdTreeLSVF3 self, itkVectorF3 arg0, double arg1, vectorUL arg2)

        Searches the neighbors
        fallen into a hypersphere 
        """
        return _itkKdTreePython.itkKdTreeLSVF3_Search(self, *args)


    def BallWithinBounds(self, arg0: 'itkVectorF3', arg1: 'itkVectorF3', arg2: 'itkVectorF3', arg3: 'double') -> "bool":
        """
        BallWithinBounds(itkKdTreeLSVF3 self, itkVectorF3 arg0, itkVectorF3 arg1, itkVectorF3 arg2, double arg3) -> bool

        Returns true if
        the intermediate k-nearest neighbors exist within the the bounding box
        defined by the lowerBound and the upperBound. Otherwise returns false.
        Returns false if the ball defined by the distance between the query
        point and the farthest neighbor touch the surface of the bounding box.

        """
        return _itkKdTreePython.itkKdTreeLSVF3_BallWithinBounds(self, arg0, arg1, arg2, arg3)


    def BoundsOverlapBall(self, arg0: 'itkVectorF3', arg1: 'itkVectorF3', arg2: 'itkVectorF3', arg3: 'double') -> "bool":
        """
        BoundsOverlapBall(itkKdTreeLSVF3 self, itkVectorF3 arg0, itkVectorF3 arg1, itkVectorF3 arg2, double arg3) -> bool

        Returns true if
        the ball defined by the distance between the query point and the
        farthest neighbor overlaps with the bounding box defined by the lower
        and the upper bounds. 
        """
        return _itkKdTreePython.itkKdTreeLSVF3_BoundsOverlapBall(self, arg0, arg1, arg2, arg3)


    def DeleteNode(self, arg0: 'itkKdTreeNodeLSVF3') -> "void":
        """
        DeleteNode(itkKdTreeLSVF3 self, itkKdTreeNodeLSVF3 arg0)

        Deletes the node
        recursively 
        """
        return _itkKdTreePython.itkKdTreeLSVF3_DeleteNode(self, arg0)


    def PrintTree(self, *args) -> "void":
        """
        PrintTree(itkKdTreeLSVF3 self, ostream arg0)
        PrintTree(itkKdTreeLSVF3 self, itkKdTreeNodeLSVF3 arg0, unsigned int arg1, unsigned int arg2, ostream os)
        PrintTree(itkKdTreeLSVF3 self, itkKdTreeNodeLSVF3 arg0, unsigned int arg1, unsigned int arg2)

        Prints out the tree
        information 
        """
        return _itkKdTreePython.itkKdTreeLSVF3_PrintTree(self, *args)


    def PlotTree(self, *args) -> "void":
        """
        PlotTree(itkKdTreeLSVF3 self, ostream os)
        PlotTree(itkKdTreeLSVF3 self, itkKdTreeNodeLSVF3 node, ostream os)
        PlotTree(itkKdTreeLSVF3 self, itkKdTreeNodeLSVF3 node)

        Prints out the tree
        information 
        """
        return _itkKdTreePython.itkKdTreeLSVF3_PlotTree(self, *args)

    __swig_destroy__ = _itkKdTreePython.delete_itkKdTreeLSVF3

    def cast(obj: 'itkLightObject') -> "itkKdTreeLSVF3 *":
        """cast(itkLightObject obj) -> itkKdTreeLSVF3"""
        return _itkKdTreePython.itkKdTreeLSVF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkKdTreeLSVF3

        Create a new object of the class itkKdTreeLSVF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkKdTreeLSVF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkKdTreeLSVF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkKdTreeLSVF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkKdTreeLSVF3.Clone = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_Clone, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.GetMeasurementVectorSize = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_GetMeasurementVectorSize, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.SetBucketSize = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_SetBucketSize, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.SetSample = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_SetSample, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.GetSample = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_GetSample, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.Size = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_Size, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.GetEmptyTerminalNode = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_GetEmptyTerminalNode, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.SetRoot = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_SetRoot, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.GetRoot = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_GetRoot, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.GetMeasurementVector = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_GetMeasurementVector, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.GetFrequency = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_GetFrequency, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.GetDistanceMetric = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_GetDistanceMetric, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.Search = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_Search, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.BallWithinBounds = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_BallWithinBounds, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.BoundsOverlapBall = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_BoundsOverlapBall, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.DeleteNode = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_DeleteNode, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.PrintTree = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_PrintTree, None, itkKdTreeLSVF3)
itkKdTreeLSVF3.PlotTree = new_instancemethod(_itkKdTreePython.itkKdTreeLSVF3_PlotTree, None, itkKdTreeLSVF3)
itkKdTreeLSVF3_swigregister = _itkKdTreePython.itkKdTreeLSVF3_swigregister
itkKdTreeLSVF3_swigregister(itkKdTreeLSVF3)

def itkKdTreeLSVF3___New_orig__() -> "itkKdTreeLSVF3_Pointer":
    """itkKdTreeLSVF3___New_orig__() -> itkKdTreeLSVF3_Pointer"""
    return _itkKdTreePython.itkKdTreeLSVF3___New_orig__()

def itkKdTreeLSVF3_cast(obj: 'itkLightObject') -> "itkKdTreeLSVF3 *":
    """itkKdTreeLSVF3_cast(itkLightObject obj) -> itkKdTreeLSVF3"""
    return _itkKdTreePython.itkKdTreeLSVF3_cast(obj)

class itkKdTreeNodeLSVF2(object):
    """Proxy of C++ itkKdTreeNodeLSVF2 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def IsTerminal(self) -> "bool":
        """IsTerminal(itkKdTreeNodeLSVF2 self) -> bool"""
        return _itkKdTreePython.itkKdTreeNodeLSVF2_IsTerminal(self)


    def GetParameters(self, arg0: 'unsigned int &', arg1: 'float &') -> "void":
        """GetParameters(itkKdTreeNodeLSVF2 self, unsigned int & arg0, float & arg1)"""
        return _itkKdTreePython.itkKdTreeNodeLSVF2_GetParameters(self, arg0, arg1)


    def Left(self, *args) -> "itkKdTreeNodeLSVF2 const *":
        """
        Left(itkKdTreeNodeLSVF2 self) -> itkKdTreeNodeLSVF2
        Left(itkKdTreeNodeLSVF2 self) -> itkKdTreeNodeLSVF2
        """
        return _itkKdTreePython.itkKdTreeNodeLSVF2_Left(self, *args)


    def Right(self, *args) -> "itkKdTreeNodeLSVF2 const *":
        """
        Right(itkKdTreeNodeLSVF2 self) -> itkKdTreeNodeLSVF2
        Right(itkKdTreeNodeLSVF2 self) -> itkKdTreeNodeLSVF2
        """
        return _itkKdTreePython.itkKdTreeNodeLSVF2_Right(self, *args)


    def Size(self) -> "unsigned int":
        """Size(itkKdTreeNodeLSVF2 self) -> unsigned int"""
        return _itkKdTreePython.itkKdTreeNodeLSVF2_Size(self)


    def GetWeightedCentroid(self, arg0: 'itkArrayD') -> "void":
        """GetWeightedCentroid(itkKdTreeNodeLSVF2 self, itkArrayD arg0)"""
        return _itkKdTreePython.itkKdTreeNodeLSVF2_GetWeightedCentroid(self, arg0)


    def GetCentroid(self, arg0: 'itkArrayD') -> "void":
        """GetCentroid(itkKdTreeNodeLSVF2 self, itkArrayD arg0)"""
        return _itkKdTreePython.itkKdTreeNodeLSVF2_GetCentroid(self, arg0)


    def GetInstanceIdentifier(self, arg0: 'unsigned long') -> "unsigned long":
        """GetInstanceIdentifier(itkKdTreeNodeLSVF2 self, unsigned long arg0) -> unsigned long"""
        return _itkKdTreePython.itkKdTreeNodeLSVF2_GetInstanceIdentifier(self, arg0)


    def AddInstanceIdentifier(self, arg0: 'unsigned long') -> "void":
        """AddInstanceIdentifier(itkKdTreeNodeLSVF2 self, unsigned long arg0)"""
        return _itkKdTreePython.itkKdTreeNodeLSVF2_AddInstanceIdentifier(self, arg0)

    __swig_destroy__ = _itkKdTreePython.delete_itkKdTreeNodeLSVF2
itkKdTreeNodeLSVF2.IsTerminal = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF2_IsTerminal, None, itkKdTreeNodeLSVF2)
itkKdTreeNodeLSVF2.GetParameters = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF2_GetParameters, None, itkKdTreeNodeLSVF2)
itkKdTreeNodeLSVF2.Left = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF2_Left, None, itkKdTreeNodeLSVF2)
itkKdTreeNodeLSVF2.Right = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF2_Right, None, itkKdTreeNodeLSVF2)
itkKdTreeNodeLSVF2.Size = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF2_Size, None, itkKdTreeNodeLSVF2)
itkKdTreeNodeLSVF2.GetWeightedCentroid = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF2_GetWeightedCentroid, None, itkKdTreeNodeLSVF2)
itkKdTreeNodeLSVF2.GetCentroid = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF2_GetCentroid, None, itkKdTreeNodeLSVF2)
itkKdTreeNodeLSVF2.GetInstanceIdentifier = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF2_GetInstanceIdentifier, None, itkKdTreeNodeLSVF2)
itkKdTreeNodeLSVF2.AddInstanceIdentifier = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF2_AddInstanceIdentifier, None, itkKdTreeNodeLSVF2)
itkKdTreeNodeLSVF2_swigregister = _itkKdTreePython.itkKdTreeNodeLSVF2_swigregister
itkKdTreeNodeLSVF2_swigregister(itkKdTreeNodeLSVF2)

class itkKdTreeNodeLSVF3(object):
    """Proxy of C++ itkKdTreeNodeLSVF3 class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def IsTerminal(self) -> "bool":
        """IsTerminal(itkKdTreeNodeLSVF3 self) -> bool"""
        return _itkKdTreePython.itkKdTreeNodeLSVF3_IsTerminal(self)


    def GetParameters(self, arg0: 'unsigned int &', arg1: 'float &') -> "void":
        """GetParameters(itkKdTreeNodeLSVF3 self, unsigned int & arg0, float & arg1)"""
        return _itkKdTreePython.itkKdTreeNodeLSVF3_GetParameters(self, arg0, arg1)


    def Left(self, *args) -> "itkKdTreeNodeLSVF3 const *":
        """
        Left(itkKdTreeNodeLSVF3 self) -> itkKdTreeNodeLSVF3
        Left(itkKdTreeNodeLSVF3 self) -> itkKdTreeNodeLSVF3
        """
        return _itkKdTreePython.itkKdTreeNodeLSVF3_Left(self, *args)


    def Right(self, *args) -> "itkKdTreeNodeLSVF3 const *":
        """
        Right(itkKdTreeNodeLSVF3 self) -> itkKdTreeNodeLSVF3
        Right(itkKdTreeNodeLSVF3 self) -> itkKdTreeNodeLSVF3
        """
        return _itkKdTreePython.itkKdTreeNodeLSVF3_Right(self, *args)


    def Size(self) -> "unsigned int":
        """Size(itkKdTreeNodeLSVF3 self) -> unsigned int"""
        return _itkKdTreePython.itkKdTreeNodeLSVF3_Size(self)


    def GetWeightedCentroid(self, arg0: 'itkArrayD') -> "void":
        """GetWeightedCentroid(itkKdTreeNodeLSVF3 self, itkArrayD arg0)"""
        return _itkKdTreePython.itkKdTreeNodeLSVF3_GetWeightedCentroid(self, arg0)


    def GetCentroid(self, arg0: 'itkArrayD') -> "void":
        """GetCentroid(itkKdTreeNodeLSVF3 self, itkArrayD arg0)"""
        return _itkKdTreePython.itkKdTreeNodeLSVF3_GetCentroid(self, arg0)


    def GetInstanceIdentifier(self, arg0: 'unsigned long') -> "unsigned long":
        """GetInstanceIdentifier(itkKdTreeNodeLSVF3 self, unsigned long arg0) -> unsigned long"""
        return _itkKdTreePython.itkKdTreeNodeLSVF3_GetInstanceIdentifier(self, arg0)


    def AddInstanceIdentifier(self, arg0: 'unsigned long') -> "void":
        """AddInstanceIdentifier(itkKdTreeNodeLSVF3 self, unsigned long arg0)"""
        return _itkKdTreePython.itkKdTreeNodeLSVF3_AddInstanceIdentifier(self, arg0)

    __swig_destroy__ = _itkKdTreePython.delete_itkKdTreeNodeLSVF3
itkKdTreeNodeLSVF3.IsTerminal = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF3_IsTerminal, None, itkKdTreeNodeLSVF3)
itkKdTreeNodeLSVF3.GetParameters = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF3_GetParameters, None, itkKdTreeNodeLSVF3)
itkKdTreeNodeLSVF3.Left = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF3_Left, None, itkKdTreeNodeLSVF3)
itkKdTreeNodeLSVF3.Right = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF3_Right, None, itkKdTreeNodeLSVF3)
itkKdTreeNodeLSVF3.Size = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF3_Size, None, itkKdTreeNodeLSVF3)
itkKdTreeNodeLSVF3.GetWeightedCentroid = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF3_GetWeightedCentroid, None, itkKdTreeNodeLSVF3)
itkKdTreeNodeLSVF3.GetCentroid = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF3_GetCentroid, None, itkKdTreeNodeLSVF3)
itkKdTreeNodeLSVF3.GetInstanceIdentifier = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF3_GetInstanceIdentifier, None, itkKdTreeNodeLSVF3)
itkKdTreeNodeLSVF3.AddInstanceIdentifier = new_instancemethod(_itkKdTreePython.itkKdTreeNodeLSVF3_AddInstanceIdentifier, None, itkKdTreeNodeLSVF3)
itkKdTreeNodeLSVF3_swigregister = _itkKdTreePython.itkKdTreeNodeLSVF3_swigregister
itkKdTreeNodeLSVF3_swigregister(itkKdTreeNodeLSVF3)



