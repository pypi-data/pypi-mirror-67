# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkQuadEdgeCellTraitsInfoPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkQuadEdgeCellTraitsInfoPython', [dirname(__file__)])
        except ImportError:
            import _itkQuadEdgeCellTraitsInfoPython
            return _itkQuadEdgeCellTraitsInfoPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkQuadEdgeCellTraitsInfoPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkQuadEdgeCellTraitsInfoPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkQuadEdgeCellTraitsInfoPython
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


import itkQuadEdgeMeshPointPython
import itkPointPython
import vnl_vector_refPython
import stdcomplexPython
import pyBasePython
import vnl_vectorPython
import vnl_matrixPython
import itkFixedArrayPython
import itkVectorPython
import itkGeometricalQuadEdgePython
import itkQuadEdgePython
import ITKCommonBasePython

def itkMapContainerULQEMPF3GQEULULBBT_New():
  return itkMapContainerULQEMPF3GQEULULBBT.New()


def itkMapContainerULQEMPF2GQEULULBBT_New():
  return itkMapContainerULQEMPF2GQEULULBBT.New()

class itkMapContainerULQEMPF2GQEULULBBT(ITKCommonBasePython.itkObject):
    """


    A wrapper of the STL "map" container.

    Define a front-end to the STL "map" container that conforms to the
    IndexedContainerInterface. This is a full-fleged Object, so there are
    events, modification time, debug, and reference count information.

    Parameters:
    -----------

    TElementIdentifier:  A type that shall be used to index the container.
    It must have a < operator defined for ordering.

    TElement:  The element type stored in the container.

    C++ includes: itkMapContainer.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkMapContainerULQEMPF2GQEULULBBT self) -> itkMapContainerULQEMPF2GQEULULBBT
        __init__(itkMapContainerULQEMPF2GQEULULBBT self, std::less< unsigned long > const & comp) -> itkMapContainerULQEMPF2GQEULULBBT



        A wrapper of the STL "map" container.

        Define a front-end to the STL "map" container that conforms to the
        IndexedContainerInterface. This is a full-fleged Object, so there are
        events, modification time, debug, and reference count information.

        Parameters:
        -----------

        TElementIdentifier:  A type that shall be used to index the container.
        It must have a < operator defined for ordering.

        TElement:  The element type stored in the container.

        C++ includes: itkMapContainer.h 
        """
        _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_swiginit(self, _itkQuadEdgeCellTraitsInfoPython.new_itkMapContainerULQEMPF2GQEULULBBT(*args))

    def __New_orig__() -> "itkMapContainerULQEMPF2GQEULULBBT_Pointer":
        """__New_orig__() -> itkMapContainerULQEMPF2GQEULULBBT_Pointer"""
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMapContainerULQEMPF2GQEULULBBT_Pointer":
        """Clone(itkMapContainerULQEMPF2GQEULULBBT self) -> itkMapContainerULQEMPF2GQEULULBBT_Pointer"""
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_Clone(self)


    def CastToSTLContainer(self) -> "std::map< unsigned long,itkQuadEdgeMeshPointF2GQEULULBBT,std::less< unsigned long >,std::allocator< std::pair< unsigned long const,itkQuadEdgeMeshPointF2GQEULULBBT > > > &":
        """
        CastToSTLContainer(itkMapContainerULQEMPF2GQEULULBBT self) -> std::map< unsigned long,itkQuadEdgeMeshPointF2GQEULULBBT,std::less< unsigned long >,std::allocator< std::pair< unsigned long const,itkQuadEdgeMeshPointF2GQEULULBBT > > > &

        Cast the
        container to a STL container type 
        """
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_CastToSTLContainer(self)


    def CastToSTLConstContainer(self) -> "std::map< unsigned long,itkQuadEdgeMeshPointF2GQEULULBBT,std::less< unsigned long >,std::allocator< std::pair< unsigned long const,itkQuadEdgeMeshPointF2GQEULULBBT > > > const &":
        """
        CastToSTLConstContainer(itkMapContainerULQEMPF2GQEULULBBT self) -> std::map< unsigned long,itkQuadEdgeMeshPointF2GQEULULBBT,std::less< unsigned long >,std::allocator< std::pair< unsigned long const,itkQuadEdgeMeshPointF2GQEULULBBT > > > const &

        Cast the
        container to a const STL container type 
        """
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_CastToSTLConstContainer(self)


    def ElementAt(self, *args) -> "itkQuadEdgeMeshPointF2GQEULULBBT const &":
        """
        ElementAt(itkMapContainerULQEMPF2GQEULULBBT self, unsigned long arg0) -> itkQuadEdgeMeshPointF2GQEULULBBT
        ElementAt(itkMapContainerULQEMPF2GQEULULBBT self, unsigned long arg0) -> itkQuadEdgeMeshPointF2GQEULULBBT

        Get a reference to the
        element at the given index. 
        """
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_ElementAt(self, *args)


    def CreateElementAt(self, arg0: 'unsigned long') -> "itkQuadEdgeMeshPointF2GQEULULBBT &":
        """
        CreateElementAt(itkMapContainerULQEMPF2GQEULULBBT self, unsigned long arg0) -> itkQuadEdgeMeshPointF2GQEULULBBT

        Get a reference to
        the element at the given index. If the index does not exist, it is
        created automatically.

        It is assumed that the value of the element is modified through the
        reference. 
        """
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_CreateElementAt(self, arg0)


    def GetElement(self, arg0: 'unsigned long') -> "itkQuadEdgeMeshPointF2GQEULULBBT":
        """
        GetElement(itkMapContainerULQEMPF2GQEULULBBT self, unsigned long arg0) -> itkQuadEdgeMeshPointF2GQEULULBBT

        Get the element at the
        specified index. There is no check for existence performed. 
        """
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_GetElement(self, arg0)


    def SetElement(self, arg0: 'unsigned long', arg1: 'itkQuadEdgeMeshPointF2GQEULULBBT') -> "void":
        """
        SetElement(itkMapContainerULQEMPF2GQEULULBBT self, unsigned long arg0, itkQuadEdgeMeshPointF2GQEULULBBT arg1)

        Set the given index
        value to the given element. If the index doesn't exist, it is
        automatically created. 
        """
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_SetElement(self, arg0, arg1)


    def InsertElement(self, arg0: 'unsigned long', arg1: 'itkQuadEdgeMeshPointF2GQEULULBBT') -> "void":
        """
        InsertElement(itkMapContainerULQEMPF2GQEULULBBT self, unsigned long arg0, itkQuadEdgeMeshPointF2GQEULULBBT arg1)

        Set the given index
        value to the given element. If the index doesn't exist, it is
        automatically created. 
        """
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_InsertElement(self, arg0, arg1)


    def IndexExists(self, arg0: 'unsigned long') -> "bool":
        """
        IndexExists(itkMapContainerULQEMPF2GQEULULBBT self, unsigned long arg0) -> bool

        Check if the STL map
        has an entry corresponding to the given index. The count will be
        either 1 or 0. 
        """
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_IndexExists(self, arg0)


    def GetElementIfIndexExists(self, arg0: 'unsigned long', arg1: 'itkQuadEdgeMeshPointF2GQEULULBBT') -> "bool":
        """
        GetElementIfIndexExists(itkMapContainerULQEMPF2GQEULULBBT self, unsigned long arg0, itkQuadEdgeMeshPointF2GQEULULBBT arg1) -> bool

        If the
        given index doesn't exist in the map, return false. Otherwise, set the
        element through the pointer (if it isn't null), and return true. 
        """
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_GetElementIfIndexExists(self, arg0, arg1)


    def CreateIndex(self, arg0: 'unsigned long') -> "void":
        """
        CreateIndex(itkMapContainerULQEMPF2GQEULULBBT self, unsigned long arg0)

        The map will create an
        entry for a given index through the indexing operator. Whether or not
        it is created, it will be assigned to the default element. 
        """
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_CreateIndex(self, arg0)


    def DeleteIndex(self, arg0: 'unsigned long') -> "void":
        """
        DeleteIndex(itkMapContainerULQEMPF2GQEULULBBT self, unsigned long arg0)

        Delete the entry in the
        STL map corresponding to the given identifier. If the entry does not
        exist, nothing happens. 
        """
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_DeleteIndex(self, arg0)


    def Size(self) -> "unsigned long":
        """
        Size(itkMapContainerULQEMPF2GQEULULBBT self) -> unsigned long

        Get the number of elements
        currently stored in the map. 
        """
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_Size(self)


    def Reserve(self, arg0: 'unsigned long') -> "void":
        """
        Reserve(itkMapContainerULQEMPF2GQEULULBBT self, unsigned long arg0)

        Tell the container to
        allocate enough memory to allow at least as many elements as the size
        given to be stored. This is NOT guaranteed to actually allocate any
        memory, but is useful if the implementation of the container allocates
        contiguous storage. 
        """
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_Reserve(self, arg0)


    def Squeeze(self) -> "void":
        """
        Squeeze(itkMapContainerULQEMPF2GQEULULBBT self)

        Tell the container to try
        to minimize its memory usage for storage of the current number of
        elements. This is NOT guaranteed to decrease memory usage. 
        """
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_Squeeze(self)


    def Initialize(self) -> "void":
        """
        Initialize(itkMapContainerULQEMPF2GQEULULBBT self)

        Tell the container to
        release any memory it may have allocated and return itself to its
        initial state. 
        """
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_Initialize(self)

    __swig_destroy__ = _itkQuadEdgeCellTraitsInfoPython.delete_itkMapContainerULQEMPF2GQEULULBBT

    def cast(obj: 'itkLightObject') -> "itkMapContainerULQEMPF2GQEULULBBT *":
        """cast(itkLightObject obj) -> itkMapContainerULQEMPF2GQEULULBBT"""
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkMapContainerULQEMPF2GQEULULBBT

        Create a new object of the class itkMapContainerULQEMPF2GQEULULBBT and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMapContainerULQEMPF2GQEULULBBT.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMapContainerULQEMPF2GQEULULBBT.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMapContainerULQEMPF2GQEULULBBT.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMapContainerULQEMPF2GQEULULBBT.Clone = new_instancemethod(_itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_Clone, None, itkMapContainerULQEMPF2GQEULULBBT)
itkMapContainerULQEMPF2GQEULULBBT.CastToSTLContainer = new_instancemethod(_itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_CastToSTLContainer, None, itkMapContainerULQEMPF2GQEULULBBT)
itkMapContainerULQEMPF2GQEULULBBT.CastToSTLConstContainer = new_instancemethod(_itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_CastToSTLConstContainer, None, itkMapContainerULQEMPF2GQEULULBBT)
itkMapContainerULQEMPF2GQEULULBBT.ElementAt = new_instancemethod(_itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_ElementAt, None, itkMapContainerULQEMPF2GQEULULBBT)
itkMapContainerULQEMPF2GQEULULBBT.CreateElementAt = new_instancemethod(_itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_CreateElementAt, None, itkMapContainerULQEMPF2GQEULULBBT)
itkMapContainerULQEMPF2GQEULULBBT.GetElement = new_instancemethod(_itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_GetElement, None, itkMapContainerULQEMPF2GQEULULBBT)
itkMapContainerULQEMPF2GQEULULBBT.SetElement = new_instancemethod(_itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_SetElement, None, itkMapContainerULQEMPF2GQEULULBBT)
itkMapContainerULQEMPF2GQEULULBBT.InsertElement = new_instancemethod(_itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_InsertElement, None, itkMapContainerULQEMPF2GQEULULBBT)
itkMapContainerULQEMPF2GQEULULBBT.IndexExists = new_instancemethod(_itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_IndexExists, None, itkMapContainerULQEMPF2GQEULULBBT)
itkMapContainerULQEMPF2GQEULULBBT.GetElementIfIndexExists = new_instancemethod(_itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_GetElementIfIndexExists, None, itkMapContainerULQEMPF2GQEULULBBT)
itkMapContainerULQEMPF2GQEULULBBT.CreateIndex = new_instancemethod(_itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_CreateIndex, None, itkMapContainerULQEMPF2GQEULULBBT)
itkMapContainerULQEMPF2GQEULULBBT.DeleteIndex = new_instancemethod(_itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_DeleteIndex, None, itkMapContainerULQEMPF2GQEULULBBT)
itkMapContainerULQEMPF2GQEULULBBT.Size = new_instancemethod(_itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_Size, None, itkMapContainerULQEMPF2GQEULULBBT)
itkMapContainerULQEMPF2GQEULULBBT.Reserve = new_instancemethod(_itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_Reserve, None, itkMapContainerULQEMPF2GQEULULBBT)
itkMapContainerULQEMPF2GQEULULBBT.Squeeze = new_instancemethod(_itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_Squeeze, None, itkMapContainerULQEMPF2GQEULULBBT)
itkMapContainerULQEMPF2GQEULULBBT.Initialize = new_instancemethod(_itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_Initialize, None, itkMapContainerULQEMPF2GQEULULBBT)
itkMapContainerULQEMPF2GQEULULBBT_swigregister = _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_swigregister
itkMapContainerULQEMPF2GQEULULBBT_swigregister(itkMapContainerULQEMPF2GQEULULBBT)

def itkMapContainerULQEMPF2GQEULULBBT___New_orig__() -> "itkMapContainerULQEMPF2GQEULULBBT_Pointer":
    """itkMapContainerULQEMPF2GQEULULBBT___New_orig__() -> itkMapContainerULQEMPF2GQEULULBBT_Pointer"""
    return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT___New_orig__()

def itkMapContainerULQEMPF2GQEULULBBT_cast(obj: 'itkLightObject') -> "itkMapContainerULQEMPF2GQEULULBBT *":
    """itkMapContainerULQEMPF2GQEULULBBT_cast(itkLightObject obj) -> itkMapContainerULQEMPF2GQEULULBBT"""
    return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF2GQEULULBBT_cast(obj)

class itkMapContainerULQEMPF3GQEULULBBT(ITKCommonBasePython.itkObject):
    """


    A wrapper of the STL "map" container.

    Define a front-end to the STL "map" container that conforms to the
    IndexedContainerInterface. This is a full-fleged Object, so there are
    events, modification time, debug, and reference count information.

    Parameters:
    -----------

    TElementIdentifier:  A type that shall be used to index the container.
    It must have a < operator defined for ordering.

    TElement:  The element type stored in the container.

    C++ includes: itkMapContainer.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkMapContainerULQEMPF3GQEULULBBT self) -> itkMapContainerULQEMPF3GQEULULBBT
        __init__(itkMapContainerULQEMPF3GQEULULBBT self, std::less< unsigned long > const & comp) -> itkMapContainerULQEMPF3GQEULULBBT



        A wrapper of the STL "map" container.

        Define a front-end to the STL "map" container that conforms to the
        IndexedContainerInterface. This is a full-fleged Object, so there are
        events, modification time, debug, and reference count information.

        Parameters:
        -----------

        TElementIdentifier:  A type that shall be used to index the container.
        It must have a < operator defined for ordering.

        TElement:  The element type stored in the container.

        C++ includes: itkMapContainer.h 
        """
        _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_swiginit(self, _itkQuadEdgeCellTraitsInfoPython.new_itkMapContainerULQEMPF3GQEULULBBT(*args))

    def __New_orig__() -> "itkMapContainerULQEMPF3GQEULULBBT_Pointer":
        """__New_orig__() -> itkMapContainerULQEMPF3GQEULULBBT_Pointer"""
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMapContainerULQEMPF3GQEULULBBT_Pointer":
        """Clone(itkMapContainerULQEMPF3GQEULULBBT self) -> itkMapContainerULQEMPF3GQEULULBBT_Pointer"""
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_Clone(self)


    def CastToSTLContainer(self) -> "std::map< unsigned long,itkQuadEdgeMeshPointF3GQEULULBBT,std::less< unsigned long >,std::allocator< std::pair< unsigned long const,itkQuadEdgeMeshPointF3GQEULULBBT > > > &":
        """
        CastToSTLContainer(itkMapContainerULQEMPF3GQEULULBBT self) -> std::map< unsigned long,itkQuadEdgeMeshPointF3GQEULULBBT,std::less< unsigned long >,std::allocator< std::pair< unsigned long const,itkQuadEdgeMeshPointF3GQEULULBBT > > > &

        Cast the
        container to a STL container type 
        """
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_CastToSTLContainer(self)


    def CastToSTLConstContainer(self) -> "std::map< unsigned long,itkQuadEdgeMeshPointF3GQEULULBBT,std::less< unsigned long >,std::allocator< std::pair< unsigned long const,itkQuadEdgeMeshPointF3GQEULULBBT > > > const &":
        """
        CastToSTLConstContainer(itkMapContainerULQEMPF3GQEULULBBT self) -> std::map< unsigned long,itkQuadEdgeMeshPointF3GQEULULBBT,std::less< unsigned long >,std::allocator< std::pair< unsigned long const,itkQuadEdgeMeshPointF3GQEULULBBT > > > const &

        Cast the
        container to a const STL container type 
        """
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_CastToSTLConstContainer(self)


    def ElementAt(self, *args) -> "itkQuadEdgeMeshPointF3GQEULULBBT const &":
        """
        ElementAt(itkMapContainerULQEMPF3GQEULULBBT self, unsigned long arg0) -> itkQuadEdgeMeshPointF3GQEULULBBT
        ElementAt(itkMapContainerULQEMPF3GQEULULBBT self, unsigned long arg0) -> itkQuadEdgeMeshPointF3GQEULULBBT

        Get a reference to the
        element at the given index. 
        """
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_ElementAt(self, *args)


    def CreateElementAt(self, arg0: 'unsigned long') -> "itkQuadEdgeMeshPointF3GQEULULBBT &":
        """
        CreateElementAt(itkMapContainerULQEMPF3GQEULULBBT self, unsigned long arg0) -> itkQuadEdgeMeshPointF3GQEULULBBT

        Get a reference to
        the element at the given index. If the index does not exist, it is
        created automatically.

        It is assumed that the value of the element is modified through the
        reference. 
        """
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_CreateElementAt(self, arg0)


    def GetElement(self, arg0: 'unsigned long') -> "itkQuadEdgeMeshPointF3GQEULULBBT":
        """
        GetElement(itkMapContainerULQEMPF3GQEULULBBT self, unsigned long arg0) -> itkQuadEdgeMeshPointF3GQEULULBBT

        Get the element at the
        specified index. There is no check for existence performed. 
        """
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_GetElement(self, arg0)


    def SetElement(self, arg0: 'unsigned long', arg1: 'itkQuadEdgeMeshPointF3GQEULULBBT') -> "void":
        """
        SetElement(itkMapContainerULQEMPF3GQEULULBBT self, unsigned long arg0, itkQuadEdgeMeshPointF3GQEULULBBT arg1)

        Set the given index
        value to the given element. If the index doesn't exist, it is
        automatically created. 
        """
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_SetElement(self, arg0, arg1)


    def InsertElement(self, arg0: 'unsigned long', arg1: 'itkQuadEdgeMeshPointF3GQEULULBBT') -> "void":
        """
        InsertElement(itkMapContainerULQEMPF3GQEULULBBT self, unsigned long arg0, itkQuadEdgeMeshPointF3GQEULULBBT arg1)

        Set the given index
        value to the given element. If the index doesn't exist, it is
        automatically created. 
        """
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_InsertElement(self, arg0, arg1)


    def IndexExists(self, arg0: 'unsigned long') -> "bool":
        """
        IndexExists(itkMapContainerULQEMPF3GQEULULBBT self, unsigned long arg0) -> bool

        Check if the STL map
        has an entry corresponding to the given index. The count will be
        either 1 or 0. 
        """
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_IndexExists(self, arg0)


    def GetElementIfIndexExists(self, arg0: 'unsigned long', arg1: 'itkQuadEdgeMeshPointF3GQEULULBBT') -> "bool":
        """
        GetElementIfIndexExists(itkMapContainerULQEMPF3GQEULULBBT self, unsigned long arg0, itkQuadEdgeMeshPointF3GQEULULBBT arg1) -> bool

        If the
        given index doesn't exist in the map, return false. Otherwise, set the
        element through the pointer (if it isn't null), and return true. 
        """
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_GetElementIfIndexExists(self, arg0, arg1)


    def CreateIndex(self, arg0: 'unsigned long') -> "void":
        """
        CreateIndex(itkMapContainerULQEMPF3GQEULULBBT self, unsigned long arg0)

        The map will create an
        entry for a given index through the indexing operator. Whether or not
        it is created, it will be assigned to the default element. 
        """
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_CreateIndex(self, arg0)


    def DeleteIndex(self, arg0: 'unsigned long') -> "void":
        """
        DeleteIndex(itkMapContainerULQEMPF3GQEULULBBT self, unsigned long arg0)

        Delete the entry in the
        STL map corresponding to the given identifier. If the entry does not
        exist, nothing happens. 
        """
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_DeleteIndex(self, arg0)


    def Size(self) -> "unsigned long":
        """
        Size(itkMapContainerULQEMPF3GQEULULBBT self) -> unsigned long

        Get the number of elements
        currently stored in the map. 
        """
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_Size(self)


    def Reserve(self, arg0: 'unsigned long') -> "void":
        """
        Reserve(itkMapContainerULQEMPF3GQEULULBBT self, unsigned long arg0)

        Tell the container to
        allocate enough memory to allow at least as many elements as the size
        given to be stored. This is NOT guaranteed to actually allocate any
        memory, but is useful if the implementation of the container allocates
        contiguous storage. 
        """
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_Reserve(self, arg0)


    def Squeeze(self) -> "void":
        """
        Squeeze(itkMapContainerULQEMPF3GQEULULBBT self)

        Tell the container to try
        to minimize its memory usage for storage of the current number of
        elements. This is NOT guaranteed to decrease memory usage. 
        """
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_Squeeze(self)


    def Initialize(self) -> "void":
        """
        Initialize(itkMapContainerULQEMPF3GQEULULBBT self)

        Tell the container to
        release any memory it may have allocated and return itself to its
        initial state. 
        """
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_Initialize(self)

    __swig_destroy__ = _itkQuadEdgeCellTraitsInfoPython.delete_itkMapContainerULQEMPF3GQEULULBBT

    def cast(obj: 'itkLightObject') -> "itkMapContainerULQEMPF3GQEULULBBT *":
        """cast(itkLightObject obj) -> itkMapContainerULQEMPF3GQEULULBBT"""
        return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkMapContainerULQEMPF3GQEULULBBT

        Create a new object of the class itkMapContainerULQEMPF3GQEULULBBT and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMapContainerULQEMPF3GQEULULBBT.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMapContainerULQEMPF3GQEULULBBT.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMapContainerULQEMPF3GQEULULBBT.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMapContainerULQEMPF3GQEULULBBT.Clone = new_instancemethod(_itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_Clone, None, itkMapContainerULQEMPF3GQEULULBBT)
itkMapContainerULQEMPF3GQEULULBBT.CastToSTLContainer = new_instancemethod(_itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_CastToSTLContainer, None, itkMapContainerULQEMPF3GQEULULBBT)
itkMapContainerULQEMPF3GQEULULBBT.CastToSTLConstContainer = new_instancemethod(_itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_CastToSTLConstContainer, None, itkMapContainerULQEMPF3GQEULULBBT)
itkMapContainerULQEMPF3GQEULULBBT.ElementAt = new_instancemethod(_itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_ElementAt, None, itkMapContainerULQEMPF3GQEULULBBT)
itkMapContainerULQEMPF3GQEULULBBT.CreateElementAt = new_instancemethod(_itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_CreateElementAt, None, itkMapContainerULQEMPF3GQEULULBBT)
itkMapContainerULQEMPF3GQEULULBBT.GetElement = new_instancemethod(_itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_GetElement, None, itkMapContainerULQEMPF3GQEULULBBT)
itkMapContainerULQEMPF3GQEULULBBT.SetElement = new_instancemethod(_itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_SetElement, None, itkMapContainerULQEMPF3GQEULULBBT)
itkMapContainerULQEMPF3GQEULULBBT.InsertElement = new_instancemethod(_itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_InsertElement, None, itkMapContainerULQEMPF3GQEULULBBT)
itkMapContainerULQEMPF3GQEULULBBT.IndexExists = new_instancemethod(_itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_IndexExists, None, itkMapContainerULQEMPF3GQEULULBBT)
itkMapContainerULQEMPF3GQEULULBBT.GetElementIfIndexExists = new_instancemethod(_itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_GetElementIfIndexExists, None, itkMapContainerULQEMPF3GQEULULBBT)
itkMapContainerULQEMPF3GQEULULBBT.CreateIndex = new_instancemethod(_itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_CreateIndex, None, itkMapContainerULQEMPF3GQEULULBBT)
itkMapContainerULQEMPF3GQEULULBBT.DeleteIndex = new_instancemethod(_itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_DeleteIndex, None, itkMapContainerULQEMPF3GQEULULBBT)
itkMapContainerULQEMPF3GQEULULBBT.Size = new_instancemethod(_itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_Size, None, itkMapContainerULQEMPF3GQEULULBBT)
itkMapContainerULQEMPF3GQEULULBBT.Reserve = new_instancemethod(_itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_Reserve, None, itkMapContainerULQEMPF3GQEULULBBT)
itkMapContainerULQEMPF3GQEULULBBT.Squeeze = new_instancemethod(_itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_Squeeze, None, itkMapContainerULQEMPF3GQEULULBBT)
itkMapContainerULQEMPF3GQEULULBBT.Initialize = new_instancemethod(_itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_Initialize, None, itkMapContainerULQEMPF3GQEULULBBT)
itkMapContainerULQEMPF3GQEULULBBT_swigregister = _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_swigregister
itkMapContainerULQEMPF3GQEULULBBT_swigregister(itkMapContainerULQEMPF3GQEULULBBT)

def itkMapContainerULQEMPF3GQEULULBBT___New_orig__() -> "itkMapContainerULQEMPF3GQEULULBBT_Pointer":
    """itkMapContainerULQEMPF3GQEULULBBT___New_orig__() -> itkMapContainerULQEMPF3GQEULULBBT_Pointer"""
    return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT___New_orig__()

def itkMapContainerULQEMPF3GQEULULBBT_cast(obj: 'itkLightObject') -> "itkMapContainerULQEMPF3GQEULULBBT *":
    """itkMapContainerULQEMPF3GQEULULBBT_cast(itkLightObject obj) -> itkMapContainerULQEMPF3GQEULULBBT"""
    return _itkQuadEdgeCellTraitsInfoPython.itkMapContainerULQEMPF3GQEULULBBT_cast(obj)

class itkQuadEdgeMeshCellTraitsInfo2FFULULUCQEMPGQEULQEMPF2GQEULULBBTGQE(object):
    """Proxy of C++ itkQuadEdgeMeshCellTraitsInfo2FFULULUCQEMPGQEULQEMPF2GQEULULBBTGQE class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkQuadEdgeMeshCellTraitsInfo2FFULULUCQEMPGQEULQEMPF2GQEULULBBTGQE self) -> itkQuadEdgeMeshCellTraitsInfo2FFULULUCQEMPGQEULQEMPF2GQEULULBBTGQE
        __init__(itkQuadEdgeMeshCellTraitsInfo2FFULULUCQEMPGQEULQEMPF2GQEULULBBTGQE self, itkQuadEdgeMeshCellTraitsInfo2FFULULUCQEMPGQEULQEMPF2GQEULULBBTGQE arg0) -> itkQuadEdgeMeshCellTraitsInfo2FFULULUCQEMPGQEULQEMPF2GQEULULBBTGQE
        """
        _itkQuadEdgeCellTraitsInfoPython.itkQuadEdgeMeshCellTraitsInfo2FFULULUCQEMPGQEULQEMPF2GQEULULBBTGQE_swiginit(self, _itkQuadEdgeCellTraitsInfoPython.new_itkQuadEdgeMeshCellTraitsInfo2FFULULUCQEMPGQEULQEMPF2GQEULULBBTGQE(*args))
    __swig_destroy__ = _itkQuadEdgeCellTraitsInfoPython.delete_itkQuadEdgeMeshCellTraitsInfo2FFULULUCQEMPGQEULQEMPF2GQEULULBBTGQE
itkQuadEdgeMeshCellTraitsInfo2FFULULUCQEMPGQEULQEMPF2GQEULULBBTGQE_swigregister = _itkQuadEdgeCellTraitsInfoPython.itkQuadEdgeMeshCellTraitsInfo2FFULULUCQEMPGQEULQEMPF2GQEULULBBTGQE_swigregister
itkQuadEdgeMeshCellTraitsInfo2FFULULUCQEMPGQEULQEMPF2GQEULULBBTGQE_swigregister(itkQuadEdgeMeshCellTraitsInfo2FFULULUCQEMPGQEULQEMPF2GQEULULBBTGQE)

class itkQuadEdgeMeshCellTraitsInfo3FFULULUCQEMPGQEULQEMPF3GQEULULBBTGQE(object):
    """Proxy of C++ itkQuadEdgeMeshCellTraitsInfo3FFULULUCQEMPGQEULQEMPF3GQEULULBBTGQE class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(itkQuadEdgeMeshCellTraitsInfo3FFULULUCQEMPGQEULQEMPF3GQEULULBBTGQE self) -> itkQuadEdgeMeshCellTraitsInfo3FFULULUCQEMPGQEULQEMPF3GQEULULBBTGQE
        __init__(itkQuadEdgeMeshCellTraitsInfo3FFULULUCQEMPGQEULQEMPF3GQEULULBBTGQE self, itkQuadEdgeMeshCellTraitsInfo3FFULULUCQEMPGQEULQEMPF3GQEULULBBTGQE arg0) -> itkQuadEdgeMeshCellTraitsInfo3FFULULUCQEMPGQEULQEMPF3GQEULULBBTGQE
        """
        _itkQuadEdgeCellTraitsInfoPython.itkQuadEdgeMeshCellTraitsInfo3FFULULUCQEMPGQEULQEMPF3GQEULULBBTGQE_swiginit(self, _itkQuadEdgeCellTraitsInfoPython.new_itkQuadEdgeMeshCellTraitsInfo3FFULULUCQEMPGQEULQEMPF3GQEULULBBTGQE(*args))
    __swig_destroy__ = _itkQuadEdgeCellTraitsInfoPython.delete_itkQuadEdgeMeshCellTraitsInfo3FFULULUCQEMPGQEULQEMPF3GQEULULBBTGQE
itkQuadEdgeMeshCellTraitsInfo3FFULULUCQEMPGQEULQEMPF3GQEULULBBTGQE_swigregister = _itkQuadEdgeCellTraitsInfoPython.itkQuadEdgeMeshCellTraitsInfo3FFULULUCQEMPGQEULQEMPF3GQEULULBBTGQE_swigregister
itkQuadEdgeMeshCellTraitsInfo3FFULULUCQEMPGQEULQEMPF3GQEULULBBTGQE_swigregister(itkQuadEdgeMeshCellTraitsInfo3FFULULUCQEMPGQEULQEMPF3GQEULULBBTGQE)



