# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _vnl_least_squares_functionPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_vnl_least_squares_functionPython', [dirname(__file__)])
        except ImportError:
            import _vnl_least_squares_functionPython
            return _vnl_least_squares_functionPython
        if fp is not None:
            try:
                _mod = imp.load_module('_vnl_least_squares_functionPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _vnl_least_squares_functionPython = swig_import_helper()
    del swig_import_helper
else:
    import _vnl_least_squares_functionPython
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


import vnl_vectorPython
import stdcomplexPython
import pyBasePython
import vnl_matrixPython
class vnl_least_squares_function(object):
    """Proxy of C++ vnl_least_squares_function class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    UseGradient_no_gradient = _vnl_least_squares_functionPython.vnl_least_squares_function_UseGradient_no_gradient
    UseGradient_use_gradient = _vnl_least_squares_functionPython.vnl_least_squares_function_UseGradient_use_gradient
    __swig_destroy__ = _vnl_least_squares_functionPython.delete_vnl_least_squares_function

    def throw_failure(self) -> "void":
        """throw_failure(vnl_least_squares_function self)"""
        return _vnl_least_squares_functionPython.vnl_least_squares_function_throw_failure(self)


    def clear_failure(self) -> "void":
        """clear_failure(vnl_least_squares_function self)"""
        return _vnl_least_squares_functionPython.vnl_least_squares_function_clear_failure(self)


    def f(self, x: 'vnl_vectorD', fx: 'vnl_vectorD') -> "void":
        """f(vnl_least_squares_function self, vnl_vectorD x, vnl_vectorD fx)"""
        return _vnl_least_squares_functionPython.vnl_least_squares_function_f(self, x, fx)


    def gradf(self, x: 'vnl_vectorD', jacobian: 'vnl_matrixD') -> "void":
        """gradf(vnl_least_squares_function self, vnl_vectorD x, vnl_matrixD jacobian)"""
        return _vnl_least_squares_functionPython.vnl_least_squares_function_gradf(self, x, jacobian)


    def fdgradf(self, x: 'vnl_vectorD', jacobian: 'vnl_matrixD', stepsize: 'double') -> "void":
        """fdgradf(vnl_least_squares_function self, vnl_vectorD x, vnl_matrixD jacobian, double stepsize)"""
        return _vnl_least_squares_functionPython.vnl_least_squares_function_fdgradf(self, x, jacobian, stepsize)


    def ffdgradf(self, x: 'vnl_vectorD', jacobian: 'vnl_matrixD', stepsize: 'double') -> "void":
        """ffdgradf(vnl_least_squares_function self, vnl_vectorD x, vnl_matrixD jacobian, double stepsize)"""
        return _vnl_least_squares_functionPython.vnl_least_squares_function_ffdgradf(self, x, jacobian, stepsize)


    def trace(self, iteration: 'int', x: 'vnl_vectorD', fx: 'vnl_vectorD') -> "void":
        """trace(vnl_least_squares_function self, int iteration, vnl_vectorD x, vnl_vectorD fx)"""
        return _vnl_least_squares_functionPython.vnl_least_squares_function_trace(self, iteration, x, fx)


    def rms(self, x: 'vnl_vectorD') -> "double":
        """rms(vnl_least_squares_function self, vnl_vectorD x) -> double"""
        return _vnl_least_squares_functionPython.vnl_least_squares_function_rms(self, x)


    def get_number_of_unknowns(self) -> "unsigned int":
        """get_number_of_unknowns(vnl_least_squares_function self) -> unsigned int"""
        return _vnl_least_squares_functionPython.vnl_least_squares_function_get_number_of_unknowns(self)


    def get_number_of_residuals(self) -> "unsigned int":
        """get_number_of_residuals(vnl_least_squares_function self) -> unsigned int"""
        return _vnl_least_squares_functionPython.vnl_least_squares_function_get_number_of_residuals(self)


    def has_gradient(self) -> "bool":
        """has_gradient(vnl_least_squares_function self) -> bool"""
        return _vnl_least_squares_functionPython.vnl_least_squares_function_has_gradient(self)

vnl_least_squares_function.throw_failure = new_instancemethod(_vnl_least_squares_functionPython.vnl_least_squares_function_throw_failure, None, vnl_least_squares_function)
vnl_least_squares_function.clear_failure = new_instancemethod(_vnl_least_squares_functionPython.vnl_least_squares_function_clear_failure, None, vnl_least_squares_function)
vnl_least_squares_function.f = new_instancemethod(_vnl_least_squares_functionPython.vnl_least_squares_function_f, None, vnl_least_squares_function)
vnl_least_squares_function.gradf = new_instancemethod(_vnl_least_squares_functionPython.vnl_least_squares_function_gradf, None, vnl_least_squares_function)
vnl_least_squares_function.fdgradf = new_instancemethod(_vnl_least_squares_functionPython.vnl_least_squares_function_fdgradf, None, vnl_least_squares_function)
vnl_least_squares_function.ffdgradf = new_instancemethod(_vnl_least_squares_functionPython.vnl_least_squares_function_ffdgradf, None, vnl_least_squares_function)
vnl_least_squares_function.trace = new_instancemethod(_vnl_least_squares_functionPython.vnl_least_squares_function_trace, None, vnl_least_squares_function)
vnl_least_squares_function.rms = new_instancemethod(_vnl_least_squares_functionPython.vnl_least_squares_function_rms, None, vnl_least_squares_function)
vnl_least_squares_function.get_number_of_unknowns = new_instancemethod(_vnl_least_squares_functionPython.vnl_least_squares_function_get_number_of_unknowns, None, vnl_least_squares_function)
vnl_least_squares_function.get_number_of_residuals = new_instancemethod(_vnl_least_squares_functionPython.vnl_least_squares_function_get_number_of_residuals, None, vnl_least_squares_function)
vnl_least_squares_function.has_gradient = new_instancemethod(_vnl_least_squares_functionPython.vnl_least_squares_function_has_gradient, None, vnl_least_squares_function)
vnl_least_squares_function_swigregister = _vnl_least_squares_functionPython.vnl_least_squares_function_swigregister
vnl_least_squares_function_swigregister(vnl_least_squares_function)



