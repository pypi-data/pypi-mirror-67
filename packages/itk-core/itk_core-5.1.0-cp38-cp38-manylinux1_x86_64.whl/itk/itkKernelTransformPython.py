# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkKernelTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkKernelTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkKernelTransformPython
            return _itkKernelTransformPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkKernelTransformPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkKernelTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkKernelTransformPython
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
import stdcomplexPython
import pyBasePython
import vnl_vectorPython
import itkCovariantVectorPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkVectorPython
import ITKCommonBasePython
import itkTransformBasePython
import itkArrayPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import itkPointPython
import itkOptimizerParametersPython
import itkArray2DPython
import itkVariableLengthVectorPython
import itkDiffusionTensor3DPython
import itkVectorContainerPython
import itkOffsetPython
import itkSizePython
import itkContinuousIndexPython
import itkIndexPython
import itkPointSetPython

def itkKernelTransformD3_New():
  return itkKernelTransformD3.New()


def itkKernelTransformD2_New():
  return itkKernelTransformD2.New()

class itkKernelTransformD2(itkTransformBasePython.itkTransformD22):
    """


    Intended to be a base class for elastic body spline and thin plate
    spline. This is implemented in as straightforward a manner as possible
    from the IEEE TMI paper by Davis, Khotanzad, Flamig, and Harms, Vol.
    16, No. 3 June 1997. Notation closely follows their paper, so if you
    have it in front of you, this code will make a lot more sense.

    KernelTransform: Provides support for defining source and target
    landmarks Defines a number of data types used in the computations
    Defines the mathematical framework used to compute all splines, so
    that subclasses need only provide a kernel specific to that spline

    This formulation allows the stiffness of the spline to be adjusted,
    allowing the spline to vary from interpolating the landmarks to
    approximating the landmarks. This part of the formulation is based on
    the short paper by R. Sprengel, K. Rohr, H. Stiehl. "Thin-Plate
    Spline Approximation for Image  Registration". In 18th International
    Conference of the IEEE Engineering in Medicine and Biology Society.
    1996.

    C++ includes: itkKernelTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkKernelTransformD2_Pointer":
        """__New_orig__() -> itkKernelTransformD2_Pointer"""
        return _itkKernelTransformPython.itkKernelTransformD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkKernelTransformD2_Pointer":
        """Clone(itkKernelTransformD2 self) -> itkKernelTransformD2_Pointer"""
        return _itkKernelTransformPython.itkKernelTransformD2_Clone(self)


    def GetModifiableSourceLandmarks(self) -> "itkPointSetPD22STD22DD *":
        """GetModifiableSourceLandmarks(itkKernelTransformD2 self) -> itkPointSetPD22STD22DD"""
        return _itkKernelTransformPython.itkKernelTransformD2_GetModifiableSourceLandmarks(self)


    def GetSourceLandmarks(self, *args) -> "itkPointSetPD22STD22DD *":
        """
        GetSourceLandmarks(itkKernelTransformD2 self) -> itkPointSetPD22STD22DD
        GetSourceLandmarks(itkKernelTransformD2 self) -> itkPointSetPD22STD22DD
        """
        return _itkKernelTransformPython.itkKernelTransformD2_GetSourceLandmarks(self, *args)


    def SetSourceLandmarks(self, arg0: 'itkPointSetPD22STD22DD') -> "void":
        """SetSourceLandmarks(itkKernelTransformD2 self, itkPointSetPD22STD22DD arg0)"""
        return _itkKernelTransformPython.itkKernelTransformD2_SetSourceLandmarks(self, arg0)


    def GetModifiableTargetLandmarks(self) -> "itkPointSetPD22STD22DD *":
        """GetModifiableTargetLandmarks(itkKernelTransformD2 self) -> itkPointSetPD22STD22DD"""
        return _itkKernelTransformPython.itkKernelTransformD2_GetModifiableTargetLandmarks(self)


    def GetTargetLandmarks(self, *args) -> "itkPointSetPD22STD22DD *":
        """
        GetTargetLandmarks(itkKernelTransformD2 self) -> itkPointSetPD22STD22DD
        GetTargetLandmarks(itkKernelTransformD2 self) -> itkPointSetPD22STD22DD
        """
        return _itkKernelTransformPython.itkKernelTransformD2_GetTargetLandmarks(self, *args)


    def SetTargetLandmarks(self, arg0: 'itkPointSetPD22STD22DD') -> "void":
        """SetTargetLandmarks(itkKernelTransformD2 self, itkPointSetPD22STD22DD arg0)"""
        return _itkKernelTransformPython.itkKernelTransformD2_SetTargetLandmarks(self, arg0)


    def GetModifiableDisplacements(self) -> "itkVectorContainerULVD2 *":
        """GetModifiableDisplacements(itkKernelTransformD2 self) -> itkVectorContainerULVD2"""
        return _itkKernelTransformPython.itkKernelTransformD2_GetModifiableDisplacements(self)


    def GetDisplacements(self, *args) -> "itkVectorContainerULVD2 *":
        """
        GetDisplacements(itkKernelTransformD2 self) -> itkVectorContainerULVD2
        GetDisplacements(itkKernelTransformD2 self) -> itkVectorContainerULVD2
        """
        return _itkKernelTransformPython.itkKernelTransformD2_GetDisplacements(self, *args)


    def ComputeWMatrix(self) -> "void":
        """
        ComputeWMatrix(itkKernelTransformD2 self)

        Compute W matrix. 
        """
        return _itkKernelTransformPython.itkKernelTransformD2_ComputeWMatrix(self)


    def TransformVector(self, *args) -> "vnl_vector_fixed< double,2 >":
        """
        TransformVector(itkKernelTransformD2 self, itkVectorD2 arg0) -> itkVectorD2
        TransformVector(itkKernelTransformD2 self, vnl_vector_fixed< double,2 > const & arg0) -> vnl_vector_fixed< double,2 >

        Method to transform
        a vector stored in a VectorImage, at a point. For global transforms,
        point is ignored and TransformVector( vector ) is called. Local
        transforms (e.g. deformation field transform) must override and
        provide required behavior. 
        """
        return _itkKernelTransformPython.itkKernelTransformD2_TransformVector(self, *args)


    def UpdateParameters(self) -> "void":
        """
        UpdateParameters(itkKernelTransformD2 self)

        Update the
        Parameters array from the landmarks coordinates. 
        """
        return _itkKernelTransformPython.itkKernelTransformD2_UpdateParameters(self)


    def SetStiffness(self, _arg: 'double') -> "void":
        """
        SetStiffness(itkKernelTransformD2 self, double _arg)

        Stiffness of the
        spline. A stiffness of zero results in the standard interpolating
        spline. A non-zero stiffness allows the spline to approximate rather
        than interpolate the landmarks. Stiffness values are usually rather
        small, typically in the range of 0.001 to 0.1. The approximating
        spline formulation is based on the short paper by R. Sprengel, K.
        Rohr, H. Stiehl. "Thin-Plate Spline Approximation for Image
        Registration". In 18th International Conference of the IEEE
        Engineering in Medicine and Biology Society. 1996. 
        """
        return _itkKernelTransformPython.itkKernelTransformD2_SetStiffness(self, _arg)


    def GetStiffness(self) -> "double":
        """GetStiffness(itkKernelTransformD2 self) -> double"""
        return _itkKernelTransformPython.itkKernelTransformD2_GetStiffness(self)

    __swig_destroy__ = _itkKernelTransformPython.delete_itkKernelTransformD2

    def cast(obj: 'itkLightObject') -> "itkKernelTransformD2 *":
        """cast(itkLightObject obj) -> itkKernelTransformD2"""
        return _itkKernelTransformPython.itkKernelTransformD2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkKernelTransformD2

        Create a new object of the class itkKernelTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkKernelTransformD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkKernelTransformD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkKernelTransformD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkKernelTransformD2.Clone = new_instancemethod(_itkKernelTransformPython.itkKernelTransformD2_Clone, None, itkKernelTransformD2)
itkKernelTransformD2.GetModifiableSourceLandmarks = new_instancemethod(_itkKernelTransformPython.itkKernelTransformD2_GetModifiableSourceLandmarks, None, itkKernelTransformD2)
itkKernelTransformD2.GetSourceLandmarks = new_instancemethod(_itkKernelTransformPython.itkKernelTransformD2_GetSourceLandmarks, None, itkKernelTransformD2)
itkKernelTransformD2.SetSourceLandmarks = new_instancemethod(_itkKernelTransformPython.itkKernelTransformD2_SetSourceLandmarks, None, itkKernelTransformD2)
itkKernelTransformD2.GetModifiableTargetLandmarks = new_instancemethod(_itkKernelTransformPython.itkKernelTransformD2_GetModifiableTargetLandmarks, None, itkKernelTransformD2)
itkKernelTransformD2.GetTargetLandmarks = new_instancemethod(_itkKernelTransformPython.itkKernelTransformD2_GetTargetLandmarks, None, itkKernelTransformD2)
itkKernelTransformD2.SetTargetLandmarks = new_instancemethod(_itkKernelTransformPython.itkKernelTransformD2_SetTargetLandmarks, None, itkKernelTransformD2)
itkKernelTransformD2.GetModifiableDisplacements = new_instancemethod(_itkKernelTransformPython.itkKernelTransformD2_GetModifiableDisplacements, None, itkKernelTransformD2)
itkKernelTransformD2.GetDisplacements = new_instancemethod(_itkKernelTransformPython.itkKernelTransformD2_GetDisplacements, None, itkKernelTransformD2)
itkKernelTransformD2.ComputeWMatrix = new_instancemethod(_itkKernelTransformPython.itkKernelTransformD2_ComputeWMatrix, None, itkKernelTransformD2)
itkKernelTransformD2.TransformVector = new_instancemethod(_itkKernelTransformPython.itkKernelTransformD2_TransformVector, None, itkKernelTransformD2)
itkKernelTransformD2.UpdateParameters = new_instancemethod(_itkKernelTransformPython.itkKernelTransformD2_UpdateParameters, None, itkKernelTransformD2)
itkKernelTransformD2.SetStiffness = new_instancemethod(_itkKernelTransformPython.itkKernelTransformD2_SetStiffness, None, itkKernelTransformD2)
itkKernelTransformD2.GetStiffness = new_instancemethod(_itkKernelTransformPython.itkKernelTransformD2_GetStiffness, None, itkKernelTransformD2)
itkKernelTransformD2_swigregister = _itkKernelTransformPython.itkKernelTransformD2_swigregister
itkKernelTransformD2_swigregister(itkKernelTransformD2)

def itkKernelTransformD2___New_orig__() -> "itkKernelTransformD2_Pointer":
    """itkKernelTransformD2___New_orig__() -> itkKernelTransformD2_Pointer"""
    return _itkKernelTransformPython.itkKernelTransformD2___New_orig__()

def itkKernelTransformD2_cast(obj: 'itkLightObject') -> "itkKernelTransformD2 *":
    """itkKernelTransformD2_cast(itkLightObject obj) -> itkKernelTransformD2"""
    return _itkKernelTransformPython.itkKernelTransformD2_cast(obj)

class itkKernelTransformD3(itkTransformBasePython.itkTransformD33):
    """


    Intended to be a base class for elastic body spline and thin plate
    spline. This is implemented in as straightforward a manner as possible
    from the IEEE TMI paper by Davis, Khotanzad, Flamig, and Harms, Vol.
    16, No. 3 June 1997. Notation closely follows their paper, so if you
    have it in front of you, this code will make a lot more sense.

    KernelTransform: Provides support for defining source and target
    landmarks Defines a number of data types used in the computations
    Defines the mathematical framework used to compute all splines, so
    that subclasses need only provide a kernel specific to that spline

    This formulation allows the stiffness of the spline to be adjusted,
    allowing the spline to vary from interpolating the landmarks to
    approximating the landmarks. This part of the formulation is based on
    the short paper by R. Sprengel, K. Rohr, H. Stiehl. "Thin-Plate
    Spline Approximation for Image  Registration". In 18th International
    Conference of the IEEE Engineering in Medicine and Biology Society.
    1996.

    C++ includes: itkKernelTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkKernelTransformD3_Pointer":
        """__New_orig__() -> itkKernelTransformD3_Pointer"""
        return _itkKernelTransformPython.itkKernelTransformD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkKernelTransformD3_Pointer":
        """Clone(itkKernelTransformD3 self) -> itkKernelTransformD3_Pointer"""
        return _itkKernelTransformPython.itkKernelTransformD3_Clone(self)


    def GetModifiableSourceLandmarks(self) -> "itkPointSetPD33STD33DD *":
        """GetModifiableSourceLandmarks(itkKernelTransformD3 self) -> itkPointSetPD33STD33DD"""
        return _itkKernelTransformPython.itkKernelTransformD3_GetModifiableSourceLandmarks(self)


    def GetSourceLandmarks(self, *args) -> "itkPointSetPD33STD33DD *":
        """
        GetSourceLandmarks(itkKernelTransformD3 self) -> itkPointSetPD33STD33DD
        GetSourceLandmarks(itkKernelTransformD3 self) -> itkPointSetPD33STD33DD
        """
        return _itkKernelTransformPython.itkKernelTransformD3_GetSourceLandmarks(self, *args)


    def SetSourceLandmarks(self, arg0: 'itkPointSetPD33STD33DD') -> "void":
        """SetSourceLandmarks(itkKernelTransformD3 self, itkPointSetPD33STD33DD arg0)"""
        return _itkKernelTransformPython.itkKernelTransformD3_SetSourceLandmarks(self, arg0)


    def GetModifiableTargetLandmarks(self) -> "itkPointSetPD33STD33DD *":
        """GetModifiableTargetLandmarks(itkKernelTransformD3 self) -> itkPointSetPD33STD33DD"""
        return _itkKernelTransformPython.itkKernelTransformD3_GetModifiableTargetLandmarks(self)


    def GetTargetLandmarks(self, *args) -> "itkPointSetPD33STD33DD *":
        """
        GetTargetLandmarks(itkKernelTransformD3 self) -> itkPointSetPD33STD33DD
        GetTargetLandmarks(itkKernelTransformD3 self) -> itkPointSetPD33STD33DD
        """
        return _itkKernelTransformPython.itkKernelTransformD3_GetTargetLandmarks(self, *args)


    def SetTargetLandmarks(self, arg0: 'itkPointSetPD33STD33DD') -> "void":
        """SetTargetLandmarks(itkKernelTransformD3 self, itkPointSetPD33STD33DD arg0)"""
        return _itkKernelTransformPython.itkKernelTransformD3_SetTargetLandmarks(self, arg0)


    def GetModifiableDisplacements(self) -> "itkVectorContainerULVD3 *":
        """GetModifiableDisplacements(itkKernelTransformD3 self) -> itkVectorContainerULVD3"""
        return _itkKernelTransformPython.itkKernelTransformD3_GetModifiableDisplacements(self)


    def GetDisplacements(self, *args) -> "itkVectorContainerULVD3 *":
        """
        GetDisplacements(itkKernelTransformD3 self) -> itkVectorContainerULVD3
        GetDisplacements(itkKernelTransformD3 self) -> itkVectorContainerULVD3
        """
        return _itkKernelTransformPython.itkKernelTransformD3_GetDisplacements(self, *args)


    def ComputeWMatrix(self) -> "void":
        """
        ComputeWMatrix(itkKernelTransformD3 self)

        Compute W matrix. 
        """
        return _itkKernelTransformPython.itkKernelTransformD3_ComputeWMatrix(self)


    def TransformVector(self, *args) -> "vnl_vector_fixed< double,3 >":
        """
        TransformVector(itkKernelTransformD3 self, itkVectorD3 arg0) -> itkVectorD3
        TransformVector(itkKernelTransformD3 self, vnl_vector_fixed< double,3 > const & arg0) -> vnl_vector_fixed< double,3 >

        Method to transform
        a vector stored in a VectorImage, at a point. For global transforms,
        point is ignored and TransformVector( vector ) is called. Local
        transforms (e.g. deformation field transform) must override and
        provide required behavior. 
        """
        return _itkKernelTransformPython.itkKernelTransformD3_TransformVector(self, *args)


    def UpdateParameters(self) -> "void":
        """
        UpdateParameters(itkKernelTransformD3 self)

        Update the
        Parameters array from the landmarks coordinates. 
        """
        return _itkKernelTransformPython.itkKernelTransformD3_UpdateParameters(self)


    def SetStiffness(self, _arg: 'double') -> "void":
        """
        SetStiffness(itkKernelTransformD3 self, double _arg)

        Stiffness of the
        spline. A stiffness of zero results in the standard interpolating
        spline. A non-zero stiffness allows the spline to approximate rather
        than interpolate the landmarks. Stiffness values are usually rather
        small, typically in the range of 0.001 to 0.1. The approximating
        spline formulation is based on the short paper by R. Sprengel, K.
        Rohr, H. Stiehl. "Thin-Plate Spline Approximation for Image
        Registration". In 18th International Conference of the IEEE
        Engineering in Medicine and Biology Society. 1996. 
        """
        return _itkKernelTransformPython.itkKernelTransformD3_SetStiffness(self, _arg)


    def GetStiffness(self) -> "double":
        """GetStiffness(itkKernelTransformD3 self) -> double"""
        return _itkKernelTransformPython.itkKernelTransformD3_GetStiffness(self)

    __swig_destroy__ = _itkKernelTransformPython.delete_itkKernelTransformD3

    def cast(obj: 'itkLightObject') -> "itkKernelTransformD3 *":
        """cast(itkLightObject obj) -> itkKernelTransformD3"""
        return _itkKernelTransformPython.itkKernelTransformD3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkKernelTransformD3

        Create a new object of the class itkKernelTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkKernelTransformD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkKernelTransformD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkKernelTransformD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkKernelTransformD3.Clone = new_instancemethod(_itkKernelTransformPython.itkKernelTransformD3_Clone, None, itkKernelTransformD3)
itkKernelTransformD3.GetModifiableSourceLandmarks = new_instancemethod(_itkKernelTransformPython.itkKernelTransformD3_GetModifiableSourceLandmarks, None, itkKernelTransformD3)
itkKernelTransformD3.GetSourceLandmarks = new_instancemethod(_itkKernelTransformPython.itkKernelTransformD3_GetSourceLandmarks, None, itkKernelTransformD3)
itkKernelTransformD3.SetSourceLandmarks = new_instancemethod(_itkKernelTransformPython.itkKernelTransformD3_SetSourceLandmarks, None, itkKernelTransformD3)
itkKernelTransformD3.GetModifiableTargetLandmarks = new_instancemethod(_itkKernelTransformPython.itkKernelTransformD3_GetModifiableTargetLandmarks, None, itkKernelTransformD3)
itkKernelTransformD3.GetTargetLandmarks = new_instancemethod(_itkKernelTransformPython.itkKernelTransformD3_GetTargetLandmarks, None, itkKernelTransformD3)
itkKernelTransformD3.SetTargetLandmarks = new_instancemethod(_itkKernelTransformPython.itkKernelTransformD3_SetTargetLandmarks, None, itkKernelTransformD3)
itkKernelTransformD3.GetModifiableDisplacements = new_instancemethod(_itkKernelTransformPython.itkKernelTransformD3_GetModifiableDisplacements, None, itkKernelTransformD3)
itkKernelTransformD3.GetDisplacements = new_instancemethod(_itkKernelTransformPython.itkKernelTransformD3_GetDisplacements, None, itkKernelTransformD3)
itkKernelTransformD3.ComputeWMatrix = new_instancemethod(_itkKernelTransformPython.itkKernelTransformD3_ComputeWMatrix, None, itkKernelTransformD3)
itkKernelTransformD3.TransformVector = new_instancemethod(_itkKernelTransformPython.itkKernelTransformD3_TransformVector, None, itkKernelTransformD3)
itkKernelTransformD3.UpdateParameters = new_instancemethod(_itkKernelTransformPython.itkKernelTransformD3_UpdateParameters, None, itkKernelTransformD3)
itkKernelTransformD3.SetStiffness = new_instancemethod(_itkKernelTransformPython.itkKernelTransformD3_SetStiffness, None, itkKernelTransformD3)
itkKernelTransformD3.GetStiffness = new_instancemethod(_itkKernelTransformPython.itkKernelTransformD3_GetStiffness, None, itkKernelTransformD3)
itkKernelTransformD3_swigregister = _itkKernelTransformPython.itkKernelTransformD3_swigregister
itkKernelTransformD3_swigregister(itkKernelTransformD3)

def itkKernelTransformD3___New_orig__() -> "itkKernelTransformD3_Pointer":
    """itkKernelTransformD3___New_orig__() -> itkKernelTransformD3_Pointer"""
    return _itkKernelTransformPython.itkKernelTransformD3___New_orig__()

def itkKernelTransformD3_cast(obj: 'itkLightObject') -> "itkKernelTransformD3 *":
    """itkKernelTransformD3_cast(itkLightObject obj) -> itkKernelTransformD3"""
    return _itkKernelTransformPython.itkKernelTransformD3_cast(obj)



