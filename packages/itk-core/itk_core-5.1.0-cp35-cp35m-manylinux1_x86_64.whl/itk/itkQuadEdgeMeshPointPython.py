# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkQuadEdgeMeshPointPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkQuadEdgeMeshPointPython', [dirname(__file__)])
        except ImportError:
            import _itkQuadEdgeMeshPointPython
            return _itkQuadEdgeMeshPointPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkQuadEdgeMeshPointPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkQuadEdgeMeshPointPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkQuadEdgeMeshPointPython
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


import itkGeometricalQuadEdgePython
import itkQuadEdgePython
import pyBasePython
import itkPointPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkFixedArrayPython
import vnl_vector_refPython
import itkVectorPython
class itkQuadEdgeMeshPointF2GQEULULBBT(itkPointPython.itkPointF2):
    """


    Wrapper around a itk::Point in order to add a reference to an entry in
    the edge ring.

    C++ includes: itkQuadEdgeMeshPoint.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkQuadEdgeMeshPointPython.delete_itkQuadEdgeMeshPointF2GQEULULBBT

    def __init__(self, *args):
        """
        __init__(itkQuadEdgeMeshPointF2GQEULULBBT self) -> itkQuadEdgeMeshPointF2GQEULULBBT
        __init__(itkQuadEdgeMeshPointF2GQEULULBBT self, itkQuadEdgeMeshPointF2GQEULULBBT arg0) -> itkQuadEdgeMeshPointF2GQEULULBBT
        __init__(itkQuadEdgeMeshPointF2GQEULULBBT self, itkPointF2 r) -> itkQuadEdgeMeshPointF2GQEULULBBT
        __init__(itkQuadEdgeMeshPointF2GQEULULBBT self, float const * r) -> itkQuadEdgeMeshPointF2GQEULULBBT



        Wrapper around a itk::Point in order to add a reference to an entry in
        the edge ring.

        C++ includes: itkQuadEdgeMeshPoint.h 
        """
        _itkQuadEdgeMeshPointPython.itkQuadEdgeMeshPointF2GQEULULBBT_swiginit(self, _itkQuadEdgeMeshPointPython.new_itkQuadEdgeMeshPointF2GQEULULBBT(*args))

    def SetEdge(self, inputEdge: 'itkGeometricalQuadEdgeULULBBF') -> "void":
        """
        SetEdge(itkQuadEdgeMeshPointF2GQEULULBBT self, itkGeometricalQuadEdgeULULBBF inputEdge)

        Accessor on m_Edge 
        """
        return _itkQuadEdgeMeshPointPython.itkQuadEdgeMeshPointF2GQEULULBBT_SetEdge(self, inputEdge)


    def SetPoint(self, point: 'itkPointF2') -> "void":
        """
        SetPoint(itkQuadEdgeMeshPointF2GQEULULBBT self, itkPointF2 point)

        Set the coordinates from a
        standard itk::Point 
        """
        return _itkQuadEdgeMeshPointPython.itkQuadEdgeMeshPointF2GQEULULBBT_SetPoint(self, point)


    def GetEdge(self, *args) -> "itkGeometricalQuadEdgeULULBBF *":
        """
        GetEdge(itkQuadEdgeMeshPointF2GQEULULBBT self) -> itkGeometricalQuadEdgeULULBBF
        GetEdge(itkQuadEdgeMeshPointF2GQEULULBBT self) -> itkGeometricalQuadEdgeULULBBF

        Accessor on m_Edge 
        """
        return _itkQuadEdgeMeshPointPython.itkQuadEdgeMeshPointF2GQEULULBBT_GetEdge(self, *args)


    def IsInternal(self) -> "bool":
        """
        IsInternal(itkQuadEdgeMeshPointF2GQEULULBBT self) -> bool

        Return
        IsOriginalInternal of the edge. See:
        GeometricalQuadEdge::isOriginInternal 
        """
        return _itkQuadEdgeMeshPointPython.itkQuadEdgeMeshPointF2GQEULULBBT_IsInternal(self)


    def GetValence(self) -> "int":
        """
        GetValence(itkQuadEdgeMeshPointF2GQEULULBBT self) -> int

        Return the valence of
        this QuadEdgeMeshPoint i.e. the number of edges constituting the Onext
        ring to which this point belongs. the valence when an entry in the
        Onext ring is present, and -1 otherwise. 
        """
        return _itkQuadEdgeMeshPointPython.itkQuadEdgeMeshPointF2GQEULULBBT_GetValence(self)

itkQuadEdgeMeshPointF2GQEULULBBT.SetEdge = new_instancemethod(_itkQuadEdgeMeshPointPython.itkQuadEdgeMeshPointF2GQEULULBBT_SetEdge, None, itkQuadEdgeMeshPointF2GQEULULBBT)
itkQuadEdgeMeshPointF2GQEULULBBT.SetPoint = new_instancemethod(_itkQuadEdgeMeshPointPython.itkQuadEdgeMeshPointF2GQEULULBBT_SetPoint, None, itkQuadEdgeMeshPointF2GQEULULBBT)
itkQuadEdgeMeshPointF2GQEULULBBT.GetEdge = new_instancemethod(_itkQuadEdgeMeshPointPython.itkQuadEdgeMeshPointF2GQEULULBBT_GetEdge, None, itkQuadEdgeMeshPointF2GQEULULBBT)
itkQuadEdgeMeshPointF2GQEULULBBT.IsInternal = new_instancemethod(_itkQuadEdgeMeshPointPython.itkQuadEdgeMeshPointF2GQEULULBBT_IsInternal, None, itkQuadEdgeMeshPointF2GQEULULBBT)
itkQuadEdgeMeshPointF2GQEULULBBT.GetValence = new_instancemethod(_itkQuadEdgeMeshPointPython.itkQuadEdgeMeshPointF2GQEULULBBT_GetValence, None, itkQuadEdgeMeshPointF2GQEULULBBT)
itkQuadEdgeMeshPointF2GQEULULBBT_swigregister = _itkQuadEdgeMeshPointPython.itkQuadEdgeMeshPointF2GQEULULBBT_swigregister
itkQuadEdgeMeshPointF2GQEULULBBT_swigregister(itkQuadEdgeMeshPointF2GQEULULBBT)

class itkQuadEdgeMeshPointF3GQEULULBBT(itkPointPython.itkPointF3):
    """


    Wrapper around a itk::Point in order to add a reference to an entry in
    the edge ring.

    C++ includes: itkQuadEdgeMeshPoint.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkQuadEdgeMeshPointPython.delete_itkQuadEdgeMeshPointF3GQEULULBBT

    def __init__(self, *args):
        """
        __init__(itkQuadEdgeMeshPointF3GQEULULBBT self) -> itkQuadEdgeMeshPointF3GQEULULBBT
        __init__(itkQuadEdgeMeshPointF3GQEULULBBT self, itkQuadEdgeMeshPointF3GQEULULBBT arg0) -> itkQuadEdgeMeshPointF3GQEULULBBT
        __init__(itkQuadEdgeMeshPointF3GQEULULBBT self, itkPointF3 r) -> itkQuadEdgeMeshPointF3GQEULULBBT
        __init__(itkQuadEdgeMeshPointF3GQEULULBBT self, float const * r) -> itkQuadEdgeMeshPointF3GQEULULBBT



        Wrapper around a itk::Point in order to add a reference to an entry in
        the edge ring.

        C++ includes: itkQuadEdgeMeshPoint.h 
        """
        _itkQuadEdgeMeshPointPython.itkQuadEdgeMeshPointF3GQEULULBBT_swiginit(self, _itkQuadEdgeMeshPointPython.new_itkQuadEdgeMeshPointF3GQEULULBBT(*args))

    def SetEdge(self, inputEdge: 'itkGeometricalQuadEdgeULULBBF') -> "void":
        """
        SetEdge(itkQuadEdgeMeshPointF3GQEULULBBT self, itkGeometricalQuadEdgeULULBBF inputEdge)

        Accessor on m_Edge 
        """
        return _itkQuadEdgeMeshPointPython.itkQuadEdgeMeshPointF3GQEULULBBT_SetEdge(self, inputEdge)


    def SetPoint(self, point: 'itkPointF3') -> "void":
        """
        SetPoint(itkQuadEdgeMeshPointF3GQEULULBBT self, itkPointF3 point)

        Set the coordinates from a
        standard itk::Point 
        """
        return _itkQuadEdgeMeshPointPython.itkQuadEdgeMeshPointF3GQEULULBBT_SetPoint(self, point)


    def GetEdge(self, *args) -> "itkGeometricalQuadEdgeULULBBF *":
        """
        GetEdge(itkQuadEdgeMeshPointF3GQEULULBBT self) -> itkGeometricalQuadEdgeULULBBF
        GetEdge(itkQuadEdgeMeshPointF3GQEULULBBT self) -> itkGeometricalQuadEdgeULULBBF

        Accessor on m_Edge 
        """
        return _itkQuadEdgeMeshPointPython.itkQuadEdgeMeshPointF3GQEULULBBT_GetEdge(self, *args)


    def IsInternal(self) -> "bool":
        """
        IsInternal(itkQuadEdgeMeshPointF3GQEULULBBT self) -> bool

        Return
        IsOriginalInternal of the edge. See:
        GeometricalQuadEdge::isOriginInternal 
        """
        return _itkQuadEdgeMeshPointPython.itkQuadEdgeMeshPointF3GQEULULBBT_IsInternal(self)


    def GetValence(self) -> "int":
        """
        GetValence(itkQuadEdgeMeshPointF3GQEULULBBT self) -> int

        Return the valence of
        this QuadEdgeMeshPoint i.e. the number of edges constituting the Onext
        ring to which this point belongs. the valence when an entry in the
        Onext ring is present, and -1 otherwise. 
        """
        return _itkQuadEdgeMeshPointPython.itkQuadEdgeMeshPointF3GQEULULBBT_GetValence(self)

itkQuadEdgeMeshPointF3GQEULULBBT.SetEdge = new_instancemethod(_itkQuadEdgeMeshPointPython.itkQuadEdgeMeshPointF3GQEULULBBT_SetEdge, None, itkQuadEdgeMeshPointF3GQEULULBBT)
itkQuadEdgeMeshPointF3GQEULULBBT.SetPoint = new_instancemethod(_itkQuadEdgeMeshPointPython.itkQuadEdgeMeshPointF3GQEULULBBT_SetPoint, None, itkQuadEdgeMeshPointF3GQEULULBBT)
itkQuadEdgeMeshPointF3GQEULULBBT.GetEdge = new_instancemethod(_itkQuadEdgeMeshPointPython.itkQuadEdgeMeshPointF3GQEULULBBT_GetEdge, None, itkQuadEdgeMeshPointF3GQEULULBBT)
itkQuadEdgeMeshPointF3GQEULULBBT.IsInternal = new_instancemethod(_itkQuadEdgeMeshPointPython.itkQuadEdgeMeshPointF3GQEULULBBT_IsInternal, None, itkQuadEdgeMeshPointF3GQEULULBBT)
itkQuadEdgeMeshPointF3GQEULULBBT.GetValence = new_instancemethod(_itkQuadEdgeMeshPointPython.itkQuadEdgeMeshPointF3GQEULULBBT_GetValence, None, itkQuadEdgeMeshPointF3GQEULULBBT)
itkQuadEdgeMeshPointF3GQEULULBBT_swigregister = _itkQuadEdgeMeshPointPython.itkQuadEdgeMeshPointF3GQEULULBBT_swigregister
itkQuadEdgeMeshPointF3GQEULULBBT_swigregister(itkQuadEdgeMeshPointF3GQEULULBBT)



