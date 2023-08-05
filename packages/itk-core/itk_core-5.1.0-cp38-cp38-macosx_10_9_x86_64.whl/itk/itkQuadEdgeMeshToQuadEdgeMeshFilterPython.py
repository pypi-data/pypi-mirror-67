# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkQuadEdgeMeshToQuadEdgeMeshFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkQuadEdgeMeshToQuadEdgeMeshFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkQuadEdgeMeshToQuadEdgeMeshFilterPython
            return _itkQuadEdgeMeshToQuadEdgeMeshFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkQuadEdgeMeshToQuadEdgeMeshFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkQuadEdgeMeshToQuadEdgeMeshFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkQuadEdgeMeshToQuadEdgeMeshFilterPython
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
import itkQuadEdgeMeshBasePython
import itkFixedArrayPython
import itkGeometricalQuadEdgePython
import itkQuadEdgePython
import itkQuadEdgeMeshLineCellPython
import itkQuadEdgeCellTraitsInfoPython
import itkQuadEdgeMeshPointPython
import itkPointPython
import itkVectorPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import vnl_vector_refPython
import itkArrayPython
import itkMapContainerPython
import itkImagePython
import itkCovariantVectorPython
import itkRGBPixelPython
import itkOffsetPython
import itkSizePython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkIndexPython
import itkRGBAPixelPython
import itkSymmetricSecondRankTensorPython
import itkImageRegionPython

def itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3_New():
  return itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3.New()


def itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2_New():
  return itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2.New()

class itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2(itkQuadEdgeMeshBasePython.itkMeshToMeshFilterQEMD2QEMD2):
    """


    Duplicates the content of a Mesh.

    Alexandre Gouaillard, Leonardo Florez-Valencia, Eric Boix  This
    implementation was contributed as a paper to the Insight
    Journalhttps://hdl.handle.net/1926/306

    C++ includes: itkQuadEdgeMeshToQuadEdgeMeshFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2_Pointer":
        """__New_orig__() -> itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2_Pointer"""
        return _itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2_Pointer":
        """Clone(itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2 self) -> itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2_Pointer"""
        return _itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2_Clone(self)

    __swig_destroy__ = _itkQuadEdgeMeshToQuadEdgeMeshFilterPython.delete_itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2

    def cast(obj: 'itkLightObject') -> "itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2 *":
        """cast(itkLightObject obj) -> itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2"""
        return _itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2

        Create a new object of the class itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2.Clone = new_instancemethod(_itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2_Clone, None, itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2)
itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2_swigregister = _itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2_swigregister
itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2_swigregister(itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2)

def itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2___New_orig__() -> "itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2_Pointer":
    """itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2___New_orig__() -> itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2_Pointer"""
    return _itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2___New_orig__()

def itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2_cast(obj: 'itkLightObject') -> "itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2 *":
    """itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2_cast(itkLightObject obj) -> itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2"""
    return _itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD2QEMD2_cast(obj)

class itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3(itkQuadEdgeMeshBasePython.itkMeshToMeshFilterQEMD3QEMD3):
    """


    Duplicates the content of a Mesh.

    Alexandre Gouaillard, Leonardo Florez-Valencia, Eric Boix  This
    implementation was contributed as a paper to the Insight
    Journalhttps://hdl.handle.net/1926/306

    C++ includes: itkQuadEdgeMeshToQuadEdgeMeshFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3_Pointer":
        """__New_orig__() -> itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3_Pointer"""
        return _itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3_Pointer":
        """Clone(itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3 self) -> itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3_Pointer"""
        return _itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3_Clone(self)

    __swig_destroy__ = _itkQuadEdgeMeshToQuadEdgeMeshFilterPython.delete_itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3

    def cast(obj: 'itkLightObject') -> "itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3 *":
        """cast(itkLightObject obj) -> itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3"""
        return _itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3

        Create a new object of the class itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3.Clone = new_instancemethod(_itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3_Clone, None, itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3)
itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3_swigregister = _itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3_swigregister
itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3_swigregister(itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3)

def itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3___New_orig__() -> "itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3_Pointer":
    """itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3___New_orig__() -> itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3_Pointer"""
    return _itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3___New_orig__()

def itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3_cast(obj: 'itkLightObject') -> "itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3 *":
    """itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3_cast(itkLightObject obj) -> itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3"""
    return _itkQuadEdgeMeshToQuadEdgeMeshFilterPython.itkQuadEdgeMeshToQuadEdgeMeshFilterQEMD3QEMD3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def quad_edge_mesh_to_quad_edge_mesh_filter(*args, **kwargs):
    """Procedural interface for QuadEdgeMeshToQuadEdgeMeshFilter"""
    import itk
    instance = itk.QuadEdgeMeshToQuadEdgeMeshFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def quad_edge_mesh_to_quad_edge_mesh_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.QuadEdgeMeshToQuadEdgeMeshFilter, itkTemplate.itkTemplate):
        filter_object = itk.QuadEdgeMeshToQuadEdgeMeshFilter.values()[0]
    else:
        filter_object = itk.QuadEdgeMeshToQuadEdgeMeshFilter

    quad_edge_mesh_to_quad_edge_mesh_filter.__doc__ = filter_object.__doc__
    quad_edge_mesh_to_quad_edge_mesh_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    quad_edge_mesh_to_quad_edge_mesh_filter.__doc__ += "Available Keyword Arguments:\n"
    quad_edge_mesh_to_quad_edge_mesh_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



