# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkPathBasePython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkPathBasePython', [dirname(__file__)])
        except ImportError:
            import _itkPathBasePython
            return _itkPathBasePython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkPathBasePython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkPathBasePython = swig_import_helper()
    del swig_import_helper
else:
    import _itkPathBasePython
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
import itkPointPython
import itkFixedArrayPython
import pyBasePython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkVectorPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import ITKCommonBasePython

def itkPathDCID33_New():
  return itkPathDCID33.New()


def itkPathDCID22_New():
  return itkPathDCID22.New()

class itkPathDCID22(ITKCommonBasePython.itkDataObject):
    """


    Represent a path through ND Space.

    This base class is intended to represent a path through an image. As a
    path, it maps a 1D parameter (such as time or arc length, etc) to an
    index (or possibly an offset or a point) in ND space. This mapping is
    done via the abstract Evaluate() method, which must be overridden in
    all instantiable subclasses. The only geometric requirement for a
    gerneral path is that it be continuous. A path may be open or closed,
    and may cross itself several times. A classic application of this
    class is the representation of contours in 2D images using chaincodes
    or freeman codes. Another use of a path is to guide the movement of an
    iterator through an image.

    Parameters:
    -----------

    TInput:  Type of the 1D parameter of the path, e.g. unsigned int or
    double.

    TOutput:  Type of the path location at the given input, e.g.
    itk::Offset< VDimension > or itk::ContinuousIndex< VDimension >

    VDimension:  Dimension of the path.

    See:  Index

    See:  Point

    See:  ContinuousIndex

    C++ includes: itkPath.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def StartOfInput(self) -> "double":
        """
        StartOfInput(itkPathDCID22 self) -> double

        Where does the path
        begin? For most types of paths, the path will begin at zero. This
        value can be overridden in children, and is necessary for iterators to
        know how to go to the beginning of a path. 
        """
        return _itkPathBasePython.itkPathDCID22_StartOfInput(self)


    def EndOfInput(self) -> "double":
        """
        EndOfInput(itkPathDCID22 self) -> double

        Where does the path end
        (what is the last valid input value)? This value is sometimes used by
        IncrementInput() to go to the end of a path. 
        """
        return _itkPathBasePython.itkPathDCID22_EndOfInput(self)


    def Evaluate(self, input: 'double const &') -> "itkContinuousIndexD2":
        """
        Evaluate(itkPathDCID22 self, double const & input) -> itkContinuousIndexD2

        Evaluate the path at
        specified location along the path. Return data is the path's
        "natural" format. 
        """
        return _itkPathBasePython.itkPathDCID22_Evaluate(self, input)


    def EvaluateToIndex(self, input: 'double const &') -> "itkIndex2":
        """
        EvaluateToIndex(itkPathDCID22 self, double const & input) -> itkIndex2

        Like Evaluate(),
        except always returns an index 
        """
        return _itkPathBasePython.itkPathDCID22_EvaluateToIndex(self, input)


    def IncrementInput(self, input: 'double &') -> "itkOffset2":
        """
        IncrementInput(itkPathDCID22 self, double & input) -> itkOffset2

        Increment the input
        variable passed by reference such that the ND index of the path moves
        to its next vertex-connected (8-connected in 2D) neighbor. Return the
        Index-space offset of the path from its prior input to its new input.
        If the path is unable to increment, input is not changed and an offset
        of Zero is returned. Children are not required to implement general
        bounds checking, but are required to return an offset of zero when
        trying to increment from the final valid input value. 
        """
        return _itkPathBasePython.itkPathDCID22_IncrementInput(self, input)

    __swig_destroy__ = _itkPathBasePython.delete_itkPathDCID22

    def cast(obj: 'itkLightObject') -> "itkPathDCID22 *":
        """cast(itkLightObject obj) -> itkPathDCID22"""
        return _itkPathBasePython.itkPathDCID22_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkPathDCID22

        Create a new object of the class itkPathDCID22 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPathDCID22.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkPathDCID22.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkPathDCID22.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkPathDCID22.StartOfInput = new_instancemethod(_itkPathBasePython.itkPathDCID22_StartOfInput, None, itkPathDCID22)
itkPathDCID22.EndOfInput = new_instancemethod(_itkPathBasePython.itkPathDCID22_EndOfInput, None, itkPathDCID22)
itkPathDCID22.Evaluate = new_instancemethod(_itkPathBasePython.itkPathDCID22_Evaluate, None, itkPathDCID22)
itkPathDCID22.EvaluateToIndex = new_instancemethod(_itkPathBasePython.itkPathDCID22_EvaluateToIndex, None, itkPathDCID22)
itkPathDCID22.IncrementInput = new_instancemethod(_itkPathBasePython.itkPathDCID22_IncrementInput, None, itkPathDCID22)
itkPathDCID22_swigregister = _itkPathBasePython.itkPathDCID22_swigregister
itkPathDCID22_swigregister(itkPathDCID22)

def itkPathDCID22_cast(obj: 'itkLightObject') -> "itkPathDCID22 *":
    """itkPathDCID22_cast(itkLightObject obj) -> itkPathDCID22"""
    return _itkPathBasePython.itkPathDCID22_cast(obj)

class itkPathDCID33(ITKCommonBasePython.itkDataObject):
    """


    Represent a path through ND Space.

    This base class is intended to represent a path through an image. As a
    path, it maps a 1D parameter (such as time or arc length, etc) to an
    index (or possibly an offset or a point) in ND space. This mapping is
    done via the abstract Evaluate() method, which must be overridden in
    all instantiable subclasses. The only geometric requirement for a
    gerneral path is that it be continuous. A path may be open or closed,
    and may cross itself several times. A classic application of this
    class is the representation of contours in 2D images using chaincodes
    or freeman codes. Another use of a path is to guide the movement of an
    iterator through an image.

    Parameters:
    -----------

    TInput:  Type of the 1D parameter of the path, e.g. unsigned int or
    double.

    TOutput:  Type of the path location at the given input, e.g.
    itk::Offset< VDimension > or itk::ContinuousIndex< VDimension >

    VDimension:  Dimension of the path.

    See:  Index

    See:  Point

    See:  ContinuousIndex

    C++ includes: itkPath.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def StartOfInput(self) -> "double":
        """
        StartOfInput(itkPathDCID33 self) -> double

        Where does the path
        begin? For most types of paths, the path will begin at zero. This
        value can be overridden in children, and is necessary for iterators to
        know how to go to the beginning of a path. 
        """
        return _itkPathBasePython.itkPathDCID33_StartOfInput(self)


    def EndOfInput(self) -> "double":
        """
        EndOfInput(itkPathDCID33 self) -> double

        Where does the path end
        (what is the last valid input value)? This value is sometimes used by
        IncrementInput() to go to the end of a path. 
        """
        return _itkPathBasePython.itkPathDCID33_EndOfInput(self)


    def Evaluate(self, input: 'double const &') -> "itkContinuousIndexD3":
        """
        Evaluate(itkPathDCID33 self, double const & input) -> itkContinuousIndexD3

        Evaluate the path at
        specified location along the path. Return data is the path's
        "natural" format. 
        """
        return _itkPathBasePython.itkPathDCID33_Evaluate(self, input)


    def EvaluateToIndex(self, input: 'double const &') -> "itkIndex3":
        """
        EvaluateToIndex(itkPathDCID33 self, double const & input) -> itkIndex3

        Like Evaluate(),
        except always returns an index 
        """
        return _itkPathBasePython.itkPathDCID33_EvaluateToIndex(self, input)


    def IncrementInput(self, input: 'double &') -> "itkOffset3":
        """
        IncrementInput(itkPathDCID33 self, double & input) -> itkOffset3

        Increment the input
        variable passed by reference such that the ND index of the path moves
        to its next vertex-connected (8-connected in 2D) neighbor. Return the
        Index-space offset of the path from its prior input to its new input.
        If the path is unable to increment, input is not changed and an offset
        of Zero is returned. Children are not required to implement general
        bounds checking, but are required to return an offset of zero when
        trying to increment from the final valid input value. 
        """
        return _itkPathBasePython.itkPathDCID33_IncrementInput(self, input)

    __swig_destroy__ = _itkPathBasePython.delete_itkPathDCID33

    def cast(obj: 'itkLightObject') -> "itkPathDCID33 *":
        """cast(itkLightObject obj) -> itkPathDCID33"""
        return _itkPathBasePython.itkPathDCID33_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkPathDCID33

        Create a new object of the class itkPathDCID33 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPathDCID33.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkPathDCID33.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkPathDCID33.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkPathDCID33.StartOfInput = new_instancemethod(_itkPathBasePython.itkPathDCID33_StartOfInput, None, itkPathDCID33)
itkPathDCID33.EndOfInput = new_instancemethod(_itkPathBasePython.itkPathDCID33_EndOfInput, None, itkPathDCID33)
itkPathDCID33.Evaluate = new_instancemethod(_itkPathBasePython.itkPathDCID33_Evaluate, None, itkPathDCID33)
itkPathDCID33.EvaluateToIndex = new_instancemethod(_itkPathBasePython.itkPathDCID33_EvaluateToIndex, None, itkPathDCID33)
itkPathDCID33.IncrementInput = new_instancemethod(_itkPathBasePython.itkPathDCID33_IncrementInput, None, itkPathDCID33)
itkPathDCID33_swigregister = _itkPathBasePython.itkPathDCID33_swigregister
itkPathDCID33_swigregister(itkPathDCID33)

def itkPathDCID33_cast(obj: 'itkLightObject') -> "itkPathDCID33 *":
    """itkPathDCID33_cast(itkLightObject obj) -> itkPathDCID33"""
    return _itkPathBasePython.itkPathDCID33_cast(obj)



