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
    from . import _itkVariableSizeMatrixPython
else:
    import _itkVariableSizeMatrixPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkVariableSizeMatrixPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkVariableSizeMatrixPython.SWIG_PyStaticMethod_New

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


import vnl_matrixPython
import stdcomplexPython
import pyBasePython
import vnl_vectorPython
import itkArrayPython
class itkVariableSizeMatrixD(object):
    r"""Proxy of C++ itkVariableSizeMatrixD class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __add__ = _swig_new_instance_method(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD___add__)
    __iadd__ = _swig_new_instance_method(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD___iadd__)
    __sub__ = _swig_new_instance_method(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD___sub__)
    __isub__ = _swig_new_instance_method(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD___isub__)
    __neg__ = _swig_new_instance_method(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD___neg__)
    __imul__ = _swig_new_instance_method(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD___imul__)
    __mul__ = _swig_new_instance_method(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD___mul__)

    def __itruediv__(self, *args):
        return _itkVariableSizeMatrixPython.itkVariableSizeMatrixD___itruediv__(self, *args)
    __idiv__ = __itruediv__



    def __truediv__(self, *args):
        return _itkVariableSizeMatrixPython.itkVariableSizeMatrixD___truediv__(self, *args)
    __div__ = __truediv__


    __call__ = _swig_new_instance_method(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD___call__)
    GetVnlMatrix = _swig_new_instance_method(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD_GetVnlMatrix)
    SetIdentity = _swig_new_instance_method(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD_SetIdentity)
    Fill = _swig_new_instance_method(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD_Fill)
    __eq__ = _swig_new_instance_method(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD___eq__)
    __ne__ = _swig_new_instance_method(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD___ne__)
    GetInverse = _swig_new_instance_method(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD_GetInverse)
    GetTranspose = _swig_new_instance_method(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD_GetTranspose)

    def __init__(self, *args):
        r"""
        __init__(itkVariableSizeMatrixD self) -> itkVariableSizeMatrixD
        __init__(itkVariableSizeMatrixD self, unsigned int rows, unsigned int cols) -> itkVariableSizeMatrixD
        __init__(itkVariableSizeMatrixD self, itkVariableSizeMatrixD matrix) -> itkVariableSizeMatrixD
        """
        _itkVariableSizeMatrixPython.itkVariableSizeMatrixD_swiginit(self, _itkVariableSizeMatrixPython.new_itkVariableSizeMatrixD(*args))
    Rows = _swig_new_instance_method(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD_Rows)
    Cols = _swig_new_instance_method(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD_Cols)
    SetSize = _swig_new_instance_method(_itkVariableSizeMatrixPython.itkVariableSizeMatrixD_SetSize)
    __swig_destroy__ = _itkVariableSizeMatrixPython.delete_itkVariableSizeMatrixD

# Register itkVariableSizeMatrixD in _itkVariableSizeMatrixPython:
_itkVariableSizeMatrixPython.itkVariableSizeMatrixD_swigregister(itkVariableSizeMatrixD)



