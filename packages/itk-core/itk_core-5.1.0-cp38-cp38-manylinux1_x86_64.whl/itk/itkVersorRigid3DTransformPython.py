# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkVersorRigid3DTransformPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkVersorRigid3DTransformPython', [dirname(__file__)])
        except ImportError:
            import _itkVersorRigid3DTransformPython
            return _itkVersorRigid3DTransformPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkVersorRigid3DTransformPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkVersorRigid3DTransformPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkVersorRigid3DTransformPython
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
import itkArrayPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import itkVersorTransformPython
import itkVersorPython
import itkPointPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkVectorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkOptimizerParametersPython
import itkArray2DPython
import itkRigid3DTransformPython
import itkMatrixOffsetTransformBasePython
import itkTransformBasePython
import itkSymmetricSecondRankTensorPython
import itkVariableLengthVectorPython
import itkDiffusionTensor3DPython

def itkVersorRigid3DTransformD_New():
  return itkVersorRigid3DTransformD.New()

class itkVersorRigid3DTransformD(itkVersorTransformPython.itkVersorTransformD):
    """


    VersorRigid3DTransform of a vector space (e.g. space coordinates)

    This transform applies a rotation and translation to the space The
    parameters for this transform can be set either using individual Set
    methods or in serialized form using SetParameters() and
    SetFixedParameters().

    The serialization of the optimizable parameters is an array of 6
    elements. The first 3 elements are the components of the versor
    representation of 3D rotation. The last 3 parameters defines the
    translation in each dimension.

    The serialization of the fixed parameters is an array of 3 elements
    defining the center of rotation.

    C++ includes: itkVersorRigid3DTransform.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkVersorRigid3DTransformD_Pointer":
        """__New_orig__() -> itkVersorRigid3DTransformD_Pointer"""
        return _itkVersorRigid3DTransformPython.itkVersorRigid3DTransformD___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkVersorRigid3DTransformD_Pointer":
        """Clone(itkVersorRigid3DTransformD self) -> itkVersorRigid3DTransformD_Pointer"""
        return _itkVersorRigid3DTransformPython.itkVersorRigid3DTransformD_Clone(self)


    def UpdateTransformParameters(self, update: 'itkArrayD', factor: 'double'=1.) -> "void":
        """
        UpdateTransformParameters(itkVersorRigid3DTransformD self, itkArrayD update, double factor=1.)
        UpdateTransformParameters(itkVersorRigid3DTransformD self, itkArrayD update)

        Update
        the transform's parameters by the values in update.

        Parameters:
        -----------

        update:  must be of the same length as returned by
        GetNumberOfParameters(). Throw an exception otherwise.

        factor:  is a scalar multiplier for each value in update.
        SetParameters is called at the end of this method, to allow the
        transform to perform any required operations on the updated parameters
        - typically a conversion to member variables for use in
        TransformPoint. 
        """
        return _itkVersorRigid3DTransformPython.itkVersorRigid3DTransformD_UpdateTransformParameters(self, update, factor)

    __swig_destroy__ = _itkVersorRigid3DTransformPython.delete_itkVersorRigid3DTransformD

    def cast(obj: 'itkLightObject') -> "itkVersorRigid3DTransformD *":
        """cast(itkLightObject obj) -> itkVersorRigid3DTransformD"""
        return _itkVersorRigid3DTransformPython.itkVersorRigid3DTransformD_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkVersorRigid3DTransformD

        Create a new object of the class itkVersorRigid3DTransformD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkVersorRigid3DTransformD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkVersorRigid3DTransformD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkVersorRigid3DTransformD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkVersorRigid3DTransformD.Clone = new_instancemethod(_itkVersorRigid3DTransformPython.itkVersorRigid3DTransformD_Clone, None, itkVersorRigid3DTransformD)
itkVersorRigid3DTransformD.UpdateTransformParameters = new_instancemethod(_itkVersorRigid3DTransformPython.itkVersorRigid3DTransformD_UpdateTransformParameters, None, itkVersorRigid3DTransformD)
itkVersorRigid3DTransformD_swigregister = _itkVersorRigid3DTransformPython.itkVersorRigid3DTransformD_swigregister
itkVersorRigid3DTransformD_swigregister(itkVersorRigid3DTransformD)

def itkVersorRigid3DTransformD___New_orig__() -> "itkVersorRigid3DTransformD_Pointer":
    """itkVersorRigid3DTransformD___New_orig__() -> itkVersorRigid3DTransformD_Pointer"""
    return _itkVersorRigid3DTransformPython.itkVersorRigid3DTransformD___New_orig__()

def itkVersorRigid3DTransformD_cast(obj: 'itkLightObject') -> "itkVersorRigid3DTransformD *":
    """itkVersorRigid3DTransformD_cast(itkLightObject obj) -> itkVersorRigid3DTransformD"""
    return _itkVersorRigid3DTransformPython.itkVersorRigid3DTransformD_cast(obj)



