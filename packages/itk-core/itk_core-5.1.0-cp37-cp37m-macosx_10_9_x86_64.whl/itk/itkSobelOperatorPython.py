# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkSobelOperatorPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkSobelOperatorPython', [dirname(__file__)])
        except ImportError:
            import _itkSobelOperatorPython
            return _itkSobelOperatorPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkSobelOperatorPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkSobelOperatorPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkSobelOperatorPython
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
import itkSizePython
import itkNeighborhoodPython
import itkRGBPixelPython
import itkFixedArrayPython
import itkOffsetPython
import itkCovariantVectorPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import vnl_vector_refPython
import itkVectorPython
class itkSobelOperatorD2(itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD2):
    """


    A NeighborhoodOperator for performing a directional Sobel edge-
    detection operation at a pixel location.

    SobelOperator is a directional NeighborhoodOperator that should be
    applied a NeighborhoodIterator using the NeighborhoodInnerProduct
    method. To create the operator:

    1) Set the direction by calling 2) call 3) You may optionally scale
    the coefficients of this operator using the method. This is useful if
    you want to take the spacing of the image into account when computing
    the edge strength. Apply the scaling only after calling to.

    The Sobel Operator in vertical direction for 2 dimensions is*
    -1  -2  -1 *             0    0   0 *             1    2 1 * * The
    Sobel Operator in horizontal direction is for 2 dimensions is*
    -1   0   1 *             -2   0   2 *             -1   0 1 *

    The current implementation of the Sobel operator is for 2 and 3
    dimensions only. The ND version is planned for future releases.

    The extension to 3D is from the publication "Irwin Sobel. An
    Isotropic 3x3x3 Volume Gradient Operator.   Technical report, Hewlett-
    Packard Laboratories, April 1995."

    The Sobel operator in 3D has the kernel

    * -1 -3 -1   0 0 0  1 3 1 * -3 -6 -3   0 0 0  3 6 3 * -1 -3 -1   0 0 0
    1 3 1 * *    x-1       x     x+1 *

    The x kernel is just rotated as required to obtain the kernel in the y
    and z directions.

    SobelOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:   Neighborhood

    See:   ForwardDifferenceOperator

    See:   BackwardDifferenceOperator  \\sphinx
    \\sphinxexample{Core/Common/CreateSobelKernel,Create Sobel Kernel}
    \\endsphinx

    C++ includes: itkSobelOperator.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkSobelOperatorPython.delete_itkSobelOperatorD2

    def __init__(self, *args):
        """
        __init__(itkSobelOperatorD2 self) -> itkSobelOperatorD2
        __init__(itkSobelOperatorD2 self, itkSobelOperatorD2 arg0) -> itkSobelOperatorD2



        A NeighborhoodOperator for performing a directional Sobel edge-
        detection operation at a pixel location.

        SobelOperator is a directional NeighborhoodOperator that should be
        applied a NeighborhoodIterator using the NeighborhoodInnerProduct
        method. To create the operator:

        1) Set the direction by calling 2) call 3) You may optionally scale
        the coefficients of this operator using the method. This is useful if
        you want to take the spacing of the image into account when computing
        the edge strength. Apply the scaling only after calling to.

        The Sobel Operator in vertical direction for 2 dimensions is*
        -1  -2  -1 *             0    0   0 *             1    2 1 * * The
        Sobel Operator in horizontal direction is for 2 dimensions is*
        -1   0   1 *             -2   0   2 *             -1   0 1 *

        The current implementation of the Sobel operator is for 2 and 3
        dimensions only. The ND version is planned for future releases.

        The extension to 3D is from the publication "Irwin Sobel. An
        Isotropic 3x3x3 Volume Gradient Operator.   Technical report, Hewlett-
        Packard Laboratories, April 1995."

        The Sobel operator in 3D has the kernel

        * -1 -3 -1   0 0 0  1 3 1 * -3 -6 -3   0 0 0  3 6 3 * -1 -3 -1   0 0 0
        1 3 1 * *    x-1       x     x+1 *

        The x kernel is just rotated as required to obtain the kernel in the y
        and z directions.

        SobelOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:   Neighborhood

        See:   ForwardDifferenceOperator

        See:   BackwardDifferenceOperator  \\sphinx
        \\sphinxexample{Core/Common/CreateSobelKernel,Create Sobel Kernel}
        \\endsphinx

        C++ includes: itkSobelOperator.h 
        """
        _itkSobelOperatorPython.itkSobelOperatorD2_swiginit(self, _itkSobelOperatorPython.new_itkSobelOperatorD2(*args))
itkSobelOperatorD2_swigregister = _itkSobelOperatorPython.itkSobelOperatorD2_swigregister
itkSobelOperatorD2_swigregister(itkSobelOperatorD2)

class itkSobelOperatorD3(itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD3):
    """


    A NeighborhoodOperator for performing a directional Sobel edge-
    detection operation at a pixel location.

    SobelOperator is a directional NeighborhoodOperator that should be
    applied a NeighborhoodIterator using the NeighborhoodInnerProduct
    method. To create the operator:

    1) Set the direction by calling 2) call 3) You may optionally scale
    the coefficients of this operator using the method. This is useful if
    you want to take the spacing of the image into account when computing
    the edge strength. Apply the scaling only after calling to.

    The Sobel Operator in vertical direction for 2 dimensions is*
    -1  -2  -1 *             0    0   0 *             1    2 1 * * The
    Sobel Operator in horizontal direction is for 2 dimensions is*
    -1   0   1 *             -2   0   2 *             -1   0 1 *

    The current implementation of the Sobel operator is for 2 and 3
    dimensions only. The ND version is planned for future releases.

    The extension to 3D is from the publication "Irwin Sobel. An
    Isotropic 3x3x3 Volume Gradient Operator.   Technical report, Hewlett-
    Packard Laboratories, April 1995."

    The Sobel operator in 3D has the kernel

    * -1 -3 -1   0 0 0  1 3 1 * -3 -6 -3   0 0 0  3 6 3 * -1 -3 -1   0 0 0
    1 3 1 * *    x-1       x     x+1 *

    The x kernel is just rotated as required to obtain the kernel in the y
    and z directions.

    SobelOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:   Neighborhood

    See:   ForwardDifferenceOperator

    See:   BackwardDifferenceOperator  \\sphinx
    \\sphinxexample{Core/Common/CreateSobelKernel,Create Sobel Kernel}
    \\endsphinx

    C++ includes: itkSobelOperator.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkSobelOperatorPython.delete_itkSobelOperatorD3

    def __init__(self, *args):
        """
        __init__(itkSobelOperatorD3 self) -> itkSobelOperatorD3
        __init__(itkSobelOperatorD3 self, itkSobelOperatorD3 arg0) -> itkSobelOperatorD3



        A NeighborhoodOperator for performing a directional Sobel edge-
        detection operation at a pixel location.

        SobelOperator is a directional NeighborhoodOperator that should be
        applied a NeighborhoodIterator using the NeighborhoodInnerProduct
        method. To create the operator:

        1) Set the direction by calling 2) call 3) You may optionally scale
        the coefficients of this operator using the method. This is useful if
        you want to take the spacing of the image into account when computing
        the edge strength. Apply the scaling only after calling to.

        The Sobel Operator in vertical direction for 2 dimensions is*
        -1  -2  -1 *             0    0   0 *             1    2 1 * * The
        Sobel Operator in horizontal direction is for 2 dimensions is*
        -1   0   1 *             -2   0   2 *             -1   0 1 *

        The current implementation of the Sobel operator is for 2 and 3
        dimensions only. The ND version is planned for future releases.

        The extension to 3D is from the publication "Irwin Sobel. An
        Isotropic 3x3x3 Volume Gradient Operator.   Technical report, Hewlett-
        Packard Laboratories, April 1995."

        The Sobel operator in 3D has the kernel

        * -1 -3 -1   0 0 0  1 3 1 * -3 -6 -3   0 0 0  3 6 3 * -1 -3 -1   0 0 0
        1 3 1 * *    x-1       x     x+1 *

        The x kernel is just rotated as required to obtain the kernel in the y
        and z directions.

        SobelOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:   Neighborhood

        See:   ForwardDifferenceOperator

        See:   BackwardDifferenceOperator  \\sphinx
        \\sphinxexample{Core/Common/CreateSobelKernel,Create Sobel Kernel}
        \\endsphinx

        C++ includes: itkSobelOperator.h 
        """
        _itkSobelOperatorPython.itkSobelOperatorD3_swiginit(self, _itkSobelOperatorPython.new_itkSobelOperatorD3(*args))
itkSobelOperatorD3_swigregister = _itkSobelOperatorPython.itkSobelOperatorD3_swigregister
itkSobelOperatorD3_swigregister(itkSobelOperatorD3)

class itkSobelOperatorF2(itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF2):
    """


    A NeighborhoodOperator for performing a directional Sobel edge-
    detection operation at a pixel location.

    SobelOperator is a directional NeighborhoodOperator that should be
    applied a NeighborhoodIterator using the NeighborhoodInnerProduct
    method. To create the operator:

    1) Set the direction by calling 2) call 3) You may optionally scale
    the coefficients of this operator using the method. This is useful if
    you want to take the spacing of the image into account when computing
    the edge strength. Apply the scaling only after calling to.

    The Sobel Operator in vertical direction for 2 dimensions is*
    -1  -2  -1 *             0    0   0 *             1    2 1 * * The
    Sobel Operator in horizontal direction is for 2 dimensions is*
    -1   0   1 *             -2   0   2 *             -1   0 1 *

    The current implementation of the Sobel operator is for 2 and 3
    dimensions only. The ND version is planned for future releases.

    The extension to 3D is from the publication "Irwin Sobel. An
    Isotropic 3x3x3 Volume Gradient Operator.   Technical report, Hewlett-
    Packard Laboratories, April 1995."

    The Sobel operator in 3D has the kernel

    * -1 -3 -1   0 0 0  1 3 1 * -3 -6 -3   0 0 0  3 6 3 * -1 -3 -1   0 0 0
    1 3 1 * *    x-1       x     x+1 *

    The x kernel is just rotated as required to obtain the kernel in the y
    and z directions.

    SobelOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:   Neighborhood

    See:   ForwardDifferenceOperator

    See:   BackwardDifferenceOperator  \\sphinx
    \\sphinxexample{Core/Common/CreateSobelKernel,Create Sobel Kernel}
    \\endsphinx

    C++ includes: itkSobelOperator.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkSobelOperatorPython.delete_itkSobelOperatorF2

    def __init__(self, *args):
        """
        __init__(itkSobelOperatorF2 self) -> itkSobelOperatorF2
        __init__(itkSobelOperatorF2 self, itkSobelOperatorF2 arg0) -> itkSobelOperatorF2



        A NeighborhoodOperator for performing a directional Sobel edge-
        detection operation at a pixel location.

        SobelOperator is a directional NeighborhoodOperator that should be
        applied a NeighborhoodIterator using the NeighborhoodInnerProduct
        method. To create the operator:

        1) Set the direction by calling 2) call 3) You may optionally scale
        the coefficients of this operator using the method. This is useful if
        you want to take the spacing of the image into account when computing
        the edge strength. Apply the scaling only after calling to.

        The Sobel Operator in vertical direction for 2 dimensions is*
        -1  -2  -1 *             0    0   0 *             1    2 1 * * The
        Sobel Operator in horizontal direction is for 2 dimensions is*
        -1   0   1 *             -2   0   2 *             -1   0 1 *

        The current implementation of the Sobel operator is for 2 and 3
        dimensions only. The ND version is planned for future releases.

        The extension to 3D is from the publication "Irwin Sobel. An
        Isotropic 3x3x3 Volume Gradient Operator.   Technical report, Hewlett-
        Packard Laboratories, April 1995."

        The Sobel operator in 3D has the kernel

        * -1 -3 -1   0 0 0  1 3 1 * -3 -6 -3   0 0 0  3 6 3 * -1 -3 -1   0 0 0
        1 3 1 * *    x-1       x     x+1 *

        The x kernel is just rotated as required to obtain the kernel in the y
        and z directions.

        SobelOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:   Neighborhood

        See:   ForwardDifferenceOperator

        See:   BackwardDifferenceOperator  \\sphinx
        \\sphinxexample{Core/Common/CreateSobelKernel,Create Sobel Kernel}
        \\endsphinx

        C++ includes: itkSobelOperator.h 
        """
        _itkSobelOperatorPython.itkSobelOperatorF2_swiginit(self, _itkSobelOperatorPython.new_itkSobelOperatorF2(*args))
itkSobelOperatorF2_swigregister = _itkSobelOperatorPython.itkSobelOperatorF2_swigregister
itkSobelOperatorF2_swigregister(itkSobelOperatorF2)

class itkSobelOperatorF3(itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF3):
    """


    A NeighborhoodOperator for performing a directional Sobel edge-
    detection operation at a pixel location.

    SobelOperator is a directional NeighborhoodOperator that should be
    applied a NeighborhoodIterator using the NeighborhoodInnerProduct
    method. To create the operator:

    1) Set the direction by calling 2) call 3) You may optionally scale
    the coefficients of this operator using the method. This is useful if
    you want to take the spacing of the image into account when computing
    the edge strength. Apply the scaling only after calling to.

    The Sobel Operator in vertical direction for 2 dimensions is*
    -1  -2  -1 *             0    0   0 *             1    2 1 * * The
    Sobel Operator in horizontal direction is for 2 dimensions is*
    -1   0   1 *             -2   0   2 *             -1   0 1 *

    The current implementation of the Sobel operator is for 2 and 3
    dimensions only. The ND version is planned for future releases.

    The extension to 3D is from the publication "Irwin Sobel. An
    Isotropic 3x3x3 Volume Gradient Operator.   Technical report, Hewlett-
    Packard Laboratories, April 1995."

    The Sobel operator in 3D has the kernel

    * -1 -3 -1   0 0 0  1 3 1 * -3 -6 -3   0 0 0  3 6 3 * -1 -3 -1   0 0 0
    1 3 1 * *    x-1       x     x+1 *

    The x kernel is just rotated as required to obtain the kernel in the y
    and z directions.

    SobelOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:   Neighborhood

    See:   ForwardDifferenceOperator

    See:   BackwardDifferenceOperator  \\sphinx
    \\sphinxexample{Core/Common/CreateSobelKernel,Create Sobel Kernel}
    \\endsphinx

    C++ includes: itkSobelOperator.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkSobelOperatorPython.delete_itkSobelOperatorF3

    def __init__(self, *args):
        """
        __init__(itkSobelOperatorF3 self) -> itkSobelOperatorF3
        __init__(itkSobelOperatorF3 self, itkSobelOperatorF3 arg0) -> itkSobelOperatorF3



        A NeighborhoodOperator for performing a directional Sobel edge-
        detection operation at a pixel location.

        SobelOperator is a directional NeighborhoodOperator that should be
        applied a NeighborhoodIterator using the NeighborhoodInnerProduct
        method. To create the operator:

        1) Set the direction by calling 2) call 3) You may optionally scale
        the coefficients of this operator using the method. This is useful if
        you want to take the spacing of the image into account when computing
        the edge strength. Apply the scaling only after calling to.

        The Sobel Operator in vertical direction for 2 dimensions is*
        -1  -2  -1 *             0    0   0 *             1    2 1 * * The
        Sobel Operator in horizontal direction is for 2 dimensions is*
        -1   0   1 *             -2   0   2 *             -1   0 1 *

        The current implementation of the Sobel operator is for 2 and 3
        dimensions only. The ND version is planned for future releases.

        The extension to 3D is from the publication "Irwin Sobel. An
        Isotropic 3x3x3 Volume Gradient Operator.   Technical report, Hewlett-
        Packard Laboratories, April 1995."

        The Sobel operator in 3D has the kernel

        * -1 -3 -1   0 0 0  1 3 1 * -3 -6 -3   0 0 0  3 6 3 * -1 -3 -1   0 0 0
        1 3 1 * *    x-1       x     x+1 *

        The x kernel is just rotated as required to obtain the kernel in the y
        and z directions.

        SobelOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:   Neighborhood

        See:   ForwardDifferenceOperator

        See:   BackwardDifferenceOperator  \\sphinx
        \\sphinxexample{Core/Common/CreateSobelKernel,Create Sobel Kernel}
        \\endsphinx

        C++ includes: itkSobelOperator.h 
        """
        _itkSobelOperatorPython.itkSobelOperatorF3_swiginit(self, _itkSobelOperatorPython.new_itkSobelOperatorF3(*args))
itkSobelOperatorF3_swigregister = _itkSobelOperatorPython.itkSobelOperatorF3_swigregister
itkSobelOperatorF3_swigregister(itkSobelOperatorF3)



