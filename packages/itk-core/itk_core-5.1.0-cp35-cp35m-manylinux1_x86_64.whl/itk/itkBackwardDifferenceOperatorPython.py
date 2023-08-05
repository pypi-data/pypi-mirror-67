# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkBackwardDifferenceOperatorPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkBackwardDifferenceOperatorPython', [dirname(__file__)])
        except ImportError:
            import _itkBackwardDifferenceOperatorPython
            return _itkBackwardDifferenceOperatorPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkBackwardDifferenceOperatorPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkBackwardDifferenceOperatorPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkBackwardDifferenceOperatorPython
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


import itkNeighborhoodOperatorPython
import itkNeighborhoodPython
import itkRGBPixelPython
import itkFixedArrayPython
import pyBasePython
import itkSizePython
import ITKCommonBasePython
import itkCovariantVectorPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import vnl_vector_refPython
import itkVectorPython
import itkOffsetPython
class itkBackwardDifferenceOperatorD2(itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD2):
    """


    Operator whose inner product with a neighborhood returns a "half"
    derivative at the center of the neighborhood.

    BackwardDifferenceOperator uses backward differences i.e. $ F(x) -
    F(x-1) $ to calculate a "half" derivative useful, among other
    things, in solving differential equations. It is a directional
    NeighborhoodOperator that should be applied to a Neighborhood using
    the inner product.

    BackwardDifferenceOperator does not have any user-declared "special
    member function", following the C++ Rule of Zero: the compiler will
    generate them if necessary.

    C++ includes: itkBackwardDifferenceOperator.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkBackwardDifferenceOperatorPython.delete_itkBackwardDifferenceOperatorD2

    def __init__(self, *args):
        """
        __init__(itkBackwardDifferenceOperatorD2 self) -> itkBackwardDifferenceOperatorD2
        __init__(itkBackwardDifferenceOperatorD2 self, itkBackwardDifferenceOperatorD2 arg0) -> itkBackwardDifferenceOperatorD2



        Operator whose inner product with a neighborhood returns a "half"
        derivative at the center of the neighborhood.

        BackwardDifferenceOperator uses backward differences i.e. $ F(x) -
        F(x-1) $ to calculate a "half" derivative useful, among other
        things, in solving differential equations. It is a directional
        NeighborhoodOperator that should be applied to a Neighborhood using
        the inner product.

        BackwardDifferenceOperator does not have any user-declared "special
        member function", following the C++ Rule of Zero: the compiler will
        generate them if necessary.

        C++ includes: itkBackwardDifferenceOperator.h 
        """
        _itkBackwardDifferenceOperatorPython.itkBackwardDifferenceOperatorD2_swiginit(self, _itkBackwardDifferenceOperatorPython.new_itkBackwardDifferenceOperatorD2(*args))
itkBackwardDifferenceOperatorD2_swigregister = _itkBackwardDifferenceOperatorPython.itkBackwardDifferenceOperatorD2_swigregister
itkBackwardDifferenceOperatorD2_swigregister(itkBackwardDifferenceOperatorD2)

class itkBackwardDifferenceOperatorD3(itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD3):
    """


    Operator whose inner product with a neighborhood returns a "half"
    derivative at the center of the neighborhood.

    BackwardDifferenceOperator uses backward differences i.e. $ F(x) -
    F(x-1) $ to calculate a "half" derivative useful, among other
    things, in solving differential equations. It is a directional
    NeighborhoodOperator that should be applied to a Neighborhood using
    the inner product.

    BackwardDifferenceOperator does not have any user-declared "special
    member function", following the C++ Rule of Zero: the compiler will
    generate them if necessary.

    C++ includes: itkBackwardDifferenceOperator.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkBackwardDifferenceOperatorPython.delete_itkBackwardDifferenceOperatorD3

    def __init__(self, *args):
        """
        __init__(itkBackwardDifferenceOperatorD3 self) -> itkBackwardDifferenceOperatorD3
        __init__(itkBackwardDifferenceOperatorD3 self, itkBackwardDifferenceOperatorD3 arg0) -> itkBackwardDifferenceOperatorD3



        Operator whose inner product with a neighborhood returns a "half"
        derivative at the center of the neighborhood.

        BackwardDifferenceOperator uses backward differences i.e. $ F(x) -
        F(x-1) $ to calculate a "half" derivative useful, among other
        things, in solving differential equations. It is a directional
        NeighborhoodOperator that should be applied to a Neighborhood using
        the inner product.

        BackwardDifferenceOperator does not have any user-declared "special
        member function", following the C++ Rule of Zero: the compiler will
        generate them if necessary.

        C++ includes: itkBackwardDifferenceOperator.h 
        """
        _itkBackwardDifferenceOperatorPython.itkBackwardDifferenceOperatorD3_swiginit(self, _itkBackwardDifferenceOperatorPython.new_itkBackwardDifferenceOperatorD3(*args))
itkBackwardDifferenceOperatorD3_swigregister = _itkBackwardDifferenceOperatorPython.itkBackwardDifferenceOperatorD3_swigregister
itkBackwardDifferenceOperatorD3_swigregister(itkBackwardDifferenceOperatorD3)

class itkBackwardDifferenceOperatorF2(itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF2):
    """


    Operator whose inner product with a neighborhood returns a "half"
    derivative at the center of the neighborhood.

    BackwardDifferenceOperator uses backward differences i.e. $ F(x) -
    F(x-1) $ to calculate a "half" derivative useful, among other
    things, in solving differential equations. It is a directional
    NeighborhoodOperator that should be applied to a Neighborhood using
    the inner product.

    BackwardDifferenceOperator does not have any user-declared "special
    member function", following the C++ Rule of Zero: the compiler will
    generate them if necessary.

    C++ includes: itkBackwardDifferenceOperator.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkBackwardDifferenceOperatorPython.delete_itkBackwardDifferenceOperatorF2

    def __init__(self, *args):
        """
        __init__(itkBackwardDifferenceOperatorF2 self) -> itkBackwardDifferenceOperatorF2
        __init__(itkBackwardDifferenceOperatorF2 self, itkBackwardDifferenceOperatorF2 arg0) -> itkBackwardDifferenceOperatorF2



        Operator whose inner product with a neighborhood returns a "half"
        derivative at the center of the neighborhood.

        BackwardDifferenceOperator uses backward differences i.e. $ F(x) -
        F(x-1) $ to calculate a "half" derivative useful, among other
        things, in solving differential equations. It is a directional
        NeighborhoodOperator that should be applied to a Neighborhood using
        the inner product.

        BackwardDifferenceOperator does not have any user-declared "special
        member function", following the C++ Rule of Zero: the compiler will
        generate them if necessary.

        C++ includes: itkBackwardDifferenceOperator.h 
        """
        _itkBackwardDifferenceOperatorPython.itkBackwardDifferenceOperatorF2_swiginit(self, _itkBackwardDifferenceOperatorPython.new_itkBackwardDifferenceOperatorF2(*args))
itkBackwardDifferenceOperatorF2_swigregister = _itkBackwardDifferenceOperatorPython.itkBackwardDifferenceOperatorF2_swigregister
itkBackwardDifferenceOperatorF2_swigregister(itkBackwardDifferenceOperatorF2)

class itkBackwardDifferenceOperatorF3(itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF3):
    """


    Operator whose inner product with a neighborhood returns a "half"
    derivative at the center of the neighborhood.

    BackwardDifferenceOperator uses backward differences i.e. $ F(x) -
    F(x-1) $ to calculate a "half" derivative useful, among other
    things, in solving differential equations. It is a directional
    NeighborhoodOperator that should be applied to a Neighborhood using
    the inner product.

    BackwardDifferenceOperator does not have any user-declared "special
    member function", following the C++ Rule of Zero: the compiler will
    generate them if necessary.

    C++ includes: itkBackwardDifferenceOperator.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkBackwardDifferenceOperatorPython.delete_itkBackwardDifferenceOperatorF3

    def __init__(self, *args):
        """
        __init__(itkBackwardDifferenceOperatorF3 self) -> itkBackwardDifferenceOperatorF3
        __init__(itkBackwardDifferenceOperatorF3 self, itkBackwardDifferenceOperatorF3 arg0) -> itkBackwardDifferenceOperatorF3



        Operator whose inner product with a neighborhood returns a "half"
        derivative at the center of the neighborhood.

        BackwardDifferenceOperator uses backward differences i.e. $ F(x) -
        F(x-1) $ to calculate a "half" derivative useful, among other
        things, in solving differential equations. It is a directional
        NeighborhoodOperator that should be applied to a Neighborhood using
        the inner product.

        BackwardDifferenceOperator does not have any user-declared "special
        member function", following the C++ Rule of Zero: the compiler will
        generate them if necessary.

        C++ includes: itkBackwardDifferenceOperator.h 
        """
        _itkBackwardDifferenceOperatorPython.itkBackwardDifferenceOperatorF3_swiginit(self, _itkBackwardDifferenceOperatorPython.new_itkBackwardDifferenceOperatorF3(*args))
itkBackwardDifferenceOperatorF3_swigregister = _itkBackwardDifferenceOperatorPython.itkBackwardDifferenceOperatorF3_swigregister
itkBackwardDifferenceOperatorF3_swigregister(itkBackwardDifferenceOperatorF3)



