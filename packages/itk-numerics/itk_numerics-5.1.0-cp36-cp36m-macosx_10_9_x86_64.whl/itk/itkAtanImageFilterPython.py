# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkAtanImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkAtanImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkAtanImageFilterPython
            return _itkAtanImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkAtanImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkAtanImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkAtanImageFilterPython
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
import itkUnaryGeneratorImageFilterPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterAPython
import itkImageSourcePython
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkImageSourceCommonPython
import itkVectorImagePython
import stdcomplexPython
import itkVariableLengthVectorPython
import itkImagePython
import itkSymmetricSecondRankTensorPython
import itkFixedArrayPython
import itkMatrixPython
import vnl_matrixPython
import vnl_vectorPython
import itkPointPython
import vnl_vector_refPython
import itkVectorPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkImageToImageFilterCommonPython
import itkImageToImageFilterBPython
import itkInPlaceImageFilterBPython

def itkAtanImageFilterID3ID3_New():
  return itkAtanImageFilterID3ID3.New()


def itkAtanImageFilterID2ID2_New():
  return itkAtanImageFilterID2ID2.New()


def itkAtanImageFilterIF3IF3_New():
  return itkAtanImageFilterIF3IF3.New()


def itkAtanImageFilterIF2IF2_New():
  return itkAtanImageFilterIF2IF2.New()

class itkAtanImageFilterID2ID2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID2ID2):
    """


    Computes the one-argument inverse tangent of each pixel.

    This filter is templated over the pixel type of the input image and
    the pixel type of the output image.

    The filter walks over all the pixels in the input image, and for each
    pixel does the following:

    cast the pixel value to double,

    apply the std::atan() function to the double value,

    cast the double value resulting from std::atan() to the pixel type of
    the output image,

    store the cast value into the output image.

    C++ includes: itkAtanImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAtanImageFilterID2ID2_Pointer":
        """__New_orig__() -> itkAtanImageFilterID2ID2_Pointer"""
        return _itkAtanImageFilterPython.itkAtanImageFilterID2ID2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAtanImageFilterID2ID2_Pointer":
        """Clone(itkAtanImageFilterID2ID2 self) -> itkAtanImageFilterID2ID2_Pointer"""
        return _itkAtanImageFilterPython.itkAtanImageFilterID2ID2_Clone(self)

    InputConvertibleToDoubleCheck = _itkAtanImageFilterPython.itkAtanImageFilterID2ID2_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkAtanImageFilterPython.itkAtanImageFilterID2ID2_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkAtanImageFilterPython.delete_itkAtanImageFilterID2ID2

    def cast(obj: 'itkLightObject') -> "itkAtanImageFilterID2ID2 *":
        """cast(itkLightObject obj) -> itkAtanImageFilterID2ID2"""
        return _itkAtanImageFilterPython.itkAtanImageFilterID2ID2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkAtanImageFilterID2ID2

        Create a new object of the class itkAtanImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAtanImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAtanImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAtanImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAtanImageFilterID2ID2.Clone = new_instancemethod(_itkAtanImageFilterPython.itkAtanImageFilterID2ID2_Clone, None, itkAtanImageFilterID2ID2)
itkAtanImageFilterID2ID2_swigregister = _itkAtanImageFilterPython.itkAtanImageFilterID2ID2_swigregister
itkAtanImageFilterID2ID2_swigregister(itkAtanImageFilterID2ID2)

def itkAtanImageFilterID2ID2___New_orig__() -> "itkAtanImageFilterID2ID2_Pointer":
    """itkAtanImageFilterID2ID2___New_orig__() -> itkAtanImageFilterID2ID2_Pointer"""
    return _itkAtanImageFilterPython.itkAtanImageFilterID2ID2___New_orig__()

def itkAtanImageFilterID2ID2_cast(obj: 'itkLightObject') -> "itkAtanImageFilterID2ID2 *":
    """itkAtanImageFilterID2ID2_cast(itkLightObject obj) -> itkAtanImageFilterID2ID2"""
    return _itkAtanImageFilterPython.itkAtanImageFilterID2ID2_cast(obj)

class itkAtanImageFilterID3ID3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID3ID3):
    """


    Computes the one-argument inverse tangent of each pixel.

    This filter is templated over the pixel type of the input image and
    the pixel type of the output image.

    The filter walks over all the pixels in the input image, and for each
    pixel does the following:

    cast the pixel value to double,

    apply the std::atan() function to the double value,

    cast the double value resulting from std::atan() to the pixel type of
    the output image,

    store the cast value into the output image.

    C++ includes: itkAtanImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAtanImageFilterID3ID3_Pointer":
        """__New_orig__() -> itkAtanImageFilterID3ID3_Pointer"""
        return _itkAtanImageFilterPython.itkAtanImageFilterID3ID3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAtanImageFilterID3ID3_Pointer":
        """Clone(itkAtanImageFilterID3ID3 self) -> itkAtanImageFilterID3ID3_Pointer"""
        return _itkAtanImageFilterPython.itkAtanImageFilterID3ID3_Clone(self)

    InputConvertibleToDoubleCheck = _itkAtanImageFilterPython.itkAtanImageFilterID3ID3_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkAtanImageFilterPython.itkAtanImageFilterID3ID3_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkAtanImageFilterPython.delete_itkAtanImageFilterID3ID3

    def cast(obj: 'itkLightObject') -> "itkAtanImageFilterID3ID3 *":
        """cast(itkLightObject obj) -> itkAtanImageFilterID3ID3"""
        return _itkAtanImageFilterPython.itkAtanImageFilterID3ID3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkAtanImageFilterID3ID3

        Create a new object of the class itkAtanImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAtanImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAtanImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAtanImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAtanImageFilterID3ID3.Clone = new_instancemethod(_itkAtanImageFilterPython.itkAtanImageFilterID3ID3_Clone, None, itkAtanImageFilterID3ID3)
itkAtanImageFilterID3ID3_swigregister = _itkAtanImageFilterPython.itkAtanImageFilterID3ID3_swigregister
itkAtanImageFilterID3ID3_swigregister(itkAtanImageFilterID3ID3)

def itkAtanImageFilterID3ID3___New_orig__() -> "itkAtanImageFilterID3ID3_Pointer":
    """itkAtanImageFilterID3ID3___New_orig__() -> itkAtanImageFilterID3ID3_Pointer"""
    return _itkAtanImageFilterPython.itkAtanImageFilterID3ID3___New_orig__()

def itkAtanImageFilterID3ID3_cast(obj: 'itkLightObject') -> "itkAtanImageFilterID3ID3 *":
    """itkAtanImageFilterID3ID3_cast(itkLightObject obj) -> itkAtanImageFilterID3ID3"""
    return _itkAtanImageFilterPython.itkAtanImageFilterID3ID3_cast(obj)

class itkAtanImageFilterIF2IF2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF2IF2):
    """


    Computes the one-argument inverse tangent of each pixel.

    This filter is templated over the pixel type of the input image and
    the pixel type of the output image.

    The filter walks over all the pixels in the input image, and for each
    pixel does the following:

    cast the pixel value to double,

    apply the std::atan() function to the double value,

    cast the double value resulting from std::atan() to the pixel type of
    the output image,

    store the cast value into the output image.

    C++ includes: itkAtanImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAtanImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkAtanImageFilterIF2IF2_Pointer"""
        return _itkAtanImageFilterPython.itkAtanImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAtanImageFilterIF2IF2_Pointer":
        """Clone(itkAtanImageFilterIF2IF2 self) -> itkAtanImageFilterIF2IF2_Pointer"""
        return _itkAtanImageFilterPython.itkAtanImageFilterIF2IF2_Clone(self)

    InputConvertibleToDoubleCheck = _itkAtanImageFilterPython.itkAtanImageFilterIF2IF2_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkAtanImageFilterPython.itkAtanImageFilterIF2IF2_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkAtanImageFilterPython.delete_itkAtanImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkAtanImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkAtanImageFilterIF2IF2"""
        return _itkAtanImageFilterPython.itkAtanImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkAtanImageFilterIF2IF2

        Create a new object of the class itkAtanImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAtanImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAtanImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAtanImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAtanImageFilterIF2IF2.Clone = new_instancemethod(_itkAtanImageFilterPython.itkAtanImageFilterIF2IF2_Clone, None, itkAtanImageFilterIF2IF2)
itkAtanImageFilterIF2IF2_swigregister = _itkAtanImageFilterPython.itkAtanImageFilterIF2IF2_swigregister
itkAtanImageFilterIF2IF2_swigregister(itkAtanImageFilterIF2IF2)

def itkAtanImageFilterIF2IF2___New_orig__() -> "itkAtanImageFilterIF2IF2_Pointer":
    """itkAtanImageFilterIF2IF2___New_orig__() -> itkAtanImageFilterIF2IF2_Pointer"""
    return _itkAtanImageFilterPython.itkAtanImageFilterIF2IF2___New_orig__()

def itkAtanImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkAtanImageFilterIF2IF2 *":
    """itkAtanImageFilterIF2IF2_cast(itkLightObject obj) -> itkAtanImageFilterIF2IF2"""
    return _itkAtanImageFilterPython.itkAtanImageFilterIF2IF2_cast(obj)

class itkAtanImageFilterIF3IF3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF3IF3):
    """


    Computes the one-argument inverse tangent of each pixel.

    This filter is templated over the pixel type of the input image and
    the pixel type of the output image.

    The filter walks over all the pixels in the input image, and for each
    pixel does the following:

    cast the pixel value to double,

    apply the std::atan() function to the double value,

    cast the double value resulting from std::atan() to the pixel type of
    the output image,

    store the cast value into the output image.

    C++ includes: itkAtanImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAtanImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkAtanImageFilterIF3IF3_Pointer"""
        return _itkAtanImageFilterPython.itkAtanImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAtanImageFilterIF3IF3_Pointer":
        """Clone(itkAtanImageFilterIF3IF3 self) -> itkAtanImageFilterIF3IF3_Pointer"""
        return _itkAtanImageFilterPython.itkAtanImageFilterIF3IF3_Clone(self)

    InputConvertibleToDoubleCheck = _itkAtanImageFilterPython.itkAtanImageFilterIF3IF3_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkAtanImageFilterPython.itkAtanImageFilterIF3IF3_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkAtanImageFilterPython.delete_itkAtanImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkAtanImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkAtanImageFilterIF3IF3"""
        return _itkAtanImageFilterPython.itkAtanImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkAtanImageFilterIF3IF3

        Create a new object of the class itkAtanImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAtanImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAtanImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAtanImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAtanImageFilterIF3IF3.Clone = new_instancemethod(_itkAtanImageFilterPython.itkAtanImageFilterIF3IF3_Clone, None, itkAtanImageFilterIF3IF3)
itkAtanImageFilterIF3IF3_swigregister = _itkAtanImageFilterPython.itkAtanImageFilterIF3IF3_swigregister
itkAtanImageFilterIF3IF3_swigregister(itkAtanImageFilterIF3IF3)

def itkAtanImageFilterIF3IF3___New_orig__() -> "itkAtanImageFilterIF3IF3_Pointer":
    """itkAtanImageFilterIF3IF3___New_orig__() -> itkAtanImageFilterIF3IF3_Pointer"""
    return _itkAtanImageFilterPython.itkAtanImageFilterIF3IF3___New_orig__()

def itkAtanImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkAtanImageFilterIF3IF3 *":
    """itkAtanImageFilterIF3IF3_cast(itkLightObject obj) -> itkAtanImageFilterIF3IF3"""
    return _itkAtanImageFilterPython.itkAtanImageFilterIF3IF3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def atan_image_filter(*args, **kwargs):
    """Procedural interface for AtanImageFilter"""
    import itk
    instance = itk.AtanImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def atan_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.AtanImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.AtanImageFilter.values()[0]
    else:
        filter_object = itk.AtanImageFilter

    atan_image_filter.__doc__ = filter_object.__doc__
    atan_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    atan_image_filter.__doc__ += "Available Keyword Arguments:\n"
    atan_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



