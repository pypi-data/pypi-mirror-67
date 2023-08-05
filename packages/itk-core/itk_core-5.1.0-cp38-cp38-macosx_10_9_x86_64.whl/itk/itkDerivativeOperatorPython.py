# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkDerivativeOperatorPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkDerivativeOperatorPython', [dirname(__file__)])
        except ImportError:
            import _itkDerivativeOperatorPython
            return _itkDerivativeOperatorPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkDerivativeOperatorPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkDerivativeOperatorPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkDerivativeOperatorPython
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
import itkNeighborhoodOperatorPython
import itkNeighborhoodPython
import itkRGBPixelPython
import itkFixedArrayPython
import itkCovariantVectorPython
import itkVectorPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import vnl_vector_refPython
import itkOffsetPython
import itkSizePython
class itkDerivativeOperatorD2(itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD2):
    """


    A NeighborhoodOperator for taking an n-th order derivative at a pixel.

    DerivativeOperator's coefficients are a tightest-fitting convolution
    kernel for calculating the n-th order directional derivative at a
    pixel. DerivativeOperator is a directional NeighborhoodOperator that
    should be applied to a Neighborhood or NeighborhoodPointer using the
    inner product method.

    An example operator to compute X derivatives of a 2D image can be
    created with: and creates a kernel that looks like:

    DerivativeOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:   Neighborhood

    See:   ForwardDifferenceOperator

    See:   BackwardDifferenceOperator  \\sphinx
    \\sphinxexample{Core/Common/CreateDerivativeKernel,Create Derivative
    Kernel} \\endsphinx

    C++ includes: itkDerivativeOperator.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def SetOrder(self, order: 'unsigned int const &') -> "void":
        """
        SetOrder(itkDerivativeOperatorD2 self, unsigned int const & order)

        Sets the order of the
        derivative. 
        """
        return _itkDerivativeOperatorPython.itkDerivativeOperatorD2_SetOrder(self, order)


    def GetOrder(self) -> "unsigned int":
        """
        GetOrder(itkDerivativeOperatorD2 self) -> unsigned int

        Returns the order of the
        derivative. 
        """
        return _itkDerivativeOperatorPython.itkDerivativeOperatorD2_GetOrder(self)

    __swig_destroy__ = _itkDerivativeOperatorPython.delete_itkDerivativeOperatorD2

    def __init__(self, *args):
        """
        __init__(itkDerivativeOperatorD2 self) -> itkDerivativeOperatorD2
        __init__(itkDerivativeOperatorD2 self, itkDerivativeOperatorD2 arg0) -> itkDerivativeOperatorD2



        A NeighborhoodOperator for taking an n-th order derivative at a pixel.

        DerivativeOperator's coefficients are a tightest-fitting convolution
        kernel for calculating the n-th order directional derivative at a
        pixel. DerivativeOperator is a directional NeighborhoodOperator that
        should be applied to a Neighborhood or NeighborhoodPointer using the
        inner product method.

        An example operator to compute X derivatives of a 2D image can be
        created with: and creates a kernel that looks like:

        DerivativeOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:   Neighborhood

        See:   ForwardDifferenceOperator

        See:   BackwardDifferenceOperator  \\sphinx
        \\sphinxexample{Core/Common/CreateDerivativeKernel,Create Derivative
        Kernel} \\endsphinx

        C++ includes: itkDerivativeOperator.h 
        """
        _itkDerivativeOperatorPython.itkDerivativeOperatorD2_swiginit(self, _itkDerivativeOperatorPython.new_itkDerivativeOperatorD2(*args))
itkDerivativeOperatorD2.SetOrder = new_instancemethod(_itkDerivativeOperatorPython.itkDerivativeOperatorD2_SetOrder, None, itkDerivativeOperatorD2)
itkDerivativeOperatorD2.GetOrder = new_instancemethod(_itkDerivativeOperatorPython.itkDerivativeOperatorD2_GetOrder, None, itkDerivativeOperatorD2)
itkDerivativeOperatorD2_swigregister = _itkDerivativeOperatorPython.itkDerivativeOperatorD2_swigregister
itkDerivativeOperatorD2_swigregister(itkDerivativeOperatorD2)

class itkDerivativeOperatorD3(itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD3):
    """


    A NeighborhoodOperator for taking an n-th order derivative at a pixel.

    DerivativeOperator's coefficients are a tightest-fitting convolution
    kernel for calculating the n-th order directional derivative at a
    pixel. DerivativeOperator is a directional NeighborhoodOperator that
    should be applied to a Neighborhood or NeighborhoodPointer using the
    inner product method.

    An example operator to compute X derivatives of a 2D image can be
    created with: and creates a kernel that looks like:

    DerivativeOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:   Neighborhood

    See:   ForwardDifferenceOperator

    See:   BackwardDifferenceOperator  \\sphinx
    \\sphinxexample{Core/Common/CreateDerivativeKernel,Create Derivative
    Kernel} \\endsphinx

    C++ includes: itkDerivativeOperator.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def SetOrder(self, order: 'unsigned int const &') -> "void":
        """
        SetOrder(itkDerivativeOperatorD3 self, unsigned int const & order)

        Sets the order of the
        derivative. 
        """
        return _itkDerivativeOperatorPython.itkDerivativeOperatorD3_SetOrder(self, order)


    def GetOrder(self) -> "unsigned int":
        """
        GetOrder(itkDerivativeOperatorD3 self) -> unsigned int

        Returns the order of the
        derivative. 
        """
        return _itkDerivativeOperatorPython.itkDerivativeOperatorD3_GetOrder(self)

    __swig_destroy__ = _itkDerivativeOperatorPython.delete_itkDerivativeOperatorD3

    def __init__(self, *args):
        """
        __init__(itkDerivativeOperatorD3 self) -> itkDerivativeOperatorD3
        __init__(itkDerivativeOperatorD3 self, itkDerivativeOperatorD3 arg0) -> itkDerivativeOperatorD3



        A NeighborhoodOperator for taking an n-th order derivative at a pixel.

        DerivativeOperator's coefficients are a tightest-fitting convolution
        kernel for calculating the n-th order directional derivative at a
        pixel. DerivativeOperator is a directional NeighborhoodOperator that
        should be applied to a Neighborhood or NeighborhoodPointer using the
        inner product method.

        An example operator to compute X derivatives of a 2D image can be
        created with: and creates a kernel that looks like:

        DerivativeOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:   Neighborhood

        See:   ForwardDifferenceOperator

        See:   BackwardDifferenceOperator  \\sphinx
        \\sphinxexample{Core/Common/CreateDerivativeKernel,Create Derivative
        Kernel} \\endsphinx

        C++ includes: itkDerivativeOperator.h 
        """
        _itkDerivativeOperatorPython.itkDerivativeOperatorD3_swiginit(self, _itkDerivativeOperatorPython.new_itkDerivativeOperatorD3(*args))
itkDerivativeOperatorD3.SetOrder = new_instancemethod(_itkDerivativeOperatorPython.itkDerivativeOperatorD3_SetOrder, None, itkDerivativeOperatorD3)
itkDerivativeOperatorD3.GetOrder = new_instancemethod(_itkDerivativeOperatorPython.itkDerivativeOperatorD3_GetOrder, None, itkDerivativeOperatorD3)
itkDerivativeOperatorD3_swigregister = _itkDerivativeOperatorPython.itkDerivativeOperatorD3_swigregister
itkDerivativeOperatorD3_swigregister(itkDerivativeOperatorD3)

class itkDerivativeOperatorF2(itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF2):
    """


    A NeighborhoodOperator for taking an n-th order derivative at a pixel.

    DerivativeOperator's coefficients are a tightest-fitting convolution
    kernel for calculating the n-th order directional derivative at a
    pixel. DerivativeOperator is a directional NeighborhoodOperator that
    should be applied to a Neighborhood or NeighborhoodPointer using the
    inner product method.

    An example operator to compute X derivatives of a 2D image can be
    created with: and creates a kernel that looks like:

    DerivativeOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:   Neighborhood

    See:   ForwardDifferenceOperator

    See:   BackwardDifferenceOperator  \\sphinx
    \\sphinxexample{Core/Common/CreateDerivativeKernel,Create Derivative
    Kernel} \\endsphinx

    C++ includes: itkDerivativeOperator.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def SetOrder(self, order: 'unsigned int const &') -> "void":
        """
        SetOrder(itkDerivativeOperatorF2 self, unsigned int const & order)

        Sets the order of the
        derivative. 
        """
        return _itkDerivativeOperatorPython.itkDerivativeOperatorF2_SetOrder(self, order)


    def GetOrder(self) -> "unsigned int":
        """
        GetOrder(itkDerivativeOperatorF2 self) -> unsigned int

        Returns the order of the
        derivative. 
        """
        return _itkDerivativeOperatorPython.itkDerivativeOperatorF2_GetOrder(self)

    __swig_destroy__ = _itkDerivativeOperatorPython.delete_itkDerivativeOperatorF2

    def __init__(self, *args):
        """
        __init__(itkDerivativeOperatorF2 self) -> itkDerivativeOperatorF2
        __init__(itkDerivativeOperatorF2 self, itkDerivativeOperatorF2 arg0) -> itkDerivativeOperatorF2



        A NeighborhoodOperator for taking an n-th order derivative at a pixel.

        DerivativeOperator's coefficients are a tightest-fitting convolution
        kernel for calculating the n-th order directional derivative at a
        pixel. DerivativeOperator is a directional NeighborhoodOperator that
        should be applied to a Neighborhood or NeighborhoodPointer using the
        inner product method.

        An example operator to compute X derivatives of a 2D image can be
        created with: and creates a kernel that looks like:

        DerivativeOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:   Neighborhood

        See:   ForwardDifferenceOperator

        See:   BackwardDifferenceOperator  \\sphinx
        \\sphinxexample{Core/Common/CreateDerivativeKernel,Create Derivative
        Kernel} \\endsphinx

        C++ includes: itkDerivativeOperator.h 
        """
        _itkDerivativeOperatorPython.itkDerivativeOperatorF2_swiginit(self, _itkDerivativeOperatorPython.new_itkDerivativeOperatorF2(*args))
itkDerivativeOperatorF2.SetOrder = new_instancemethod(_itkDerivativeOperatorPython.itkDerivativeOperatorF2_SetOrder, None, itkDerivativeOperatorF2)
itkDerivativeOperatorF2.GetOrder = new_instancemethod(_itkDerivativeOperatorPython.itkDerivativeOperatorF2_GetOrder, None, itkDerivativeOperatorF2)
itkDerivativeOperatorF2_swigregister = _itkDerivativeOperatorPython.itkDerivativeOperatorF2_swigregister
itkDerivativeOperatorF2_swigregister(itkDerivativeOperatorF2)

class itkDerivativeOperatorF3(itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF3):
    """


    A NeighborhoodOperator for taking an n-th order derivative at a pixel.

    DerivativeOperator's coefficients are a tightest-fitting convolution
    kernel for calculating the n-th order directional derivative at a
    pixel. DerivativeOperator is a directional NeighborhoodOperator that
    should be applied to a Neighborhood or NeighborhoodPointer using the
    inner product method.

    An example operator to compute X derivatives of a 2D image can be
    created with: and creates a kernel that looks like:

    DerivativeOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:   Neighborhood

    See:   ForwardDifferenceOperator

    See:   BackwardDifferenceOperator  \\sphinx
    \\sphinxexample{Core/Common/CreateDerivativeKernel,Create Derivative
    Kernel} \\endsphinx

    C++ includes: itkDerivativeOperator.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def SetOrder(self, order: 'unsigned int const &') -> "void":
        """
        SetOrder(itkDerivativeOperatorF3 self, unsigned int const & order)

        Sets the order of the
        derivative. 
        """
        return _itkDerivativeOperatorPython.itkDerivativeOperatorF3_SetOrder(self, order)


    def GetOrder(self) -> "unsigned int":
        """
        GetOrder(itkDerivativeOperatorF3 self) -> unsigned int

        Returns the order of the
        derivative. 
        """
        return _itkDerivativeOperatorPython.itkDerivativeOperatorF3_GetOrder(self)

    __swig_destroy__ = _itkDerivativeOperatorPython.delete_itkDerivativeOperatorF3

    def __init__(self, *args):
        """
        __init__(itkDerivativeOperatorF3 self) -> itkDerivativeOperatorF3
        __init__(itkDerivativeOperatorF3 self, itkDerivativeOperatorF3 arg0) -> itkDerivativeOperatorF3



        A NeighborhoodOperator for taking an n-th order derivative at a pixel.

        DerivativeOperator's coefficients are a tightest-fitting convolution
        kernel for calculating the n-th order directional derivative at a
        pixel. DerivativeOperator is a directional NeighborhoodOperator that
        should be applied to a Neighborhood or NeighborhoodPointer using the
        inner product method.

        An example operator to compute X derivatives of a 2D image can be
        created with: and creates a kernel that looks like:

        DerivativeOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:   Neighborhood

        See:   ForwardDifferenceOperator

        See:   BackwardDifferenceOperator  \\sphinx
        \\sphinxexample{Core/Common/CreateDerivativeKernel,Create Derivative
        Kernel} \\endsphinx

        C++ includes: itkDerivativeOperator.h 
        """
        _itkDerivativeOperatorPython.itkDerivativeOperatorF3_swiginit(self, _itkDerivativeOperatorPython.new_itkDerivativeOperatorF3(*args))
itkDerivativeOperatorF3.SetOrder = new_instancemethod(_itkDerivativeOperatorPython.itkDerivativeOperatorF3_SetOrder, None, itkDerivativeOperatorF3)
itkDerivativeOperatorF3.GetOrder = new_instancemethod(_itkDerivativeOperatorPython.itkDerivativeOperatorF3_GetOrder, None, itkDerivativeOperatorF3)
itkDerivativeOperatorF3_swigregister = _itkDerivativeOperatorPython.itkDerivativeOperatorF3_swigregister
itkDerivativeOperatorF3_swigregister(itkDerivativeOperatorF3)



