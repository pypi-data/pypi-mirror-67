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
    from . import _itkRoundImageFilterPython
else:
    import _itkRoundImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkRoundImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkRoundImageFilterPython.SWIG_PyStaticMethod_New

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
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImagePython
import stdcomplexPython
import itkVectorPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import itkFixedArrayPython
import itkOffsetPython
import itkSizePython
import itkCovariantVectorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkSymmetricSecondRankTensorPython
import itkRGBAPixelPython
import itkImageRegionPython
import itkIndexPython
import itkRGBPixelPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterAPython

def itkRoundImageFilterID3ID3_New():
  return itkRoundImageFilterID3ID3.New()


def itkRoundImageFilterID2ID2_New():
  return itkRoundImageFilterID2ID2.New()


def itkRoundImageFilterIF3IF3_New():
  return itkRoundImageFilterIF3IF3.New()


def itkRoundImageFilterIF2IF2_New():
  return itkRoundImageFilterIF2IF2.New()

class itkRoundImageFilterID2ID2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID2ID2):
    r"""Proxy of C++ itkRoundImageFilterID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRoundImageFilterPython.itkRoundImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkRoundImageFilterPython.itkRoundImageFilterID2ID2_Clone)
    __swig_destroy__ = _itkRoundImageFilterPython.delete_itkRoundImageFilterID2ID2
    cast = _swig_new_static_method(_itkRoundImageFilterPython.itkRoundImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkRoundImageFilterID2ID2

        Create a new object of the class itkRoundImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRoundImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRoundImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRoundImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRoundImageFilterID2ID2 in _itkRoundImageFilterPython:
_itkRoundImageFilterPython.itkRoundImageFilterID2ID2_swigregister(itkRoundImageFilterID2ID2)
itkRoundImageFilterID2ID2___New_orig__ = _itkRoundImageFilterPython.itkRoundImageFilterID2ID2___New_orig__
itkRoundImageFilterID2ID2_cast = _itkRoundImageFilterPython.itkRoundImageFilterID2ID2_cast

class itkRoundImageFilterID3ID3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID3ID3):
    r"""Proxy of C++ itkRoundImageFilterID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRoundImageFilterPython.itkRoundImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkRoundImageFilterPython.itkRoundImageFilterID3ID3_Clone)
    __swig_destroy__ = _itkRoundImageFilterPython.delete_itkRoundImageFilterID3ID3
    cast = _swig_new_static_method(_itkRoundImageFilterPython.itkRoundImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkRoundImageFilterID3ID3

        Create a new object of the class itkRoundImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRoundImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRoundImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRoundImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRoundImageFilterID3ID3 in _itkRoundImageFilterPython:
_itkRoundImageFilterPython.itkRoundImageFilterID3ID3_swigregister(itkRoundImageFilterID3ID3)
itkRoundImageFilterID3ID3___New_orig__ = _itkRoundImageFilterPython.itkRoundImageFilterID3ID3___New_orig__
itkRoundImageFilterID3ID3_cast = _itkRoundImageFilterPython.itkRoundImageFilterID3ID3_cast

class itkRoundImageFilterIF2IF2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF2IF2):
    r"""Proxy of C++ itkRoundImageFilterIF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRoundImageFilterPython.itkRoundImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkRoundImageFilterPython.itkRoundImageFilterIF2IF2_Clone)
    __swig_destroy__ = _itkRoundImageFilterPython.delete_itkRoundImageFilterIF2IF2
    cast = _swig_new_static_method(_itkRoundImageFilterPython.itkRoundImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkRoundImageFilterIF2IF2

        Create a new object of the class itkRoundImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRoundImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRoundImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRoundImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRoundImageFilterIF2IF2 in _itkRoundImageFilterPython:
_itkRoundImageFilterPython.itkRoundImageFilterIF2IF2_swigregister(itkRoundImageFilterIF2IF2)
itkRoundImageFilterIF2IF2___New_orig__ = _itkRoundImageFilterPython.itkRoundImageFilterIF2IF2___New_orig__
itkRoundImageFilterIF2IF2_cast = _itkRoundImageFilterPython.itkRoundImageFilterIF2IF2_cast

class itkRoundImageFilterIF3IF3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF3IF3):
    r"""Proxy of C++ itkRoundImageFilterIF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRoundImageFilterPython.itkRoundImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkRoundImageFilterPython.itkRoundImageFilterIF3IF3_Clone)
    __swig_destroy__ = _itkRoundImageFilterPython.delete_itkRoundImageFilterIF3IF3
    cast = _swig_new_static_method(_itkRoundImageFilterPython.itkRoundImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkRoundImageFilterIF3IF3

        Create a new object of the class itkRoundImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRoundImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkRoundImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkRoundImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRoundImageFilterIF3IF3 in _itkRoundImageFilterPython:
_itkRoundImageFilterPython.itkRoundImageFilterIF3IF3_swigregister(itkRoundImageFilterIF3IF3)
itkRoundImageFilterIF3IF3___New_orig__ = _itkRoundImageFilterPython.itkRoundImageFilterIF3IF3___New_orig__
itkRoundImageFilterIF3IF3_cast = _itkRoundImageFilterPython.itkRoundImageFilterIF3IF3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def round_image_filter(*args, **kwargs):
    """Procedural interface for RoundImageFilter"""
    import itk
    instance = itk.RoundImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def round_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.RoundImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.RoundImageFilter.values()[0]
    else:
        filter_object = itk.RoundImageFilter

    round_image_filter.__doc__ = filter_object.__doc__
    round_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    round_image_filter.__doc__ += "Available Keyword Arguments:\n"
    round_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



