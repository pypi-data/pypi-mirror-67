# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkMeanImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkMeanImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkMeanImageFilterPython
            return _itkMeanImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkMeanImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkMeanImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkMeanImageFilterPython
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


import itkBoxImageFilterPython
import itkImageToImageFilterAPython
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

def itkMeanImageFilterID3ID3_New():
  return itkMeanImageFilterID3ID3.New()


def itkMeanImageFilterID2ID2_New():
  return itkMeanImageFilterID2ID2.New()


def itkMeanImageFilterIF3IF3_New():
  return itkMeanImageFilterIF3IF3.New()


def itkMeanImageFilterIF2IF2_New():
  return itkMeanImageFilterIF2IF2.New()


def itkMeanImageFilterIUS3IUS3_New():
  return itkMeanImageFilterIUS3IUS3.New()


def itkMeanImageFilterIUS2IUS2_New():
  return itkMeanImageFilterIUS2IUS2.New()


def itkMeanImageFilterIUC3IUC3_New():
  return itkMeanImageFilterIUC3IUC3.New()


def itkMeanImageFilterIUC2IUC2_New():
  return itkMeanImageFilterIUC2IUC2.New()


def itkMeanImageFilterISS3ISS3_New():
  return itkMeanImageFilterISS3ISS3.New()


def itkMeanImageFilterISS2ISS2_New():
  return itkMeanImageFilterISS2ISS2.New()

class itkMeanImageFilterID2ID2(itkBoxImageFilterPython.itkBoxImageFilterID2ID2):
    """


    Applies an averaging filter to an image.

    Computes an image where a given pixel is the mean value of the the
    pixels in a neighborhood about the corresponding input pixel.

    A mean filter is one of the family of linear filters.

    See:  Image

    See:  Neighborhood

    See:  NeighborhoodOperator

    See:  NeighborhoodIterator

    C++ includes: itkMeanImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMeanImageFilterID2ID2_Pointer":
        """__New_orig__() -> itkMeanImageFilterID2ID2_Pointer"""
        return _itkMeanImageFilterPython.itkMeanImageFilterID2ID2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMeanImageFilterID2ID2_Pointer":
        """Clone(itkMeanImageFilterID2ID2 self) -> itkMeanImageFilterID2ID2_Pointer"""
        return _itkMeanImageFilterPython.itkMeanImageFilterID2ID2_Clone(self)

    InputHasNumericTraitsCheck = _itkMeanImageFilterPython.itkMeanImageFilterID2ID2_InputHasNumericTraitsCheck
    __swig_destroy__ = _itkMeanImageFilterPython.delete_itkMeanImageFilterID2ID2

    def cast(obj: 'itkLightObject') -> "itkMeanImageFilterID2ID2 *":
        """cast(itkLightObject obj) -> itkMeanImageFilterID2ID2"""
        return _itkMeanImageFilterPython.itkMeanImageFilterID2ID2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkMeanImageFilterID2ID2

        Create a new object of the class itkMeanImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeanImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeanImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeanImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMeanImageFilterID2ID2.Clone = new_instancemethod(_itkMeanImageFilterPython.itkMeanImageFilterID2ID2_Clone, None, itkMeanImageFilterID2ID2)
itkMeanImageFilterID2ID2_swigregister = _itkMeanImageFilterPython.itkMeanImageFilterID2ID2_swigregister
itkMeanImageFilterID2ID2_swigregister(itkMeanImageFilterID2ID2)

def itkMeanImageFilterID2ID2___New_orig__() -> "itkMeanImageFilterID2ID2_Pointer":
    """itkMeanImageFilterID2ID2___New_orig__() -> itkMeanImageFilterID2ID2_Pointer"""
    return _itkMeanImageFilterPython.itkMeanImageFilterID2ID2___New_orig__()

def itkMeanImageFilterID2ID2_cast(obj: 'itkLightObject') -> "itkMeanImageFilterID2ID2 *":
    """itkMeanImageFilterID2ID2_cast(itkLightObject obj) -> itkMeanImageFilterID2ID2"""
    return _itkMeanImageFilterPython.itkMeanImageFilterID2ID2_cast(obj)

class itkMeanImageFilterID3ID3(itkBoxImageFilterPython.itkBoxImageFilterID3ID3):
    """


    Applies an averaging filter to an image.

    Computes an image where a given pixel is the mean value of the the
    pixels in a neighborhood about the corresponding input pixel.

    A mean filter is one of the family of linear filters.

    See:  Image

    See:  Neighborhood

    See:  NeighborhoodOperator

    See:  NeighborhoodIterator

    C++ includes: itkMeanImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMeanImageFilterID3ID3_Pointer":
        """__New_orig__() -> itkMeanImageFilterID3ID3_Pointer"""
        return _itkMeanImageFilterPython.itkMeanImageFilterID3ID3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMeanImageFilterID3ID3_Pointer":
        """Clone(itkMeanImageFilterID3ID3 self) -> itkMeanImageFilterID3ID3_Pointer"""
        return _itkMeanImageFilterPython.itkMeanImageFilterID3ID3_Clone(self)

    InputHasNumericTraitsCheck = _itkMeanImageFilterPython.itkMeanImageFilterID3ID3_InputHasNumericTraitsCheck
    __swig_destroy__ = _itkMeanImageFilterPython.delete_itkMeanImageFilterID3ID3

    def cast(obj: 'itkLightObject') -> "itkMeanImageFilterID3ID3 *":
        """cast(itkLightObject obj) -> itkMeanImageFilterID3ID3"""
        return _itkMeanImageFilterPython.itkMeanImageFilterID3ID3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkMeanImageFilterID3ID3

        Create a new object of the class itkMeanImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeanImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeanImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeanImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMeanImageFilterID3ID3.Clone = new_instancemethod(_itkMeanImageFilterPython.itkMeanImageFilterID3ID3_Clone, None, itkMeanImageFilterID3ID3)
itkMeanImageFilterID3ID3_swigregister = _itkMeanImageFilterPython.itkMeanImageFilterID3ID3_swigregister
itkMeanImageFilterID3ID3_swigregister(itkMeanImageFilterID3ID3)

def itkMeanImageFilterID3ID3___New_orig__() -> "itkMeanImageFilterID3ID3_Pointer":
    """itkMeanImageFilterID3ID3___New_orig__() -> itkMeanImageFilterID3ID3_Pointer"""
    return _itkMeanImageFilterPython.itkMeanImageFilterID3ID3___New_orig__()

def itkMeanImageFilterID3ID3_cast(obj: 'itkLightObject') -> "itkMeanImageFilterID3ID3 *":
    """itkMeanImageFilterID3ID3_cast(itkLightObject obj) -> itkMeanImageFilterID3ID3"""
    return _itkMeanImageFilterPython.itkMeanImageFilterID3ID3_cast(obj)

class itkMeanImageFilterIF2IF2(itkBoxImageFilterPython.itkBoxImageFilterIF2IF2):
    """


    Applies an averaging filter to an image.

    Computes an image where a given pixel is the mean value of the the
    pixels in a neighborhood about the corresponding input pixel.

    A mean filter is one of the family of linear filters.

    See:  Image

    See:  Neighborhood

    See:  NeighborhoodOperator

    See:  NeighborhoodIterator

    C++ includes: itkMeanImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMeanImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkMeanImageFilterIF2IF2_Pointer"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMeanImageFilterIF2IF2_Pointer":
        """Clone(itkMeanImageFilterIF2IF2 self) -> itkMeanImageFilterIF2IF2_Pointer"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIF2IF2_Clone(self)

    InputHasNumericTraitsCheck = _itkMeanImageFilterPython.itkMeanImageFilterIF2IF2_InputHasNumericTraitsCheck
    __swig_destroy__ = _itkMeanImageFilterPython.delete_itkMeanImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkMeanImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkMeanImageFilterIF2IF2"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkMeanImageFilterIF2IF2

        Create a new object of the class itkMeanImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeanImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeanImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeanImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMeanImageFilterIF2IF2.Clone = new_instancemethod(_itkMeanImageFilterPython.itkMeanImageFilterIF2IF2_Clone, None, itkMeanImageFilterIF2IF2)
itkMeanImageFilterIF2IF2_swigregister = _itkMeanImageFilterPython.itkMeanImageFilterIF2IF2_swigregister
itkMeanImageFilterIF2IF2_swigregister(itkMeanImageFilterIF2IF2)

def itkMeanImageFilterIF2IF2___New_orig__() -> "itkMeanImageFilterIF2IF2_Pointer":
    """itkMeanImageFilterIF2IF2___New_orig__() -> itkMeanImageFilterIF2IF2_Pointer"""
    return _itkMeanImageFilterPython.itkMeanImageFilterIF2IF2___New_orig__()

def itkMeanImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkMeanImageFilterIF2IF2 *":
    """itkMeanImageFilterIF2IF2_cast(itkLightObject obj) -> itkMeanImageFilterIF2IF2"""
    return _itkMeanImageFilterPython.itkMeanImageFilterIF2IF2_cast(obj)

class itkMeanImageFilterIF3IF3(itkBoxImageFilterPython.itkBoxImageFilterIF3IF3):
    """


    Applies an averaging filter to an image.

    Computes an image where a given pixel is the mean value of the the
    pixels in a neighborhood about the corresponding input pixel.

    A mean filter is one of the family of linear filters.

    See:  Image

    See:  Neighborhood

    See:  NeighborhoodOperator

    See:  NeighborhoodIterator

    C++ includes: itkMeanImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMeanImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkMeanImageFilterIF3IF3_Pointer"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMeanImageFilterIF3IF3_Pointer":
        """Clone(itkMeanImageFilterIF3IF3 self) -> itkMeanImageFilterIF3IF3_Pointer"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIF3IF3_Clone(self)

    InputHasNumericTraitsCheck = _itkMeanImageFilterPython.itkMeanImageFilterIF3IF3_InputHasNumericTraitsCheck
    __swig_destroy__ = _itkMeanImageFilterPython.delete_itkMeanImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkMeanImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkMeanImageFilterIF3IF3"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkMeanImageFilterIF3IF3

        Create a new object of the class itkMeanImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeanImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeanImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeanImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMeanImageFilterIF3IF3.Clone = new_instancemethod(_itkMeanImageFilterPython.itkMeanImageFilterIF3IF3_Clone, None, itkMeanImageFilterIF3IF3)
itkMeanImageFilterIF3IF3_swigregister = _itkMeanImageFilterPython.itkMeanImageFilterIF3IF3_swigregister
itkMeanImageFilterIF3IF3_swigregister(itkMeanImageFilterIF3IF3)

def itkMeanImageFilterIF3IF3___New_orig__() -> "itkMeanImageFilterIF3IF3_Pointer":
    """itkMeanImageFilterIF3IF3___New_orig__() -> itkMeanImageFilterIF3IF3_Pointer"""
    return _itkMeanImageFilterPython.itkMeanImageFilterIF3IF3___New_orig__()

def itkMeanImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkMeanImageFilterIF3IF3 *":
    """itkMeanImageFilterIF3IF3_cast(itkLightObject obj) -> itkMeanImageFilterIF3IF3"""
    return _itkMeanImageFilterPython.itkMeanImageFilterIF3IF3_cast(obj)

class itkMeanImageFilterISS2ISS2(itkBoxImageFilterPython.itkBoxImageFilterISS2ISS2):
    """


    Applies an averaging filter to an image.

    Computes an image where a given pixel is the mean value of the the
    pixels in a neighborhood about the corresponding input pixel.

    A mean filter is one of the family of linear filters.

    See:  Image

    See:  Neighborhood

    See:  NeighborhoodOperator

    See:  NeighborhoodIterator

    C++ includes: itkMeanImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMeanImageFilterISS2ISS2_Pointer":
        """__New_orig__() -> itkMeanImageFilterISS2ISS2_Pointer"""
        return _itkMeanImageFilterPython.itkMeanImageFilterISS2ISS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMeanImageFilterISS2ISS2_Pointer":
        """Clone(itkMeanImageFilterISS2ISS2 self) -> itkMeanImageFilterISS2ISS2_Pointer"""
        return _itkMeanImageFilterPython.itkMeanImageFilterISS2ISS2_Clone(self)

    InputHasNumericTraitsCheck = _itkMeanImageFilterPython.itkMeanImageFilterISS2ISS2_InputHasNumericTraitsCheck
    __swig_destroy__ = _itkMeanImageFilterPython.delete_itkMeanImageFilterISS2ISS2

    def cast(obj: 'itkLightObject') -> "itkMeanImageFilterISS2ISS2 *":
        """cast(itkLightObject obj) -> itkMeanImageFilterISS2ISS2"""
        return _itkMeanImageFilterPython.itkMeanImageFilterISS2ISS2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkMeanImageFilterISS2ISS2

        Create a new object of the class itkMeanImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeanImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeanImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeanImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMeanImageFilterISS2ISS2.Clone = new_instancemethod(_itkMeanImageFilterPython.itkMeanImageFilterISS2ISS2_Clone, None, itkMeanImageFilterISS2ISS2)
itkMeanImageFilterISS2ISS2_swigregister = _itkMeanImageFilterPython.itkMeanImageFilterISS2ISS2_swigregister
itkMeanImageFilterISS2ISS2_swigregister(itkMeanImageFilterISS2ISS2)

def itkMeanImageFilterISS2ISS2___New_orig__() -> "itkMeanImageFilterISS2ISS2_Pointer":
    """itkMeanImageFilterISS2ISS2___New_orig__() -> itkMeanImageFilterISS2ISS2_Pointer"""
    return _itkMeanImageFilterPython.itkMeanImageFilterISS2ISS2___New_orig__()

def itkMeanImageFilterISS2ISS2_cast(obj: 'itkLightObject') -> "itkMeanImageFilterISS2ISS2 *":
    """itkMeanImageFilterISS2ISS2_cast(itkLightObject obj) -> itkMeanImageFilterISS2ISS2"""
    return _itkMeanImageFilterPython.itkMeanImageFilterISS2ISS2_cast(obj)

class itkMeanImageFilterISS3ISS3(itkBoxImageFilterPython.itkBoxImageFilterISS3ISS3):
    """


    Applies an averaging filter to an image.

    Computes an image where a given pixel is the mean value of the the
    pixels in a neighborhood about the corresponding input pixel.

    A mean filter is one of the family of linear filters.

    See:  Image

    See:  Neighborhood

    See:  NeighborhoodOperator

    See:  NeighborhoodIterator

    C++ includes: itkMeanImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMeanImageFilterISS3ISS3_Pointer":
        """__New_orig__() -> itkMeanImageFilterISS3ISS3_Pointer"""
        return _itkMeanImageFilterPython.itkMeanImageFilterISS3ISS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMeanImageFilterISS3ISS3_Pointer":
        """Clone(itkMeanImageFilterISS3ISS3 self) -> itkMeanImageFilterISS3ISS3_Pointer"""
        return _itkMeanImageFilterPython.itkMeanImageFilterISS3ISS3_Clone(self)

    InputHasNumericTraitsCheck = _itkMeanImageFilterPython.itkMeanImageFilterISS3ISS3_InputHasNumericTraitsCheck
    __swig_destroy__ = _itkMeanImageFilterPython.delete_itkMeanImageFilterISS3ISS3

    def cast(obj: 'itkLightObject') -> "itkMeanImageFilterISS3ISS3 *":
        """cast(itkLightObject obj) -> itkMeanImageFilterISS3ISS3"""
        return _itkMeanImageFilterPython.itkMeanImageFilterISS3ISS3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkMeanImageFilterISS3ISS3

        Create a new object of the class itkMeanImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeanImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeanImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeanImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMeanImageFilterISS3ISS3.Clone = new_instancemethod(_itkMeanImageFilterPython.itkMeanImageFilterISS3ISS3_Clone, None, itkMeanImageFilterISS3ISS3)
itkMeanImageFilterISS3ISS3_swigregister = _itkMeanImageFilterPython.itkMeanImageFilterISS3ISS3_swigregister
itkMeanImageFilterISS3ISS3_swigregister(itkMeanImageFilterISS3ISS3)

def itkMeanImageFilterISS3ISS3___New_orig__() -> "itkMeanImageFilterISS3ISS3_Pointer":
    """itkMeanImageFilterISS3ISS3___New_orig__() -> itkMeanImageFilterISS3ISS3_Pointer"""
    return _itkMeanImageFilterPython.itkMeanImageFilterISS3ISS3___New_orig__()

def itkMeanImageFilterISS3ISS3_cast(obj: 'itkLightObject') -> "itkMeanImageFilterISS3ISS3 *":
    """itkMeanImageFilterISS3ISS3_cast(itkLightObject obj) -> itkMeanImageFilterISS3ISS3"""
    return _itkMeanImageFilterPython.itkMeanImageFilterISS3ISS3_cast(obj)

class itkMeanImageFilterIUC2IUC2(itkBoxImageFilterPython.itkBoxImageFilterIUC2IUC2):
    """


    Applies an averaging filter to an image.

    Computes an image where a given pixel is the mean value of the the
    pixels in a neighborhood about the corresponding input pixel.

    A mean filter is one of the family of linear filters.

    See:  Image

    See:  Neighborhood

    See:  NeighborhoodOperator

    See:  NeighborhoodIterator

    C++ includes: itkMeanImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMeanImageFilterIUC2IUC2_Pointer":
        """__New_orig__() -> itkMeanImageFilterIUC2IUC2_Pointer"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIUC2IUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMeanImageFilterIUC2IUC2_Pointer":
        """Clone(itkMeanImageFilterIUC2IUC2 self) -> itkMeanImageFilterIUC2IUC2_Pointer"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIUC2IUC2_Clone(self)

    InputHasNumericTraitsCheck = _itkMeanImageFilterPython.itkMeanImageFilterIUC2IUC2_InputHasNumericTraitsCheck
    __swig_destroy__ = _itkMeanImageFilterPython.delete_itkMeanImageFilterIUC2IUC2

    def cast(obj: 'itkLightObject') -> "itkMeanImageFilterIUC2IUC2 *":
        """cast(itkLightObject obj) -> itkMeanImageFilterIUC2IUC2"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIUC2IUC2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkMeanImageFilterIUC2IUC2

        Create a new object of the class itkMeanImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeanImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeanImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeanImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMeanImageFilterIUC2IUC2.Clone = new_instancemethod(_itkMeanImageFilterPython.itkMeanImageFilterIUC2IUC2_Clone, None, itkMeanImageFilterIUC2IUC2)
itkMeanImageFilterIUC2IUC2_swigregister = _itkMeanImageFilterPython.itkMeanImageFilterIUC2IUC2_swigregister
itkMeanImageFilterIUC2IUC2_swigregister(itkMeanImageFilterIUC2IUC2)

def itkMeanImageFilterIUC2IUC2___New_orig__() -> "itkMeanImageFilterIUC2IUC2_Pointer":
    """itkMeanImageFilterIUC2IUC2___New_orig__() -> itkMeanImageFilterIUC2IUC2_Pointer"""
    return _itkMeanImageFilterPython.itkMeanImageFilterIUC2IUC2___New_orig__()

def itkMeanImageFilterIUC2IUC2_cast(obj: 'itkLightObject') -> "itkMeanImageFilterIUC2IUC2 *":
    """itkMeanImageFilterIUC2IUC2_cast(itkLightObject obj) -> itkMeanImageFilterIUC2IUC2"""
    return _itkMeanImageFilterPython.itkMeanImageFilterIUC2IUC2_cast(obj)

class itkMeanImageFilterIUC3IUC3(itkBoxImageFilterPython.itkBoxImageFilterIUC3IUC3):
    """


    Applies an averaging filter to an image.

    Computes an image where a given pixel is the mean value of the the
    pixels in a neighborhood about the corresponding input pixel.

    A mean filter is one of the family of linear filters.

    See:  Image

    See:  Neighborhood

    See:  NeighborhoodOperator

    See:  NeighborhoodIterator

    C++ includes: itkMeanImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMeanImageFilterIUC3IUC3_Pointer":
        """__New_orig__() -> itkMeanImageFilterIUC3IUC3_Pointer"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIUC3IUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMeanImageFilterIUC3IUC3_Pointer":
        """Clone(itkMeanImageFilterIUC3IUC3 self) -> itkMeanImageFilterIUC3IUC3_Pointer"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIUC3IUC3_Clone(self)

    InputHasNumericTraitsCheck = _itkMeanImageFilterPython.itkMeanImageFilterIUC3IUC3_InputHasNumericTraitsCheck
    __swig_destroy__ = _itkMeanImageFilterPython.delete_itkMeanImageFilterIUC3IUC3

    def cast(obj: 'itkLightObject') -> "itkMeanImageFilterIUC3IUC3 *":
        """cast(itkLightObject obj) -> itkMeanImageFilterIUC3IUC3"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIUC3IUC3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkMeanImageFilterIUC3IUC3

        Create a new object of the class itkMeanImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeanImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeanImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeanImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMeanImageFilterIUC3IUC3.Clone = new_instancemethod(_itkMeanImageFilterPython.itkMeanImageFilterIUC3IUC3_Clone, None, itkMeanImageFilterIUC3IUC3)
itkMeanImageFilterIUC3IUC3_swigregister = _itkMeanImageFilterPython.itkMeanImageFilterIUC3IUC3_swigregister
itkMeanImageFilterIUC3IUC3_swigregister(itkMeanImageFilterIUC3IUC3)

def itkMeanImageFilterIUC3IUC3___New_orig__() -> "itkMeanImageFilterIUC3IUC3_Pointer":
    """itkMeanImageFilterIUC3IUC3___New_orig__() -> itkMeanImageFilterIUC3IUC3_Pointer"""
    return _itkMeanImageFilterPython.itkMeanImageFilterIUC3IUC3___New_orig__()

def itkMeanImageFilterIUC3IUC3_cast(obj: 'itkLightObject') -> "itkMeanImageFilterIUC3IUC3 *":
    """itkMeanImageFilterIUC3IUC3_cast(itkLightObject obj) -> itkMeanImageFilterIUC3IUC3"""
    return _itkMeanImageFilterPython.itkMeanImageFilterIUC3IUC3_cast(obj)

class itkMeanImageFilterIUS2IUS2(itkBoxImageFilterPython.itkBoxImageFilterIUS2IUS2):
    """


    Applies an averaging filter to an image.

    Computes an image where a given pixel is the mean value of the the
    pixels in a neighborhood about the corresponding input pixel.

    A mean filter is one of the family of linear filters.

    See:  Image

    See:  Neighborhood

    See:  NeighborhoodOperator

    See:  NeighborhoodIterator

    C++ includes: itkMeanImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMeanImageFilterIUS2IUS2_Pointer":
        """__New_orig__() -> itkMeanImageFilterIUS2IUS2_Pointer"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIUS2IUS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMeanImageFilterIUS2IUS2_Pointer":
        """Clone(itkMeanImageFilterIUS2IUS2 self) -> itkMeanImageFilterIUS2IUS2_Pointer"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIUS2IUS2_Clone(self)

    InputHasNumericTraitsCheck = _itkMeanImageFilterPython.itkMeanImageFilterIUS2IUS2_InputHasNumericTraitsCheck
    __swig_destroy__ = _itkMeanImageFilterPython.delete_itkMeanImageFilterIUS2IUS2

    def cast(obj: 'itkLightObject') -> "itkMeanImageFilterIUS2IUS2 *":
        """cast(itkLightObject obj) -> itkMeanImageFilterIUS2IUS2"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIUS2IUS2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkMeanImageFilterIUS2IUS2

        Create a new object of the class itkMeanImageFilterIUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeanImageFilterIUS2IUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeanImageFilterIUS2IUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeanImageFilterIUS2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMeanImageFilterIUS2IUS2.Clone = new_instancemethod(_itkMeanImageFilterPython.itkMeanImageFilterIUS2IUS2_Clone, None, itkMeanImageFilterIUS2IUS2)
itkMeanImageFilterIUS2IUS2_swigregister = _itkMeanImageFilterPython.itkMeanImageFilterIUS2IUS2_swigregister
itkMeanImageFilterIUS2IUS2_swigregister(itkMeanImageFilterIUS2IUS2)

def itkMeanImageFilterIUS2IUS2___New_orig__() -> "itkMeanImageFilterIUS2IUS2_Pointer":
    """itkMeanImageFilterIUS2IUS2___New_orig__() -> itkMeanImageFilterIUS2IUS2_Pointer"""
    return _itkMeanImageFilterPython.itkMeanImageFilterIUS2IUS2___New_orig__()

def itkMeanImageFilterIUS2IUS2_cast(obj: 'itkLightObject') -> "itkMeanImageFilterIUS2IUS2 *":
    """itkMeanImageFilterIUS2IUS2_cast(itkLightObject obj) -> itkMeanImageFilterIUS2IUS2"""
    return _itkMeanImageFilterPython.itkMeanImageFilterIUS2IUS2_cast(obj)

class itkMeanImageFilterIUS3IUS3(itkBoxImageFilterPython.itkBoxImageFilterIUS3IUS3):
    """


    Applies an averaging filter to an image.

    Computes an image where a given pixel is the mean value of the the
    pixels in a neighborhood about the corresponding input pixel.

    A mean filter is one of the family of linear filters.

    See:  Image

    See:  Neighborhood

    See:  NeighborhoodOperator

    See:  NeighborhoodIterator

    C++ includes: itkMeanImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMeanImageFilterIUS3IUS3_Pointer":
        """__New_orig__() -> itkMeanImageFilterIUS3IUS3_Pointer"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIUS3IUS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMeanImageFilterIUS3IUS3_Pointer":
        """Clone(itkMeanImageFilterIUS3IUS3 self) -> itkMeanImageFilterIUS3IUS3_Pointer"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIUS3IUS3_Clone(self)

    InputHasNumericTraitsCheck = _itkMeanImageFilterPython.itkMeanImageFilterIUS3IUS3_InputHasNumericTraitsCheck
    __swig_destroy__ = _itkMeanImageFilterPython.delete_itkMeanImageFilterIUS3IUS3

    def cast(obj: 'itkLightObject') -> "itkMeanImageFilterIUS3IUS3 *":
        """cast(itkLightObject obj) -> itkMeanImageFilterIUS3IUS3"""
        return _itkMeanImageFilterPython.itkMeanImageFilterIUS3IUS3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkMeanImageFilterIUS3IUS3

        Create a new object of the class itkMeanImageFilterIUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeanImageFilterIUS3IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeanImageFilterIUS3IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeanImageFilterIUS3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMeanImageFilterIUS3IUS3.Clone = new_instancemethod(_itkMeanImageFilterPython.itkMeanImageFilterIUS3IUS3_Clone, None, itkMeanImageFilterIUS3IUS3)
itkMeanImageFilterIUS3IUS3_swigregister = _itkMeanImageFilterPython.itkMeanImageFilterIUS3IUS3_swigregister
itkMeanImageFilterIUS3IUS3_swigregister(itkMeanImageFilterIUS3IUS3)

def itkMeanImageFilterIUS3IUS3___New_orig__() -> "itkMeanImageFilterIUS3IUS3_Pointer":
    """itkMeanImageFilterIUS3IUS3___New_orig__() -> itkMeanImageFilterIUS3IUS3_Pointer"""
    return _itkMeanImageFilterPython.itkMeanImageFilterIUS3IUS3___New_orig__()

def itkMeanImageFilterIUS3IUS3_cast(obj: 'itkLightObject') -> "itkMeanImageFilterIUS3IUS3 *":
    """itkMeanImageFilterIUS3IUS3_cast(itkLightObject obj) -> itkMeanImageFilterIUS3IUS3"""
    return _itkMeanImageFilterPython.itkMeanImageFilterIUS3IUS3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def mean_image_filter(*args, **kwargs):
    """Procedural interface for MeanImageFilter"""
    import itk
    instance = itk.MeanImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def mean_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.MeanImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.MeanImageFilter.values()[0]
    else:
        filter_object = itk.MeanImageFilter

    mean_image_filter.__doc__ = filter_object.__doc__
    mean_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    mean_image_filter.__doc__ += "Available Keyword Arguments:\n"
    mean_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



