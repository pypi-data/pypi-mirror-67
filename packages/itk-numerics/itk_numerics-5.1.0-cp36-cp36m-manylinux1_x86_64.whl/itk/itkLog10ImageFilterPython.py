# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkLog10ImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkLog10ImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkLog10ImageFilterPython
            return _itkLog10ImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkLog10ImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkLog10ImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkLog10ImageFilterPython
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
import itkImagePython
import ITKCommonBasePython
import pyBasePython
import itkVectorPython
import itkFixedArrayPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import vnl_vector_refPython
import itkSizePython
import itkOffsetPython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkCovariantVectorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkSymmetricSecondRankTensorPython
import itkImageRegionPython
import itkIndexPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterAPython

def itkLog10ImageFilterID3ID3_New():
  return itkLog10ImageFilterID3ID3.New()


def itkLog10ImageFilterID2ID2_New():
  return itkLog10ImageFilterID2ID2.New()


def itkLog10ImageFilterIF3IF3_New():
  return itkLog10ImageFilterIF3IF3.New()


def itkLog10ImageFilterIF2IF2_New():
  return itkLog10ImageFilterIF2IF2.New()


def itkLog10ImageFilterIUS3IUS3_New():
  return itkLog10ImageFilterIUS3IUS3.New()


def itkLog10ImageFilterIUS2IUS2_New():
  return itkLog10ImageFilterIUS2IUS2.New()


def itkLog10ImageFilterIUC3IUC3_New():
  return itkLog10ImageFilterIUC3IUC3.New()


def itkLog10ImageFilterIUC2IUC2_New():
  return itkLog10ImageFilterIUC2IUC2.New()


def itkLog10ImageFilterISS3ISS3_New():
  return itkLog10ImageFilterISS3ISS3.New()


def itkLog10ImageFilterISS2ISS2_New():
  return itkLog10ImageFilterISS2ISS2.New()

class itkLog10ImageFilterID2ID2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID2ID2):
    """


    Computes the log10 of each pixel.

    The computation is performed using std::log10(x).

    C++ includes: itkLog10ImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLog10ImageFilterID2ID2_Pointer":
        """__New_orig__() -> itkLog10ImageFilterID2ID2_Pointer"""
        return _itkLog10ImageFilterPython.itkLog10ImageFilterID2ID2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLog10ImageFilterID2ID2_Pointer":
        """Clone(itkLog10ImageFilterID2ID2 self) -> itkLog10ImageFilterID2ID2_Pointer"""
        return _itkLog10ImageFilterPython.itkLog10ImageFilterID2ID2_Clone(self)

    InputConvertibleToDoubleCheck = _itkLog10ImageFilterPython.itkLog10ImageFilterID2ID2_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkLog10ImageFilterPython.itkLog10ImageFilterID2ID2_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkLog10ImageFilterPython.delete_itkLog10ImageFilterID2ID2

    def cast(obj: 'itkLightObject') -> "itkLog10ImageFilterID2ID2 *":
        """cast(itkLightObject obj) -> itkLog10ImageFilterID2ID2"""
        return _itkLog10ImageFilterPython.itkLog10ImageFilterID2ID2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLog10ImageFilterID2ID2

        Create a new object of the class itkLog10ImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLog10ImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLog10ImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLog10ImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLog10ImageFilterID2ID2.Clone = new_instancemethod(_itkLog10ImageFilterPython.itkLog10ImageFilterID2ID2_Clone, None, itkLog10ImageFilterID2ID2)
itkLog10ImageFilterID2ID2_swigregister = _itkLog10ImageFilterPython.itkLog10ImageFilterID2ID2_swigregister
itkLog10ImageFilterID2ID2_swigregister(itkLog10ImageFilterID2ID2)

def itkLog10ImageFilterID2ID2___New_orig__() -> "itkLog10ImageFilterID2ID2_Pointer":
    """itkLog10ImageFilterID2ID2___New_orig__() -> itkLog10ImageFilterID2ID2_Pointer"""
    return _itkLog10ImageFilterPython.itkLog10ImageFilterID2ID2___New_orig__()

def itkLog10ImageFilterID2ID2_cast(obj: 'itkLightObject') -> "itkLog10ImageFilterID2ID2 *":
    """itkLog10ImageFilterID2ID2_cast(itkLightObject obj) -> itkLog10ImageFilterID2ID2"""
    return _itkLog10ImageFilterPython.itkLog10ImageFilterID2ID2_cast(obj)

class itkLog10ImageFilterID3ID3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID3ID3):
    """


    Computes the log10 of each pixel.

    The computation is performed using std::log10(x).

    C++ includes: itkLog10ImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLog10ImageFilterID3ID3_Pointer":
        """__New_orig__() -> itkLog10ImageFilterID3ID3_Pointer"""
        return _itkLog10ImageFilterPython.itkLog10ImageFilterID3ID3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLog10ImageFilterID3ID3_Pointer":
        """Clone(itkLog10ImageFilterID3ID3 self) -> itkLog10ImageFilterID3ID3_Pointer"""
        return _itkLog10ImageFilterPython.itkLog10ImageFilterID3ID3_Clone(self)

    InputConvertibleToDoubleCheck = _itkLog10ImageFilterPython.itkLog10ImageFilterID3ID3_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkLog10ImageFilterPython.itkLog10ImageFilterID3ID3_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkLog10ImageFilterPython.delete_itkLog10ImageFilterID3ID3

    def cast(obj: 'itkLightObject') -> "itkLog10ImageFilterID3ID3 *":
        """cast(itkLightObject obj) -> itkLog10ImageFilterID3ID3"""
        return _itkLog10ImageFilterPython.itkLog10ImageFilterID3ID3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLog10ImageFilterID3ID3

        Create a new object of the class itkLog10ImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLog10ImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLog10ImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLog10ImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLog10ImageFilterID3ID3.Clone = new_instancemethod(_itkLog10ImageFilterPython.itkLog10ImageFilterID3ID3_Clone, None, itkLog10ImageFilterID3ID3)
itkLog10ImageFilterID3ID3_swigregister = _itkLog10ImageFilterPython.itkLog10ImageFilterID3ID3_swigregister
itkLog10ImageFilterID3ID3_swigregister(itkLog10ImageFilterID3ID3)

def itkLog10ImageFilterID3ID3___New_orig__() -> "itkLog10ImageFilterID3ID3_Pointer":
    """itkLog10ImageFilterID3ID3___New_orig__() -> itkLog10ImageFilterID3ID3_Pointer"""
    return _itkLog10ImageFilterPython.itkLog10ImageFilterID3ID3___New_orig__()

def itkLog10ImageFilterID3ID3_cast(obj: 'itkLightObject') -> "itkLog10ImageFilterID3ID3 *":
    """itkLog10ImageFilterID3ID3_cast(itkLightObject obj) -> itkLog10ImageFilterID3ID3"""
    return _itkLog10ImageFilterPython.itkLog10ImageFilterID3ID3_cast(obj)

class itkLog10ImageFilterIF2IF2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF2IF2):
    """


    Computes the log10 of each pixel.

    The computation is performed using std::log10(x).

    C++ includes: itkLog10ImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLog10ImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkLog10ImageFilterIF2IF2_Pointer"""
        return _itkLog10ImageFilterPython.itkLog10ImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLog10ImageFilterIF2IF2_Pointer":
        """Clone(itkLog10ImageFilterIF2IF2 self) -> itkLog10ImageFilterIF2IF2_Pointer"""
        return _itkLog10ImageFilterPython.itkLog10ImageFilterIF2IF2_Clone(self)

    InputConvertibleToDoubleCheck = _itkLog10ImageFilterPython.itkLog10ImageFilterIF2IF2_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkLog10ImageFilterPython.itkLog10ImageFilterIF2IF2_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkLog10ImageFilterPython.delete_itkLog10ImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkLog10ImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkLog10ImageFilterIF2IF2"""
        return _itkLog10ImageFilterPython.itkLog10ImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLog10ImageFilterIF2IF2

        Create a new object of the class itkLog10ImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLog10ImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLog10ImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLog10ImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLog10ImageFilterIF2IF2.Clone = new_instancemethod(_itkLog10ImageFilterPython.itkLog10ImageFilterIF2IF2_Clone, None, itkLog10ImageFilterIF2IF2)
itkLog10ImageFilterIF2IF2_swigregister = _itkLog10ImageFilterPython.itkLog10ImageFilterIF2IF2_swigregister
itkLog10ImageFilterIF2IF2_swigregister(itkLog10ImageFilterIF2IF2)

def itkLog10ImageFilterIF2IF2___New_orig__() -> "itkLog10ImageFilterIF2IF2_Pointer":
    """itkLog10ImageFilterIF2IF2___New_orig__() -> itkLog10ImageFilterIF2IF2_Pointer"""
    return _itkLog10ImageFilterPython.itkLog10ImageFilterIF2IF2___New_orig__()

def itkLog10ImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkLog10ImageFilterIF2IF2 *":
    """itkLog10ImageFilterIF2IF2_cast(itkLightObject obj) -> itkLog10ImageFilterIF2IF2"""
    return _itkLog10ImageFilterPython.itkLog10ImageFilterIF2IF2_cast(obj)

class itkLog10ImageFilterIF3IF3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF3IF3):
    """


    Computes the log10 of each pixel.

    The computation is performed using std::log10(x).

    C++ includes: itkLog10ImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLog10ImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkLog10ImageFilterIF3IF3_Pointer"""
        return _itkLog10ImageFilterPython.itkLog10ImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLog10ImageFilterIF3IF3_Pointer":
        """Clone(itkLog10ImageFilterIF3IF3 self) -> itkLog10ImageFilterIF3IF3_Pointer"""
        return _itkLog10ImageFilterPython.itkLog10ImageFilterIF3IF3_Clone(self)

    InputConvertibleToDoubleCheck = _itkLog10ImageFilterPython.itkLog10ImageFilterIF3IF3_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkLog10ImageFilterPython.itkLog10ImageFilterIF3IF3_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkLog10ImageFilterPython.delete_itkLog10ImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkLog10ImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkLog10ImageFilterIF3IF3"""
        return _itkLog10ImageFilterPython.itkLog10ImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLog10ImageFilterIF3IF3

        Create a new object of the class itkLog10ImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLog10ImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLog10ImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLog10ImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLog10ImageFilterIF3IF3.Clone = new_instancemethod(_itkLog10ImageFilterPython.itkLog10ImageFilterIF3IF3_Clone, None, itkLog10ImageFilterIF3IF3)
itkLog10ImageFilterIF3IF3_swigregister = _itkLog10ImageFilterPython.itkLog10ImageFilterIF3IF3_swigregister
itkLog10ImageFilterIF3IF3_swigregister(itkLog10ImageFilterIF3IF3)

def itkLog10ImageFilterIF3IF3___New_orig__() -> "itkLog10ImageFilterIF3IF3_Pointer":
    """itkLog10ImageFilterIF3IF3___New_orig__() -> itkLog10ImageFilterIF3IF3_Pointer"""
    return _itkLog10ImageFilterPython.itkLog10ImageFilterIF3IF3___New_orig__()

def itkLog10ImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkLog10ImageFilterIF3IF3 *":
    """itkLog10ImageFilterIF3IF3_cast(itkLightObject obj) -> itkLog10ImageFilterIF3IF3"""
    return _itkLog10ImageFilterPython.itkLog10ImageFilterIF3IF3_cast(obj)

class itkLog10ImageFilterISS2ISS2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterISS2ISS2):
    """


    Computes the log10 of each pixel.

    The computation is performed using std::log10(x).

    C++ includes: itkLog10ImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLog10ImageFilterISS2ISS2_Pointer":
        """__New_orig__() -> itkLog10ImageFilterISS2ISS2_Pointer"""
        return _itkLog10ImageFilterPython.itkLog10ImageFilterISS2ISS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLog10ImageFilterISS2ISS2_Pointer":
        """Clone(itkLog10ImageFilterISS2ISS2 self) -> itkLog10ImageFilterISS2ISS2_Pointer"""
        return _itkLog10ImageFilterPython.itkLog10ImageFilterISS2ISS2_Clone(self)

    InputConvertibleToDoubleCheck = _itkLog10ImageFilterPython.itkLog10ImageFilterISS2ISS2_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkLog10ImageFilterPython.itkLog10ImageFilterISS2ISS2_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkLog10ImageFilterPython.delete_itkLog10ImageFilterISS2ISS2

    def cast(obj: 'itkLightObject') -> "itkLog10ImageFilterISS2ISS2 *":
        """cast(itkLightObject obj) -> itkLog10ImageFilterISS2ISS2"""
        return _itkLog10ImageFilterPython.itkLog10ImageFilterISS2ISS2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLog10ImageFilterISS2ISS2

        Create a new object of the class itkLog10ImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLog10ImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLog10ImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLog10ImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLog10ImageFilterISS2ISS2.Clone = new_instancemethod(_itkLog10ImageFilterPython.itkLog10ImageFilterISS2ISS2_Clone, None, itkLog10ImageFilterISS2ISS2)
itkLog10ImageFilterISS2ISS2_swigregister = _itkLog10ImageFilterPython.itkLog10ImageFilterISS2ISS2_swigregister
itkLog10ImageFilterISS2ISS2_swigregister(itkLog10ImageFilterISS2ISS2)

def itkLog10ImageFilterISS2ISS2___New_orig__() -> "itkLog10ImageFilterISS2ISS2_Pointer":
    """itkLog10ImageFilterISS2ISS2___New_orig__() -> itkLog10ImageFilterISS2ISS2_Pointer"""
    return _itkLog10ImageFilterPython.itkLog10ImageFilterISS2ISS2___New_orig__()

def itkLog10ImageFilterISS2ISS2_cast(obj: 'itkLightObject') -> "itkLog10ImageFilterISS2ISS2 *":
    """itkLog10ImageFilterISS2ISS2_cast(itkLightObject obj) -> itkLog10ImageFilterISS2ISS2"""
    return _itkLog10ImageFilterPython.itkLog10ImageFilterISS2ISS2_cast(obj)

class itkLog10ImageFilterISS3ISS3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterISS3ISS3):
    """


    Computes the log10 of each pixel.

    The computation is performed using std::log10(x).

    C++ includes: itkLog10ImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLog10ImageFilterISS3ISS3_Pointer":
        """__New_orig__() -> itkLog10ImageFilterISS3ISS3_Pointer"""
        return _itkLog10ImageFilterPython.itkLog10ImageFilterISS3ISS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLog10ImageFilterISS3ISS3_Pointer":
        """Clone(itkLog10ImageFilterISS3ISS3 self) -> itkLog10ImageFilterISS3ISS3_Pointer"""
        return _itkLog10ImageFilterPython.itkLog10ImageFilterISS3ISS3_Clone(self)

    InputConvertibleToDoubleCheck = _itkLog10ImageFilterPython.itkLog10ImageFilterISS3ISS3_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkLog10ImageFilterPython.itkLog10ImageFilterISS3ISS3_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkLog10ImageFilterPython.delete_itkLog10ImageFilterISS3ISS3

    def cast(obj: 'itkLightObject') -> "itkLog10ImageFilterISS3ISS3 *":
        """cast(itkLightObject obj) -> itkLog10ImageFilterISS3ISS3"""
        return _itkLog10ImageFilterPython.itkLog10ImageFilterISS3ISS3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLog10ImageFilterISS3ISS3

        Create a new object of the class itkLog10ImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLog10ImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLog10ImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLog10ImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLog10ImageFilterISS3ISS3.Clone = new_instancemethod(_itkLog10ImageFilterPython.itkLog10ImageFilterISS3ISS3_Clone, None, itkLog10ImageFilterISS3ISS3)
itkLog10ImageFilterISS3ISS3_swigregister = _itkLog10ImageFilterPython.itkLog10ImageFilterISS3ISS3_swigregister
itkLog10ImageFilterISS3ISS3_swigregister(itkLog10ImageFilterISS3ISS3)

def itkLog10ImageFilterISS3ISS3___New_orig__() -> "itkLog10ImageFilterISS3ISS3_Pointer":
    """itkLog10ImageFilterISS3ISS3___New_orig__() -> itkLog10ImageFilterISS3ISS3_Pointer"""
    return _itkLog10ImageFilterPython.itkLog10ImageFilterISS3ISS3___New_orig__()

def itkLog10ImageFilterISS3ISS3_cast(obj: 'itkLightObject') -> "itkLog10ImageFilterISS3ISS3 *":
    """itkLog10ImageFilterISS3ISS3_cast(itkLightObject obj) -> itkLog10ImageFilterISS3ISS3"""
    return _itkLog10ImageFilterPython.itkLog10ImageFilterISS3ISS3_cast(obj)

class itkLog10ImageFilterIUC2IUC2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUC2IUC2):
    """


    Computes the log10 of each pixel.

    The computation is performed using std::log10(x).

    C++ includes: itkLog10ImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLog10ImageFilterIUC2IUC2_Pointer":
        """__New_orig__() -> itkLog10ImageFilterIUC2IUC2_Pointer"""
        return _itkLog10ImageFilterPython.itkLog10ImageFilterIUC2IUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLog10ImageFilterIUC2IUC2_Pointer":
        """Clone(itkLog10ImageFilterIUC2IUC2 self) -> itkLog10ImageFilterIUC2IUC2_Pointer"""
        return _itkLog10ImageFilterPython.itkLog10ImageFilterIUC2IUC2_Clone(self)

    InputConvertibleToDoubleCheck = _itkLog10ImageFilterPython.itkLog10ImageFilterIUC2IUC2_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkLog10ImageFilterPython.itkLog10ImageFilterIUC2IUC2_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkLog10ImageFilterPython.delete_itkLog10ImageFilterIUC2IUC2

    def cast(obj: 'itkLightObject') -> "itkLog10ImageFilterIUC2IUC2 *":
        """cast(itkLightObject obj) -> itkLog10ImageFilterIUC2IUC2"""
        return _itkLog10ImageFilterPython.itkLog10ImageFilterIUC2IUC2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLog10ImageFilterIUC2IUC2

        Create a new object of the class itkLog10ImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLog10ImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLog10ImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLog10ImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLog10ImageFilterIUC2IUC2.Clone = new_instancemethod(_itkLog10ImageFilterPython.itkLog10ImageFilterIUC2IUC2_Clone, None, itkLog10ImageFilterIUC2IUC2)
itkLog10ImageFilterIUC2IUC2_swigregister = _itkLog10ImageFilterPython.itkLog10ImageFilterIUC2IUC2_swigregister
itkLog10ImageFilterIUC2IUC2_swigregister(itkLog10ImageFilterIUC2IUC2)

def itkLog10ImageFilterIUC2IUC2___New_orig__() -> "itkLog10ImageFilterIUC2IUC2_Pointer":
    """itkLog10ImageFilterIUC2IUC2___New_orig__() -> itkLog10ImageFilterIUC2IUC2_Pointer"""
    return _itkLog10ImageFilterPython.itkLog10ImageFilterIUC2IUC2___New_orig__()

def itkLog10ImageFilterIUC2IUC2_cast(obj: 'itkLightObject') -> "itkLog10ImageFilterIUC2IUC2 *":
    """itkLog10ImageFilterIUC2IUC2_cast(itkLightObject obj) -> itkLog10ImageFilterIUC2IUC2"""
    return _itkLog10ImageFilterPython.itkLog10ImageFilterIUC2IUC2_cast(obj)

class itkLog10ImageFilterIUC3IUC3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUC3IUC3):
    """


    Computes the log10 of each pixel.

    The computation is performed using std::log10(x).

    C++ includes: itkLog10ImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLog10ImageFilterIUC3IUC3_Pointer":
        """__New_orig__() -> itkLog10ImageFilterIUC3IUC3_Pointer"""
        return _itkLog10ImageFilterPython.itkLog10ImageFilterIUC3IUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLog10ImageFilterIUC3IUC3_Pointer":
        """Clone(itkLog10ImageFilterIUC3IUC3 self) -> itkLog10ImageFilterIUC3IUC3_Pointer"""
        return _itkLog10ImageFilterPython.itkLog10ImageFilterIUC3IUC3_Clone(self)

    InputConvertibleToDoubleCheck = _itkLog10ImageFilterPython.itkLog10ImageFilterIUC3IUC3_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkLog10ImageFilterPython.itkLog10ImageFilterIUC3IUC3_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkLog10ImageFilterPython.delete_itkLog10ImageFilterIUC3IUC3

    def cast(obj: 'itkLightObject') -> "itkLog10ImageFilterIUC3IUC3 *":
        """cast(itkLightObject obj) -> itkLog10ImageFilterIUC3IUC3"""
        return _itkLog10ImageFilterPython.itkLog10ImageFilterIUC3IUC3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLog10ImageFilterIUC3IUC3

        Create a new object of the class itkLog10ImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLog10ImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLog10ImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLog10ImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLog10ImageFilterIUC3IUC3.Clone = new_instancemethod(_itkLog10ImageFilterPython.itkLog10ImageFilterIUC3IUC3_Clone, None, itkLog10ImageFilterIUC3IUC3)
itkLog10ImageFilterIUC3IUC3_swigregister = _itkLog10ImageFilterPython.itkLog10ImageFilterIUC3IUC3_swigregister
itkLog10ImageFilterIUC3IUC3_swigregister(itkLog10ImageFilterIUC3IUC3)

def itkLog10ImageFilterIUC3IUC3___New_orig__() -> "itkLog10ImageFilterIUC3IUC3_Pointer":
    """itkLog10ImageFilterIUC3IUC3___New_orig__() -> itkLog10ImageFilterIUC3IUC3_Pointer"""
    return _itkLog10ImageFilterPython.itkLog10ImageFilterIUC3IUC3___New_orig__()

def itkLog10ImageFilterIUC3IUC3_cast(obj: 'itkLightObject') -> "itkLog10ImageFilterIUC3IUC3 *":
    """itkLog10ImageFilterIUC3IUC3_cast(itkLightObject obj) -> itkLog10ImageFilterIUC3IUC3"""
    return _itkLog10ImageFilterPython.itkLog10ImageFilterIUC3IUC3_cast(obj)

class itkLog10ImageFilterIUS2IUS2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUS2IUS2):
    """


    Computes the log10 of each pixel.

    The computation is performed using std::log10(x).

    C++ includes: itkLog10ImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLog10ImageFilterIUS2IUS2_Pointer":
        """__New_orig__() -> itkLog10ImageFilterIUS2IUS2_Pointer"""
        return _itkLog10ImageFilterPython.itkLog10ImageFilterIUS2IUS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLog10ImageFilterIUS2IUS2_Pointer":
        """Clone(itkLog10ImageFilterIUS2IUS2 self) -> itkLog10ImageFilterIUS2IUS2_Pointer"""
        return _itkLog10ImageFilterPython.itkLog10ImageFilterIUS2IUS2_Clone(self)

    InputConvertibleToDoubleCheck = _itkLog10ImageFilterPython.itkLog10ImageFilterIUS2IUS2_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkLog10ImageFilterPython.itkLog10ImageFilterIUS2IUS2_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkLog10ImageFilterPython.delete_itkLog10ImageFilterIUS2IUS2

    def cast(obj: 'itkLightObject') -> "itkLog10ImageFilterIUS2IUS2 *":
        """cast(itkLightObject obj) -> itkLog10ImageFilterIUS2IUS2"""
        return _itkLog10ImageFilterPython.itkLog10ImageFilterIUS2IUS2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLog10ImageFilterIUS2IUS2

        Create a new object of the class itkLog10ImageFilterIUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLog10ImageFilterIUS2IUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLog10ImageFilterIUS2IUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLog10ImageFilterIUS2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLog10ImageFilterIUS2IUS2.Clone = new_instancemethod(_itkLog10ImageFilterPython.itkLog10ImageFilterIUS2IUS2_Clone, None, itkLog10ImageFilterIUS2IUS2)
itkLog10ImageFilterIUS2IUS2_swigregister = _itkLog10ImageFilterPython.itkLog10ImageFilterIUS2IUS2_swigregister
itkLog10ImageFilterIUS2IUS2_swigregister(itkLog10ImageFilterIUS2IUS2)

def itkLog10ImageFilterIUS2IUS2___New_orig__() -> "itkLog10ImageFilterIUS2IUS2_Pointer":
    """itkLog10ImageFilterIUS2IUS2___New_orig__() -> itkLog10ImageFilterIUS2IUS2_Pointer"""
    return _itkLog10ImageFilterPython.itkLog10ImageFilterIUS2IUS2___New_orig__()

def itkLog10ImageFilterIUS2IUS2_cast(obj: 'itkLightObject') -> "itkLog10ImageFilterIUS2IUS2 *":
    """itkLog10ImageFilterIUS2IUS2_cast(itkLightObject obj) -> itkLog10ImageFilterIUS2IUS2"""
    return _itkLog10ImageFilterPython.itkLog10ImageFilterIUS2IUS2_cast(obj)

class itkLog10ImageFilterIUS3IUS3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUS3IUS3):
    """


    Computes the log10 of each pixel.

    The computation is performed using std::log10(x).

    C++ includes: itkLog10ImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkLog10ImageFilterIUS3IUS3_Pointer":
        """__New_orig__() -> itkLog10ImageFilterIUS3IUS3_Pointer"""
        return _itkLog10ImageFilterPython.itkLog10ImageFilterIUS3IUS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkLog10ImageFilterIUS3IUS3_Pointer":
        """Clone(itkLog10ImageFilterIUS3IUS3 self) -> itkLog10ImageFilterIUS3IUS3_Pointer"""
        return _itkLog10ImageFilterPython.itkLog10ImageFilterIUS3IUS3_Clone(self)

    InputConvertibleToDoubleCheck = _itkLog10ImageFilterPython.itkLog10ImageFilterIUS3IUS3_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkLog10ImageFilterPython.itkLog10ImageFilterIUS3IUS3_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkLog10ImageFilterPython.delete_itkLog10ImageFilterIUS3IUS3

    def cast(obj: 'itkLightObject') -> "itkLog10ImageFilterIUS3IUS3 *":
        """cast(itkLightObject obj) -> itkLog10ImageFilterIUS3IUS3"""
        return _itkLog10ImageFilterPython.itkLog10ImageFilterIUS3IUS3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkLog10ImageFilterIUS3IUS3

        Create a new object of the class itkLog10ImageFilterIUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLog10ImageFilterIUS3IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLog10ImageFilterIUS3IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLog10ImageFilterIUS3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkLog10ImageFilterIUS3IUS3.Clone = new_instancemethod(_itkLog10ImageFilterPython.itkLog10ImageFilterIUS3IUS3_Clone, None, itkLog10ImageFilterIUS3IUS3)
itkLog10ImageFilterIUS3IUS3_swigregister = _itkLog10ImageFilterPython.itkLog10ImageFilterIUS3IUS3_swigregister
itkLog10ImageFilterIUS3IUS3_swigregister(itkLog10ImageFilterIUS3IUS3)

def itkLog10ImageFilterIUS3IUS3___New_orig__() -> "itkLog10ImageFilterIUS3IUS3_Pointer":
    """itkLog10ImageFilterIUS3IUS3___New_orig__() -> itkLog10ImageFilterIUS3IUS3_Pointer"""
    return _itkLog10ImageFilterPython.itkLog10ImageFilterIUS3IUS3___New_orig__()

def itkLog10ImageFilterIUS3IUS3_cast(obj: 'itkLightObject') -> "itkLog10ImageFilterIUS3IUS3 *":
    """itkLog10ImageFilterIUS3IUS3_cast(itkLightObject obj) -> itkLog10ImageFilterIUS3IUS3"""
    return _itkLog10ImageFilterPython.itkLog10ImageFilterIUS3IUS3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def log10_image_filter(*args, **kwargs):
    """Procedural interface for Log10ImageFilter"""
    import itk
    instance = itk.Log10ImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def log10_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.Log10ImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.Log10ImageFilter.values()[0]
    else:
        filter_object = itk.Log10ImageFilter

    log10_image_filter.__doc__ = filter_object.__doc__
    log10_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    log10_image_filter.__doc__ += "Available Keyword Arguments:\n"
    log10_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



