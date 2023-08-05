# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkAtan2ImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkAtan2ImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkAtan2ImageFilterPython
            return _itkAtan2ImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkAtan2ImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkAtan2ImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkAtan2ImageFilterPython
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


import itkBinaryGeneratorImageFilterPython
import itkVectorPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import pyBasePython
import itkFixedArrayPython
import vnl_vector_refPython
import itkInPlaceImageFilterBPython
import itkImageToImageFilterBPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkIndexPython
import itkSizePython
import itkOffsetPython
import ITKCommonBasePython
import itkImagePython
import itkPointPython
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
import itkSimpleDataObjectDecoratorPython
import itkArrayPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterAPython

def itkAtan2ImageFilterID3ID3ID3_New():
  return itkAtan2ImageFilterID3ID3ID3.New()


def itkAtan2ImageFilterID2ID2ID2_New():
  return itkAtan2ImageFilterID2ID2ID2.New()


def itkAtan2ImageFilterIF3IF3IF3_New():
  return itkAtan2ImageFilterIF3IF3IF3.New()


def itkAtan2ImageFilterIF2IF2IF2_New():
  return itkAtan2ImageFilterIF2IF2IF2.New()

class itkAtan2ImageFilterID2ID2ID2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterID2ID2ID2):
    """


    Computes two argument inverse tangent.

    The first argument to the atan function is provided by a pixel in the
    first input image (SetInput1()) and the corresponding pixel in the
    second input image (SetInput2()) is used as the second argument.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Both pixel input types are cast to double in order to be used as
    parameters of std::atan2(). The resulting double value is cast to the
    output pixel type.

    C++ includes: itkAtan2ImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAtan2ImageFilterID2ID2ID2_Pointer":
        """__New_orig__() -> itkAtan2ImageFilterID2ID2ID2_Pointer"""
        return _itkAtan2ImageFilterPython.itkAtan2ImageFilterID2ID2ID2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAtan2ImageFilterID2ID2ID2_Pointer":
        """Clone(itkAtan2ImageFilterID2ID2ID2 self) -> itkAtan2ImageFilterID2ID2ID2_Pointer"""
        return _itkAtan2ImageFilterPython.itkAtan2ImageFilterID2ID2ID2_Clone(self)

    Input1ConvertibleToDoubleCheck = _itkAtan2ImageFilterPython.itkAtan2ImageFilterID2ID2ID2_Input1ConvertibleToDoubleCheck
    Input2ConvertibleToDoubleCheck = _itkAtan2ImageFilterPython.itkAtan2ImageFilterID2ID2ID2_Input2ConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkAtan2ImageFilterPython.itkAtan2ImageFilterID2ID2ID2_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkAtan2ImageFilterPython.delete_itkAtan2ImageFilterID2ID2ID2

    def cast(obj: 'itkLightObject') -> "itkAtan2ImageFilterID2ID2ID2 *":
        """cast(itkLightObject obj) -> itkAtan2ImageFilterID2ID2ID2"""
        return _itkAtan2ImageFilterPython.itkAtan2ImageFilterID2ID2ID2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkAtan2ImageFilterID2ID2ID2

        Create a new object of the class itkAtan2ImageFilterID2ID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAtan2ImageFilterID2ID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAtan2ImageFilterID2ID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAtan2ImageFilterID2ID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAtan2ImageFilterID2ID2ID2.Clone = new_instancemethod(_itkAtan2ImageFilterPython.itkAtan2ImageFilterID2ID2ID2_Clone, None, itkAtan2ImageFilterID2ID2ID2)
itkAtan2ImageFilterID2ID2ID2_swigregister = _itkAtan2ImageFilterPython.itkAtan2ImageFilterID2ID2ID2_swigregister
itkAtan2ImageFilterID2ID2ID2_swigregister(itkAtan2ImageFilterID2ID2ID2)

def itkAtan2ImageFilterID2ID2ID2___New_orig__() -> "itkAtan2ImageFilterID2ID2ID2_Pointer":
    """itkAtan2ImageFilterID2ID2ID2___New_orig__() -> itkAtan2ImageFilterID2ID2ID2_Pointer"""
    return _itkAtan2ImageFilterPython.itkAtan2ImageFilterID2ID2ID2___New_orig__()

def itkAtan2ImageFilterID2ID2ID2_cast(obj: 'itkLightObject') -> "itkAtan2ImageFilterID2ID2ID2 *":
    """itkAtan2ImageFilterID2ID2ID2_cast(itkLightObject obj) -> itkAtan2ImageFilterID2ID2ID2"""
    return _itkAtan2ImageFilterPython.itkAtan2ImageFilterID2ID2ID2_cast(obj)

class itkAtan2ImageFilterID3ID3ID3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterID3ID3ID3):
    """


    Computes two argument inverse tangent.

    The first argument to the atan function is provided by a pixel in the
    first input image (SetInput1()) and the corresponding pixel in the
    second input image (SetInput2()) is used as the second argument.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Both pixel input types are cast to double in order to be used as
    parameters of std::atan2(). The resulting double value is cast to the
    output pixel type.

    C++ includes: itkAtan2ImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAtan2ImageFilterID3ID3ID3_Pointer":
        """__New_orig__() -> itkAtan2ImageFilterID3ID3ID3_Pointer"""
        return _itkAtan2ImageFilterPython.itkAtan2ImageFilterID3ID3ID3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAtan2ImageFilterID3ID3ID3_Pointer":
        """Clone(itkAtan2ImageFilterID3ID3ID3 self) -> itkAtan2ImageFilterID3ID3ID3_Pointer"""
        return _itkAtan2ImageFilterPython.itkAtan2ImageFilterID3ID3ID3_Clone(self)

    Input1ConvertibleToDoubleCheck = _itkAtan2ImageFilterPython.itkAtan2ImageFilterID3ID3ID3_Input1ConvertibleToDoubleCheck
    Input2ConvertibleToDoubleCheck = _itkAtan2ImageFilterPython.itkAtan2ImageFilterID3ID3ID3_Input2ConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkAtan2ImageFilterPython.itkAtan2ImageFilterID3ID3ID3_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkAtan2ImageFilterPython.delete_itkAtan2ImageFilterID3ID3ID3

    def cast(obj: 'itkLightObject') -> "itkAtan2ImageFilterID3ID3ID3 *":
        """cast(itkLightObject obj) -> itkAtan2ImageFilterID3ID3ID3"""
        return _itkAtan2ImageFilterPython.itkAtan2ImageFilterID3ID3ID3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkAtan2ImageFilterID3ID3ID3

        Create a new object of the class itkAtan2ImageFilterID3ID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAtan2ImageFilterID3ID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAtan2ImageFilterID3ID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAtan2ImageFilterID3ID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAtan2ImageFilterID3ID3ID3.Clone = new_instancemethod(_itkAtan2ImageFilterPython.itkAtan2ImageFilterID3ID3ID3_Clone, None, itkAtan2ImageFilterID3ID3ID3)
itkAtan2ImageFilterID3ID3ID3_swigregister = _itkAtan2ImageFilterPython.itkAtan2ImageFilterID3ID3ID3_swigregister
itkAtan2ImageFilterID3ID3ID3_swigregister(itkAtan2ImageFilterID3ID3ID3)

def itkAtan2ImageFilterID3ID3ID3___New_orig__() -> "itkAtan2ImageFilterID3ID3ID3_Pointer":
    """itkAtan2ImageFilterID3ID3ID3___New_orig__() -> itkAtan2ImageFilterID3ID3ID3_Pointer"""
    return _itkAtan2ImageFilterPython.itkAtan2ImageFilterID3ID3ID3___New_orig__()

def itkAtan2ImageFilterID3ID3ID3_cast(obj: 'itkLightObject') -> "itkAtan2ImageFilterID3ID3ID3 *":
    """itkAtan2ImageFilterID3ID3ID3_cast(itkLightObject obj) -> itkAtan2ImageFilterID3ID3ID3"""
    return _itkAtan2ImageFilterPython.itkAtan2ImageFilterID3ID3ID3_cast(obj)

class itkAtan2ImageFilterIF2IF2IF2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIF2IF2IF2):
    """


    Computes two argument inverse tangent.

    The first argument to the atan function is provided by a pixel in the
    first input image (SetInput1()) and the corresponding pixel in the
    second input image (SetInput2()) is used as the second argument.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Both pixel input types are cast to double in order to be used as
    parameters of std::atan2(). The resulting double value is cast to the
    output pixel type.

    C++ includes: itkAtan2ImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAtan2ImageFilterIF2IF2IF2_Pointer":
        """__New_orig__() -> itkAtan2ImageFilterIF2IF2IF2_Pointer"""
        return _itkAtan2ImageFilterPython.itkAtan2ImageFilterIF2IF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAtan2ImageFilterIF2IF2IF2_Pointer":
        """Clone(itkAtan2ImageFilterIF2IF2IF2 self) -> itkAtan2ImageFilterIF2IF2IF2_Pointer"""
        return _itkAtan2ImageFilterPython.itkAtan2ImageFilterIF2IF2IF2_Clone(self)

    Input1ConvertibleToDoubleCheck = _itkAtan2ImageFilterPython.itkAtan2ImageFilterIF2IF2IF2_Input1ConvertibleToDoubleCheck
    Input2ConvertibleToDoubleCheck = _itkAtan2ImageFilterPython.itkAtan2ImageFilterIF2IF2IF2_Input2ConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkAtan2ImageFilterPython.itkAtan2ImageFilterIF2IF2IF2_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkAtan2ImageFilterPython.delete_itkAtan2ImageFilterIF2IF2IF2

    def cast(obj: 'itkLightObject') -> "itkAtan2ImageFilterIF2IF2IF2 *":
        """cast(itkLightObject obj) -> itkAtan2ImageFilterIF2IF2IF2"""
        return _itkAtan2ImageFilterPython.itkAtan2ImageFilterIF2IF2IF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkAtan2ImageFilterIF2IF2IF2

        Create a new object of the class itkAtan2ImageFilterIF2IF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAtan2ImageFilterIF2IF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAtan2ImageFilterIF2IF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAtan2ImageFilterIF2IF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAtan2ImageFilterIF2IF2IF2.Clone = new_instancemethod(_itkAtan2ImageFilterPython.itkAtan2ImageFilterIF2IF2IF2_Clone, None, itkAtan2ImageFilterIF2IF2IF2)
itkAtan2ImageFilterIF2IF2IF2_swigregister = _itkAtan2ImageFilterPython.itkAtan2ImageFilterIF2IF2IF2_swigregister
itkAtan2ImageFilterIF2IF2IF2_swigregister(itkAtan2ImageFilterIF2IF2IF2)

def itkAtan2ImageFilterIF2IF2IF2___New_orig__() -> "itkAtan2ImageFilterIF2IF2IF2_Pointer":
    """itkAtan2ImageFilterIF2IF2IF2___New_orig__() -> itkAtan2ImageFilterIF2IF2IF2_Pointer"""
    return _itkAtan2ImageFilterPython.itkAtan2ImageFilterIF2IF2IF2___New_orig__()

def itkAtan2ImageFilterIF2IF2IF2_cast(obj: 'itkLightObject') -> "itkAtan2ImageFilterIF2IF2IF2 *":
    """itkAtan2ImageFilterIF2IF2IF2_cast(itkLightObject obj) -> itkAtan2ImageFilterIF2IF2IF2"""
    return _itkAtan2ImageFilterPython.itkAtan2ImageFilterIF2IF2IF2_cast(obj)

class itkAtan2ImageFilterIF3IF3IF3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIF3IF3IF3):
    """


    Computes two argument inverse tangent.

    The first argument to the atan function is provided by a pixel in the
    first input image (SetInput1()) and the corresponding pixel in the
    second input image (SetInput2()) is used as the second argument.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Both pixel input types are cast to double in order to be used as
    parameters of std::atan2(). The resulting double value is cast to the
    output pixel type.

    C++ includes: itkAtan2ImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAtan2ImageFilterIF3IF3IF3_Pointer":
        """__New_orig__() -> itkAtan2ImageFilterIF3IF3IF3_Pointer"""
        return _itkAtan2ImageFilterPython.itkAtan2ImageFilterIF3IF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAtan2ImageFilterIF3IF3IF3_Pointer":
        """Clone(itkAtan2ImageFilterIF3IF3IF3 self) -> itkAtan2ImageFilterIF3IF3IF3_Pointer"""
        return _itkAtan2ImageFilterPython.itkAtan2ImageFilterIF3IF3IF3_Clone(self)

    Input1ConvertibleToDoubleCheck = _itkAtan2ImageFilterPython.itkAtan2ImageFilterIF3IF3IF3_Input1ConvertibleToDoubleCheck
    Input2ConvertibleToDoubleCheck = _itkAtan2ImageFilterPython.itkAtan2ImageFilterIF3IF3IF3_Input2ConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkAtan2ImageFilterPython.itkAtan2ImageFilterIF3IF3IF3_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkAtan2ImageFilterPython.delete_itkAtan2ImageFilterIF3IF3IF3

    def cast(obj: 'itkLightObject') -> "itkAtan2ImageFilterIF3IF3IF3 *":
        """cast(itkLightObject obj) -> itkAtan2ImageFilterIF3IF3IF3"""
        return _itkAtan2ImageFilterPython.itkAtan2ImageFilterIF3IF3IF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkAtan2ImageFilterIF3IF3IF3

        Create a new object of the class itkAtan2ImageFilterIF3IF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAtan2ImageFilterIF3IF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAtan2ImageFilterIF3IF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAtan2ImageFilterIF3IF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAtan2ImageFilterIF3IF3IF3.Clone = new_instancemethod(_itkAtan2ImageFilterPython.itkAtan2ImageFilterIF3IF3IF3_Clone, None, itkAtan2ImageFilterIF3IF3IF3)
itkAtan2ImageFilterIF3IF3IF3_swigregister = _itkAtan2ImageFilterPython.itkAtan2ImageFilterIF3IF3IF3_swigregister
itkAtan2ImageFilterIF3IF3IF3_swigregister(itkAtan2ImageFilterIF3IF3IF3)

def itkAtan2ImageFilterIF3IF3IF3___New_orig__() -> "itkAtan2ImageFilterIF3IF3IF3_Pointer":
    """itkAtan2ImageFilterIF3IF3IF3___New_orig__() -> itkAtan2ImageFilterIF3IF3IF3_Pointer"""
    return _itkAtan2ImageFilterPython.itkAtan2ImageFilterIF3IF3IF3___New_orig__()

def itkAtan2ImageFilterIF3IF3IF3_cast(obj: 'itkLightObject') -> "itkAtan2ImageFilterIF3IF3IF3 *":
    """itkAtan2ImageFilterIF3IF3IF3_cast(itkLightObject obj) -> itkAtan2ImageFilterIF3IF3IF3"""
    return _itkAtan2ImageFilterPython.itkAtan2ImageFilterIF3IF3IF3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def atan2_image_filter(*args, **kwargs):
    """Procedural interface for Atan2ImageFilter"""
    import itk
    instance = itk.Atan2ImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def atan2_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.Atan2ImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.Atan2ImageFilter.values()[0]
    else:
        filter_object = itk.Atan2ImageFilter

    atan2_image_filter.__doc__ = filter_object.__doc__
    atan2_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    atan2_image_filter.__doc__ += "Available Keyword Arguments:\n"
    atan2_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



