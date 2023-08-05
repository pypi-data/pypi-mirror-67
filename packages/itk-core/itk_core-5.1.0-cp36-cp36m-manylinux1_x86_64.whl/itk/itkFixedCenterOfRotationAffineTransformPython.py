# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkFixedCenterOfRotationAffineTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkFixedCenterOfRotationAffineTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkFixedCenterOfRotationAffineTransformPython
            return _itkFixedCenterOfRotationAffineTransformPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkFixedCenterOfRotationAffineTransformPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkFixedCenterOfRotationAffineTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkFixedCenterOfRotationAffineTransformPython
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
import itkScalableAffineTransformPython
import itkTransformBasePython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkPointPython
import itkVariableLengthVectorPython
import itkOptimizerParametersPython
import itkArrayPython
import itkArray2DPython
import itkAffineTransformPython
import itkMatrixOffsetTransformBasePython

def itkFixedCenterOfRotationAffineTransformD3_New():
  return itkFixedCenterOfRotationAffineTransformD3.New()


def itkFixedCenterOfRotationAffineTransformD2_New():
  return itkFixedCenterOfRotationAffineTransformD2.New()

class itkFixedCenterOfRotationAffineTransformD2(itkScalableAffineTransformPython.itkScalableAffineTransformD2):
    """


    Affine transformation with a specified center of rotation.

    This class implements an Affine transform in which the rotation center
    can be explicitly selected.

    C++ includes: itkFixedCenterOfRotationAffineTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkFixedCenterOfRotationAffineTransformD2_Pointer":
        """__New_orig__() -> itkFixedCenterOfRotationAffineTransformD2_Pointer"""
        return _itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkFixedCenterOfRotationAffineTransformD2_Pointer":
        """Clone(itkFixedCenterOfRotationAffineTransformD2 self) -> itkFixedCenterOfRotationAffineTransformD2_Pointer"""
        return _itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD2_Clone(self)


    def SetCenterOfRotationComponent(self, cor: 'itkPointD2') -> "void":
        """
        SetCenterOfRotationComponent(itkFixedCenterOfRotationAffineTransformD2 self, itkPointD2 cor)

        Set
        and Get the center of rotation 
        """
        return _itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD2_SetCenterOfRotationComponent(self, cor)


    def GetCenterOfRotationComponent(self) -> "itkPointD2":
        """GetCenterOfRotationComponent(itkFixedCenterOfRotationAffineTransformD2 self) -> itkPointD2"""
        return _itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD2_GetCenterOfRotationComponent(self)


    def SetMatrixComponent(self, matrix: 'itkMatrixD22') -> "void":
        """
        SetMatrixComponent(itkFixedCenterOfRotationAffineTransformD2 self, itkMatrixD22 matrix)

        Set the matrix
        of the transform. The matrix should not include scale 
        """
        return _itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD2_SetMatrixComponent(self, matrix)


    def GetMatrixComponent(self) -> "itkMatrixD22 const &":
        """
        GetMatrixComponent(itkFixedCenterOfRotationAffineTransformD2 self) -> itkMatrixD22

        Get matrix of
        the transform 
        """
        return _itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD2_GetMatrixComponent(self)


    def SetOffsetComponent(self, offset: 'itkVectorD2') -> "void":
        """
        SetOffsetComponent(itkFixedCenterOfRotationAffineTransformD2 self, itkVectorD2 offset)

        Set offset
        (origin) of the Transform. 
        """
        return _itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD2_SetOffsetComponent(self, offset)


    def GetOffsetComponent(self) -> "itkVectorD2 const &":
        """
        GetOffsetComponent(itkFixedCenterOfRotationAffineTransformD2 self) -> itkVectorD2

        Get offset of
        the transform. 
        """
        return _itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD2_GetOffsetComponent(self)

    __swig_destroy__ = _itkFixedCenterOfRotationAffineTransformPython.delete_itkFixedCenterOfRotationAffineTransformD2

    def cast(obj: 'itkLightObject') -> "itkFixedCenterOfRotationAffineTransformD2 *":
        """cast(itkLightObject obj) -> itkFixedCenterOfRotationAffineTransformD2"""
        return _itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkFixedCenterOfRotationAffineTransformD2

        Create a new object of the class itkFixedCenterOfRotationAffineTransformD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFixedCenterOfRotationAffineTransformD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFixedCenterOfRotationAffineTransformD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFixedCenterOfRotationAffineTransformD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFixedCenterOfRotationAffineTransformD2.Clone = new_instancemethod(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD2_Clone, None, itkFixedCenterOfRotationAffineTransformD2)
itkFixedCenterOfRotationAffineTransformD2.SetCenterOfRotationComponent = new_instancemethod(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD2_SetCenterOfRotationComponent, None, itkFixedCenterOfRotationAffineTransformD2)
itkFixedCenterOfRotationAffineTransformD2.GetCenterOfRotationComponent = new_instancemethod(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD2_GetCenterOfRotationComponent, None, itkFixedCenterOfRotationAffineTransformD2)
itkFixedCenterOfRotationAffineTransformD2.SetMatrixComponent = new_instancemethod(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD2_SetMatrixComponent, None, itkFixedCenterOfRotationAffineTransformD2)
itkFixedCenterOfRotationAffineTransformD2.GetMatrixComponent = new_instancemethod(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD2_GetMatrixComponent, None, itkFixedCenterOfRotationAffineTransformD2)
itkFixedCenterOfRotationAffineTransformD2.SetOffsetComponent = new_instancemethod(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD2_SetOffsetComponent, None, itkFixedCenterOfRotationAffineTransformD2)
itkFixedCenterOfRotationAffineTransformD2.GetOffsetComponent = new_instancemethod(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD2_GetOffsetComponent, None, itkFixedCenterOfRotationAffineTransformD2)
itkFixedCenterOfRotationAffineTransformD2_swigregister = _itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD2_swigregister
itkFixedCenterOfRotationAffineTransformD2_swigregister(itkFixedCenterOfRotationAffineTransformD2)

def itkFixedCenterOfRotationAffineTransformD2___New_orig__() -> "itkFixedCenterOfRotationAffineTransformD2_Pointer":
    """itkFixedCenterOfRotationAffineTransformD2___New_orig__() -> itkFixedCenterOfRotationAffineTransformD2_Pointer"""
    return _itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD2___New_orig__()

def itkFixedCenterOfRotationAffineTransformD2_cast(obj: 'itkLightObject') -> "itkFixedCenterOfRotationAffineTransformD2 *":
    """itkFixedCenterOfRotationAffineTransformD2_cast(itkLightObject obj) -> itkFixedCenterOfRotationAffineTransformD2"""
    return _itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD2_cast(obj)

class itkFixedCenterOfRotationAffineTransformD3(itkScalableAffineTransformPython.itkScalableAffineTransformD3):
    """


    Affine transformation with a specified center of rotation.

    This class implements an Affine transform in which the rotation center
    can be explicitly selected.

    C++ includes: itkFixedCenterOfRotationAffineTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkFixedCenterOfRotationAffineTransformD3_Pointer":
        """__New_orig__() -> itkFixedCenterOfRotationAffineTransformD3_Pointer"""
        return _itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkFixedCenterOfRotationAffineTransformD3_Pointer":
        """Clone(itkFixedCenterOfRotationAffineTransformD3 self) -> itkFixedCenterOfRotationAffineTransformD3_Pointer"""
        return _itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD3_Clone(self)


    def SetCenterOfRotationComponent(self, cor: 'itkPointD3') -> "void":
        """
        SetCenterOfRotationComponent(itkFixedCenterOfRotationAffineTransformD3 self, itkPointD3 cor)

        Set
        and Get the center of rotation 
        """
        return _itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD3_SetCenterOfRotationComponent(self, cor)


    def GetCenterOfRotationComponent(self) -> "itkPointD3":
        """GetCenterOfRotationComponent(itkFixedCenterOfRotationAffineTransformD3 self) -> itkPointD3"""
        return _itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD3_GetCenterOfRotationComponent(self)


    def SetMatrixComponent(self, matrix: 'itkMatrixD33') -> "void":
        """
        SetMatrixComponent(itkFixedCenterOfRotationAffineTransformD3 self, itkMatrixD33 matrix)

        Set the matrix
        of the transform. The matrix should not include scale 
        """
        return _itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD3_SetMatrixComponent(self, matrix)


    def GetMatrixComponent(self) -> "itkMatrixD33 const &":
        """
        GetMatrixComponent(itkFixedCenterOfRotationAffineTransformD3 self) -> itkMatrixD33

        Get matrix of
        the transform 
        """
        return _itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD3_GetMatrixComponent(self)


    def SetOffsetComponent(self, offset: 'itkVectorD3') -> "void":
        """
        SetOffsetComponent(itkFixedCenterOfRotationAffineTransformD3 self, itkVectorD3 offset)

        Set offset
        (origin) of the Transform. 
        """
        return _itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD3_SetOffsetComponent(self, offset)


    def GetOffsetComponent(self) -> "itkVectorD3 const &":
        """
        GetOffsetComponent(itkFixedCenterOfRotationAffineTransformD3 self) -> itkVectorD3

        Get offset of
        the transform. 
        """
        return _itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD3_GetOffsetComponent(self)

    __swig_destroy__ = _itkFixedCenterOfRotationAffineTransformPython.delete_itkFixedCenterOfRotationAffineTransformD3

    def cast(obj: 'itkLightObject') -> "itkFixedCenterOfRotationAffineTransformD3 *":
        """cast(itkLightObject obj) -> itkFixedCenterOfRotationAffineTransformD3"""
        return _itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkFixedCenterOfRotationAffineTransformD3

        Create a new object of the class itkFixedCenterOfRotationAffineTransformD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFixedCenterOfRotationAffineTransformD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFixedCenterOfRotationAffineTransformD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFixedCenterOfRotationAffineTransformD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkFixedCenterOfRotationAffineTransformD3.Clone = new_instancemethod(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD3_Clone, None, itkFixedCenterOfRotationAffineTransformD3)
itkFixedCenterOfRotationAffineTransformD3.SetCenterOfRotationComponent = new_instancemethod(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD3_SetCenterOfRotationComponent, None, itkFixedCenterOfRotationAffineTransformD3)
itkFixedCenterOfRotationAffineTransformD3.GetCenterOfRotationComponent = new_instancemethod(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD3_GetCenterOfRotationComponent, None, itkFixedCenterOfRotationAffineTransformD3)
itkFixedCenterOfRotationAffineTransformD3.SetMatrixComponent = new_instancemethod(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD3_SetMatrixComponent, None, itkFixedCenterOfRotationAffineTransformD3)
itkFixedCenterOfRotationAffineTransformD3.GetMatrixComponent = new_instancemethod(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD3_GetMatrixComponent, None, itkFixedCenterOfRotationAffineTransformD3)
itkFixedCenterOfRotationAffineTransformD3.SetOffsetComponent = new_instancemethod(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD3_SetOffsetComponent, None, itkFixedCenterOfRotationAffineTransformD3)
itkFixedCenterOfRotationAffineTransformD3.GetOffsetComponent = new_instancemethod(_itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD3_GetOffsetComponent, None, itkFixedCenterOfRotationAffineTransformD3)
itkFixedCenterOfRotationAffineTransformD3_swigregister = _itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD3_swigregister
itkFixedCenterOfRotationAffineTransformD3_swigregister(itkFixedCenterOfRotationAffineTransformD3)

def itkFixedCenterOfRotationAffineTransformD3___New_orig__() -> "itkFixedCenterOfRotationAffineTransformD3_Pointer":
    """itkFixedCenterOfRotationAffineTransformD3___New_orig__() -> itkFixedCenterOfRotationAffineTransformD3_Pointer"""
    return _itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD3___New_orig__()

def itkFixedCenterOfRotationAffineTransformD3_cast(obj: 'itkLightObject') -> "itkFixedCenterOfRotationAffineTransformD3 *":
    """itkFixedCenterOfRotationAffineTransformD3_cast(itkLightObject obj) -> itkFixedCenterOfRotationAffineTransformD3"""
    return _itkFixedCenterOfRotationAffineTransformPython.itkFixedCenterOfRotationAffineTransformD3_cast(obj)



