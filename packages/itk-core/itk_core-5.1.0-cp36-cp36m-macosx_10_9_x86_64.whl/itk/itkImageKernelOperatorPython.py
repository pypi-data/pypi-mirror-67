# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkImageKernelOperatorPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkImageKernelOperatorPython', [dirname(__file__)])
        except ImportError:
            import _itkImageKernelOperatorPython
            return _itkImageKernelOperatorPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkImageKernelOperatorPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkImageKernelOperatorPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkImageKernelOperatorPython
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
import itkImagePython
import itkOffsetPython
import itkSizePython
import itkSymmetricSecondRankTensorPython
import itkFixedArrayPython
import itkMatrixPython
import vnl_matrixPython
import vnl_vectorPython
import stdcomplexPython
import itkPointPython
import vnl_vector_refPython
import itkVectorPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import itkRGBAPixelPython
import itkImageRegionPython
import itkIndexPython
import itkRGBPixelPython
import itkNeighborhoodOperatorPython
import itkNeighborhoodPython
class itkImageKernelOperatorD2(itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD2):
    """


    A NeighborhoodOperator whose coefficients are from an image.

    This code was contributed in the Insight Journal paper:

    "Image Kernel Convolution" by Tustison N., Gee
    J.https://hdl.handle.net/1926/1323http://www.insight-
    journal.org/browse/publication/208

    ImageKernelOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:  NeighborhoodIterator

    See:   Neighborhood

    C++ includes: itkImageKernelOperator.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def SetImageKernel(self, kernel: 'itkImageD2') -> "void":
        """
        SetImageKernel(itkImageKernelOperatorD2 self, itkImageD2 kernel)

        Set the image
        kernel. Only images with odd size in all dimensions are allowed. If an
        image with an even size is passed as an argument, an exception will be
        thrown. 
        """
        return _itkImageKernelOperatorPython.itkImageKernelOperatorD2_SetImageKernel(self, kernel)


    def GetImageKernel(self) -> "itkImageD2 const *":
        """
        GetImageKernel(itkImageKernelOperatorD2 self) -> itkImageD2

        Get the image
        kernel. 
        """
        return _itkImageKernelOperatorPython.itkImageKernelOperatorD2_GetImageKernel(self)

    __swig_destroy__ = _itkImageKernelOperatorPython.delete_itkImageKernelOperatorD2

    def __init__(self, *args):
        """
        __init__(itkImageKernelOperatorD2 self, itkImageKernelOperatorD2 arg0) -> itkImageKernelOperatorD2
        __init__(itkImageKernelOperatorD2 self) -> itkImageKernelOperatorD2



        A NeighborhoodOperator whose coefficients are from an image.

        This code was contributed in the Insight Journal paper:

        "Image Kernel Convolution" by Tustison N., Gee
        J.https://hdl.handle.net/1926/1323http://www.insight-
        journal.org/browse/publication/208

        ImageKernelOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:  NeighborhoodIterator

        See:   Neighborhood

        C++ includes: itkImageKernelOperator.h 
        """
        _itkImageKernelOperatorPython.itkImageKernelOperatorD2_swiginit(self, _itkImageKernelOperatorPython.new_itkImageKernelOperatorD2(*args))
itkImageKernelOperatorD2.SetImageKernel = new_instancemethod(_itkImageKernelOperatorPython.itkImageKernelOperatorD2_SetImageKernel, None, itkImageKernelOperatorD2)
itkImageKernelOperatorD2.GetImageKernel = new_instancemethod(_itkImageKernelOperatorPython.itkImageKernelOperatorD2_GetImageKernel, None, itkImageKernelOperatorD2)
itkImageKernelOperatorD2_swigregister = _itkImageKernelOperatorPython.itkImageKernelOperatorD2_swigregister
itkImageKernelOperatorD2_swigregister(itkImageKernelOperatorD2)

class itkImageKernelOperatorD3(itkNeighborhoodOperatorPython.itkNeighborhoodOperatorD3):
    """


    A NeighborhoodOperator whose coefficients are from an image.

    This code was contributed in the Insight Journal paper:

    "Image Kernel Convolution" by Tustison N., Gee
    J.https://hdl.handle.net/1926/1323http://www.insight-
    journal.org/browse/publication/208

    ImageKernelOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:  NeighborhoodIterator

    See:   Neighborhood

    C++ includes: itkImageKernelOperator.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def SetImageKernel(self, kernel: 'itkImageD3') -> "void":
        """
        SetImageKernel(itkImageKernelOperatorD3 self, itkImageD3 kernel)

        Set the image
        kernel. Only images with odd size in all dimensions are allowed. If an
        image with an even size is passed as an argument, an exception will be
        thrown. 
        """
        return _itkImageKernelOperatorPython.itkImageKernelOperatorD3_SetImageKernel(self, kernel)


    def GetImageKernel(self) -> "itkImageD3 const *":
        """
        GetImageKernel(itkImageKernelOperatorD3 self) -> itkImageD3

        Get the image
        kernel. 
        """
        return _itkImageKernelOperatorPython.itkImageKernelOperatorD3_GetImageKernel(self)

    __swig_destroy__ = _itkImageKernelOperatorPython.delete_itkImageKernelOperatorD3

    def __init__(self, *args):
        """
        __init__(itkImageKernelOperatorD3 self, itkImageKernelOperatorD3 arg0) -> itkImageKernelOperatorD3
        __init__(itkImageKernelOperatorD3 self) -> itkImageKernelOperatorD3



        A NeighborhoodOperator whose coefficients are from an image.

        This code was contributed in the Insight Journal paper:

        "Image Kernel Convolution" by Tustison N., Gee
        J.https://hdl.handle.net/1926/1323http://www.insight-
        journal.org/browse/publication/208

        ImageKernelOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:  NeighborhoodIterator

        See:   Neighborhood

        C++ includes: itkImageKernelOperator.h 
        """
        _itkImageKernelOperatorPython.itkImageKernelOperatorD3_swiginit(self, _itkImageKernelOperatorPython.new_itkImageKernelOperatorD3(*args))
itkImageKernelOperatorD3.SetImageKernel = new_instancemethod(_itkImageKernelOperatorPython.itkImageKernelOperatorD3_SetImageKernel, None, itkImageKernelOperatorD3)
itkImageKernelOperatorD3.GetImageKernel = new_instancemethod(_itkImageKernelOperatorPython.itkImageKernelOperatorD3_GetImageKernel, None, itkImageKernelOperatorD3)
itkImageKernelOperatorD3_swigregister = _itkImageKernelOperatorPython.itkImageKernelOperatorD3_swigregister
itkImageKernelOperatorD3_swigregister(itkImageKernelOperatorD3)

class itkImageKernelOperatorF2(itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF2):
    """


    A NeighborhoodOperator whose coefficients are from an image.

    This code was contributed in the Insight Journal paper:

    "Image Kernel Convolution" by Tustison N., Gee
    J.https://hdl.handle.net/1926/1323http://www.insight-
    journal.org/browse/publication/208

    ImageKernelOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:  NeighborhoodIterator

    See:   Neighborhood

    C++ includes: itkImageKernelOperator.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def SetImageKernel(self, kernel: 'itkImageF2') -> "void":
        """
        SetImageKernel(itkImageKernelOperatorF2 self, itkImageF2 kernel)

        Set the image
        kernel. Only images with odd size in all dimensions are allowed. If an
        image with an even size is passed as an argument, an exception will be
        thrown. 
        """
        return _itkImageKernelOperatorPython.itkImageKernelOperatorF2_SetImageKernel(self, kernel)


    def GetImageKernel(self) -> "itkImageF2 const *":
        """
        GetImageKernel(itkImageKernelOperatorF2 self) -> itkImageF2

        Get the image
        kernel. 
        """
        return _itkImageKernelOperatorPython.itkImageKernelOperatorF2_GetImageKernel(self)

    __swig_destroy__ = _itkImageKernelOperatorPython.delete_itkImageKernelOperatorF2

    def __init__(self, *args):
        """
        __init__(itkImageKernelOperatorF2 self, itkImageKernelOperatorF2 arg0) -> itkImageKernelOperatorF2
        __init__(itkImageKernelOperatorF2 self) -> itkImageKernelOperatorF2



        A NeighborhoodOperator whose coefficients are from an image.

        This code was contributed in the Insight Journal paper:

        "Image Kernel Convolution" by Tustison N., Gee
        J.https://hdl.handle.net/1926/1323http://www.insight-
        journal.org/browse/publication/208

        ImageKernelOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:  NeighborhoodIterator

        See:   Neighborhood

        C++ includes: itkImageKernelOperator.h 
        """
        _itkImageKernelOperatorPython.itkImageKernelOperatorF2_swiginit(self, _itkImageKernelOperatorPython.new_itkImageKernelOperatorF2(*args))
itkImageKernelOperatorF2.SetImageKernel = new_instancemethod(_itkImageKernelOperatorPython.itkImageKernelOperatorF2_SetImageKernel, None, itkImageKernelOperatorF2)
itkImageKernelOperatorF2.GetImageKernel = new_instancemethod(_itkImageKernelOperatorPython.itkImageKernelOperatorF2_GetImageKernel, None, itkImageKernelOperatorF2)
itkImageKernelOperatorF2_swigregister = _itkImageKernelOperatorPython.itkImageKernelOperatorF2_swigregister
itkImageKernelOperatorF2_swigregister(itkImageKernelOperatorF2)

class itkImageKernelOperatorF3(itkNeighborhoodOperatorPython.itkNeighborhoodOperatorF3):
    """


    A NeighborhoodOperator whose coefficients are from an image.

    This code was contributed in the Insight Journal paper:

    "Image Kernel Convolution" by Tustison N., Gee
    J.https://hdl.handle.net/1926/1323http://www.insight-
    journal.org/browse/publication/208

    ImageKernelOperator does not have any user-declared "special member
    function", following the C++ Rule of Zero: the compiler will generate
    them if necessary.

    See:   NeighborhoodOperator

    See:  NeighborhoodIterator

    See:   Neighborhood

    C++ includes: itkImageKernelOperator.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def SetImageKernel(self, kernel: 'itkImageF3') -> "void":
        """
        SetImageKernel(itkImageKernelOperatorF3 self, itkImageF3 kernel)

        Set the image
        kernel. Only images with odd size in all dimensions are allowed. If an
        image with an even size is passed as an argument, an exception will be
        thrown. 
        """
        return _itkImageKernelOperatorPython.itkImageKernelOperatorF3_SetImageKernel(self, kernel)


    def GetImageKernel(self) -> "itkImageF3 const *":
        """
        GetImageKernel(itkImageKernelOperatorF3 self) -> itkImageF3

        Get the image
        kernel. 
        """
        return _itkImageKernelOperatorPython.itkImageKernelOperatorF3_GetImageKernel(self)

    __swig_destroy__ = _itkImageKernelOperatorPython.delete_itkImageKernelOperatorF3

    def __init__(self, *args):
        """
        __init__(itkImageKernelOperatorF3 self, itkImageKernelOperatorF3 arg0) -> itkImageKernelOperatorF3
        __init__(itkImageKernelOperatorF3 self) -> itkImageKernelOperatorF3



        A NeighborhoodOperator whose coefficients are from an image.

        This code was contributed in the Insight Journal paper:

        "Image Kernel Convolution" by Tustison N., Gee
        J.https://hdl.handle.net/1926/1323http://www.insight-
        journal.org/browse/publication/208

        ImageKernelOperator does not have any user-declared "special member
        function", following the C++ Rule of Zero: the compiler will generate
        them if necessary.

        See:   NeighborhoodOperator

        See:  NeighborhoodIterator

        See:   Neighborhood

        C++ includes: itkImageKernelOperator.h 
        """
        _itkImageKernelOperatorPython.itkImageKernelOperatorF3_swiginit(self, _itkImageKernelOperatorPython.new_itkImageKernelOperatorF3(*args))
itkImageKernelOperatorF3.SetImageKernel = new_instancemethod(_itkImageKernelOperatorPython.itkImageKernelOperatorF3_SetImageKernel, None, itkImageKernelOperatorF3)
itkImageKernelOperatorF3.GetImageKernel = new_instancemethod(_itkImageKernelOperatorPython.itkImageKernelOperatorF3_GetImageKernel, None, itkImageKernelOperatorF3)
itkImageKernelOperatorF3_swigregister = _itkImageKernelOperatorPython.itkImageKernelOperatorF3_swigregister
itkImageKernelOperatorF3_swigregister(itkImageKernelOperatorF3)



