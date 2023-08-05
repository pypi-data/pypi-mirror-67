# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkExpImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkExpImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkExpImageFilterPython
            return _itkExpImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkExpImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkExpImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkExpImageFilterPython
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


import itkUnaryGeneratorImageFilterPython
import itkInPlaceImageFilterBPython
import ITKCommonBasePython
import pyBasePython
import itkImageToImageFilterBPython
import itkImageSourcePython
import itkImagePython
import itkCovariantVectorPython
import itkVectorPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkRGBPixelPython
import itkPointPython
import itkOffsetPython
import itkSizePython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkIndexPython
import itkRGBAPixelPython
import itkSymmetricSecondRankTensorPython
import itkImageRegionPython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterAPython

def itkExpImageFilterID3ID3_New():
  return itkExpImageFilterID3ID3.New()


def itkExpImageFilterID2ID2_New():
  return itkExpImageFilterID2ID2.New()


def itkExpImageFilterIF3IF3_New():
  return itkExpImageFilterIF3IF3.New()


def itkExpImageFilterIF2IF2_New():
  return itkExpImageFilterIF2IF2.New()


def itkExpImageFilterIUS3IUS3_New():
  return itkExpImageFilterIUS3IUS3.New()


def itkExpImageFilterIUS2IUS2_New():
  return itkExpImageFilterIUS2IUS2.New()


def itkExpImageFilterIUC3IUC3_New():
  return itkExpImageFilterIUC3IUC3.New()


def itkExpImageFilterIUC2IUC2_New():
  return itkExpImageFilterIUC2IUC2.New()


def itkExpImageFilterISS3ISS3_New():
  return itkExpImageFilterISS3ISS3.New()


def itkExpImageFilterISS2ISS2_New():
  return itkExpImageFilterISS2ISS2.New()

class itkExpImageFilterID2ID2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID2ID2):
    """


    Computes the exponential function of each pixel.

    The computation is performed using std::exp(x).

    C++ includes: itkExpImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkExpImageFilterID2ID2_Pointer":
        """__New_orig__() -> itkExpImageFilterID2ID2_Pointer"""
        return _itkExpImageFilterPython.itkExpImageFilterID2ID2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkExpImageFilterID2ID2_Pointer":
        """Clone(itkExpImageFilterID2ID2 self) -> itkExpImageFilterID2ID2_Pointer"""
        return _itkExpImageFilterPython.itkExpImageFilterID2ID2_Clone(self)

    InputConvertibleToDoubleCheck = _itkExpImageFilterPython.itkExpImageFilterID2ID2_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkExpImageFilterPython.itkExpImageFilterID2ID2_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkExpImageFilterPython.delete_itkExpImageFilterID2ID2

    def cast(obj: 'itkLightObject') -> "itkExpImageFilterID2ID2 *":
        """cast(itkLightObject obj) -> itkExpImageFilterID2ID2"""
        return _itkExpImageFilterPython.itkExpImageFilterID2ID2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkExpImageFilterID2ID2

        Create a new object of the class itkExpImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExpImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkExpImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkExpImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkExpImageFilterID2ID2.Clone = new_instancemethod(_itkExpImageFilterPython.itkExpImageFilterID2ID2_Clone, None, itkExpImageFilterID2ID2)
itkExpImageFilterID2ID2_swigregister = _itkExpImageFilterPython.itkExpImageFilterID2ID2_swigregister
itkExpImageFilterID2ID2_swigregister(itkExpImageFilterID2ID2)

def itkExpImageFilterID2ID2___New_orig__() -> "itkExpImageFilterID2ID2_Pointer":
    """itkExpImageFilterID2ID2___New_orig__() -> itkExpImageFilterID2ID2_Pointer"""
    return _itkExpImageFilterPython.itkExpImageFilterID2ID2___New_orig__()

def itkExpImageFilterID2ID2_cast(obj: 'itkLightObject') -> "itkExpImageFilterID2ID2 *":
    """itkExpImageFilterID2ID2_cast(itkLightObject obj) -> itkExpImageFilterID2ID2"""
    return _itkExpImageFilterPython.itkExpImageFilterID2ID2_cast(obj)

class itkExpImageFilterID3ID3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID3ID3):
    """


    Computes the exponential function of each pixel.

    The computation is performed using std::exp(x).

    C++ includes: itkExpImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkExpImageFilterID3ID3_Pointer":
        """__New_orig__() -> itkExpImageFilterID3ID3_Pointer"""
        return _itkExpImageFilterPython.itkExpImageFilterID3ID3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkExpImageFilterID3ID3_Pointer":
        """Clone(itkExpImageFilterID3ID3 self) -> itkExpImageFilterID3ID3_Pointer"""
        return _itkExpImageFilterPython.itkExpImageFilterID3ID3_Clone(self)

    InputConvertibleToDoubleCheck = _itkExpImageFilterPython.itkExpImageFilterID3ID3_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkExpImageFilterPython.itkExpImageFilterID3ID3_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkExpImageFilterPython.delete_itkExpImageFilterID3ID3

    def cast(obj: 'itkLightObject') -> "itkExpImageFilterID3ID3 *":
        """cast(itkLightObject obj) -> itkExpImageFilterID3ID3"""
        return _itkExpImageFilterPython.itkExpImageFilterID3ID3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkExpImageFilterID3ID3

        Create a new object of the class itkExpImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExpImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkExpImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkExpImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkExpImageFilterID3ID3.Clone = new_instancemethod(_itkExpImageFilterPython.itkExpImageFilterID3ID3_Clone, None, itkExpImageFilterID3ID3)
itkExpImageFilterID3ID3_swigregister = _itkExpImageFilterPython.itkExpImageFilterID3ID3_swigregister
itkExpImageFilterID3ID3_swigregister(itkExpImageFilterID3ID3)

def itkExpImageFilterID3ID3___New_orig__() -> "itkExpImageFilterID3ID3_Pointer":
    """itkExpImageFilterID3ID3___New_orig__() -> itkExpImageFilterID3ID3_Pointer"""
    return _itkExpImageFilterPython.itkExpImageFilterID3ID3___New_orig__()

def itkExpImageFilterID3ID3_cast(obj: 'itkLightObject') -> "itkExpImageFilterID3ID3 *":
    """itkExpImageFilterID3ID3_cast(itkLightObject obj) -> itkExpImageFilterID3ID3"""
    return _itkExpImageFilterPython.itkExpImageFilterID3ID3_cast(obj)

class itkExpImageFilterIF2IF2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF2IF2):
    """


    Computes the exponential function of each pixel.

    The computation is performed using std::exp(x).

    C++ includes: itkExpImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkExpImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkExpImageFilterIF2IF2_Pointer"""
        return _itkExpImageFilterPython.itkExpImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkExpImageFilterIF2IF2_Pointer":
        """Clone(itkExpImageFilterIF2IF2 self) -> itkExpImageFilterIF2IF2_Pointer"""
        return _itkExpImageFilterPython.itkExpImageFilterIF2IF2_Clone(self)

    InputConvertibleToDoubleCheck = _itkExpImageFilterPython.itkExpImageFilterIF2IF2_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkExpImageFilterPython.itkExpImageFilterIF2IF2_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkExpImageFilterPython.delete_itkExpImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkExpImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkExpImageFilterIF2IF2"""
        return _itkExpImageFilterPython.itkExpImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkExpImageFilterIF2IF2

        Create a new object of the class itkExpImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExpImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkExpImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkExpImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkExpImageFilterIF2IF2.Clone = new_instancemethod(_itkExpImageFilterPython.itkExpImageFilterIF2IF2_Clone, None, itkExpImageFilterIF2IF2)
itkExpImageFilterIF2IF2_swigregister = _itkExpImageFilterPython.itkExpImageFilterIF2IF2_swigregister
itkExpImageFilterIF2IF2_swigregister(itkExpImageFilterIF2IF2)

def itkExpImageFilterIF2IF2___New_orig__() -> "itkExpImageFilterIF2IF2_Pointer":
    """itkExpImageFilterIF2IF2___New_orig__() -> itkExpImageFilterIF2IF2_Pointer"""
    return _itkExpImageFilterPython.itkExpImageFilterIF2IF2___New_orig__()

def itkExpImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkExpImageFilterIF2IF2 *":
    """itkExpImageFilterIF2IF2_cast(itkLightObject obj) -> itkExpImageFilterIF2IF2"""
    return _itkExpImageFilterPython.itkExpImageFilterIF2IF2_cast(obj)

class itkExpImageFilterIF3IF3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF3IF3):
    """


    Computes the exponential function of each pixel.

    The computation is performed using std::exp(x).

    C++ includes: itkExpImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkExpImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkExpImageFilterIF3IF3_Pointer"""
        return _itkExpImageFilterPython.itkExpImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkExpImageFilterIF3IF3_Pointer":
        """Clone(itkExpImageFilterIF3IF3 self) -> itkExpImageFilterIF3IF3_Pointer"""
        return _itkExpImageFilterPython.itkExpImageFilterIF3IF3_Clone(self)

    InputConvertibleToDoubleCheck = _itkExpImageFilterPython.itkExpImageFilterIF3IF3_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkExpImageFilterPython.itkExpImageFilterIF3IF3_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkExpImageFilterPython.delete_itkExpImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkExpImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkExpImageFilterIF3IF3"""
        return _itkExpImageFilterPython.itkExpImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkExpImageFilterIF3IF3

        Create a new object of the class itkExpImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExpImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkExpImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkExpImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkExpImageFilterIF3IF3.Clone = new_instancemethod(_itkExpImageFilterPython.itkExpImageFilterIF3IF3_Clone, None, itkExpImageFilterIF3IF3)
itkExpImageFilterIF3IF3_swigregister = _itkExpImageFilterPython.itkExpImageFilterIF3IF3_swigregister
itkExpImageFilterIF3IF3_swigregister(itkExpImageFilterIF3IF3)

def itkExpImageFilterIF3IF3___New_orig__() -> "itkExpImageFilterIF3IF3_Pointer":
    """itkExpImageFilterIF3IF3___New_orig__() -> itkExpImageFilterIF3IF3_Pointer"""
    return _itkExpImageFilterPython.itkExpImageFilterIF3IF3___New_orig__()

def itkExpImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkExpImageFilterIF3IF3 *":
    """itkExpImageFilterIF3IF3_cast(itkLightObject obj) -> itkExpImageFilterIF3IF3"""
    return _itkExpImageFilterPython.itkExpImageFilterIF3IF3_cast(obj)

class itkExpImageFilterISS2ISS2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterISS2ISS2):
    """


    Computes the exponential function of each pixel.

    The computation is performed using std::exp(x).

    C++ includes: itkExpImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkExpImageFilterISS2ISS2_Pointer":
        """__New_orig__() -> itkExpImageFilterISS2ISS2_Pointer"""
        return _itkExpImageFilterPython.itkExpImageFilterISS2ISS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkExpImageFilterISS2ISS2_Pointer":
        """Clone(itkExpImageFilterISS2ISS2 self) -> itkExpImageFilterISS2ISS2_Pointer"""
        return _itkExpImageFilterPython.itkExpImageFilterISS2ISS2_Clone(self)

    InputConvertibleToDoubleCheck = _itkExpImageFilterPython.itkExpImageFilterISS2ISS2_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkExpImageFilterPython.itkExpImageFilterISS2ISS2_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkExpImageFilterPython.delete_itkExpImageFilterISS2ISS2

    def cast(obj: 'itkLightObject') -> "itkExpImageFilterISS2ISS2 *":
        """cast(itkLightObject obj) -> itkExpImageFilterISS2ISS2"""
        return _itkExpImageFilterPython.itkExpImageFilterISS2ISS2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkExpImageFilterISS2ISS2

        Create a new object of the class itkExpImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExpImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkExpImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkExpImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkExpImageFilterISS2ISS2.Clone = new_instancemethod(_itkExpImageFilterPython.itkExpImageFilterISS2ISS2_Clone, None, itkExpImageFilterISS2ISS2)
itkExpImageFilterISS2ISS2_swigregister = _itkExpImageFilterPython.itkExpImageFilterISS2ISS2_swigregister
itkExpImageFilterISS2ISS2_swigregister(itkExpImageFilterISS2ISS2)

def itkExpImageFilterISS2ISS2___New_orig__() -> "itkExpImageFilterISS2ISS2_Pointer":
    """itkExpImageFilterISS2ISS2___New_orig__() -> itkExpImageFilterISS2ISS2_Pointer"""
    return _itkExpImageFilterPython.itkExpImageFilterISS2ISS2___New_orig__()

def itkExpImageFilterISS2ISS2_cast(obj: 'itkLightObject') -> "itkExpImageFilterISS2ISS2 *":
    """itkExpImageFilterISS2ISS2_cast(itkLightObject obj) -> itkExpImageFilterISS2ISS2"""
    return _itkExpImageFilterPython.itkExpImageFilterISS2ISS2_cast(obj)

class itkExpImageFilterISS3ISS3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterISS3ISS3):
    """


    Computes the exponential function of each pixel.

    The computation is performed using std::exp(x).

    C++ includes: itkExpImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkExpImageFilterISS3ISS3_Pointer":
        """__New_orig__() -> itkExpImageFilterISS3ISS3_Pointer"""
        return _itkExpImageFilterPython.itkExpImageFilterISS3ISS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkExpImageFilterISS3ISS3_Pointer":
        """Clone(itkExpImageFilterISS3ISS3 self) -> itkExpImageFilterISS3ISS3_Pointer"""
        return _itkExpImageFilterPython.itkExpImageFilterISS3ISS3_Clone(self)

    InputConvertibleToDoubleCheck = _itkExpImageFilterPython.itkExpImageFilterISS3ISS3_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkExpImageFilterPython.itkExpImageFilterISS3ISS3_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkExpImageFilterPython.delete_itkExpImageFilterISS3ISS3

    def cast(obj: 'itkLightObject') -> "itkExpImageFilterISS3ISS3 *":
        """cast(itkLightObject obj) -> itkExpImageFilterISS3ISS3"""
        return _itkExpImageFilterPython.itkExpImageFilterISS3ISS3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkExpImageFilterISS3ISS3

        Create a new object of the class itkExpImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExpImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkExpImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkExpImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkExpImageFilterISS3ISS3.Clone = new_instancemethod(_itkExpImageFilterPython.itkExpImageFilterISS3ISS3_Clone, None, itkExpImageFilterISS3ISS3)
itkExpImageFilterISS3ISS3_swigregister = _itkExpImageFilterPython.itkExpImageFilterISS3ISS3_swigregister
itkExpImageFilterISS3ISS3_swigregister(itkExpImageFilterISS3ISS3)

def itkExpImageFilterISS3ISS3___New_orig__() -> "itkExpImageFilterISS3ISS3_Pointer":
    """itkExpImageFilterISS3ISS3___New_orig__() -> itkExpImageFilterISS3ISS3_Pointer"""
    return _itkExpImageFilterPython.itkExpImageFilterISS3ISS3___New_orig__()

def itkExpImageFilterISS3ISS3_cast(obj: 'itkLightObject') -> "itkExpImageFilterISS3ISS3 *":
    """itkExpImageFilterISS3ISS3_cast(itkLightObject obj) -> itkExpImageFilterISS3ISS3"""
    return _itkExpImageFilterPython.itkExpImageFilterISS3ISS3_cast(obj)

class itkExpImageFilterIUC2IUC2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUC2IUC2):
    """


    Computes the exponential function of each pixel.

    The computation is performed using std::exp(x).

    C++ includes: itkExpImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkExpImageFilterIUC2IUC2_Pointer":
        """__New_orig__() -> itkExpImageFilterIUC2IUC2_Pointer"""
        return _itkExpImageFilterPython.itkExpImageFilterIUC2IUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkExpImageFilterIUC2IUC2_Pointer":
        """Clone(itkExpImageFilterIUC2IUC2 self) -> itkExpImageFilterIUC2IUC2_Pointer"""
        return _itkExpImageFilterPython.itkExpImageFilterIUC2IUC2_Clone(self)

    InputConvertibleToDoubleCheck = _itkExpImageFilterPython.itkExpImageFilterIUC2IUC2_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkExpImageFilterPython.itkExpImageFilterIUC2IUC2_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkExpImageFilterPython.delete_itkExpImageFilterIUC2IUC2

    def cast(obj: 'itkLightObject') -> "itkExpImageFilterIUC2IUC2 *":
        """cast(itkLightObject obj) -> itkExpImageFilterIUC2IUC2"""
        return _itkExpImageFilterPython.itkExpImageFilterIUC2IUC2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkExpImageFilterIUC2IUC2

        Create a new object of the class itkExpImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExpImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkExpImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkExpImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkExpImageFilterIUC2IUC2.Clone = new_instancemethod(_itkExpImageFilterPython.itkExpImageFilterIUC2IUC2_Clone, None, itkExpImageFilterIUC2IUC2)
itkExpImageFilterIUC2IUC2_swigregister = _itkExpImageFilterPython.itkExpImageFilterIUC2IUC2_swigregister
itkExpImageFilterIUC2IUC2_swigregister(itkExpImageFilterIUC2IUC2)

def itkExpImageFilterIUC2IUC2___New_orig__() -> "itkExpImageFilterIUC2IUC2_Pointer":
    """itkExpImageFilterIUC2IUC2___New_orig__() -> itkExpImageFilterIUC2IUC2_Pointer"""
    return _itkExpImageFilterPython.itkExpImageFilterIUC2IUC2___New_orig__()

def itkExpImageFilterIUC2IUC2_cast(obj: 'itkLightObject') -> "itkExpImageFilterIUC2IUC2 *":
    """itkExpImageFilterIUC2IUC2_cast(itkLightObject obj) -> itkExpImageFilterIUC2IUC2"""
    return _itkExpImageFilterPython.itkExpImageFilterIUC2IUC2_cast(obj)

class itkExpImageFilterIUC3IUC3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUC3IUC3):
    """


    Computes the exponential function of each pixel.

    The computation is performed using std::exp(x).

    C++ includes: itkExpImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkExpImageFilterIUC3IUC3_Pointer":
        """__New_orig__() -> itkExpImageFilterIUC3IUC3_Pointer"""
        return _itkExpImageFilterPython.itkExpImageFilterIUC3IUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkExpImageFilterIUC3IUC3_Pointer":
        """Clone(itkExpImageFilterIUC3IUC3 self) -> itkExpImageFilterIUC3IUC3_Pointer"""
        return _itkExpImageFilterPython.itkExpImageFilterIUC3IUC3_Clone(self)

    InputConvertibleToDoubleCheck = _itkExpImageFilterPython.itkExpImageFilterIUC3IUC3_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkExpImageFilterPython.itkExpImageFilterIUC3IUC3_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkExpImageFilterPython.delete_itkExpImageFilterIUC3IUC3

    def cast(obj: 'itkLightObject') -> "itkExpImageFilterIUC3IUC3 *":
        """cast(itkLightObject obj) -> itkExpImageFilterIUC3IUC3"""
        return _itkExpImageFilterPython.itkExpImageFilterIUC3IUC3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkExpImageFilterIUC3IUC3

        Create a new object of the class itkExpImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExpImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkExpImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkExpImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkExpImageFilterIUC3IUC3.Clone = new_instancemethod(_itkExpImageFilterPython.itkExpImageFilterIUC3IUC3_Clone, None, itkExpImageFilterIUC3IUC3)
itkExpImageFilterIUC3IUC3_swigregister = _itkExpImageFilterPython.itkExpImageFilterIUC3IUC3_swigregister
itkExpImageFilterIUC3IUC3_swigregister(itkExpImageFilterIUC3IUC3)

def itkExpImageFilterIUC3IUC3___New_orig__() -> "itkExpImageFilterIUC3IUC3_Pointer":
    """itkExpImageFilterIUC3IUC3___New_orig__() -> itkExpImageFilterIUC3IUC3_Pointer"""
    return _itkExpImageFilterPython.itkExpImageFilterIUC3IUC3___New_orig__()

def itkExpImageFilterIUC3IUC3_cast(obj: 'itkLightObject') -> "itkExpImageFilterIUC3IUC3 *":
    """itkExpImageFilterIUC3IUC3_cast(itkLightObject obj) -> itkExpImageFilterIUC3IUC3"""
    return _itkExpImageFilterPython.itkExpImageFilterIUC3IUC3_cast(obj)

class itkExpImageFilterIUS2IUS2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUS2IUS2):
    """


    Computes the exponential function of each pixel.

    The computation is performed using std::exp(x).

    C++ includes: itkExpImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkExpImageFilterIUS2IUS2_Pointer":
        """__New_orig__() -> itkExpImageFilterIUS2IUS2_Pointer"""
        return _itkExpImageFilterPython.itkExpImageFilterIUS2IUS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkExpImageFilterIUS2IUS2_Pointer":
        """Clone(itkExpImageFilterIUS2IUS2 self) -> itkExpImageFilterIUS2IUS2_Pointer"""
        return _itkExpImageFilterPython.itkExpImageFilterIUS2IUS2_Clone(self)

    InputConvertibleToDoubleCheck = _itkExpImageFilterPython.itkExpImageFilterIUS2IUS2_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkExpImageFilterPython.itkExpImageFilterIUS2IUS2_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkExpImageFilterPython.delete_itkExpImageFilterIUS2IUS2

    def cast(obj: 'itkLightObject') -> "itkExpImageFilterIUS2IUS2 *":
        """cast(itkLightObject obj) -> itkExpImageFilterIUS2IUS2"""
        return _itkExpImageFilterPython.itkExpImageFilterIUS2IUS2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkExpImageFilterIUS2IUS2

        Create a new object of the class itkExpImageFilterIUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExpImageFilterIUS2IUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkExpImageFilterIUS2IUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkExpImageFilterIUS2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkExpImageFilterIUS2IUS2.Clone = new_instancemethod(_itkExpImageFilterPython.itkExpImageFilterIUS2IUS2_Clone, None, itkExpImageFilterIUS2IUS2)
itkExpImageFilterIUS2IUS2_swigregister = _itkExpImageFilterPython.itkExpImageFilterIUS2IUS2_swigregister
itkExpImageFilterIUS2IUS2_swigregister(itkExpImageFilterIUS2IUS2)

def itkExpImageFilterIUS2IUS2___New_orig__() -> "itkExpImageFilterIUS2IUS2_Pointer":
    """itkExpImageFilterIUS2IUS2___New_orig__() -> itkExpImageFilterIUS2IUS2_Pointer"""
    return _itkExpImageFilterPython.itkExpImageFilterIUS2IUS2___New_orig__()

def itkExpImageFilterIUS2IUS2_cast(obj: 'itkLightObject') -> "itkExpImageFilterIUS2IUS2 *":
    """itkExpImageFilterIUS2IUS2_cast(itkLightObject obj) -> itkExpImageFilterIUS2IUS2"""
    return _itkExpImageFilterPython.itkExpImageFilterIUS2IUS2_cast(obj)

class itkExpImageFilterIUS3IUS3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUS3IUS3):
    """


    Computes the exponential function of each pixel.

    The computation is performed using std::exp(x).

    C++ includes: itkExpImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkExpImageFilterIUS3IUS3_Pointer":
        """__New_orig__() -> itkExpImageFilterIUS3IUS3_Pointer"""
        return _itkExpImageFilterPython.itkExpImageFilterIUS3IUS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkExpImageFilterIUS3IUS3_Pointer":
        """Clone(itkExpImageFilterIUS3IUS3 self) -> itkExpImageFilterIUS3IUS3_Pointer"""
        return _itkExpImageFilterPython.itkExpImageFilterIUS3IUS3_Clone(self)

    InputConvertibleToDoubleCheck = _itkExpImageFilterPython.itkExpImageFilterIUS3IUS3_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkExpImageFilterPython.itkExpImageFilterIUS3IUS3_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkExpImageFilterPython.delete_itkExpImageFilterIUS3IUS3

    def cast(obj: 'itkLightObject') -> "itkExpImageFilterIUS3IUS3 *":
        """cast(itkLightObject obj) -> itkExpImageFilterIUS3IUS3"""
        return _itkExpImageFilterPython.itkExpImageFilterIUS3IUS3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkExpImageFilterIUS3IUS3

        Create a new object of the class itkExpImageFilterIUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExpImageFilterIUS3IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkExpImageFilterIUS3IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkExpImageFilterIUS3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkExpImageFilterIUS3IUS3.Clone = new_instancemethod(_itkExpImageFilterPython.itkExpImageFilterIUS3IUS3_Clone, None, itkExpImageFilterIUS3IUS3)
itkExpImageFilterIUS3IUS3_swigregister = _itkExpImageFilterPython.itkExpImageFilterIUS3IUS3_swigregister
itkExpImageFilterIUS3IUS3_swigregister(itkExpImageFilterIUS3IUS3)

def itkExpImageFilterIUS3IUS3___New_orig__() -> "itkExpImageFilterIUS3IUS3_Pointer":
    """itkExpImageFilterIUS3IUS3___New_orig__() -> itkExpImageFilterIUS3IUS3_Pointer"""
    return _itkExpImageFilterPython.itkExpImageFilterIUS3IUS3___New_orig__()

def itkExpImageFilterIUS3IUS3_cast(obj: 'itkLightObject') -> "itkExpImageFilterIUS3IUS3 *":
    """itkExpImageFilterIUS3IUS3_cast(itkLightObject obj) -> itkExpImageFilterIUS3IUS3"""
    return _itkExpImageFilterPython.itkExpImageFilterIUS3IUS3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def exp_image_filter(*args, **kwargs):
    """Procedural interface for ExpImageFilter"""
    import itk
    instance = itk.ExpImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def exp_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.ExpImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.ExpImageFilter.values()[0]
    else:
        filter_object = itk.ExpImageFilter

    exp_image_filter.__doc__ = filter_object.__doc__
    exp_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    exp_image_filter.__doc__ += "Available Keyword Arguments:\n"
    exp_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



