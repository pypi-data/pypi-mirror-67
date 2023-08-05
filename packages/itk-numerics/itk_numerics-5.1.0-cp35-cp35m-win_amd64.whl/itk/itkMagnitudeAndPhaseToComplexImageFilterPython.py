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
    from . import _itkMagnitudeAndPhaseToComplexImageFilterPython
else:
    import _itkMagnitudeAndPhaseToComplexImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkMagnitudeAndPhaseToComplexImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkMagnitudeAndPhaseToComplexImageFilterPython.SWIG_PyStaticMethod_New

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


import ITKCommonBasePython
import pyBasePython
import itkBinaryGeneratorImageFilterPython
import itkRGBPixelPython
import itkFixedArrayPython
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkImagePython
import itkPointPython
import itkVectorPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import vnl_vector_refPython
import itkRGBAPixelPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkSymmetricSecondRankTensorPython
import itkInPlaceImageFilterBPython
import itkImageToImageFilterBPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterAPython
import itkSimpleDataObjectDecoratorPython
import itkArrayPython

def itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3_New():
  return itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3.New()


def itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3_New():
  return itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3.New()


def itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2_New():
  return itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2.New()


def itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2_New():
  return itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2.New()

class itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterID2ID2ICF2):
    r"""Proxy of C++ itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2___New_orig__)
    Clone = _swig_new_instance_method(_itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2_Clone)
    Input1ConvertibleToDoubleCheck = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2_Input1ConvertibleToDoubleCheck
    
    Input2ConvertibleToDoubleCheck = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2_Input2ConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkMagnitudeAndPhaseToComplexImageFilterPython.delete_itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2
    cast = _swig_new_static_method(_itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2_cast)

    def New(*args, **kargs):
        """New() -> itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2

        Create a new object of the class itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2 in _itkMagnitudeAndPhaseToComplexImageFilterPython:
_itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2_swigregister(itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2)
itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2___New_orig__ = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2___New_orig__
itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2_cast = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2_cast

class itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterID3ID3ICF3):
    r"""Proxy of C++ itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3___New_orig__)
    Clone = _swig_new_instance_method(_itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3_Clone)
    Input1ConvertibleToDoubleCheck = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3_Input1ConvertibleToDoubleCheck
    
    Input2ConvertibleToDoubleCheck = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3_Input2ConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkMagnitudeAndPhaseToComplexImageFilterPython.delete_itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3
    cast = _swig_new_static_method(_itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3_cast)

    def New(*args, **kargs):
        """New() -> itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3

        Create a new object of the class itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3 in _itkMagnitudeAndPhaseToComplexImageFilterPython:
_itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3_swigregister(itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3)
itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3___New_orig__ = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3___New_orig__
itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3_cast = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3_cast

class itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIF2IF2ICF2):
    r"""Proxy of C++ itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2___New_orig__)
    Clone = _swig_new_instance_method(_itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2_Clone)
    Input1ConvertibleToDoubleCheck = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2_Input1ConvertibleToDoubleCheck
    
    Input2ConvertibleToDoubleCheck = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2_Input2ConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkMagnitudeAndPhaseToComplexImageFilterPython.delete_itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2
    cast = _swig_new_static_method(_itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2_cast)

    def New(*args, **kargs):
        """New() -> itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2

        Create a new object of the class itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2 in _itkMagnitudeAndPhaseToComplexImageFilterPython:
_itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2_swigregister(itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2)
itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2___New_orig__ = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2___New_orig__
itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2_cast = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2_cast

class itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIF3IF3ICF3):
    r"""Proxy of C++ itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3___New_orig__)
    Clone = _swig_new_instance_method(_itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3_Clone)
    Input1ConvertibleToDoubleCheck = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3_Input1ConvertibleToDoubleCheck
    
    Input2ConvertibleToDoubleCheck = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3_Input2ConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkMagnitudeAndPhaseToComplexImageFilterPython.delete_itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3
    cast = _swig_new_static_method(_itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3_cast)

    def New(*args, **kargs):
        """New() -> itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3

        Create a new object of the class itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3 in _itkMagnitudeAndPhaseToComplexImageFilterPython:
_itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3_swigregister(itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3)
itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3___New_orig__ = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3___New_orig__
itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3_cast = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def magnitude_and_phase_to_complex_image_filter(*args, **kwargs):
    """Procedural interface for MagnitudeAndPhaseToComplexImageFilter"""
    import itk
    instance = itk.MagnitudeAndPhaseToComplexImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def magnitude_and_phase_to_complex_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.MagnitudeAndPhaseToComplexImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.MagnitudeAndPhaseToComplexImageFilter.values()[0]
    else:
        filter_object = itk.MagnitudeAndPhaseToComplexImageFilter

    magnitude_and_phase_to_complex_image_filter.__doc__ = filter_object.__doc__
    magnitude_and_phase_to_complex_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    magnitude_and_phase_to_complex_image_filter.__doc__ += "Available Keyword Arguments:\n"
    magnitude_and_phase_to_complex_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



