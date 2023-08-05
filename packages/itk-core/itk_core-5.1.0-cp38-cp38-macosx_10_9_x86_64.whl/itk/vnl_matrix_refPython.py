# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _vnl_matrix_refPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_vnl_matrix_refPython', [dirname(__file__)])
        except ImportError:
            import _vnl_matrix_refPython
            return _vnl_matrix_refPython
        if fp is not None:
            try:
                _mod = imp.load_module('_vnl_matrix_refPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _vnl_matrix_refPython = swig_import_helper()
    del swig_import_helper
else:
    import _vnl_matrix_refPython
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


import vnl_matrixPython
import stdcomplexPython
import pyBasePython
import vnl_vectorPython
class vnl_matrix_refD(vnl_matrixPython.vnl_matrixD):
    """Proxy of C++ vnl_matrix_refD class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(vnl_matrix_refD self, unsigned int row, unsigned int col, double const * datablck) -> vnl_matrix_refD
        __init__(vnl_matrix_refD self, vnl_matrix_refD other) -> vnl_matrix_refD
        """
        _vnl_matrix_refPython.vnl_matrix_refD_swiginit(self, _vnl_matrix_refPython.new_vnl_matrix_refD(*args))
    __swig_destroy__ = _vnl_matrix_refPython.delete_vnl_matrix_refD

    def non_const(self) -> "vnl_matrix_refD &":
        """non_const(vnl_matrix_refD self) -> vnl_matrix_refD"""
        return _vnl_matrix_refPython.vnl_matrix_refD_non_const(self)

vnl_matrix_refD.non_const = new_instancemethod(_vnl_matrix_refPython.vnl_matrix_refD_non_const, None, vnl_matrix_refD)
vnl_matrix_refD_swigregister = _vnl_matrix_refPython.vnl_matrix_refD_swigregister
vnl_matrix_refD_swigregister(vnl_matrix_refD)

class vnl_matrix_refF(vnl_matrixPython.vnl_matrixF):
    """Proxy of C++ vnl_matrix_refF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(vnl_matrix_refF self, unsigned int row, unsigned int col, float const * datablck) -> vnl_matrix_refF
        __init__(vnl_matrix_refF self, vnl_matrix_refF other) -> vnl_matrix_refF
        """
        _vnl_matrix_refPython.vnl_matrix_refF_swiginit(self, _vnl_matrix_refPython.new_vnl_matrix_refF(*args))
    __swig_destroy__ = _vnl_matrix_refPython.delete_vnl_matrix_refF

    def non_const(self) -> "vnl_matrix_refF &":
        """non_const(vnl_matrix_refF self) -> vnl_matrix_refF"""
        return _vnl_matrix_refPython.vnl_matrix_refF_non_const(self)

vnl_matrix_refF.non_const = new_instancemethod(_vnl_matrix_refPython.vnl_matrix_refF_non_const, None, vnl_matrix_refF)
vnl_matrix_refF_swigregister = _vnl_matrix_refPython.vnl_matrix_refF_swigregister
vnl_matrix_refF_swigregister(vnl_matrix_refF)



