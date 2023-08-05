# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkSinImageFilterPython
else:
    import _itkSinImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkSinImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkSinImageFilterPython.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import itkUnaryGeneratorImageFilterPython
import itkImageRegionPython
import ITKCommonBasePython
import pyBasePython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterBPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImagePython
import itkFixedArrayPython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkVectorPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import itkCovariantVectorPython
import itkPointPython
import vnl_matrix_fixedPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterAPython
import itkInPlaceImageFilterBPython

def itkSinImageFilterID3ID3_New():
  return itkSinImageFilterID3ID3.New()


def itkSinImageFilterID2ID2_New():
  return itkSinImageFilterID2ID2.New()


def itkSinImageFilterIF3IF3_New():
  return itkSinImageFilterIF3IF3.New()


def itkSinImageFilterIF2IF2_New():
  return itkSinImageFilterIF2IF2.New()

class itkSinImageFilterID2ID2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID2ID2):
    r"""Proxy of C++ itkSinImageFilterID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSinImageFilterPython.itkSinImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkSinImageFilterPython.itkSinImageFilterID2ID2_Clone)
    InputConvertibleToDoubleCheck = _itkSinImageFilterPython.itkSinImageFilterID2ID2_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkSinImageFilterPython.itkSinImageFilterID2ID2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSinImageFilterPython.delete_itkSinImageFilterID2ID2
    cast = _swig_new_static_method(_itkSinImageFilterPython.itkSinImageFilterID2ID2_cast)

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


# Register itkSinImageFilterID2ID2 in _itkSinImageFilterPython:
_itkSinImageFilterPython.itkSinImageFilterID2ID2_swigregister(itkSinImageFilterID2ID2)
itkSinImageFilterID2ID2___New_orig__ = _itkSinImageFilterPython.itkSinImageFilterID2ID2___New_orig__
itkSinImageFilterID2ID2_cast = _itkSinImageFilterPython.itkSinImageFilterID2ID2_cast

class itkSinImageFilterID3ID3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID3ID3):
    r"""Proxy of C++ itkSinImageFilterID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSinImageFilterPython.itkSinImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkSinImageFilterPython.itkSinImageFilterID3ID3_Clone)
    InputConvertibleToDoubleCheck = _itkSinImageFilterPython.itkSinImageFilterID3ID3_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkSinImageFilterPython.itkSinImageFilterID3ID3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSinImageFilterPython.delete_itkSinImageFilterID3ID3
    cast = _swig_new_static_method(_itkSinImageFilterPython.itkSinImageFilterID3ID3_cast)

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


# Register itkSinImageFilterID3ID3 in _itkSinImageFilterPython:
_itkSinImageFilterPython.itkSinImageFilterID3ID3_swigregister(itkSinImageFilterID3ID3)
itkSinImageFilterID3ID3___New_orig__ = _itkSinImageFilterPython.itkSinImageFilterID3ID3___New_orig__
itkSinImageFilterID3ID3_cast = _itkSinImageFilterPython.itkSinImageFilterID3ID3_cast

class itkSinImageFilterIF2IF2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF2IF2):
    r"""Proxy of C++ itkSinImageFilterIF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSinImageFilterPython.itkSinImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkSinImageFilterPython.itkSinImageFilterIF2IF2_Clone)
    InputConvertibleToDoubleCheck = _itkSinImageFilterPython.itkSinImageFilterIF2IF2_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkSinImageFilterPython.itkSinImageFilterIF2IF2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSinImageFilterPython.delete_itkSinImageFilterIF2IF2
    cast = _swig_new_static_method(_itkSinImageFilterPython.itkSinImageFilterIF2IF2_cast)

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


# Register itkSinImageFilterIF2IF2 in _itkSinImageFilterPython:
_itkSinImageFilterPython.itkSinImageFilterIF2IF2_swigregister(itkSinImageFilterIF2IF2)
itkSinImageFilterIF2IF2___New_orig__ = _itkSinImageFilterPython.itkSinImageFilterIF2IF2___New_orig__
itkSinImageFilterIF2IF2_cast = _itkSinImageFilterPython.itkSinImageFilterIF2IF2_cast

class itkSinImageFilterIF3IF3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF3IF3):
    r"""Proxy of C++ itkSinImageFilterIF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSinImageFilterPython.itkSinImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkSinImageFilterPython.itkSinImageFilterIF3IF3_Clone)
    InputConvertibleToDoubleCheck = _itkSinImageFilterPython.itkSinImageFilterIF3IF3_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkSinImageFilterPython.itkSinImageFilterIF3IF3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSinImageFilterPython.delete_itkSinImageFilterIF3IF3
    cast = _swig_new_static_method(_itkSinImageFilterPython.itkSinImageFilterIF3IF3_cast)

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


# Register itkSinImageFilterIF3IF3 in _itkSinImageFilterPython:
_itkSinImageFilterPython.itkSinImageFilterIF3IF3_swigregister(itkSinImageFilterIF3IF3)
itkSinImageFilterIF3IF3___New_orig__ = _itkSinImageFilterPython.itkSinImageFilterIF3IF3___New_orig__
itkSinImageFilterIF3IF3_cast = _itkSinImageFilterPython.itkSinImageFilterIF3IF3_cast


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



