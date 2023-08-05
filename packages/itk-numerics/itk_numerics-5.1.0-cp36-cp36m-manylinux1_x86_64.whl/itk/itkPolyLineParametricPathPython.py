# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkPolyLineParametricPathPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkPolyLineParametricPathPython', [dirname(__file__)])
        except ImportError:
            import _itkPolyLineParametricPathPython
            return _itkPolyLineParametricPathPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkPolyLineParametricPathPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkPolyLineParametricPathPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkPolyLineParametricPathPython
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


import itkContinuousIndexPython
import itkIndexPython
import itkSizePython
import pyBasePython
import itkOffsetPython
import itkPointPython
import vnl_vector_refPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import itkVectorPython
import itkFixedArrayPython
import ITKCommonBasePython
import itkParametricPathPython
import itkPathBasePython
import itkVectorContainerPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython

def itkPolyLineParametricPath3_New():
  return itkPolyLineParametricPath3.New()


def itkPolyLineParametricPath2_New():
  return itkPolyLineParametricPath2.New()

class itkPolyLineParametricPath2(itkParametricPathPython.itkParametricPath2):
    """


    Represent a path of line segments through ND Space.

    This class is intended to represent parametric paths through an image,
    where the paths are composed of line segments. Each line segment
    traverses one unit of input. A classic application of this class is
    the representation of contours in 2D images, especially when the
    contours only need to be approximately correct. Another use of a path
    is to guide the movement of an iterator through an image.

    See:  EllipseParametricPath

    See:  FourierSeriesPath

    See:  OrthogonallyCorrectedParametricPath

    See:   ParametricPath

    See:  ChainCodePath

    See:   Path

    See:  ContinuousIndex

    See:  Index

    See:  Offset

    See:  Vector

    C++ includes: itkPolyLineParametricPath.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def AddVertex(self, vertex: 'itkContinuousIndexD2') -> "void":
        """
        AddVertex(itkPolyLineParametricPath2 self, itkContinuousIndexD2 vertex)

        Evaluate the first
        derivative of the ND output with respect to the 1D input. This is an
        exact, algebraic function. Add a vertex (and a connecting line segment
        to the previous vertex). Adding a vertex has the additional effect of
        extending the domain of the PolyLineParametricPath by 1.0 (each pair
        of consecutive vertices is separated by one unit of input). 
        """
        return _itkPolyLineParametricPathPython.itkPolyLineParametricPath2_AddVertex(self, vertex)


    def __New_orig__() -> "itkPolyLineParametricPath2_Pointer":
        """__New_orig__() -> itkPolyLineParametricPath2_Pointer"""
        return _itkPolyLineParametricPathPython.itkPolyLineParametricPath2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkPolyLineParametricPath2_Pointer":
        """Clone(itkPolyLineParametricPath2 self) -> itkPolyLineParametricPath2_Pointer"""
        return _itkPolyLineParametricPathPython.itkPolyLineParametricPath2_Clone(self)


    def GetModifiableVertexList(self) -> "itkVectorContainerUICID2 *":
        """GetModifiableVertexList(itkPolyLineParametricPath2 self) -> itkVectorContainerUICID2"""
        return _itkPolyLineParametricPathPython.itkPolyLineParametricPath2_GetModifiableVertexList(self)


    def GetVertexList(self, *args) -> "itkVectorContainerUICID2 *":
        """
        GetVertexList(itkPolyLineParametricPath2 self) -> itkVectorContainerUICID2
        GetVertexList(itkPolyLineParametricPath2 self) -> itkVectorContainerUICID2
        """
        return _itkPolyLineParametricPathPython.itkPolyLineParametricPath2_GetVertexList(self, *args)

    __swig_destroy__ = _itkPolyLineParametricPathPython.delete_itkPolyLineParametricPath2

    def cast(obj: 'itkLightObject') -> "itkPolyLineParametricPath2 *":
        """cast(itkLightObject obj) -> itkPolyLineParametricPath2"""
        return _itkPolyLineParametricPathPython.itkPolyLineParametricPath2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkPolyLineParametricPath2

        Create a new object of the class itkPolyLineParametricPath2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPolyLineParametricPath2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkPolyLineParametricPath2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkPolyLineParametricPath2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkPolyLineParametricPath2.AddVertex = new_instancemethod(_itkPolyLineParametricPathPython.itkPolyLineParametricPath2_AddVertex, None, itkPolyLineParametricPath2)
itkPolyLineParametricPath2.Clone = new_instancemethod(_itkPolyLineParametricPathPython.itkPolyLineParametricPath2_Clone, None, itkPolyLineParametricPath2)
itkPolyLineParametricPath2.GetModifiableVertexList = new_instancemethod(_itkPolyLineParametricPathPython.itkPolyLineParametricPath2_GetModifiableVertexList, None, itkPolyLineParametricPath2)
itkPolyLineParametricPath2.GetVertexList = new_instancemethod(_itkPolyLineParametricPathPython.itkPolyLineParametricPath2_GetVertexList, None, itkPolyLineParametricPath2)
itkPolyLineParametricPath2_swigregister = _itkPolyLineParametricPathPython.itkPolyLineParametricPath2_swigregister
itkPolyLineParametricPath2_swigregister(itkPolyLineParametricPath2)

def itkPolyLineParametricPath2___New_orig__() -> "itkPolyLineParametricPath2_Pointer":
    """itkPolyLineParametricPath2___New_orig__() -> itkPolyLineParametricPath2_Pointer"""
    return _itkPolyLineParametricPathPython.itkPolyLineParametricPath2___New_orig__()

def itkPolyLineParametricPath2_cast(obj: 'itkLightObject') -> "itkPolyLineParametricPath2 *":
    """itkPolyLineParametricPath2_cast(itkLightObject obj) -> itkPolyLineParametricPath2"""
    return _itkPolyLineParametricPathPython.itkPolyLineParametricPath2_cast(obj)

class itkPolyLineParametricPath3(itkParametricPathPython.itkParametricPath3):
    """


    Represent a path of line segments through ND Space.

    This class is intended to represent parametric paths through an image,
    where the paths are composed of line segments. Each line segment
    traverses one unit of input. A classic application of this class is
    the representation of contours in 2D images, especially when the
    contours only need to be approximately correct. Another use of a path
    is to guide the movement of an iterator through an image.

    See:  EllipseParametricPath

    See:  FourierSeriesPath

    See:  OrthogonallyCorrectedParametricPath

    See:   ParametricPath

    See:  ChainCodePath

    See:   Path

    See:  ContinuousIndex

    See:  Index

    See:  Offset

    See:  Vector

    C++ includes: itkPolyLineParametricPath.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def AddVertex(self, vertex: 'itkContinuousIndexD3') -> "void":
        """
        AddVertex(itkPolyLineParametricPath3 self, itkContinuousIndexD3 vertex)

        Evaluate the first
        derivative of the ND output with respect to the 1D input. This is an
        exact, algebraic function. Add a vertex (and a connecting line segment
        to the previous vertex). Adding a vertex has the additional effect of
        extending the domain of the PolyLineParametricPath by 1.0 (each pair
        of consecutive vertices is separated by one unit of input). 
        """
        return _itkPolyLineParametricPathPython.itkPolyLineParametricPath3_AddVertex(self, vertex)


    def __New_orig__() -> "itkPolyLineParametricPath3_Pointer":
        """__New_orig__() -> itkPolyLineParametricPath3_Pointer"""
        return _itkPolyLineParametricPathPython.itkPolyLineParametricPath3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkPolyLineParametricPath3_Pointer":
        """Clone(itkPolyLineParametricPath3 self) -> itkPolyLineParametricPath3_Pointer"""
        return _itkPolyLineParametricPathPython.itkPolyLineParametricPath3_Clone(self)


    def GetModifiableVertexList(self) -> "itkVectorContainerUICID3 *":
        """GetModifiableVertexList(itkPolyLineParametricPath3 self) -> itkVectorContainerUICID3"""
        return _itkPolyLineParametricPathPython.itkPolyLineParametricPath3_GetModifiableVertexList(self)


    def GetVertexList(self, *args) -> "itkVectorContainerUICID3 *":
        """
        GetVertexList(itkPolyLineParametricPath3 self) -> itkVectorContainerUICID3
        GetVertexList(itkPolyLineParametricPath3 self) -> itkVectorContainerUICID3
        """
        return _itkPolyLineParametricPathPython.itkPolyLineParametricPath3_GetVertexList(self, *args)

    __swig_destroy__ = _itkPolyLineParametricPathPython.delete_itkPolyLineParametricPath3

    def cast(obj: 'itkLightObject') -> "itkPolyLineParametricPath3 *":
        """cast(itkLightObject obj) -> itkPolyLineParametricPath3"""
        return _itkPolyLineParametricPathPython.itkPolyLineParametricPath3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkPolyLineParametricPath3

        Create a new object of the class itkPolyLineParametricPath3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPolyLineParametricPath3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkPolyLineParametricPath3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkPolyLineParametricPath3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkPolyLineParametricPath3.AddVertex = new_instancemethod(_itkPolyLineParametricPathPython.itkPolyLineParametricPath3_AddVertex, None, itkPolyLineParametricPath3)
itkPolyLineParametricPath3.Clone = new_instancemethod(_itkPolyLineParametricPathPython.itkPolyLineParametricPath3_Clone, None, itkPolyLineParametricPath3)
itkPolyLineParametricPath3.GetModifiableVertexList = new_instancemethod(_itkPolyLineParametricPathPython.itkPolyLineParametricPath3_GetModifiableVertexList, None, itkPolyLineParametricPath3)
itkPolyLineParametricPath3.GetVertexList = new_instancemethod(_itkPolyLineParametricPathPython.itkPolyLineParametricPath3_GetVertexList, None, itkPolyLineParametricPath3)
itkPolyLineParametricPath3_swigregister = _itkPolyLineParametricPathPython.itkPolyLineParametricPath3_swigregister
itkPolyLineParametricPath3_swigregister(itkPolyLineParametricPath3)

def itkPolyLineParametricPath3___New_orig__() -> "itkPolyLineParametricPath3_Pointer":
    """itkPolyLineParametricPath3___New_orig__() -> itkPolyLineParametricPath3_Pointer"""
    return _itkPolyLineParametricPathPython.itkPolyLineParametricPath3___New_orig__()

def itkPolyLineParametricPath3_cast(obj: 'itkLightObject') -> "itkPolyLineParametricPath3 *":
    """itkPolyLineParametricPath3_cast(itkLightObject obj) -> itkPolyLineParametricPath3"""
    return _itkPolyLineParametricPathPython.itkPolyLineParametricPath3_cast(obj)



