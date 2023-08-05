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
    from . import _itkCosImageFilterPython
else:
    import _itkCosImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkCosImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkCosImageFilterPython.SWIG_PyStaticMethod_New

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
import ITKCommonBasePython
import pyBasePython
import itkInPlaceImageFilterBPython
import itkImageToImageFilterBPython
import itkVectorImagePython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkVariableLengthVectorPython
import stdcomplexPython
import itkImagePython
import itkMatrixPython
import vnl_matrixPython
import vnl_vectorPython
import vnl_matrix_fixedPython
import itkPointPython
import itkFixedArrayPython
import itkVectorPython
import vnl_vector_refPython
import itkCovariantVectorPython
import itkSymmetricSecondRankTensorPython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkImageRegionPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterAPython

def itkCosImageFilterID3ID3_New():
  return itkCosImageFilterID3ID3.New()


def itkCosImageFilterID2ID2_New():
  return itkCosImageFilterID2ID2.New()


def itkCosImageFilterIF3IF3_New():
  return itkCosImageFilterIF3IF3.New()


def itkCosImageFilterIF2IF2_New():
  return itkCosImageFilterIF2IF2.New()

class itkCosImageFilterID2ID2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID2ID2):
    r"""Proxy of C++ itkCosImageFilterID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCosImageFilterPython.itkCosImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkCosImageFilterPython.itkCosImageFilterID2ID2_Clone)
    InputConvertibleToDoubleCheck = _itkCosImageFilterPython.itkCosImageFilterID2ID2_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkCosImageFilterPython.itkCosImageFilterID2ID2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkCosImageFilterPython.delete_itkCosImageFilterID2ID2
    cast = _swig_new_static_method(_itkCosImageFilterPython.itkCosImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkCosImageFilterID2ID2

        Create a new object of the class itkCosImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCosImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCosImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCosImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCosImageFilterID2ID2 in _itkCosImageFilterPython:
_itkCosImageFilterPython.itkCosImageFilterID2ID2_swigregister(itkCosImageFilterID2ID2)
itkCosImageFilterID2ID2___New_orig__ = _itkCosImageFilterPython.itkCosImageFilterID2ID2___New_orig__
itkCosImageFilterID2ID2_cast = _itkCosImageFilterPython.itkCosImageFilterID2ID2_cast

class itkCosImageFilterID3ID3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID3ID3):
    r"""Proxy of C++ itkCosImageFilterID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCosImageFilterPython.itkCosImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkCosImageFilterPython.itkCosImageFilterID3ID3_Clone)
    InputConvertibleToDoubleCheck = _itkCosImageFilterPython.itkCosImageFilterID3ID3_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkCosImageFilterPython.itkCosImageFilterID3ID3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkCosImageFilterPython.delete_itkCosImageFilterID3ID3
    cast = _swig_new_static_method(_itkCosImageFilterPython.itkCosImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkCosImageFilterID3ID3

        Create a new object of the class itkCosImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCosImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCosImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCosImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCosImageFilterID3ID3 in _itkCosImageFilterPython:
_itkCosImageFilterPython.itkCosImageFilterID3ID3_swigregister(itkCosImageFilterID3ID3)
itkCosImageFilterID3ID3___New_orig__ = _itkCosImageFilterPython.itkCosImageFilterID3ID3___New_orig__
itkCosImageFilterID3ID3_cast = _itkCosImageFilterPython.itkCosImageFilterID3ID3_cast

class itkCosImageFilterIF2IF2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF2IF2):
    r"""Proxy of C++ itkCosImageFilterIF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCosImageFilterPython.itkCosImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkCosImageFilterPython.itkCosImageFilterIF2IF2_Clone)
    InputConvertibleToDoubleCheck = _itkCosImageFilterPython.itkCosImageFilterIF2IF2_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkCosImageFilterPython.itkCosImageFilterIF2IF2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkCosImageFilterPython.delete_itkCosImageFilterIF2IF2
    cast = _swig_new_static_method(_itkCosImageFilterPython.itkCosImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkCosImageFilterIF2IF2

        Create a new object of the class itkCosImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCosImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCosImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCosImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCosImageFilterIF2IF2 in _itkCosImageFilterPython:
_itkCosImageFilterPython.itkCosImageFilterIF2IF2_swigregister(itkCosImageFilterIF2IF2)
itkCosImageFilterIF2IF2___New_orig__ = _itkCosImageFilterPython.itkCosImageFilterIF2IF2___New_orig__
itkCosImageFilterIF2IF2_cast = _itkCosImageFilterPython.itkCosImageFilterIF2IF2_cast

class itkCosImageFilterIF3IF3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF3IF3):
    r"""Proxy of C++ itkCosImageFilterIF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCosImageFilterPython.itkCosImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkCosImageFilterPython.itkCosImageFilterIF3IF3_Clone)
    InputConvertibleToDoubleCheck = _itkCosImageFilterPython.itkCosImageFilterIF3IF3_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkCosImageFilterPython.itkCosImageFilterIF3IF3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkCosImageFilterPython.delete_itkCosImageFilterIF3IF3
    cast = _swig_new_static_method(_itkCosImageFilterPython.itkCosImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkCosImageFilterIF3IF3

        Create a new object of the class itkCosImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCosImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCosImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCosImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCosImageFilterIF3IF3 in _itkCosImageFilterPython:
_itkCosImageFilterPython.itkCosImageFilterIF3IF3_swigregister(itkCosImageFilterIF3IF3)
itkCosImageFilterIF3IF3___New_orig__ = _itkCosImageFilterPython.itkCosImageFilterIF3IF3___New_orig__
itkCosImageFilterIF3IF3_cast = _itkCosImageFilterPython.itkCosImageFilterIF3IF3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def cos_image_filter(*args, **kwargs):
    """Procedural interface for CosImageFilter"""
    import itk
    instance = itk.CosImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def cos_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.CosImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.CosImageFilter.values()[0]
    else:
        filter_object = itk.CosImageFilter

    cos_image_filter.__doc__ = filter_object.__doc__
    cos_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    cos_image_filter.__doc__ += "Available Keyword Arguments:\n"
    cos_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



