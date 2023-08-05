# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkAbsImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkAbsImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkAbsImageFilterPython
            return _itkAbsImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkAbsImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkAbsImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkAbsImageFilterPython
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

def itkAbsImageFilterID3ID3_New():
  return itkAbsImageFilterID3ID3.New()


def itkAbsImageFilterID2ID2_New():
  return itkAbsImageFilterID2ID2.New()


def itkAbsImageFilterIF3IF3_New():
  return itkAbsImageFilterIF3IF3.New()


def itkAbsImageFilterIF2IF2_New():
  return itkAbsImageFilterIF2IF2.New()


def itkAbsImageFilterIUS3IUS3_New():
  return itkAbsImageFilterIUS3IUS3.New()


def itkAbsImageFilterIUS2IUS2_New():
  return itkAbsImageFilterIUS2IUS2.New()


def itkAbsImageFilterIUC3IUC3_New():
  return itkAbsImageFilterIUC3IUC3.New()


def itkAbsImageFilterIUC2IUC2_New():
  return itkAbsImageFilterIUC2IUC2.New()


def itkAbsImageFilterISS3ISS3_New():
  return itkAbsImageFilterISS3ISS3.New()


def itkAbsImageFilterISS2ISS2_New():
  return itkAbsImageFilterISS2ISS2.New()

class itkAbsImageFilterID2ID2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID2ID2):
    """


    Computes the absolute value of each pixel.

    itk::Math::abs() is used to perform the computation.

    C++ includes: itkAbsImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAbsImageFilterID2ID2_Pointer":
        """__New_orig__() -> itkAbsImageFilterID2ID2_Pointer"""
        return _itkAbsImageFilterPython.itkAbsImageFilterID2ID2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAbsImageFilterID2ID2_Pointer":
        """Clone(itkAbsImageFilterID2ID2 self) -> itkAbsImageFilterID2ID2_Pointer"""
        return _itkAbsImageFilterPython.itkAbsImageFilterID2ID2_Clone(self)

    ConvertibleCheck = _itkAbsImageFilterPython.itkAbsImageFilterID2ID2_ConvertibleCheck
    InputGreaterThanIntCheck = _itkAbsImageFilterPython.itkAbsImageFilterID2ID2_InputGreaterThanIntCheck
    __swig_destroy__ = _itkAbsImageFilterPython.delete_itkAbsImageFilterID2ID2

    def cast(obj: 'itkLightObject') -> "itkAbsImageFilterID2ID2 *":
        """cast(itkLightObject obj) -> itkAbsImageFilterID2ID2"""
        return _itkAbsImageFilterPython.itkAbsImageFilterID2ID2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkAbsImageFilterID2ID2

        Create a new object of the class itkAbsImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAbsImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAbsImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAbsImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAbsImageFilterID2ID2.Clone = new_instancemethod(_itkAbsImageFilterPython.itkAbsImageFilterID2ID2_Clone, None, itkAbsImageFilterID2ID2)
itkAbsImageFilterID2ID2_swigregister = _itkAbsImageFilterPython.itkAbsImageFilterID2ID2_swigregister
itkAbsImageFilterID2ID2_swigregister(itkAbsImageFilterID2ID2)

def itkAbsImageFilterID2ID2___New_orig__() -> "itkAbsImageFilterID2ID2_Pointer":
    """itkAbsImageFilterID2ID2___New_orig__() -> itkAbsImageFilterID2ID2_Pointer"""
    return _itkAbsImageFilterPython.itkAbsImageFilterID2ID2___New_orig__()

def itkAbsImageFilterID2ID2_cast(obj: 'itkLightObject') -> "itkAbsImageFilterID2ID2 *":
    """itkAbsImageFilterID2ID2_cast(itkLightObject obj) -> itkAbsImageFilterID2ID2"""
    return _itkAbsImageFilterPython.itkAbsImageFilterID2ID2_cast(obj)

class itkAbsImageFilterID3ID3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID3ID3):
    """


    Computes the absolute value of each pixel.

    itk::Math::abs() is used to perform the computation.

    C++ includes: itkAbsImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAbsImageFilterID3ID3_Pointer":
        """__New_orig__() -> itkAbsImageFilterID3ID3_Pointer"""
        return _itkAbsImageFilterPython.itkAbsImageFilterID3ID3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAbsImageFilterID3ID3_Pointer":
        """Clone(itkAbsImageFilterID3ID3 self) -> itkAbsImageFilterID3ID3_Pointer"""
        return _itkAbsImageFilterPython.itkAbsImageFilterID3ID3_Clone(self)

    ConvertibleCheck = _itkAbsImageFilterPython.itkAbsImageFilterID3ID3_ConvertibleCheck
    InputGreaterThanIntCheck = _itkAbsImageFilterPython.itkAbsImageFilterID3ID3_InputGreaterThanIntCheck
    __swig_destroy__ = _itkAbsImageFilterPython.delete_itkAbsImageFilterID3ID3

    def cast(obj: 'itkLightObject') -> "itkAbsImageFilterID3ID3 *":
        """cast(itkLightObject obj) -> itkAbsImageFilterID3ID3"""
        return _itkAbsImageFilterPython.itkAbsImageFilterID3ID3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkAbsImageFilterID3ID3

        Create a new object of the class itkAbsImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAbsImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAbsImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAbsImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAbsImageFilterID3ID3.Clone = new_instancemethod(_itkAbsImageFilterPython.itkAbsImageFilterID3ID3_Clone, None, itkAbsImageFilterID3ID3)
itkAbsImageFilterID3ID3_swigregister = _itkAbsImageFilterPython.itkAbsImageFilterID3ID3_swigregister
itkAbsImageFilterID3ID3_swigregister(itkAbsImageFilterID3ID3)

def itkAbsImageFilterID3ID3___New_orig__() -> "itkAbsImageFilterID3ID3_Pointer":
    """itkAbsImageFilterID3ID3___New_orig__() -> itkAbsImageFilterID3ID3_Pointer"""
    return _itkAbsImageFilterPython.itkAbsImageFilterID3ID3___New_orig__()

def itkAbsImageFilterID3ID3_cast(obj: 'itkLightObject') -> "itkAbsImageFilterID3ID3 *":
    """itkAbsImageFilterID3ID3_cast(itkLightObject obj) -> itkAbsImageFilterID3ID3"""
    return _itkAbsImageFilterPython.itkAbsImageFilterID3ID3_cast(obj)

class itkAbsImageFilterIF2IF2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF2IF2):
    """


    Computes the absolute value of each pixel.

    itk::Math::abs() is used to perform the computation.

    C++ includes: itkAbsImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAbsImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkAbsImageFilterIF2IF2_Pointer"""
        return _itkAbsImageFilterPython.itkAbsImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAbsImageFilterIF2IF2_Pointer":
        """Clone(itkAbsImageFilterIF2IF2 self) -> itkAbsImageFilterIF2IF2_Pointer"""
        return _itkAbsImageFilterPython.itkAbsImageFilterIF2IF2_Clone(self)

    ConvertibleCheck = _itkAbsImageFilterPython.itkAbsImageFilterIF2IF2_ConvertibleCheck
    InputGreaterThanIntCheck = _itkAbsImageFilterPython.itkAbsImageFilterIF2IF2_InputGreaterThanIntCheck
    __swig_destroy__ = _itkAbsImageFilterPython.delete_itkAbsImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkAbsImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkAbsImageFilterIF2IF2"""
        return _itkAbsImageFilterPython.itkAbsImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkAbsImageFilterIF2IF2

        Create a new object of the class itkAbsImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAbsImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAbsImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAbsImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAbsImageFilterIF2IF2.Clone = new_instancemethod(_itkAbsImageFilterPython.itkAbsImageFilterIF2IF2_Clone, None, itkAbsImageFilterIF2IF2)
itkAbsImageFilterIF2IF2_swigregister = _itkAbsImageFilterPython.itkAbsImageFilterIF2IF2_swigregister
itkAbsImageFilterIF2IF2_swigregister(itkAbsImageFilterIF2IF2)

def itkAbsImageFilterIF2IF2___New_orig__() -> "itkAbsImageFilterIF2IF2_Pointer":
    """itkAbsImageFilterIF2IF2___New_orig__() -> itkAbsImageFilterIF2IF2_Pointer"""
    return _itkAbsImageFilterPython.itkAbsImageFilterIF2IF2___New_orig__()

def itkAbsImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkAbsImageFilterIF2IF2 *":
    """itkAbsImageFilterIF2IF2_cast(itkLightObject obj) -> itkAbsImageFilterIF2IF2"""
    return _itkAbsImageFilterPython.itkAbsImageFilterIF2IF2_cast(obj)

class itkAbsImageFilterIF3IF3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF3IF3):
    """


    Computes the absolute value of each pixel.

    itk::Math::abs() is used to perform the computation.

    C++ includes: itkAbsImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAbsImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkAbsImageFilterIF3IF3_Pointer"""
        return _itkAbsImageFilterPython.itkAbsImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAbsImageFilterIF3IF3_Pointer":
        """Clone(itkAbsImageFilterIF3IF3 self) -> itkAbsImageFilterIF3IF3_Pointer"""
        return _itkAbsImageFilterPython.itkAbsImageFilterIF3IF3_Clone(self)

    ConvertibleCheck = _itkAbsImageFilterPython.itkAbsImageFilterIF3IF3_ConvertibleCheck
    InputGreaterThanIntCheck = _itkAbsImageFilterPython.itkAbsImageFilterIF3IF3_InputGreaterThanIntCheck
    __swig_destroy__ = _itkAbsImageFilterPython.delete_itkAbsImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkAbsImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkAbsImageFilterIF3IF3"""
        return _itkAbsImageFilterPython.itkAbsImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkAbsImageFilterIF3IF3

        Create a new object of the class itkAbsImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAbsImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAbsImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAbsImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAbsImageFilterIF3IF3.Clone = new_instancemethod(_itkAbsImageFilterPython.itkAbsImageFilterIF3IF3_Clone, None, itkAbsImageFilterIF3IF3)
itkAbsImageFilterIF3IF3_swigregister = _itkAbsImageFilterPython.itkAbsImageFilterIF3IF3_swigregister
itkAbsImageFilterIF3IF3_swigregister(itkAbsImageFilterIF3IF3)

def itkAbsImageFilterIF3IF3___New_orig__() -> "itkAbsImageFilterIF3IF3_Pointer":
    """itkAbsImageFilterIF3IF3___New_orig__() -> itkAbsImageFilterIF3IF3_Pointer"""
    return _itkAbsImageFilterPython.itkAbsImageFilterIF3IF3___New_orig__()

def itkAbsImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkAbsImageFilterIF3IF3 *":
    """itkAbsImageFilterIF3IF3_cast(itkLightObject obj) -> itkAbsImageFilterIF3IF3"""
    return _itkAbsImageFilterPython.itkAbsImageFilterIF3IF3_cast(obj)

class itkAbsImageFilterISS2ISS2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterISS2ISS2):
    """


    Computes the absolute value of each pixel.

    itk::Math::abs() is used to perform the computation.

    C++ includes: itkAbsImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAbsImageFilterISS2ISS2_Pointer":
        """__New_orig__() -> itkAbsImageFilterISS2ISS2_Pointer"""
        return _itkAbsImageFilterPython.itkAbsImageFilterISS2ISS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAbsImageFilterISS2ISS2_Pointer":
        """Clone(itkAbsImageFilterISS2ISS2 self) -> itkAbsImageFilterISS2ISS2_Pointer"""
        return _itkAbsImageFilterPython.itkAbsImageFilterISS2ISS2_Clone(self)

    ConvertibleCheck = _itkAbsImageFilterPython.itkAbsImageFilterISS2ISS2_ConvertibleCheck
    InputGreaterThanIntCheck = _itkAbsImageFilterPython.itkAbsImageFilterISS2ISS2_InputGreaterThanIntCheck
    __swig_destroy__ = _itkAbsImageFilterPython.delete_itkAbsImageFilterISS2ISS2

    def cast(obj: 'itkLightObject') -> "itkAbsImageFilterISS2ISS2 *":
        """cast(itkLightObject obj) -> itkAbsImageFilterISS2ISS2"""
        return _itkAbsImageFilterPython.itkAbsImageFilterISS2ISS2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkAbsImageFilterISS2ISS2

        Create a new object of the class itkAbsImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAbsImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAbsImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAbsImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAbsImageFilterISS2ISS2.Clone = new_instancemethod(_itkAbsImageFilterPython.itkAbsImageFilterISS2ISS2_Clone, None, itkAbsImageFilterISS2ISS2)
itkAbsImageFilterISS2ISS2_swigregister = _itkAbsImageFilterPython.itkAbsImageFilterISS2ISS2_swigregister
itkAbsImageFilterISS2ISS2_swigregister(itkAbsImageFilterISS2ISS2)

def itkAbsImageFilterISS2ISS2___New_orig__() -> "itkAbsImageFilterISS2ISS2_Pointer":
    """itkAbsImageFilterISS2ISS2___New_orig__() -> itkAbsImageFilterISS2ISS2_Pointer"""
    return _itkAbsImageFilterPython.itkAbsImageFilterISS2ISS2___New_orig__()

def itkAbsImageFilterISS2ISS2_cast(obj: 'itkLightObject') -> "itkAbsImageFilterISS2ISS2 *":
    """itkAbsImageFilterISS2ISS2_cast(itkLightObject obj) -> itkAbsImageFilterISS2ISS2"""
    return _itkAbsImageFilterPython.itkAbsImageFilterISS2ISS2_cast(obj)

class itkAbsImageFilterISS3ISS3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterISS3ISS3):
    """


    Computes the absolute value of each pixel.

    itk::Math::abs() is used to perform the computation.

    C++ includes: itkAbsImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAbsImageFilterISS3ISS3_Pointer":
        """__New_orig__() -> itkAbsImageFilterISS3ISS3_Pointer"""
        return _itkAbsImageFilterPython.itkAbsImageFilterISS3ISS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAbsImageFilterISS3ISS3_Pointer":
        """Clone(itkAbsImageFilterISS3ISS3 self) -> itkAbsImageFilterISS3ISS3_Pointer"""
        return _itkAbsImageFilterPython.itkAbsImageFilterISS3ISS3_Clone(self)

    ConvertibleCheck = _itkAbsImageFilterPython.itkAbsImageFilterISS3ISS3_ConvertibleCheck
    InputGreaterThanIntCheck = _itkAbsImageFilterPython.itkAbsImageFilterISS3ISS3_InputGreaterThanIntCheck
    __swig_destroy__ = _itkAbsImageFilterPython.delete_itkAbsImageFilterISS3ISS3

    def cast(obj: 'itkLightObject') -> "itkAbsImageFilterISS3ISS3 *":
        """cast(itkLightObject obj) -> itkAbsImageFilterISS3ISS3"""
        return _itkAbsImageFilterPython.itkAbsImageFilterISS3ISS3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkAbsImageFilterISS3ISS3

        Create a new object of the class itkAbsImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAbsImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAbsImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAbsImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAbsImageFilterISS3ISS3.Clone = new_instancemethod(_itkAbsImageFilterPython.itkAbsImageFilterISS3ISS3_Clone, None, itkAbsImageFilterISS3ISS3)
itkAbsImageFilterISS3ISS3_swigregister = _itkAbsImageFilterPython.itkAbsImageFilterISS3ISS3_swigregister
itkAbsImageFilterISS3ISS3_swigregister(itkAbsImageFilterISS3ISS3)

def itkAbsImageFilterISS3ISS3___New_orig__() -> "itkAbsImageFilterISS3ISS3_Pointer":
    """itkAbsImageFilterISS3ISS3___New_orig__() -> itkAbsImageFilterISS3ISS3_Pointer"""
    return _itkAbsImageFilterPython.itkAbsImageFilterISS3ISS3___New_orig__()

def itkAbsImageFilterISS3ISS3_cast(obj: 'itkLightObject') -> "itkAbsImageFilterISS3ISS3 *":
    """itkAbsImageFilterISS3ISS3_cast(itkLightObject obj) -> itkAbsImageFilterISS3ISS3"""
    return _itkAbsImageFilterPython.itkAbsImageFilterISS3ISS3_cast(obj)

class itkAbsImageFilterIUC2IUC2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUC2IUC2):
    """


    Computes the absolute value of each pixel.

    itk::Math::abs() is used to perform the computation.

    C++ includes: itkAbsImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAbsImageFilterIUC2IUC2_Pointer":
        """__New_orig__() -> itkAbsImageFilterIUC2IUC2_Pointer"""
        return _itkAbsImageFilterPython.itkAbsImageFilterIUC2IUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAbsImageFilterIUC2IUC2_Pointer":
        """Clone(itkAbsImageFilterIUC2IUC2 self) -> itkAbsImageFilterIUC2IUC2_Pointer"""
        return _itkAbsImageFilterPython.itkAbsImageFilterIUC2IUC2_Clone(self)

    ConvertibleCheck = _itkAbsImageFilterPython.itkAbsImageFilterIUC2IUC2_ConvertibleCheck
    InputGreaterThanIntCheck = _itkAbsImageFilterPython.itkAbsImageFilterIUC2IUC2_InputGreaterThanIntCheck
    __swig_destroy__ = _itkAbsImageFilterPython.delete_itkAbsImageFilterIUC2IUC2

    def cast(obj: 'itkLightObject') -> "itkAbsImageFilterIUC2IUC2 *":
        """cast(itkLightObject obj) -> itkAbsImageFilterIUC2IUC2"""
        return _itkAbsImageFilterPython.itkAbsImageFilterIUC2IUC2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkAbsImageFilterIUC2IUC2

        Create a new object of the class itkAbsImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAbsImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAbsImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAbsImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAbsImageFilterIUC2IUC2.Clone = new_instancemethod(_itkAbsImageFilterPython.itkAbsImageFilterIUC2IUC2_Clone, None, itkAbsImageFilterIUC2IUC2)
itkAbsImageFilterIUC2IUC2_swigregister = _itkAbsImageFilterPython.itkAbsImageFilterIUC2IUC2_swigregister
itkAbsImageFilterIUC2IUC2_swigregister(itkAbsImageFilterIUC2IUC2)

def itkAbsImageFilterIUC2IUC2___New_orig__() -> "itkAbsImageFilterIUC2IUC2_Pointer":
    """itkAbsImageFilterIUC2IUC2___New_orig__() -> itkAbsImageFilterIUC2IUC2_Pointer"""
    return _itkAbsImageFilterPython.itkAbsImageFilterIUC2IUC2___New_orig__()

def itkAbsImageFilterIUC2IUC2_cast(obj: 'itkLightObject') -> "itkAbsImageFilterIUC2IUC2 *":
    """itkAbsImageFilterIUC2IUC2_cast(itkLightObject obj) -> itkAbsImageFilterIUC2IUC2"""
    return _itkAbsImageFilterPython.itkAbsImageFilterIUC2IUC2_cast(obj)

class itkAbsImageFilterIUC3IUC3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUC3IUC3):
    """


    Computes the absolute value of each pixel.

    itk::Math::abs() is used to perform the computation.

    C++ includes: itkAbsImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAbsImageFilterIUC3IUC3_Pointer":
        """__New_orig__() -> itkAbsImageFilterIUC3IUC3_Pointer"""
        return _itkAbsImageFilterPython.itkAbsImageFilterIUC3IUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAbsImageFilterIUC3IUC3_Pointer":
        """Clone(itkAbsImageFilterIUC3IUC3 self) -> itkAbsImageFilterIUC3IUC3_Pointer"""
        return _itkAbsImageFilterPython.itkAbsImageFilterIUC3IUC3_Clone(self)

    ConvertibleCheck = _itkAbsImageFilterPython.itkAbsImageFilterIUC3IUC3_ConvertibleCheck
    InputGreaterThanIntCheck = _itkAbsImageFilterPython.itkAbsImageFilterIUC3IUC3_InputGreaterThanIntCheck
    __swig_destroy__ = _itkAbsImageFilterPython.delete_itkAbsImageFilterIUC3IUC3

    def cast(obj: 'itkLightObject') -> "itkAbsImageFilterIUC3IUC3 *":
        """cast(itkLightObject obj) -> itkAbsImageFilterIUC3IUC3"""
        return _itkAbsImageFilterPython.itkAbsImageFilterIUC3IUC3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkAbsImageFilterIUC3IUC3

        Create a new object of the class itkAbsImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAbsImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAbsImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAbsImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAbsImageFilterIUC3IUC3.Clone = new_instancemethod(_itkAbsImageFilterPython.itkAbsImageFilterIUC3IUC3_Clone, None, itkAbsImageFilterIUC3IUC3)
itkAbsImageFilterIUC3IUC3_swigregister = _itkAbsImageFilterPython.itkAbsImageFilterIUC3IUC3_swigregister
itkAbsImageFilterIUC3IUC3_swigregister(itkAbsImageFilterIUC3IUC3)

def itkAbsImageFilterIUC3IUC3___New_orig__() -> "itkAbsImageFilterIUC3IUC3_Pointer":
    """itkAbsImageFilterIUC3IUC3___New_orig__() -> itkAbsImageFilterIUC3IUC3_Pointer"""
    return _itkAbsImageFilterPython.itkAbsImageFilterIUC3IUC3___New_orig__()

def itkAbsImageFilterIUC3IUC3_cast(obj: 'itkLightObject') -> "itkAbsImageFilterIUC3IUC3 *":
    """itkAbsImageFilterIUC3IUC3_cast(itkLightObject obj) -> itkAbsImageFilterIUC3IUC3"""
    return _itkAbsImageFilterPython.itkAbsImageFilterIUC3IUC3_cast(obj)

class itkAbsImageFilterIUS2IUS2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUS2IUS2):
    """


    Computes the absolute value of each pixel.

    itk::Math::abs() is used to perform the computation.

    C++ includes: itkAbsImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAbsImageFilterIUS2IUS2_Pointer":
        """__New_orig__() -> itkAbsImageFilterIUS2IUS2_Pointer"""
        return _itkAbsImageFilterPython.itkAbsImageFilterIUS2IUS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAbsImageFilterIUS2IUS2_Pointer":
        """Clone(itkAbsImageFilterIUS2IUS2 self) -> itkAbsImageFilterIUS2IUS2_Pointer"""
        return _itkAbsImageFilterPython.itkAbsImageFilterIUS2IUS2_Clone(self)

    ConvertibleCheck = _itkAbsImageFilterPython.itkAbsImageFilterIUS2IUS2_ConvertibleCheck
    InputGreaterThanIntCheck = _itkAbsImageFilterPython.itkAbsImageFilterIUS2IUS2_InputGreaterThanIntCheck
    __swig_destroy__ = _itkAbsImageFilterPython.delete_itkAbsImageFilterIUS2IUS2

    def cast(obj: 'itkLightObject') -> "itkAbsImageFilterIUS2IUS2 *":
        """cast(itkLightObject obj) -> itkAbsImageFilterIUS2IUS2"""
        return _itkAbsImageFilterPython.itkAbsImageFilterIUS2IUS2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkAbsImageFilterIUS2IUS2

        Create a new object of the class itkAbsImageFilterIUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAbsImageFilterIUS2IUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAbsImageFilterIUS2IUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAbsImageFilterIUS2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAbsImageFilterIUS2IUS2.Clone = new_instancemethod(_itkAbsImageFilterPython.itkAbsImageFilterIUS2IUS2_Clone, None, itkAbsImageFilterIUS2IUS2)
itkAbsImageFilterIUS2IUS2_swigregister = _itkAbsImageFilterPython.itkAbsImageFilterIUS2IUS2_swigregister
itkAbsImageFilterIUS2IUS2_swigregister(itkAbsImageFilterIUS2IUS2)

def itkAbsImageFilterIUS2IUS2___New_orig__() -> "itkAbsImageFilterIUS2IUS2_Pointer":
    """itkAbsImageFilterIUS2IUS2___New_orig__() -> itkAbsImageFilterIUS2IUS2_Pointer"""
    return _itkAbsImageFilterPython.itkAbsImageFilterIUS2IUS2___New_orig__()

def itkAbsImageFilterIUS2IUS2_cast(obj: 'itkLightObject') -> "itkAbsImageFilterIUS2IUS2 *":
    """itkAbsImageFilterIUS2IUS2_cast(itkLightObject obj) -> itkAbsImageFilterIUS2IUS2"""
    return _itkAbsImageFilterPython.itkAbsImageFilterIUS2IUS2_cast(obj)

class itkAbsImageFilterIUS3IUS3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUS3IUS3):
    """


    Computes the absolute value of each pixel.

    itk::Math::abs() is used to perform the computation.

    C++ includes: itkAbsImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAbsImageFilterIUS3IUS3_Pointer":
        """__New_orig__() -> itkAbsImageFilterIUS3IUS3_Pointer"""
        return _itkAbsImageFilterPython.itkAbsImageFilterIUS3IUS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAbsImageFilterIUS3IUS3_Pointer":
        """Clone(itkAbsImageFilterIUS3IUS3 self) -> itkAbsImageFilterIUS3IUS3_Pointer"""
        return _itkAbsImageFilterPython.itkAbsImageFilterIUS3IUS3_Clone(self)

    ConvertibleCheck = _itkAbsImageFilterPython.itkAbsImageFilterIUS3IUS3_ConvertibleCheck
    InputGreaterThanIntCheck = _itkAbsImageFilterPython.itkAbsImageFilterIUS3IUS3_InputGreaterThanIntCheck
    __swig_destroy__ = _itkAbsImageFilterPython.delete_itkAbsImageFilterIUS3IUS3

    def cast(obj: 'itkLightObject') -> "itkAbsImageFilterIUS3IUS3 *":
        """cast(itkLightObject obj) -> itkAbsImageFilterIUS3IUS3"""
        return _itkAbsImageFilterPython.itkAbsImageFilterIUS3IUS3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkAbsImageFilterIUS3IUS3

        Create a new object of the class itkAbsImageFilterIUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAbsImageFilterIUS3IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAbsImageFilterIUS3IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAbsImageFilterIUS3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAbsImageFilterIUS3IUS3.Clone = new_instancemethod(_itkAbsImageFilterPython.itkAbsImageFilterIUS3IUS3_Clone, None, itkAbsImageFilterIUS3IUS3)
itkAbsImageFilterIUS3IUS3_swigregister = _itkAbsImageFilterPython.itkAbsImageFilterIUS3IUS3_swigregister
itkAbsImageFilterIUS3IUS3_swigregister(itkAbsImageFilterIUS3IUS3)

def itkAbsImageFilterIUS3IUS3___New_orig__() -> "itkAbsImageFilterIUS3IUS3_Pointer":
    """itkAbsImageFilterIUS3IUS3___New_orig__() -> itkAbsImageFilterIUS3IUS3_Pointer"""
    return _itkAbsImageFilterPython.itkAbsImageFilterIUS3IUS3___New_orig__()

def itkAbsImageFilterIUS3IUS3_cast(obj: 'itkLightObject') -> "itkAbsImageFilterIUS3IUS3 *":
    """itkAbsImageFilterIUS3IUS3_cast(itkLightObject obj) -> itkAbsImageFilterIUS3IUS3"""
    return _itkAbsImageFilterPython.itkAbsImageFilterIUS3IUS3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def abs_image_filter(*args, **kwargs):
    """Procedural interface for AbsImageFilter"""
    import itk
    instance = itk.AbsImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def abs_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.AbsImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.AbsImageFilter.values()[0]
    else:
        filter_object = itk.AbsImageFilter

    abs_image_filter.__doc__ = filter_object.__doc__
    abs_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    abs_image_filter.__doc__ += "Available Keyword Arguments:\n"
    abs_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



