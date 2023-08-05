# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkSinImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkSinImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkSinImageFilterPython
            return _itkSinImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkSinImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkSinImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkSinImageFilterPython
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
import itkIndexPython
import itkOffsetPython
import itkSizePython
import pyBasePython
import stdcomplexPython
import ITKCommonBasePython
import itkVariableLengthVectorPython
import itkImagePython
import itkFixedArrayPython
import itkRGBAPixelPython
import itkPointPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import itkVectorPython
import itkRGBPixelPython
import itkImageRegionPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterAPython

def itkSinImageFilterID3ID3_New():
  return itkSinImageFilterID3ID3.New()


def itkSinImageFilterID2ID2_New():
  return itkSinImageFilterID2ID2.New()


def itkSinImageFilterIF3IF3_New():
  return itkSinImageFilterIF3IF3.New()


def itkSinImageFilterIF2IF2_New():
  return itkSinImageFilterIF2IF2.New()

class itkSinImageFilterID2ID2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID2ID2):
    """


    Computes the sine of each pixel.

    The computations are performed using std::sin(x).

    C++ includes: itkSinImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSinImageFilterID2ID2_Pointer":
        """__New_orig__() -> itkSinImageFilterID2ID2_Pointer"""
        return _itkSinImageFilterPython.itkSinImageFilterID2ID2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSinImageFilterID2ID2_Pointer":
        """Clone(itkSinImageFilterID2ID2 self) -> itkSinImageFilterID2ID2_Pointer"""
        return _itkSinImageFilterPython.itkSinImageFilterID2ID2_Clone(self)

    InputConvertibleToDoubleCheck = _itkSinImageFilterPython.itkSinImageFilterID2ID2_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkSinImageFilterPython.itkSinImageFilterID2ID2_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkSinImageFilterPython.delete_itkSinImageFilterID2ID2

    def cast(obj: 'itkLightObject') -> "itkSinImageFilterID2ID2 *":
        """cast(itkLightObject obj) -> itkSinImageFilterID2ID2"""
        return _itkSinImageFilterPython.itkSinImageFilterID2ID2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkSinImageFilterID2ID2

        Create a new object of the class itkSinImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSinImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSinImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSinImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSinImageFilterID2ID2.Clone = new_instancemethod(_itkSinImageFilterPython.itkSinImageFilterID2ID2_Clone, None, itkSinImageFilterID2ID2)
itkSinImageFilterID2ID2_swigregister = _itkSinImageFilterPython.itkSinImageFilterID2ID2_swigregister
itkSinImageFilterID2ID2_swigregister(itkSinImageFilterID2ID2)

def itkSinImageFilterID2ID2___New_orig__() -> "itkSinImageFilterID2ID2_Pointer":
    """itkSinImageFilterID2ID2___New_orig__() -> itkSinImageFilterID2ID2_Pointer"""
    return _itkSinImageFilterPython.itkSinImageFilterID2ID2___New_orig__()

def itkSinImageFilterID2ID2_cast(obj: 'itkLightObject') -> "itkSinImageFilterID2ID2 *":
    """itkSinImageFilterID2ID2_cast(itkLightObject obj) -> itkSinImageFilterID2ID2"""
    return _itkSinImageFilterPython.itkSinImageFilterID2ID2_cast(obj)

class itkSinImageFilterID3ID3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID3ID3):
    """


    Computes the sine of each pixel.

    The computations are performed using std::sin(x).

    C++ includes: itkSinImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSinImageFilterID3ID3_Pointer":
        """__New_orig__() -> itkSinImageFilterID3ID3_Pointer"""
        return _itkSinImageFilterPython.itkSinImageFilterID3ID3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSinImageFilterID3ID3_Pointer":
        """Clone(itkSinImageFilterID3ID3 self) -> itkSinImageFilterID3ID3_Pointer"""
        return _itkSinImageFilterPython.itkSinImageFilterID3ID3_Clone(self)

    InputConvertibleToDoubleCheck = _itkSinImageFilterPython.itkSinImageFilterID3ID3_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkSinImageFilterPython.itkSinImageFilterID3ID3_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkSinImageFilterPython.delete_itkSinImageFilterID3ID3

    def cast(obj: 'itkLightObject') -> "itkSinImageFilterID3ID3 *":
        """cast(itkLightObject obj) -> itkSinImageFilterID3ID3"""
        return _itkSinImageFilterPython.itkSinImageFilterID3ID3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkSinImageFilterID3ID3

        Create a new object of the class itkSinImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSinImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSinImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSinImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSinImageFilterID3ID3.Clone = new_instancemethod(_itkSinImageFilterPython.itkSinImageFilterID3ID3_Clone, None, itkSinImageFilterID3ID3)
itkSinImageFilterID3ID3_swigregister = _itkSinImageFilterPython.itkSinImageFilterID3ID3_swigregister
itkSinImageFilterID3ID3_swigregister(itkSinImageFilterID3ID3)

def itkSinImageFilterID3ID3___New_orig__() -> "itkSinImageFilterID3ID3_Pointer":
    """itkSinImageFilterID3ID3___New_orig__() -> itkSinImageFilterID3ID3_Pointer"""
    return _itkSinImageFilterPython.itkSinImageFilterID3ID3___New_orig__()

def itkSinImageFilterID3ID3_cast(obj: 'itkLightObject') -> "itkSinImageFilterID3ID3 *":
    """itkSinImageFilterID3ID3_cast(itkLightObject obj) -> itkSinImageFilterID3ID3"""
    return _itkSinImageFilterPython.itkSinImageFilterID3ID3_cast(obj)

class itkSinImageFilterIF2IF2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF2IF2):
    """


    Computes the sine of each pixel.

    The computations are performed using std::sin(x).

    C++ includes: itkSinImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSinImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkSinImageFilterIF2IF2_Pointer"""
        return _itkSinImageFilterPython.itkSinImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSinImageFilterIF2IF2_Pointer":
        """Clone(itkSinImageFilterIF2IF2 self) -> itkSinImageFilterIF2IF2_Pointer"""
        return _itkSinImageFilterPython.itkSinImageFilterIF2IF2_Clone(self)

    InputConvertibleToDoubleCheck = _itkSinImageFilterPython.itkSinImageFilterIF2IF2_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkSinImageFilterPython.itkSinImageFilterIF2IF2_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkSinImageFilterPython.delete_itkSinImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkSinImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkSinImageFilterIF2IF2"""
        return _itkSinImageFilterPython.itkSinImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkSinImageFilterIF2IF2

        Create a new object of the class itkSinImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSinImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSinImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSinImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSinImageFilterIF2IF2.Clone = new_instancemethod(_itkSinImageFilterPython.itkSinImageFilterIF2IF2_Clone, None, itkSinImageFilterIF2IF2)
itkSinImageFilterIF2IF2_swigregister = _itkSinImageFilterPython.itkSinImageFilterIF2IF2_swigregister
itkSinImageFilterIF2IF2_swigregister(itkSinImageFilterIF2IF2)

def itkSinImageFilterIF2IF2___New_orig__() -> "itkSinImageFilterIF2IF2_Pointer":
    """itkSinImageFilterIF2IF2___New_orig__() -> itkSinImageFilterIF2IF2_Pointer"""
    return _itkSinImageFilterPython.itkSinImageFilterIF2IF2___New_orig__()

def itkSinImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkSinImageFilterIF2IF2 *":
    """itkSinImageFilterIF2IF2_cast(itkLightObject obj) -> itkSinImageFilterIF2IF2"""
    return _itkSinImageFilterPython.itkSinImageFilterIF2IF2_cast(obj)

class itkSinImageFilterIF3IF3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF3IF3):
    """


    Computes the sine of each pixel.

    The computations are performed using std::sin(x).

    C++ includes: itkSinImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSinImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkSinImageFilterIF3IF3_Pointer"""
        return _itkSinImageFilterPython.itkSinImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSinImageFilterIF3IF3_Pointer":
        """Clone(itkSinImageFilterIF3IF3 self) -> itkSinImageFilterIF3IF3_Pointer"""
        return _itkSinImageFilterPython.itkSinImageFilterIF3IF3_Clone(self)

    InputConvertibleToDoubleCheck = _itkSinImageFilterPython.itkSinImageFilterIF3IF3_InputConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkSinImageFilterPython.itkSinImageFilterIF3IF3_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkSinImageFilterPython.delete_itkSinImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkSinImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkSinImageFilterIF3IF3"""
        return _itkSinImageFilterPython.itkSinImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkSinImageFilterIF3IF3

        Create a new object of the class itkSinImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSinImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSinImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSinImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSinImageFilterIF3IF3.Clone = new_instancemethod(_itkSinImageFilterPython.itkSinImageFilterIF3IF3_Clone, None, itkSinImageFilterIF3IF3)
itkSinImageFilterIF3IF3_swigregister = _itkSinImageFilterPython.itkSinImageFilterIF3IF3_swigregister
itkSinImageFilterIF3IF3_swigregister(itkSinImageFilterIF3IF3)

def itkSinImageFilterIF3IF3___New_orig__() -> "itkSinImageFilterIF3IF3_Pointer":
    """itkSinImageFilterIF3IF3___New_orig__() -> itkSinImageFilterIF3IF3_Pointer"""
    return _itkSinImageFilterPython.itkSinImageFilterIF3IF3___New_orig__()

def itkSinImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkSinImageFilterIF3IF3 *":
    """itkSinImageFilterIF3IF3_cast(itkLightObject obj) -> itkSinImageFilterIF3IF3"""
    return _itkSinImageFilterPython.itkSinImageFilterIF3IF3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def sin_image_filter(*args, **kwargs):
    """Procedural interface for SinImageFilter"""
    import itk
    instance = itk.SinImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def sin_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.SinImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.SinImageFilter.values()[0]
    else:
        filter_object = itk.SinImageFilter

    sin_image_filter.__doc__ = filter_object.__doc__
    sin_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    sin_image_filter.__doc__ += "Available Keyword Arguments:\n"
    sin_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



