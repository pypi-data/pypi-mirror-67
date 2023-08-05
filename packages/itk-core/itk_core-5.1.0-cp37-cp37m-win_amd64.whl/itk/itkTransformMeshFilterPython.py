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
    from . import _itkTransformMeshFilterPython
else:
    import _itkTransformMeshFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkTransformMeshFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkTransformMeshFilterPython.SWIG_PyStaticMethod_New

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


import itkTransformBasePython
import itkVectorPython
import vnl_vector_refPython
import stdcomplexPython
import pyBasePython
import vnl_vectorPython
import vnl_matrixPython
import itkFixedArrayPython
import itkPointPython
import ITKCommonBasePython
import itkCovariantVectorPython
import itkVariableLengthVectorPython
import itkArray2DPython
import itkArrayPython
import itkOptimizerParametersPython
import vnl_matrix_fixedPython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import itkMeshToMeshFilterPython
import itkMeshBasePython
import itkBoundingBoxPython
import itkVectorContainerPython
import itkOffsetPython
import itkSizePython
import itkContinuousIndexPython
import itkIndexPython
import itkMapContainerPython
import itkPointSetPython
import itkMeshSourcePython

def itkTransformMeshFilterMD3MD3TF33_New():
  return itkTransformMeshFilterMD3MD3TF33.New()


def itkTransformMeshFilterMD3MD3TD33_New():
  return itkTransformMeshFilterMD3MD3TD33.New()


def itkTransformMeshFilterMF3MF3TF33_New():
  return itkTransformMeshFilterMF3MF3TF33.New()


def itkTransformMeshFilterMF3MF3TD33_New():
  return itkTransformMeshFilterMF3MF3TD33.New()


def itkTransformMeshFilterMD2MD2TF22_New():
  return itkTransformMeshFilterMD2MD2TF22.New()


def itkTransformMeshFilterMD2MD2TD22_New():
  return itkTransformMeshFilterMD2MD2TD22.New()


def itkTransformMeshFilterMF2MF2TF22_New():
  return itkTransformMeshFilterMF2MF2TF22.New()


def itkTransformMeshFilterMF2MF2TD22_New():
  return itkTransformMeshFilterMF2MF2TD22.New()

class itkTransformMeshFilterMD2MD2TD22(itkMeshToMeshFilterPython.itkMeshToMeshFilterMD2MD2):
    r"""Proxy of C++ itkTransformMeshFilterMD2MD2TD22 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMD2MD2TD22___New_orig__)
    Clone = _swig_new_instance_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMD2MD2TD22_Clone)
    SetTransform = _swig_new_instance_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMD2MD2TD22_SetTransform)
    GetModifiableTransform = _swig_new_instance_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMD2MD2TD22_GetModifiableTransform)
    GetTransform = _swig_new_instance_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMD2MD2TD22_GetTransform)
    __swig_destroy__ = _itkTransformMeshFilterPython.delete_itkTransformMeshFilterMD2MD2TD22
    cast = _swig_new_static_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMD2MD2TD22_cast)

    def New(*args, **kargs):
        """New() -> itkTransformMeshFilterMD2MD2TD22

        Create a new object of the class itkTransformMeshFilterMD2MD2TD22 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTransformMeshFilterMD2MD2TD22.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTransformMeshFilterMD2MD2TD22.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTransformMeshFilterMD2MD2TD22.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTransformMeshFilterMD2MD2TD22 in _itkTransformMeshFilterPython:
_itkTransformMeshFilterPython.itkTransformMeshFilterMD2MD2TD22_swigregister(itkTransformMeshFilterMD2MD2TD22)
itkTransformMeshFilterMD2MD2TD22___New_orig__ = _itkTransformMeshFilterPython.itkTransformMeshFilterMD2MD2TD22___New_orig__
itkTransformMeshFilterMD2MD2TD22_cast = _itkTransformMeshFilterPython.itkTransformMeshFilterMD2MD2TD22_cast

class itkTransformMeshFilterMD2MD2TF22(itkMeshToMeshFilterPython.itkMeshToMeshFilterMD2MD2):
    r"""Proxy of C++ itkTransformMeshFilterMD2MD2TF22 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMD2MD2TF22___New_orig__)
    Clone = _swig_new_instance_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMD2MD2TF22_Clone)
    SetTransform = _swig_new_instance_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMD2MD2TF22_SetTransform)
    GetModifiableTransform = _swig_new_instance_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMD2MD2TF22_GetModifiableTransform)
    GetTransform = _swig_new_instance_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMD2MD2TF22_GetTransform)
    __swig_destroy__ = _itkTransformMeshFilterPython.delete_itkTransformMeshFilterMD2MD2TF22
    cast = _swig_new_static_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMD2MD2TF22_cast)

    def New(*args, **kargs):
        """New() -> itkTransformMeshFilterMD2MD2TF22

        Create a new object of the class itkTransformMeshFilterMD2MD2TF22 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTransformMeshFilterMD2MD2TF22.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTransformMeshFilterMD2MD2TF22.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTransformMeshFilterMD2MD2TF22.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTransformMeshFilterMD2MD2TF22 in _itkTransformMeshFilterPython:
_itkTransformMeshFilterPython.itkTransformMeshFilterMD2MD2TF22_swigregister(itkTransformMeshFilterMD2MD2TF22)
itkTransformMeshFilterMD2MD2TF22___New_orig__ = _itkTransformMeshFilterPython.itkTransformMeshFilterMD2MD2TF22___New_orig__
itkTransformMeshFilterMD2MD2TF22_cast = _itkTransformMeshFilterPython.itkTransformMeshFilterMD2MD2TF22_cast

class itkTransformMeshFilterMD3MD3TD33(itkMeshToMeshFilterPython.itkMeshToMeshFilterMD3MD3):
    r"""Proxy of C++ itkTransformMeshFilterMD3MD3TD33 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMD3MD3TD33___New_orig__)
    Clone = _swig_new_instance_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMD3MD3TD33_Clone)
    SetTransform = _swig_new_instance_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMD3MD3TD33_SetTransform)
    GetModifiableTransform = _swig_new_instance_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMD3MD3TD33_GetModifiableTransform)
    GetTransform = _swig_new_instance_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMD3MD3TD33_GetTransform)
    __swig_destroy__ = _itkTransformMeshFilterPython.delete_itkTransformMeshFilterMD3MD3TD33
    cast = _swig_new_static_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMD3MD3TD33_cast)

    def New(*args, **kargs):
        """New() -> itkTransformMeshFilterMD3MD3TD33

        Create a new object of the class itkTransformMeshFilterMD3MD3TD33 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTransformMeshFilterMD3MD3TD33.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTransformMeshFilterMD3MD3TD33.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTransformMeshFilterMD3MD3TD33.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTransformMeshFilterMD3MD3TD33 in _itkTransformMeshFilterPython:
_itkTransformMeshFilterPython.itkTransformMeshFilterMD3MD3TD33_swigregister(itkTransformMeshFilterMD3MD3TD33)
itkTransformMeshFilterMD3MD3TD33___New_orig__ = _itkTransformMeshFilterPython.itkTransformMeshFilterMD3MD3TD33___New_orig__
itkTransformMeshFilterMD3MD3TD33_cast = _itkTransformMeshFilterPython.itkTransformMeshFilterMD3MD3TD33_cast

class itkTransformMeshFilterMD3MD3TF33(itkMeshToMeshFilterPython.itkMeshToMeshFilterMD3MD3):
    r"""Proxy of C++ itkTransformMeshFilterMD3MD3TF33 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMD3MD3TF33___New_orig__)
    Clone = _swig_new_instance_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMD3MD3TF33_Clone)
    SetTransform = _swig_new_instance_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMD3MD3TF33_SetTransform)
    GetModifiableTransform = _swig_new_instance_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMD3MD3TF33_GetModifiableTransform)
    GetTransform = _swig_new_instance_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMD3MD3TF33_GetTransform)
    __swig_destroy__ = _itkTransformMeshFilterPython.delete_itkTransformMeshFilterMD3MD3TF33
    cast = _swig_new_static_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMD3MD3TF33_cast)

    def New(*args, **kargs):
        """New() -> itkTransformMeshFilterMD3MD3TF33

        Create a new object of the class itkTransformMeshFilterMD3MD3TF33 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTransformMeshFilterMD3MD3TF33.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTransformMeshFilterMD3MD3TF33.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTransformMeshFilterMD3MD3TF33.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTransformMeshFilterMD3MD3TF33 in _itkTransformMeshFilterPython:
_itkTransformMeshFilterPython.itkTransformMeshFilterMD3MD3TF33_swigregister(itkTransformMeshFilterMD3MD3TF33)
itkTransformMeshFilterMD3MD3TF33___New_orig__ = _itkTransformMeshFilterPython.itkTransformMeshFilterMD3MD3TF33___New_orig__
itkTransformMeshFilterMD3MD3TF33_cast = _itkTransformMeshFilterPython.itkTransformMeshFilterMD3MD3TF33_cast

class itkTransformMeshFilterMF2MF2TD22(itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2MF2):
    r"""Proxy of C++ itkTransformMeshFilterMF2MF2TD22 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMF2MF2TD22___New_orig__)
    Clone = _swig_new_instance_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMF2MF2TD22_Clone)
    SetTransform = _swig_new_instance_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMF2MF2TD22_SetTransform)
    GetModifiableTransform = _swig_new_instance_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMF2MF2TD22_GetModifiableTransform)
    GetTransform = _swig_new_instance_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMF2MF2TD22_GetTransform)
    __swig_destroy__ = _itkTransformMeshFilterPython.delete_itkTransformMeshFilterMF2MF2TD22
    cast = _swig_new_static_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMF2MF2TD22_cast)

    def New(*args, **kargs):
        """New() -> itkTransformMeshFilterMF2MF2TD22

        Create a new object of the class itkTransformMeshFilterMF2MF2TD22 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTransformMeshFilterMF2MF2TD22.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTransformMeshFilterMF2MF2TD22.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTransformMeshFilterMF2MF2TD22.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTransformMeshFilterMF2MF2TD22 in _itkTransformMeshFilterPython:
_itkTransformMeshFilterPython.itkTransformMeshFilterMF2MF2TD22_swigregister(itkTransformMeshFilterMF2MF2TD22)
itkTransformMeshFilterMF2MF2TD22___New_orig__ = _itkTransformMeshFilterPython.itkTransformMeshFilterMF2MF2TD22___New_orig__
itkTransformMeshFilterMF2MF2TD22_cast = _itkTransformMeshFilterPython.itkTransformMeshFilterMF2MF2TD22_cast

class itkTransformMeshFilterMF2MF2TF22(itkMeshToMeshFilterPython.itkMeshToMeshFilterMF2MF2):
    r"""Proxy of C++ itkTransformMeshFilterMF2MF2TF22 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMF2MF2TF22___New_orig__)
    Clone = _swig_new_instance_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMF2MF2TF22_Clone)
    SetTransform = _swig_new_instance_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMF2MF2TF22_SetTransform)
    GetModifiableTransform = _swig_new_instance_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMF2MF2TF22_GetModifiableTransform)
    GetTransform = _swig_new_instance_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMF2MF2TF22_GetTransform)
    __swig_destroy__ = _itkTransformMeshFilterPython.delete_itkTransformMeshFilterMF2MF2TF22
    cast = _swig_new_static_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMF2MF2TF22_cast)

    def New(*args, **kargs):
        """New() -> itkTransformMeshFilterMF2MF2TF22

        Create a new object of the class itkTransformMeshFilterMF2MF2TF22 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTransformMeshFilterMF2MF2TF22.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTransformMeshFilterMF2MF2TF22.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTransformMeshFilterMF2MF2TF22.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTransformMeshFilterMF2MF2TF22 in _itkTransformMeshFilterPython:
_itkTransformMeshFilterPython.itkTransformMeshFilterMF2MF2TF22_swigregister(itkTransformMeshFilterMF2MF2TF22)
itkTransformMeshFilterMF2MF2TF22___New_orig__ = _itkTransformMeshFilterPython.itkTransformMeshFilterMF2MF2TF22___New_orig__
itkTransformMeshFilterMF2MF2TF22_cast = _itkTransformMeshFilterPython.itkTransformMeshFilterMF2MF2TF22_cast

class itkTransformMeshFilterMF3MF3TD33(itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3MF3):
    r"""Proxy of C++ itkTransformMeshFilterMF3MF3TD33 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMF3MF3TD33___New_orig__)
    Clone = _swig_new_instance_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMF3MF3TD33_Clone)
    SetTransform = _swig_new_instance_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMF3MF3TD33_SetTransform)
    GetModifiableTransform = _swig_new_instance_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMF3MF3TD33_GetModifiableTransform)
    GetTransform = _swig_new_instance_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMF3MF3TD33_GetTransform)
    __swig_destroy__ = _itkTransformMeshFilterPython.delete_itkTransformMeshFilterMF3MF3TD33
    cast = _swig_new_static_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMF3MF3TD33_cast)

    def New(*args, **kargs):
        """New() -> itkTransformMeshFilterMF3MF3TD33

        Create a new object of the class itkTransformMeshFilterMF3MF3TD33 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTransformMeshFilterMF3MF3TD33.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTransformMeshFilterMF3MF3TD33.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTransformMeshFilterMF3MF3TD33.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTransformMeshFilterMF3MF3TD33 in _itkTransformMeshFilterPython:
_itkTransformMeshFilterPython.itkTransformMeshFilterMF3MF3TD33_swigregister(itkTransformMeshFilterMF3MF3TD33)
itkTransformMeshFilterMF3MF3TD33___New_orig__ = _itkTransformMeshFilterPython.itkTransformMeshFilterMF3MF3TD33___New_orig__
itkTransformMeshFilterMF3MF3TD33_cast = _itkTransformMeshFilterPython.itkTransformMeshFilterMF3MF3TD33_cast

class itkTransformMeshFilterMF3MF3TF33(itkMeshToMeshFilterPython.itkMeshToMeshFilterMF3MF3):
    r"""Proxy of C++ itkTransformMeshFilterMF3MF3TF33 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMF3MF3TF33___New_orig__)
    Clone = _swig_new_instance_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMF3MF3TF33_Clone)
    SetTransform = _swig_new_instance_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMF3MF3TF33_SetTransform)
    GetModifiableTransform = _swig_new_instance_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMF3MF3TF33_GetModifiableTransform)
    GetTransform = _swig_new_instance_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMF3MF3TF33_GetTransform)
    __swig_destroy__ = _itkTransformMeshFilterPython.delete_itkTransformMeshFilterMF3MF3TF33
    cast = _swig_new_static_method(_itkTransformMeshFilterPython.itkTransformMeshFilterMF3MF3TF33_cast)

    def New(*args, **kargs):
        """New() -> itkTransformMeshFilterMF3MF3TF33

        Create a new object of the class itkTransformMeshFilterMF3MF3TF33 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTransformMeshFilterMF3MF3TF33.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTransformMeshFilterMF3MF3TF33.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTransformMeshFilterMF3MF3TF33.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTransformMeshFilterMF3MF3TF33 in _itkTransformMeshFilterPython:
_itkTransformMeshFilterPython.itkTransformMeshFilterMF3MF3TF33_swigregister(itkTransformMeshFilterMF3MF3TF33)
itkTransformMeshFilterMF3MF3TF33___New_orig__ = _itkTransformMeshFilterPython.itkTransformMeshFilterMF3MF3TF33___New_orig__
itkTransformMeshFilterMF3MF3TF33_cast = _itkTransformMeshFilterPython.itkTransformMeshFilterMF3MF3TF33_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def transform_mesh_filter(*args, **kwargs):
    """Procedural interface for TransformMeshFilter"""
    import itk
    instance = itk.TransformMeshFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def transform_mesh_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.TransformMeshFilter, itkTemplate.itkTemplate):
        filter_object = itk.TransformMeshFilter.values()[0]
    else:
        filter_object = itk.TransformMeshFilter

    transform_mesh_filter.__doc__ = filter_object.__doc__
    transform_mesh_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    transform_mesh_filter.__doc__ += "Available Keyword Arguments:\n"
    transform_mesh_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



