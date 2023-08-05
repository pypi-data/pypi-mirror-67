# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkLogImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkLogImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkLogImageFilterPython
            return _itkLogImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkLogImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkLogImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkLogImageFilterPython
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
import itkImageToImageFilterBPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import stdcomplexPython
import pyBasePython
import itkIndexPython
import itkSizePython
import itkOffsetPython
import ITKCommonBasePython
import itkImagePython
import itkPointPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import itkFixedArrayPython
import itkVectorPython
import itkMatrixPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import itkRGBAPixelPython
import itkImageRegionPython
import itkRGBPixelPython
import itkSymmetricSecondRankTensorPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterAPython

def itkLogImageFilterID3ID3_New():
  return itkLogImageFilterID3ID3.New()


def itkLogImageFilterID2ID2_New():
  return itkLogImageFilterID2ID2.New()


def itkLogImageFilterIF3IF3_New():
  return itkLogImageFilterIF3IF3.New()


def itkLogImageFilterIF2IF2_New():
  return itkLogImageFilterIF2IF2.New()


def itkLogImageFilterIUS3IUS3_New():
  return itkLogImageFilterIUS3IUS3.New()


def itkLogImageFilterIUS2IUS2_New():
  return itkLogImageFilterIUS2IUS2.New()


def itkLogImageFilterIUC3IUC3_New():
  return itkLogImageFilterIUC3IUC3.New()


def itkLogImageFilterIUC2IUC2_New():
  return itkLogImageFilterIUC2IUC2.New()


def itkLogImageFilterISS3ISS3_New():
  return itkLogImageFilterISS3ISS3.New()


def itkLogImageFilterISS2ISS2_New():
  return itkLogImageFilterISS2ISS2.New()

class itkLogImageFilterID2ID2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID2ID2):
    """


    Computes the log() of each pixel.

    C++ includes: itkLogImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLogImageFilterID2ID2_Pointer":
        """__New_orig__() -> itkLogImageFilterID2ID2_Pointer"""
        return _itkLogImageFilterPython.itkLogImageFilterID2ID2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLogImageFilterID2ID2_Pointer":
        """Clone(itkLogImageFilterID2ID2 self) -> itkLogImageFilterID2ID2_Pointer"""
        return _itkLogImageFilterPython.itkLogImageFilterID2ID2_Clone(self)

    InputConvertibleToDoubleCheck = _itkLogImageFilterPython.itkLogImageFilterID2ID2_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkLogImageFilterPython.itkLogImageFilterID2ID2_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkLogImageFilterPython.delete_itkLogImageFilterID2ID2

    def cast(obj: 'itkLightObject') -> "itkLogImageFilterID2ID2 *":
        """cast(itkLightObject obj) -> itkLogImageFilterID2ID2"""
        return _itkLogImageFilterPython.itkLogImageFilterID2ID2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLogImageFilterID2ID2

        Create a new object of the class itkLogImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLogImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLogImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLogImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLogImageFilterID2ID2.Clone = new_instancemethod(_itkLogImageFilterPython.itkLogImageFilterID2ID2_Clone, None, itkLogImageFilterID2ID2)
itkLogImageFilterID2ID2_swigregister = _itkLogImageFilterPython.itkLogImageFilterID2ID2_swigregister
itkLogImageFilterID2ID2_swigregister(itkLogImageFilterID2ID2)

def itkLogImageFilterID2ID2___New_orig__() -> "itkLogImageFilterID2ID2_Pointer":
    """itkLogImageFilterID2ID2___New_orig__() -> itkLogImageFilterID2ID2_Pointer"""
    return _itkLogImageFilterPython.itkLogImageFilterID2ID2___New_orig__()

def itkLogImageFilterID2ID2_cast(obj: 'itkLightObject') -> "itkLogImageFilterID2ID2 *":
    """itkLogImageFilterID2ID2_cast(itkLightObject obj) -> itkLogImageFilterID2ID2"""
    return _itkLogImageFilterPython.itkLogImageFilterID2ID2_cast(obj)

class itkLogImageFilterID3ID3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID3ID3):
    """


    Computes the log() of each pixel.

    C++ includes: itkLogImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLogImageFilterID3ID3_Pointer":
        """__New_orig__() -> itkLogImageFilterID3ID3_Pointer"""
        return _itkLogImageFilterPython.itkLogImageFilterID3ID3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLogImageFilterID3ID3_Pointer":
        """Clone(itkLogImageFilterID3ID3 self) -> itkLogImageFilterID3ID3_Pointer"""
        return _itkLogImageFilterPython.itkLogImageFilterID3ID3_Clone(self)

    InputConvertibleToDoubleCheck = _itkLogImageFilterPython.itkLogImageFilterID3ID3_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkLogImageFilterPython.itkLogImageFilterID3ID3_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkLogImageFilterPython.delete_itkLogImageFilterID3ID3

    def cast(obj: 'itkLightObject') -> "itkLogImageFilterID3ID3 *":
        """cast(itkLightObject obj) -> itkLogImageFilterID3ID3"""
        return _itkLogImageFilterPython.itkLogImageFilterID3ID3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLogImageFilterID3ID3

        Create a new object of the class itkLogImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLogImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLogImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLogImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLogImageFilterID3ID3.Clone = new_instancemethod(_itkLogImageFilterPython.itkLogImageFilterID3ID3_Clone, None, itkLogImageFilterID3ID3)
itkLogImageFilterID3ID3_swigregister = _itkLogImageFilterPython.itkLogImageFilterID3ID3_swigregister
itkLogImageFilterID3ID3_swigregister(itkLogImageFilterID3ID3)

def itkLogImageFilterID3ID3___New_orig__() -> "itkLogImageFilterID3ID3_Pointer":
    """itkLogImageFilterID3ID3___New_orig__() -> itkLogImageFilterID3ID3_Pointer"""
    return _itkLogImageFilterPython.itkLogImageFilterID3ID3___New_orig__()

def itkLogImageFilterID3ID3_cast(obj: 'itkLightObject') -> "itkLogImageFilterID3ID3 *":
    """itkLogImageFilterID3ID3_cast(itkLightObject obj) -> itkLogImageFilterID3ID3"""
    return _itkLogImageFilterPython.itkLogImageFilterID3ID3_cast(obj)

class itkLogImageFilterIF2IF2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF2IF2):
    """


    Computes the log() of each pixel.

    C++ includes: itkLogImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLogImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkLogImageFilterIF2IF2_Pointer"""
        return _itkLogImageFilterPython.itkLogImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLogImageFilterIF2IF2_Pointer":
        """Clone(itkLogImageFilterIF2IF2 self) -> itkLogImageFilterIF2IF2_Pointer"""
        return _itkLogImageFilterPython.itkLogImageFilterIF2IF2_Clone(self)

    InputConvertibleToDoubleCheck = _itkLogImageFilterPython.itkLogImageFilterIF2IF2_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkLogImageFilterPython.itkLogImageFilterIF2IF2_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkLogImageFilterPython.delete_itkLogImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkLogImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkLogImageFilterIF2IF2"""
        return _itkLogImageFilterPython.itkLogImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLogImageFilterIF2IF2

        Create a new object of the class itkLogImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLogImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLogImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLogImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLogImageFilterIF2IF2.Clone = new_instancemethod(_itkLogImageFilterPython.itkLogImageFilterIF2IF2_Clone, None, itkLogImageFilterIF2IF2)
itkLogImageFilterIF2IF2_swigregister = _itkLogImageFilterPython.itkLogImageFilterIF2IF2_swigregister
itkLogImageFilterIF2IF2_swigregister(itkLogImageFilterIF2IF2)

def itkLogImageFilterIF2IF2___New_orig__() -> "itkLogImageFilterIF2IF2_Pointer":
    """itkLogImageFilterIF2IF2___New_orig__() -> itkLogImageFilterIF2IF2_Pointer"""
    return _itkLogImageFilterPython.itkLogImageFilterIF2IF2___New_orig__()

def itkLogImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkLogImageFilterIF2IF2 *":
    """itkLogImageFilterIF2IF2_cast(itkLightObject obj) -> itkLogImageFilterIF2IF2"""
    return _itkLogImageFilterPython.itkLogImageFilterIF2IF2_cast(obj)

class itkLogImageFilterIF3IF3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF3IF3):
    """


    Computes the log() of each pixel.

    C++ includes: itkLogImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLogImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkLogImageFilterIF3IF3_Pointer"""
        return _itkLogImageFilterPython.itkLogImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLogImageFilterIF3IF3_Pointer":
        """Clone(itkLogImageFilterIF3IF3 self) -> itkLogImageFilterIF3IF3_Pointer"""
        return _itkLogImageFilterPython.itkLogImageFilterIF3IF3_Clone(self)

    InputConvertibleToDoubleCheck = _itkLogImageFilterPython.itkLogImageFilterIF3IF3_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkLogImageFilterPython.itkLogImageFilterIF3IF3_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkLogImageFilterPython.delete_itkLogImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkLogImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkLogImageFilterIF3IF3"""
        return _itkLogImageFilterPython.itkLogImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLogImageFilterIF3IF3

        Create a new object of the class itkLogImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLogImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLogImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLogImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLogImageFilterIF3IF3.Clone = new_instancemethod(_itkLogImageFilterPython.itkLogImageFilterIF3IF3_Clone, None, itkLogImageFilterIF3IF3)
itkLogImageFilterIF3IF3_swigregister = _itkLogImageFilterPython.itkLogImageFilterIF3IF3_swigregister
itkLogImageFilterIF3IF3_swigregister(itkLogImageFilterIF3IF3)

def itkLogImageFilterIF3IF3___New_orig__() -> "itkLogImageFilterIF3IF3_Pointer":
    """itkLogImageFilterIF3IF3___New_orig__() -> itkLogImageFilterIF3IF3_Pointer"""
    return _itkLogImageFilterPython.itkLogImageFilterIF3IF3___New_orig__()

def itkLogImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkLogImageFilterIF3IF3 *":
    """itkLogImageFilterIF3IF3_cast(itkLightObject obj) -> itkLogImageFilterIF3IF3"""
    return _itkLogImageFilterPython.itkLogImageFilterIF3IF3_cast(obj)

class itkLogImageFilterISS2ISS2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterISS2ISS2):
    """


    Computes the log() of each pixel.

    C++ includes: itkLogImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLogImageFilterISS2ISS2_Pointer":
        """__New_orig__() -> itkLogImageFilterISS2ISS2_Pointer"""
        return _itkLogImageFilterPython.itkLogImageFilterISS2ISS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLogImageFilterISS2ISS2_Pointer":
        """Clone(itkLogImageFilterISS2ISS2 self) -> itkLogImageFilterISS2ISS2_Pointer"""
        return _itkLogImageFilterPython.itkLogImageFilterISS2ISS2_Clone(self)

    InputConvertibleToDoubleCheck = _itkLogImageFilterPython.itkLogImageFilterISS2ISS2_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkLogImageFilterPython.itkLogImageFilterISS2ISS2_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkLogImageFilterPython.delete_itkLogImageFilterISS2ISS2

    def cast(obj: 'itkLightObject') -> "itkLogImageFilterISS2ISS2 *":
        """cast(itkLightObject obj) -> itkLogImageFilterISS2ISS2"""
        return _itkLogImageFilterPython.itkLogImageFilterISS2ISS2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLogImageFilterISS2ISS2

        Create a new object of the class itkLogImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLogImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLogImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLogImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLogImageFilterISS2ISS2.Clone = new_instancemethod(_itkLogImageFilterPython.itkLogImageFilterISS2ISS2_Clone, None, itkLogImageFilterISS2ISS2)
itkLogImageFilterISS2ISS2_swigregister = _itkLogImageFilterPython.itkLogImageFilterISS2ISS2_swigregister
itkLogImageFilterISS2ISS2_swigregister(itkLogImageFilterISS2ISS2)

def itkLogImageFilterISS2ISS2___New_orig__() -> "itkLogImageFilterISS2ISS2_Pointer":
    """itkLogImageFilterISS2ISS2___New_orig__() -> itkLogImageFilterISS2ISS2_Pointer"""
    return _itkLogImageFilterPython.itkLogImageFilterISS2ISS2___New_orig__()

def itkLogImageFilterISS2ISS2_cast(obj: 'itkLightObject') -> "itkLogImageFilterISS2ISS2 *":
    """itkLogImageFilterISS2ISS2_cast(itkLightObject obj) -> itkLogImageFilterISS2ISS2"""
    return _itkLogImageFilterPython.itkLogImageFilterISS2ISS2_cast(obj)

class itkLogImageFilterISS3ISS3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterISS3ISS3):
    """


    Computes the log() of each pixel.

    C++ includes: itkLogImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLogImageFilterISS3ISS3_Pointer":
        """__New_orig__() -> itkLogImageFilterISS3ISS3_Pointer"""
        return _itkLogImageFilterPython.itkLogImageFilterISS3ISS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLogImageFilterISS3ISS3_Pointer":
        """Clone(itkLogImageFilterISS3ISS3 self) -> itkLogImageFilterISS3ISS3_Pointer"""
        return _itkLogImageFilterPython.itkLogImageFilterISS3ISS3_Clone(self)

    InputConvertibleToDoubleCheck = _itkLogImageFilterPython.itkLogImageFilterISS3ISS3_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkLogImageFilterPython.itkLogImageFilterISS3ISS3_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkLogImageFilterPython.delete_itkLogImageFilterISS3ISS3

    def cast(obj: 'itkLightObject') -> "itkLogImageFilterISS3ISS3 *":
        """cast(itkLightObject obj) -> itkLogImageFilterISS3ISS3"""
        return _itkLogImageFilterPython.itkLogImageFilterISS3ISS3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLogImageFilterISS3ISS3

        Create a new object of the class itkLogImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLogImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLogImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLogImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLogImageFilterISS3ISS3.Clone = new_instancemethod(_itkLogImageFilterPython.itkLogImageFilterISS3ISS3_Clone, None, itkLogImageFilterISS3ISS3)
itkLogImageFilterISS3ISS3_swigregister = _itkLogImageFilterPython.itkLogImageFilterISS3ISS3_swigregister
itkLogImageFilterISS3ISS3_swigregister(itkLogImageFilterISS3ISS3)

def itkLogImageFilterISS3ISS3___New_orig__() -> "itkLogImageFilterISS3ISS3_Pointer":
    """itkLogImageFilterISS3ISS3___New_orig__() -> itkLogImageFilterISS3ISS3_Pointer"""
    return _itkLogImageFilterPython.itkLogImageFilterISS3ISS3___New_orig__()

def itkLogImageFilterISS3ISS3_cast(obj: 'itkLightObject') -> "itkLogImageFilterISS3ISS3 *":
    """itkLogImageFilterISS3ISS3_cast(itkLightObject obj) -> itkLogImageFilterISS3ISS3"""
    return _itkLogImageFilterPython.itkLogImageFilterISS3ISS3_cast(obj)

class itkLogImageFilterIUC2IUC2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUC2IUC2):
    """


    Computes the log() of each pixel.

    C++ includes: itkLogImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLogImageFilterIUC2IUC2_Pointer":
        """__New_orig__() -> itkLogImageFilterIUC2IUC2_Pointer"""
        return _itkLogImageFilterPython.itkLogImageFilterIUC2IUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLogImageFilterIUC2IUC2_Pointer":
        """Clone(itkLogImageFilterIUC2IUC2 self) -> itkLogImageFilterIUC2IUC2_Pointer"""
        return _itkLogImageFilterPython.itkLogImageFilterIUC2IUC2_Clone(self)

    InputConvertibleToDoubleCheck = _itkLogImageFilterPython.itkLogImageFilterIUC2IUC2_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkLogImageFilterPython.itkLogImageFilterIUC2IUC2_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkLogImageFilterPython.delete_itkLogImageFilterIUC2IUC2

    def cast(obj: 'itkLightObject') -> "itkLogImageFilterIUC2IUC2 *":
        """cast(itkLightObject obj) -> itkLogImageFilterIUC2IUC2"""
        return _itkLogImageFilterPython.itkLogImageFilterIUC2IUC2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLogImageFilterIUC2IUC2

        Create a new object of the class itkLogImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLogImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLogImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLogImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLogImageFilterIUC2IUC2.Clone = new_instancemethod(_itkLogImageFilterPython.itkLogImageFilterIUC2IUC2_Clone, None, itkLogImageFilterIUC2IUC2)
itkLogImageFilterIUC2IUC2_swigregister = _itkLogImageFilterPython.itkLogImageFilterIUC2IUC2_swigregister
itkLogImageFilterIUC2IUC2_swigregister(itkLogImageFilterIUC2IUC2)

def itkLogImageFilterIUC2IUC2___New_orig__() -> "itkLogImageFilterIUC2IUC2_Pointer":
    """itkLogImageFilterIUC2IUC2___New_orig__() -> itkLogImageFilterIUC2IUC2_Pointer"""
    return _itkLogImageFilterPython.itkLogImageFilterIUC2IUC2___New_orig__()

def itkLogImageFilterIUC2IUC2_cast(obj: 'itkLightObject') -> "itkLogImageFilterIUC2IUC2 *":
    """itkLogImageFilterIUC2IUC2_cast(itkLightObject obj) -> itkLogImageFilterIUC2IUC2"""
    return _itkLogImageFilterPython.itkLogImageFilterIUC2IUC2_cast(obj)

class itkLogImageFilterIUC3IUC3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUC3IUC3):
    """


    Computes the log() of each pixel.

    C++ includes: itkLogImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLogImageFilterIUC3IUC3_Pointer":
        """__New_orig__() -> itkLogImageFilterIUC3IUC3_Pointer"""
        return _itkLogImageFilterPython.itkLogImageFilterIUC3IUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLogImageFilterIUC3IUC3_Pointer":
        """Clone(itkLogImageFilterIUC3IUC3 self) -> itkLogImageFilterIUC3IUC3_Pointer"""
        return _itkLogImageFilterPython.itkLogImageFilterIUC3IUC3_Clone(self)

    InputConvertibleToDoubleCheck = _itkLogImageFilterPython.itkLogImageFilterIUC3IUC3_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkLogImageFilterPython.itkLogImageFilterIUC3IUC3_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkLogImageFilterPython.delete_itkLogImageFilterIUC3IUC3

    def cast(obj: 'itkLightObject') -> "itkLogImageFilterIUC3IUC3 *":
        """cast(itkLightObject obj) -> itkLogImageFilterIUC3IUC3"""
        return _itkLogImageFilterPython.itkLogImageFilterIUC3IUC3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLogImageFilterIUC3IUC3

        Create a new object of the class itkLogImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLogImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLogImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLogImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLogImageFilterIUC3IUC3.Clone = new_instancemethod(_itkLogImageFilterPython.itkLogImageFilterIUC3IUC3_Clone, None, itkLogImageFilterIUC3IUC3)
itkLogImageFilterIUC3IUC3_swigregister = _itkLogImageFilterPython.itkLogImageFilterIUC3IUC3_swigregister
itkLogImageFilterIUC3IUC3_swigregister(itkLogImageFilterIUC3IUC3)

def itkLogImageFilterIUC3IUC3___New_orig__() -> "itkLogImageFilterIUC3IUC3_Pointer":
    """itkLogImageFilterIUC3IUC3___New_orig__() -> itkLogImageFilterIUC3IUC3_Pointer"""
    return _itkLogImageFilterPython.itkLogImageFilterIUC3IUC3___New_orig__()

def itkLogImageFilterIUC3IUC3_cast(obj: 'itkLightObject') -> "itkLogImageFilterIUC3IUC3 *":
    """itkLogImageFilterIUC3IUC3_cast(itkLightObject obj) -> itkLogImageFilterIUC3IUC3"""
    return _itkLogImageFilterPython.itkLogImageFilterIUC3IUC3_cast(obj)

class itkLogImageFilterIUS2IUS2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUS2IUS2):
    """


    Computes the log() of each pixel.

    C++ includes: itkLogImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLogImageFilterIUS2IUS2_Pointer":
        """__New_orig__() -> itkLogImageFilterIUS2IUS2_Pointer"""
        return _itkLogImageFilterPython.itkLogImageFilterIUS2IUS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLogImageFilterIUS2IUS2_Pointer":
        """Clone(itkLogImageFilterIUS2IUS2 self) -> itkLogImageFilterIUS2IUS2_Pointer"""
        return _itkLogImageFilterPython.itkLogImageFilterIUS2IUS2_Clone(self)

    InputConvertibleToDoubleCheck = _itkLogImageFilterPython.itkLogImageFilterIUS2IUS2_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkLogImageFilterPython.itkLogImageFilterIUS2IUS2_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkLogImageFilterPython.delete_itkLogImageFilterIUS2IUS2

    def cast(obj: 'itkLightObject') -> "itkLogImageFilterIUS2IUS2 *":
        """cast(itkLightObject obj) -> itkLogImageFilterIUS2IUS2"""
        return _itkLogImageFilterPython.itkLogImageFilterIUS2IUS2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLogImageFilterIUS2IUS2

        Create a new object of the class itkLogImageFilterIUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLogImageFilterIUS2IUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLogImageFilterIUS2IUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLogImageFilterIUS2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLogImageFilterIUS2IUS2.Clone = new_instancemethod(_itkLogImageFilterPython.itkLogImageFilterIUS2IUS2_Clone, None, itkLogImageFilterIUS2IUS2)
itkLogImageFilterIUS2IUS2_swigregister = _itkLogImageFilterPython.itkLogImageFilterIUS2IUS2_swigregister
itkLogImageFilterIUS2IUS2_swigregister(itkLogImageFilterIUS2IUS2)

def itkLogImageFilterIUS2IUS2___New_orig__() -> "itkLogImageFilterIUS2IUS2_Pointer":
    """itkLogImageFilterIUS2IUS2___New_orig__() -> itkLogImageFilterIUS2IUS2_Pointer"""
    return _itkLogImageFilterPython.itkLogImageFilterIUS2IUS2___New_orig__()

def itkLogImageFilterIUS2IUS2_cast(obj: 'itkLightObject') -> "itkLogImageFilterIUS2IUS2 *":
    """itkLogImageFilterIUS2IUS2_cast(itkLightObject obj) -> itkLogImageFilterIUS2IUS2"""
    return _itkLogImageFilterPython.itkLogImageFilterIUS2IUS2_cast(obj)

class itkLogImageFilterIUS3IUS3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUS3IUS3):
    """


    Computes the log() of each pixel.

    C++ includes: itkLogImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLogImageFilterIUS3IUS3_Pointer":
        """__New_orig__() -> itkLogImageFilterIUS3IUS3_Pointer"""
        return _itkLogImageFilterPython.itkLogImageFilterIUS3IUS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLogImageFilterIUS3IUS3_Pointer":
        """Clone(itkLogImageFilterIUS3IUS3 self) -> itkLogImageFilterIUS3IUS3_Pointer"""
        return _itkLogImageFilterPython.itkLogImageFilterIUS3IUS3_Clone(self)

    InputConvertibleToDoubleCheck = _itkLogImageFilterPython.itkLogImageFilterIUS3IUS3_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkLogImageFilterPython.itkLogImageFilterIUS3IUS3_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkLogImageFilterPython.delete_itkLogImageFilterIUS3IUS3

    def cast(obj: 'itkLightObject') -> "itkLogImageFilterIUS3IUS3 *":
        """cast(itkLightObject obj) -> itkLogImageFilterIUS3IUS3"""
        return _itkLogImageFilterPython.itkLogImageFilterIUS3IUS3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLogImageFilterIUS3IUS3

        Create a new object of the class itkLogImageFilterIUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLogImageFilterIUS3IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLogImageFilterIUS3IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLogImageFilterIUS3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLogImageFilterIUS3IUS3.Clone = new_instancemethod(_itkLogImageFilterPython.itkLogImageFilterIUS3IUS3_Clone, None, itkLogImageFilterIUS3IUS3)
itkLogImageFilterIUS3IUS3_swigregister = _itkLogImageFilterPython.itkLogImageFilterIUS3IUS3_swigregister
itkLogImageFilterIUS3IUS3_swigregister(itkLogImageFilterIUS3IUS3)

def itkLogImageFilterIUS3IUS3___New_orig__() -> "itkLogImageFilterIUS3IUS3_Pointer":
    """itkLogImageFilterIUS3IUS3___New_orig__() -> itkLogImageFilterIUS3IUS3_Pointer"""
    return _itkLogImageFilterPython.itkLogImageFilterIUS3IUS3___New_orig__()

def itkLogImageFilterIUS3IUS3_cast(obj: 'itkLightObject') -> "itkLogImageFilterIUS3IUS3 *":
    """itkLogImageFilterIUS3IUS3_cast(itkLightObject obj) -> itkLogImageFilterIUS3IUS3"""
    return _itkLogImageFilterPython.itkLogImageFilterIUS3IUS3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def log_image_filter(*args, **kwargs):
    """Procedural interface for LogImageFilter"""
    import itk
    instance = itk.LogImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def log_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.LogImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.LogImageFilter.values()[0]
    else:
        filter_object = itk.LogImageFilter

    log_image_filter.__doc__ = filter_object.__doc__
    log_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    log_image_filter.__doc__ += "Available Keyword Arguments:\n"
    log_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



