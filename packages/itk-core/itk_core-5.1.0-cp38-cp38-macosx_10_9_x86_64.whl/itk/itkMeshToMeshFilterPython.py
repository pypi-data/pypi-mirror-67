# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkMeshToMeshFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkMeshToMeshFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkMeshToMeshFilterPython
            return _itkMeshToMeshFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkMeshToMeshFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkMeshToMeshFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkMeshToMeshFilterPython
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
import itkMeshSourcePython
import itkPointSetPython
import itkVectorContainerPython
import itkContinuousIndexPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkPointPython
import itkVectorPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkMatrixPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import itkMeshBasePython
import itkBoundingBoxPython
import itkMapContainerPython
import itkArrayPython

def itkMeshToMeshFilterMD3MD3_New():
  return itkMeshToMeshFilterMD3MD3.New()


def itkMeshToMeshFilterMF3MF3_New():
  return itkMeshToMeshFilterMF3MF3.New()


def itkMeshToMeshFilterMD2MD2_New():
  return itkMeshToMeshFilterMD2MD2.New()


def itkMeshToMeshFilterMF2MF2_New():
  return itkMeshToMeshFilterMF2MF2.New()

class itkMeshToMeshFilterMD2MD2(itkMeshSourcePython.itkMeshSourceMD2):
    """


    MeshToMeshFilter is the base class for all process objects that output
    mesh data, and require mesh data as input. Specifically, this class
    defines the SetInput() method for defining the input to a filter.

    C++ includes: itkMeshToMeshFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMeshToMeshFilterMD2MD2_Pointer":
        """__New_orig__() -> itkMeshToMeshFilterMD2MD2_Pointer"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMD2MD2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMeshToMeshFilterMD2MD2_Pointer":
        """Clone(itkMeshToMeshFilterMD2MD2 self) -> itkMeshToMeshFilterMD2MD2_Pointer"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMD2MD2_Clone(self)


    def SetInput(self, input: 'itkMeshD2') -> "void":
        """SetInput(itkMeshToMeshFilterMD2MD2 self, itkMeshD2 input)"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMD2MD2_SetInput(self, input)


    def GetInput(self, *args) -> "itkMeshD2 const *":
        """
        GetInput(itkMeshToMeshFilterMD2MD2 self) -> itkMeshD2
        GetInput(itkMeshToMeshFilterMD2MD2 self, unsigned int idx) -> itkMeshD2

        Get the mesh input of this
        process object. 
        """
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMD2MD2_GetInput(self, *args)

    __swig_destroy__ = _itkMeshToMeshFilterPython.delete_itkMeshToMeshFilterMD2MD2

    def cast(obj: 'itkLightObject') -> "itkMeshToMeshFilterMD2MD2 *":
        """cast(itkLightObject obj) -> itkMeshToMeshFilterMD2MD2"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMD2MD2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkMeshToMeshFilterMD2MD2

        Create a new object of the class itkMeshToMeshFilterMD2MD2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeshToMeshFilterMD2MD2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeshToMeshFilterMD2MD2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeshToMeshFilterMD2MD2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMeshToMeshFilterMD2MD2.Clone = new_instancemethod(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMD2MD2_Clone, None, itkMeshToMeshFilterMD2MD2)
itkMeshToMeshFilterMD2MD2.SetInput = new_instancemethod(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMD2MD2_SetInput, None, itkMeshToMeshFilterMD2MD2)
itkMeshToMeshFilterMD2MD2.GetInput = new_instancemethod(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMD2MD2_GetInput, None, itkMeshToMeshFilterMD2MD2)
itkMeshToMeshFilterMD2MD2_swigregister = _itkMeshToMeshFilterPython.itkMeshToMeshFilterMD2MD2_swigregister
itkMeshToMeshFilterMD2MD2_swigregister(itkMeshToMeshFilterMD2MD2)

def itkMeshToMeshFilterMD2MD2___New_orig__() -> "itkMeshToMeshFilterMD2MD2_Pointer":
    """itkMeshToMeshFilterMD2MD2___New_orig__() -> itkMeshToMeshFilterMD2MD2_Pointer"""
    return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMD2MD2___New_orig__()

def itkMeshToMeshFilterMD2MD2_cast(obj: 'itkLightObject') -> "itkMeshToMeshFilterMD2MD2 *":
    """itkMeshToMeshFilterMD2MD2_cast(itkLightObject obj) -> itkMeshToMeshFilterMD2MD2"""
    return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMD2MD2_cast(obj)

class itkMeshToMeshFilterMD3MD3(itkMeshSourcePython.itkMeshSourceMD3):
    """


    MeshToMeshFilter is the base class for all process objects that output
    mesh data, and require mesh data as input. Specifically, this class
    defines the SetInput() method for defining the input to a filter.

    C++ includes: itkMeshToMeshFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMeshToMeshFilterMD3MD3_Pointer":
        """__New_orig__() -> itkMeshToMeshFilterMD3MD3_Pointer"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMD3MD3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMeshToMeshFilterMD3MD3_Pointer":
        """Clone(itkMeshToMeshFilterMD3MD3 self) -> itkMeshToMeshFilterMD3MD3_Pointer"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMD3MD3_Clone(self)


    def SetInput(self, input: 'itkMeshD3') -> "void":
        """SetInput(itkMeshToMeshFilterMD3MD3 self, itkMeshD3 input)"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMD3MD3_SetInput(self, input)


    def GetInput(self, *args) -> "itkMeshD3 const *":
        """
        GetInput(itkMeshToMeshFilterMD3MD3 self) -> itkMeshD3
        GetInput(itkMeshToMeshFilterMD3MD3 self, unsigned int idx) -> itkMeshD3

        Get the mesh input of this
        process object. 
        """
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMD3MD3_GetInput(self, *args)

    __swig_destroy__ = _itkMeshToMeshFilterPython.delete_itkMeshToMeshFilterMD3MD3

    def cast(obj: 'itkLightObject') -> "itkMeshToMeshFilterMD3MD3 *":
        """cast(itkLightObject obj) -> itkMeshToMeshFilterMD3MD3"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMD3MD3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkMeshToMeshFilterMD3MD3

        Create a new object of the class itkMeshToMeshFilterMD3MD3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeshToMeshFilterMD3MD3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeshToMeshFilterMD3MD3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeshToMeshFilterMD3MD3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMeshToMeshFilterMD3MD3.Clone = new_instancemethod(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMD3MD3_Clone, None, itkMeshToMeshFilterMD3MD3)
itkMeshToMeshFilterMD3MD3.SetInput = new_instancemethod(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMD3MD3_SetInput, None, itkMeshToMeshFilterMD3MD3)
itkMeshToMeshFilterMD3MD3.GetInput = new_instancemethod(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMD3MD3_GetInput, None, itkMeshToMeshFilterMD3MD3)
itkMeshToMeshFilterMD3MD3_swigregister = _itkMeshToMeshFilterPython.itkMeshToMeshFilterMD3MD3_swigregister
itkMeshToMeshFilterMD3MD3_swigregister(itkMeshToMeshFilterMD3MD3)

def itkMeshToMeshFilterMD3MD3___New_orig__() -> "itkMeshToMeshFilterMD3MD3_Pointer":
    """itkMeshToMeshFilterMD3MD3___New_orig__() -> itkMeshToMeshFilterMD3MD3_Pointer"""
    return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMD3MD3___New_orig__()

def itkMeshToMeshFilterMD3MD3_cast(obj: 'itkLightObject') -> "itkMeshToMeshFilterMD3MD3 *":
    """itkMeshToMeshFilterMD3MD3_cast(itkLightObject obj) -> itkMeshToMeshFilterMD3MD3"""
    return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMD3MD3_cast(obj)

class itkMeshToMeshFilterMF2MF2(itkMeshSourcePython.itkMeshSourceMF2):
    """


    MeshToMeshFilter is the base class for all process objects that output
    mesh data, and require mesh data as input. Specifically, this class
    defines the SetInput() method for defining the input to a filter.

    C++ includes: itkMeshToMeshFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMeshToMeshFilterMF2MF2_Pointer":
        """__New_orig__() -> itkMeshToMeshFilterMF2MF2_Pointer"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2MF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMeshToMeshFilterMF2MF2_Pointer":
        """Clone(itkMeshToMeshFilterMF2MF2 self) -> itkMeshToMeshFilterMF2MF2_Pointer"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2MF2_Clone(self)


    def SetInput(self, input: 'itkMeshF2') -> "void":
        """SetInput(itkMeshToMeshFilterMF2MF2 self, itkMeshF2 input)"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2MF2_SetInput(self, input)


    def GetInput(self, *args) -> "itkMeshF2 const *":
        """
        GetInput(itkMeshToMeshFilterMF2MF2 self) -> itkMeshF2
        GetInput(itkMeshToMeshFilterMF2MF2 self, unsigned int idx) -> itkMeshF2

        Get the mesh input of this
        process object. 
        """
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2MF2_GetInput(self, *args)

    __swig_destroy__ = _itkMeshToMeshFilterPython.delete_itkMeshToMeshFilterMF2MF2

    def cast(obj: 'itkLightObject') -> "itkMeshToMeshFilterMF2MF2 *":
        """cast(itkLightObject obj) -> itkMeshToMeshFilterMF2MF2"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2MF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkMeshToMeshFilterMF2MF2

        Create a new object of the class itkMeshToMeshFilterMF2MF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeshToMeshFilterMF2MF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeshToMeshFilterMF2MF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeshToMeshFilterMF2MF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMeshToMeshFilterMF2MF2.Clone = new_instancemethod(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2MF2_Clone, None, itkMeshToMeshFilterMF2MF2)
itkMeshToMeshFilterMF2MF2.SetInput = new_instancemethod(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2MF2_SetInput, None, itkMeshToMeshFilterMF2MF2)
itkMeshToMeshFilterMF2MF2.GetInput = new_instancemethod(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2MF2_GetInput, None, itkMeshToMeshFilterMF2MF2)
itkMeshToMeshFilterMF2MF2_swigregister = _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2MF2_swigregister
itkMeshToMeshFilterMF2MF2_swigregister(itkMeshToMeshFilterMF2MF2)

def itkMeshToMeshFilterMF2MF2___New_orig__() -> "itkMeshToMeshFilterMF2MF2_Pointer":
    """itkMeshToMeshFilterMF2MF2___New_orig__() -> itkMeshToMeshFilterMF2MF2_Pointer"""
    return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2MF2___New_orig__()

def itkMeshToMeshFilterMF2MF2_cast(obj: 'itkLightObject') -> "itkMeshToMeshFilterMF2MF2 *":
    """itkMeshToMeshFilterMF2MF2_cast(itkLightObject obj) -> itkMeshToMeshFilterMF2MF2"""
    return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2MF2_cast(obj)

class itkMeshToMeshFilterMF3MF3(itkMeshSourcePython.itkMeshSourceMF3):
    """


    MeshToMeshFilter is the base class for all process objects that output
    mesh data, and require mesh data as input. Specifically, this class
    defines the SetInput() method for defining the input to a filter.

    C++ includes: itkMeshToMeshFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMeshToMeshFilterMF3MF3_Pointer":
        """__New_orig__() -> itkMeshToMeshFilterMF3MF3_Pointer"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3MF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMeshToMeshFilterMF3MF3_Pointer":
        """Clone(itkMeshToMeshFilterMF3MF3 self) -> itkMeshToMeshFilterMF3MF3_Pointer"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3MF3_Clone(self)


    def SetInput(self, input: 'itkMeshF3') -> "void":
        """SetInput(itkMeshToMeshFilterMF3MF3 self, itkMeshF3 input)"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3MF3_SetInput(self, input)


    def GetInput(self, *args) -> "itkMeshF3 const *":
        """
        GetInput(itkMeshToMeshFilterMF3MF3 self) -> itkMeshF3
        GetInput(itkMeshToMeshFilterMF3MF3 self, unsigned int idx) -> itkMeshF3

        Get the mesh input of this
        process object. 
        """
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3MF3_GetInput(self, *args)

    __swig_destroy__ = _itkMeshToMeshFilterPython.delete_itkMeshToMeshFilterMF3MF3

    def cast(obj: 'itkLightObject') -> "itkMeshToMeshFilterMF3MF3 *":
        """cast(itkLightObject obj) -> itkMeshToMeshFilterMF3MF3"""
        return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3MF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkMeshToMeshFilterMF3MF3

        Create a new object of the class itkMeshToMeshFilterMF3MF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeshToMeshFilterMF3MF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeshToMeshFilterMF3MF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeshToMeshFilterMF3MF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMeshToMeshFilterMF3MF3.Clone = new_instancemethod(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3MF3_Clone, None, itkMeshToMeshFilterMF3MF3)
itkMeshToMeshFilterMF3MF3.SetInput = new_instancemethod(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3MF3_SetInput, None, itkMeshToMeshFilterMF3MF3)
itkMeshToMeshFilterMF3MF3.GetInput = new_instancemethod(_itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3MF3_GetInput, None, itkMeshToMeshFilterMF3MF3)
itkMeshToMeshFilterMF3MF3_swigregister = _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3MF3_swigregister
itkMeshToMeshFilterMF3MF3_swigregister(itkMeshToMeshFilterMF3MF3)

def itkMeshToMeshFilterMF3MF3___New_orig__() -> "itkMeshToMeshFilterMF3MF3_Pointer":
    """itkMeshToMeshFilterMF3MF3___New_orig__() -> itkMeshToMeshFilterMF3MF3_Pointer"""
    return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3MF3___New_orig__()

def itkMeshToMeshFilterMF3MF3_cast(obj: 'itkLightObject') -> "itkMeshToMeshFilterMF3MF3 *":
    """itkMeshToMeshFilterMF3MF3_cast(itkLightObject obj) -> itkMeshToMeshFilterMF3MF3"""
    return _itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3MF3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def mesh_to_mesh_filter(*args, **kwargs):
    """Procedural interface for MeshToMeshFilter"""
    import itk
    instance = itk.MeshToMeshFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def mesh_to_mesh_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.MeshToMeshFilter, itkTemplate.itkTemplate):
        filter_object = itk.MeshToMeshFilter.values()[0]
    else:
        filter_object = itk.MeshToMeshFilter

    mesh_to_mesh_filter.__doc__ = filter_object.__doc__
    mesh_to_mesh_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    mesh_to_mesh_filter.__doc__ += "Available Keyword Arguments:\n"
    mesh_to_mesh_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



