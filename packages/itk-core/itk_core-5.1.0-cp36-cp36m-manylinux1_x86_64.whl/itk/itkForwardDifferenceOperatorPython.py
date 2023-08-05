# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkForwardDifferenceOperatorPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkForwardDifferenceOperatorPython', [dirname(__file__)])
        except ImportError:
            import _itkForwardDifferenceOperatorPython
            return _itkForwardDifferenceOperatorPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkForwardDifferenceOperatorPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkForwardDifferenceOperatorPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkForwardDifferenceOperatorPython
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
import itkSizePython
import pyBasePython
import ITKCommonBasePython
import itkNeighborhoodPython
import itkVectorPython
import itkFixedArrayPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import vnl_vector_refPython
import itkOffsetPython
import itkRGBPixelPython
import itkCovariantVectorPython
class itkForwardDifferenceOperatorD2(itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD2):
    """


    Operator whose inner product with a neighborhood returns a "half"
    derivative at the center of the neighborhood.

    ForwardDifferenceOperator uses forward differences i.e. F(x+1) - F(x)
    to calculate a "half" derivative useful, among other things, in
    solving differential equations. It is a directional
    NeighborhoodOperator that should be applied to a Neighborhood using
    the inner product.

    ForwardDifferenceOperator does not have any user-declared "special
    member function", following the C++ Rule of Zero: the compiler will
    generate them if necessary.

    C++ includes: itkForwardDifferenceOperator.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkForwardDifferenceOperatorPython.delete_itkForwardDifferenceOperatorD2

    def __init__(self, *args):
        """
        __init__(itkForwardDifferenceOperatorD2 self) -> itkForwardDifferenceOperatorD2
        __init__(itkForwardDifferenceOperatorD2 self, itkForwardDifferenceOperatorD2 arg0) -> itkForwardDifferenceOperatorD2



        Operator whose inner product with a neighborhood returns a "half"
        derivative at the center of the neighborhood.

        ForwardDifferenceOperator uses forward differences i.e. F(x+1) - F(x)
        to calculate a "half" derivative useful, among other things, in
        solving differential equations. It is a directional
        NeighborhoodOperator that should be applied to a Neighborhood using
        the inner product.

        ForwardDifferenceOperator does not have any user-declared "special
        member function", following the C++ Rule of Zero: the compiler will
        generate them if necessary.

        C++ includes: itkForwardDifferenceOperator.h 
        """
        _itkForwardDifferenceOperatorPython.itkForwardDifferenceOperatorD2_swiginit(self, _itkForwardDifferenceOperatorPython.new_itkForwardDifferenceOperatorD2(*args))
itkForwardDifferenceOperatorD2_swigregister = _itkForwardDifferenceOperatorPython.itkForwardDifferenceOperatorD2_swigregister
itkForwardDifferenceOperatorD2_swigregister(itkForwardDifferenceOperatorD2)

class itkForwardDifferenceOperatorD3(itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD3):
    """


    Operator whose inner product with a neighborhood returns a "half"
    derivative at the center of the neighborhood.

    ForwardDifferenceOperator uses forward differences i.e. F(x+1) - F(x)
    to calculate a "half" derivative useful, among other things, in
    solving differential equations. It is a directional
    NeighborhoodOperator that should be applied to a Neighborhood using
    the inner product.

    ForwardDifferenceOperator does not have any user-declared "special
    member function", following the C++ Rule of Zero: the compiler will
    generate them if necessary.

    C++ includes: itkForwardDifferenceOperator.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkForwardDifferenceOperatorPython.delete_itkForwardDifferenceOperatorD3

    def __init__(self, *args):
        """
        __init__(itkForwardDifferenceOperatorD3 self) -> itkForwardDifferenceOperatorD3
        __init__(itkForwardDifferenceOperatorD3 self, itkForwardDifferenceOperatorD3 arg0) -> itkForwardDifferenceOperatorD3



        Operator whose inner product with a neighborhood returns a "half"
        derivative at the center of the neighborhood.

        ForwardDifferenceOperator uses forward differences i.e. F(x+1) - F(x)
        to calculate a "half" derivative useful, among other things, in
        solving differential equations. It is a directional
        NeighborhoodOperator that should be applied to a Neighborhood using
        the inner product.

        ForwardDifferenceOperator does not have any user-declared "special
        member function", following the C++ Rule of Zero: the compiler will
        generate them if necessary.

        C++ includes: itkForwardDifferenceOperator.h 
        """
        _itkForwardDifferenceOperatorPython.itkForwardDifferenceOperatorD3_swiginit(self, _itkForwardDifferenceOperatorPython.new_itkForwardDifferenceOperatorD3(*args))
itkForwardDifferenceOperatorD3_swigregister = _itkForwardDifferenceOperatorPython.itkForwardDifferenceOperatorD3_swigregister
itkForwardDifferenceOperatorD3_swigregister(itkForwardDifferenceOperatorD3)

class itkForwardDifferenceOperatorF2(itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF2):
    """


    Operator whose inner product with a neighborhood returns a "half"
    derivative at the center of the neighborhood.

    ForwardDifferenceOperator uses forward differences i.e. F(x+1) - F(x)
    to calculate a "half" derivative useful, among other things, in
    solving differential equations. It is a directional
    NeighborhoodOperator that should be applied to a Neighborhood using
    the inner product.

    ForwardDifferenceOperator does not have any user-declared "special
    member function", following the C++ Rule of Zero: the compiler will
    generate them if necessary.

    C++ includes: itkForwardDifferenceOperator.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkForwardDifferenceOperatorPython.delete_itkForwardDifferenceOperatorF2

    def __init__(self, *args):
        """
        __init__(itkForwardDifferenceOperatorF2 self) -> itkForwardDifferenceOperatorF2
        __init__(itkForwardDifferenceOperatorF2 self, itkForwardDifferenceOperatorF2 arg0) -> itkForwardDifferenceOperatorF2



        Operator whose inner product with a neighborhood returns a "half"
        derivative at the center of the neighborhood.

        ForwardDifferenceOperator uses forward differences i.e. F(x+1) - F(x)
        to calculate a "half" derivative useful, among other things, in
        solving differential equations. It is a directional
        NeighborhoodOperator that should be applied to a Neighborhood using
        the inner product.

        ForwardDifferenceOperator does not have any user-declared "special
        member function", following the C++ Rule of Zero: the compiler will
        generate them if necessary.

        C++ includes: itkForwardDifferenceOperator.h 
        """
        _itkForwardDifferenceOperatorPython.itkForwardDifferenceOperatorF2_swiginit(self, _itkForwardDifferenceOperatorPython.new_itkForwardDifferenceOperatorF2(*args))
itkForwardDifferenceOperatorF2_swigregister = _itkForwardDifferenceOperatorPython.itkForwardDifferenceOperatorF2_swigregister
itkForwardDifferenceOperatorF2_swigregister(itkForwardDifferenceOperatorF2)

class itkForwardDifferenceOperatorF3(itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF3):
    """


    Operator whose inner product with a neighborhood returns a "half"
    derivative at the center of the neighborhood.

    ForwardDifferenceOperator uses forward differences i.e. F(x+1) - F(x)
    to calculate a "half" derivative useful, among other things, in
    solving differential equations. It is a directional
    NeighborhoodOperator that should be applied to a Neighborhood using
    the inner product.

    ForwardDifferenceOperator does not have any user-declared "special
    member function", following the C++ Rule of Zero: the compiler will
    generate them if necessary.

    C++ includes: itkForwardDifferenceOperator.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkForwardDifferenceOperatorPython.delete_itkForwardDifferenceOperatorF3

    def __init__(self, *args):
        """
        __init__(itkForwardDifferenceOperatorF3 self) -> itkForwardDifferenceOperatorF3
        __init__(itkForwardDifferenceOperatorF3 self, itkForwardDifferenceOperatorF3 arg0) -> itkForwardDifferenceOperatorF3



        Operator whose inner product with a neighborhood returns a "half"
        derivative at the center of the neighborhood.

        ForwardDifferenceOperator uses forward differences i.e. F(x+1) - F(x)
        to calculate a "half" derivative useful, among other things, in
        solving differential equations. It is a directional
        NeighborhoodOperator that should be applied to a Neighborhood using
        the inner product.

        ForwardDifferenceOperator does not have any user-declared "special
        member function", following the C++ Rule of Zero: the compiler will
        generate them if necessary.

        C++ includes: itkForwardDifferenceOperator.h 
        """
        _itkForwardDifferenceOperatorPython.itkForwardDifferenceOperatorF3_swiginit(self, _itkForwardDifferenceOperatorPython.new_itkForwardDifferenceOperatorF3(*args))
itkForwardDifferenceOperatorF3_swigregister = _itkForwardDifferenceOperatorPython.itkForwardDifferenceOperatorF3_swigregister
itkForwardDifferenceOperatorF3_swigregister(itkForwardDifferenceOperatorF3)



