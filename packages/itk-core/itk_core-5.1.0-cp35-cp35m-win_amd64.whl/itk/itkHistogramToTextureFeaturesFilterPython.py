# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkHistogramToTextureFeaturesFilterPython
else:
    import _itkHistogramToTextureFeaturesFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkHistogramToTextureFeaturesFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkHistogramToTextureFeaturesFilterPython.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import ITKCommonBasePython
import pyBasePython
import itkHistogramPython
import itkSamplePython
import itkFixedArrayPython
import itkArrayPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import itkVectorPython
import vnl_vector_refPython
import itkSimpleDataObjectDecoratorPython
import itkRGBAPixelPython
import itkCovariantVectorPython
import itkRGBPixelPython

def itkHistogramToTextureFeaturesFilterHF_New():
  return itkHistogramToTextureFeaturesFilterHF.New()


def itkHistogramToTextureFeaturesFilterHD_New():
  return itkHistogramToTextureFeaturesFilterHD.New()

class itkHistogramToTextureFeaturesFilterEnums(object):
    r"""Proxy of C++ itkHistogramToTextureFeaturesFilterEnums class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    TextureFeature_Energy = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterEnums_TextureFeature_Energy
    
    TextureFeature_Entropy = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterEnums_TextureFeature_Entropy
    
    TextureFeature_Correlation = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterEnums_TextureFeature_Correlation
    
    TextureFeature_InverseDifferenceMoment = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterEnums_TextureFeature_InverseDifferenceMoment
    
    TextureFeature_Inertia = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterEnums_TextureFeature_Inertia
    
    TextureFeature_ClusterShade = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterEnums_TextureFeature_ClusterShade
    
    TextureFeature_ClusterProminence = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterEnums_TextureFeature_ClusterProminence
    
    TextureFeature_HaralickCorrelation = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterEnums_TextureFeature_HaralickCorrelation
    
    TextureFeature_InvalidFeatureName = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterEnums_TextureFeature_InvalidFeatureName
    

    def __init__(self, *args):
        r"""
        __init__(itkHistogramToTextureFeaturesFilterEnums self) -> itkHistogramToTextureFeaturesFilterEnums
        __init__(itkHistogramToTextureFeaturesFilterEnums self, itkHistogramToTextureFeaturesFilterEnums arg0) -> itkHistogramToTextureFeaturesFilterEnums
        """
        _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterEnums_swiginit(self, _itkHistogramToTextureFeaturesFilterPython.new_itkHistogramToTextureFeaturesFilterEnums(*args))
    __swig_destroy__ = _itkHistogramToTextureFeaturesFilterPython.delete_itkHistogramToTextureFeaturesFilterEnums

# Register itkHistogramToTextureFeaturesFilterEnums in _itkHistogramToTextureFeaturesFilterPython:
_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterEnums_swigregister(itkHistogramToTextureFeaturesFilterEnums)

class itkHistogramToTextureFeaturesFilterHD(ITKCommonBasePython.itkProcessObject):
    r"""Proxy of C++ itkHistogramToTextureFeaturesFilterHD class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD___New_orig__)
    Clone = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_Clone)
    SetInput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_SetInput)
    GetInput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetInput)
    GetEnergy = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetEnergy)
    GetEnergyOutput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetEnergyOutput)
    GetEntropy = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetEntropy)
    GetEntropyOutput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetEntropyOutput)
    GetCorrelation = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetCorrelation)
    GetCorrelationOutput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetCorrelationOutput)
    GetInverseDifferenceMoment = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetInverseDifferenceMoment)
    GetInverseDifferenceMomentOutput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetInverseDifferenceMomentOutput)
    GetInertia = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetInertia)
    GetInertiaOutput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetInertiaOutput)
    GetClusterShade = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetClusterShade)
    GetClusterShadeOutput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetClusterShadeOutput)
    GetClusterProminence = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetClusterProminence)
    GetClusterProminenceOutput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetClusterProminenceOutput)
    GetHaralickCorrelation = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetHaralickCorrelation)
    GetHaralickCorrelationOutput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetHaralickCorrelationOutput)
    GetFeature = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_GetFeature)
    __swig_destroy__ = _itkHistogramToTextureFeaturesFilterPython.delete_itkHistogramToTextureFeaturesFilterHD
    cast = _swig_new_static_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_cast)

    def New(*args, **kargs):
        """New() -> itkHistogramToTextureFeaturesFilterHD

        Create a new object of the class itkHistogramToTextureFeaturesFilterHD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHistogramToTextureFeaturesFilterHD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkHistogramToTextureFeaturesFilterHD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkHistogramToTextureFeaturesFilterHD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHistogramToTextureFeaturesFilterHD in _itkHistogramToTextureFeaturesFilterPython:
_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_swigregister(itkHistogramToTextureFeaturesFilterHD)
itkHistogramToTextureFeaturesFilterHD___New_orig__ = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD___New_orig__
itkHistogramToTextureFeaturesFilterHD_cast = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHD_cast

class itkHistogramToTextureFeaturesFilterHF(ITKCommonBasePython.itkProcessObject):
    r"""Proxy of C++ itkHistogramToTextureFeaturesFilterHF class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF___New_orig__)
    Clone = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_Clone)
    SetInput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_SetInput)
    GetInput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetInput)
    GetEnergy = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetEnergy)
    GetEnergyOutput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetEnergyOutput)
    GetEntropy = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetEntropy)
    GetEntropyOutput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetEntropyOutput)
    GetCorrelation = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetCorrelation)
    GetCorrelationOutput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetCorrelationOutput)
    GetInverseDifferenceMoment = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetInverseDifferenceMoment)
    GetInverseDifferenceMomentOutput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetInverseDifferenceMomentOutput)
    GetInertia = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetInertia)
    GetInertiaOutput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetInertiaOutput)
    GetClusterShade = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetClusterShade)
    GetClusterShadeOutput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetClusterShadeOutput)
    GetClusterProminence = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetClusterProminence)
    GetClusterProminenceOutput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetClusterProminenceOutput)
    GetHaralickCorrelation = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetHaralickCorrelation)
    GetHaralickCorrelationOutput = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetHaralickCorrelationOutput)
    GetFeature = _swig_new_instance_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_GetFeature)
    __swig_destroy__ = _itkHistogramToTextureFeaturesFilterPython.delete_itkHistogramToTextureFeaturesFilterHF
    cast = _swig_new_static_method(_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_cast)

    def New(*args, **kargs):
        """New() -> itkHistogramToTextureFeaturesFilterHF

        Create a new object of the class itkHistogramToTextureFeaturesFilterHF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkHistogramToTextureFeaturesFilterHF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkHistogramToTextureFeaturesFilterHF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkHistogramToTextureFeaturesFilterHF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkHistogramToTextureFeaturesFilterHF in _itkHistogramToTextureFeaturesFilterPython:
_itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_swigregister(itkHistogramToTextureFeaturesFilterHF)
itkHistogramToTextureFeaturesFilterHF___New_orig__ = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF___New_orig__
itkHistogramToTextureFeaturesFilterHF_cast = _itkHistogramToTextureFeaturesFilterPython.itkHistogramToTextureFeaturesFilterHF_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def histogram_to_texture_features_filter(*args, **kwargs):
    """Procedural interface for HistogramToTextureFeaturesFilter"""
    import itk
    instance = itk.HistogramToTextureFeaturesFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def histogram_to_texture_features_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.HistogramToTextureFeaturesFilter, itkTemplate.itkTemplate):
        filter_object = itk.HistogramToTextureFeaturesFilter.values()[0]
    else:
        filter_object = itk.HistogramToTextureFeaturesFilter

    histogram_to_texture_features_filter.__doc__ = filter_object.__doc__
    histogram_to_texture_features_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    histogram_to_texture_features_filter.__doc__ += "Available Keyword Arguments:\n"
    histogram_to_texture_features_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



