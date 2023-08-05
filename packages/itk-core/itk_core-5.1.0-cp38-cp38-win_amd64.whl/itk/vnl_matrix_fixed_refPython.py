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
    from . import _vnl_matrix_fixed_refPython
else:
    import _vnl_matrix_fixed_refPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _vnl_matrix_fixed_refPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _vnl_matrix_fixed_refPython.SWIG_PyStaticMethod_New

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


import vnl_matrix_fixedPython
import vnl_vectorPython
import stdcomplexPython
import pyBasePython
import vnl_matrixPython
class vnl_matrix_fixed_ref_constF_3_3(object):
    r"""Proxy of C++ vnl_matrix_fixed_ref_constF_3_3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(vnl_matrix_fixed_ref_constF_3_3 self, vnl_matrix_fixedF_3_3 rhs) -> vnl_matrix_fixed_ref_constF_3_3
        __init__(vnl_matrix_fixed_ref_constF_3_3 self, float const * dataptr) -> vnl_matrix_fixed_ref_constF_3_3
        __init__(vnl_matrix_fixed_ref_constF_3_3 self, vnl_matrix_fixed_ref_constF_3_3 rhs) -> vnl_matrix_fixed_ref_constF_3_3
        """
        _vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_swiginit(self, _vnl_matrix_fixed_refPython.new_vnl_matrix_fixed_ref_constF_3_3(*args))
    get_row = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_get_row)
    get_column = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_get_column)
    get_diagonal = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_get_diagonal)
    data_block = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_data_block)
    begin = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_begin)
    end = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_end)
    __call__ = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3___call__)
    rows = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_rows)
    columns = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_columns)
    cols = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_cols)
    size = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_size)
    _print = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3__print)
    copy_out = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_copy_out)
    transpose = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_transpose)
    conjugate_transpose = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_conjugate_transpose)
    extract = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_extract)
    get_n_rows = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_get_n_rows)
    get_n_columns = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_get_n_columns)
    array_one_norm = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_array_one_norm)
    array_two_norm = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_array_two_norm)
    array_inf_norm = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_array_inf_norm)
    absolute_value_sum = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_absolute_value_sum)
    absolute_value_max = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_absolute_value_max)
    operator_one_norm = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_operator_one_norm)
    operator_inf_norm = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_operator_inf_norm)
    frobenius_norm = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_frobenius_norm)
    fro_norm = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_fro_norm)
    rms = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_rms)
    min_value = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_min_value)
    max_value = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_max_value)
    arg_min = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_arg_min)
    arg_max = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_arg_max)
    mean = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_mean)
    empty = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_empty)
    is_identity = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_is_identity)
    is_zero = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_is_zero)
    is_finite = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_is_finite)
    has_nans = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_has_nans)
    assert_size = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_assert_size)
    assert_finite = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_assert_finite)
    add = _swig_new_static_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_add)
    sub = _swig_new_static_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_sub)
    mul = _swig_new_static_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_mul)
    div = _swig_new_static_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_div)
    equal = _swig_new_static_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_equal)
    __swig_destroy__ = _vnl_matrix_fixed_refPython.delete_vnl_matrix_fixed_ref_constF_3_3

# Register vnl_matrix_fixed_ref_constF_3_3 in _vnl_matrix_fixed_refPython:
_vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_swigregister(vnl_matrix_fixed_ref_constF_3_3)
vnl_matrix_fixed_ref_constF_3_3_add = _vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_add
vnl_matrix_fixed_ref_constF_3_3_sub = _vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_sub
vnl_matrix_fixed_ref_constF_3_3_mul = _vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_mul
vnl_matrix_fixed_ref_constF_3_3_div = _vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_div
vnl_matrix_fixed_ref_constF_3_3_equal = _vnl_matrix_fixed_refPython.vnl_matrix_fixed_ref_constF_3_3_equal

class vnl_matrix_fixed_refF_3_3(vnl_matrix_fixed_ref_constF_3_3):
    r"""Proxy of C++ vnl_matrix_fixed_refF_3_3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    data_block = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3_data_block)
    put = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3_put)
    get = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3_get)
    __call__ = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3___call__)
    fill = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3_fill)
    fill_diagonal = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3_fill_diagonal)
    set_diagonal = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3_set_diagonal)
    copy_in = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3_copy_in)
    set = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3_set)
    inplace_transpose = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3_inplace_transpose)

    def __itruediv__(self, *args):
        return _vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3___itruediv__(self, *args)
    __idiv__ = __itruediv__


    __iadd__ = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3___iadd__)
    __isub__ = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3___isub__)
    __neg__ = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3___neg__)
    __imul__ = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3___imul__)
    update = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3_update)
    set_column = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3_set_column)
    set_columns = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3_set_columns)
    set_row = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3_set_row)
    set_identity = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3_set_identity)
    flipud = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3_flipud)
    fliplr = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3_fliplr)
    normalize_rows = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3_normalize_rows)
    normalize_columns = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3_normalize_columns)
    scale_row = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3_scale_row)
    scale_column = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3_scale_column)
    read_ascii = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3_read_ascii)
    as_matrix = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3_as_matrix)
    begin = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3_begin)
    end = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3_end)
    operator_eq = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3_operator_eq)
    __eq__ = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3___eq__)
    __ne__ = _swig_new_instance_method(_vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3___ne__)

    def __init__(self, *args):
        r"""
        __init__(vnl_matrix_fixed_refF_3_3 self, vnl_matrix_fixedF_3_3 rhs) -> vnl_matrix_fixed_refF_3_3
        __init__(vnl_matrix_fixed_refF_3_3 self, float * dataptr) -> vnl_matrix_fixed_refF_3_3
        __init__(vnl_matrix_fixed_refF_3_3 self, vnl_matrix_fixed_refF_3_3 arg0) -> vnl_matrix_fixed_refF_3_3
        """
        _vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3_swiginit(self, _vnl_matrix_fixed_refPython.new_vnl_matrix_fixed_refF_3_3(*args))
    __swig_destroy__ = _vnl_matrix_fixed_refPython.delete_vnl_matrix_fixed_refF_3_3

# Register vnl_matrix_fixed_refF_3_3 in _vnl_matrix_fixed_refPython:
_vnl_matrix_fixed_refPython.vnl_matrix_fixed_refF_3_3_swigregister(vnl_matrix_fixed_refF_3_3)



