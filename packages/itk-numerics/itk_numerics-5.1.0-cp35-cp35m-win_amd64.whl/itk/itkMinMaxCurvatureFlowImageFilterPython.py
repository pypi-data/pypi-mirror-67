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
    from . import _itkMinMaxCurvatureFlowImageFilterPython
else:
    import _itkMinMaxCurvatureFlowImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkMinMaxCurvatureFlowImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkMinMaxCurvatureFlowImageFilterPython.SWIG_PyStaticMethod_New

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
import itkCurvatureFlowImageFilterPython
import itkDenseFiniteDifferenceImageFilterPython
import itkFiniteDifferenceImageFilterPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterBPython
import itkImagePython
import itkPointPython
import itkFixedArrayPython
import itkVectorPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import vnl_vector_refPython
import itkRGBAPixelPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkRGBPixelPython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkImageRegionPython
import itkSymmetricSecondRankTensorPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkImageToImageFilterAPython
import itkFiniteDifferenceFunctionPython

def itkMinMaxCurvatureFlowImageFilterID3ID3_New():
  return itkMinMaxCurvatureFlowImageFilterID3ID3.New()


def itkMinMaxCurvatureFlowImageFilterID2ID2_New():
  return itkMinMaxCurvatureFlowImageFilterID2ID2.New()


def itkMinMaxCurvatureFlowImageFilterIF3IF3_New():
  return itkMinMaxCurvatureFlowImageFilterIF3IF3.New()


def itkMinMaxCurvatureFlowImageFilterIF2IF2_New():
  return itkMinMaxCurvatureFlowImageFilterIF2IF2.New()

class itkMinMaxCurvatureFlowImageFilterID2ID2(itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID2ID2):
    r"""Proxy of C++ itkMinMaxCurvatureFlowImageFilterID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2_Clone)
    SetStencilRadius = _swig_new_instance_method(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2_SetStencilRadius)
    GetStencilRadius = _swig_new_instance_method(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2_GetStencilRadius)
    UnsignedLongConvertibleToOutputCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2_UnsignedLongConvertibleToOutputCheck
    
    OutputLessThanComparableCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2_OutputLessThanComparableCheck
    
    LongConvertibleToOutputCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2_LongConvertibleToOutputCheck
    
    OutputDoubleComparableCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2_OutputDoubleComparableCheck
    
    OutputDoubleMultiplyAndAssignOperatorCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2_OutputDoubleMultiplyAndAssignOperatorCheck
    
    OutputGreaterThanUnsignedLongCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2_OutputGreaterThanUnsignedLongCheck
    
    UnsignedLongOutputAditiveOperatorsCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2_UnsignedLongOutputAditiveOperatorsCheck
    
    __swig_destroy__ = _itkMinMaxCurvatureFlowImageFilterPython.delete_itkMinMaxCurvatureFlowImageFilterID2ID2
    cast = _swig_new_static_method(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkMinMaxCurvatureFlowImageFilterID2ID2

        Create a new object of the class itkMinMaxCurvatureFlowImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMinMaxCurvatureFlowImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMinMaxCurvatureFlowImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMinMaxCurvatureFlowImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMinMaxCurvatureFlowImageFilterID2ID2 in _itkMinMaxCurvatureFlowImageFilterPython:
_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2_swigregister(itkMinMaxCurvatureFlowImageFilterID2ID2)
itkMinMaxCurvatureFlowImageFilterID2ID2___New_orig__ = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2___New_orig__
itkMinMaxCurvatureFlowImageFilterID2ID2_cast = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2_cast

class itkMinMaxCurvatureFlowImageFilterID3ID3(itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID3ID3):
    r"""Proxy of C++ itkMinMaxCurvatureFlowImageFilterID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3_Clone)
    SetStencilRadius = _swig_new_instance_method(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3_SetStencilRadius)
    GetStencilRadius = _swig_new_instance_method(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3_GetStencilRadius)
    UnsignedLongConvertibleToOutputCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3_UnsignedLongConvertibleToOutputCheck
    
    OutputLessThanComparableCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3_OutputLessThanComparableCheck
    
    LongConvertibleToOutputCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3_LongConvertibleToOutputCheck
    
    OutputDoubleComparableCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3_OutputDoubleComparableCheck
    
    OutputDoubleMultiplyAndAssignOperatorCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3_OutputDoubleMultiplyAndAssignOperatorCheck
    
    OutputGreaterThanUnsignedLongCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3_OutputGreaterThanUnsignedLongCheck
    
    UnsignedLongOutputAditiveOperatorsCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3_UnsignedLongOutputAditiveOperatorsCheck
    
    __swig_destroy__ = _itkMinMaxCurvatureFlowImageFilterPython.delete_itkMinMaxCurvatureFlowImageFilterID3ID3
    cast = _swig_new_static_method(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkMinMaxCurvatureFlowImageFilterID3ID3

        Create a new object of the class itkMinMaxCurvatureFlowImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMinMaxCurvatureFlowImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMinMaxCurvatureFlowImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMinMaxCurvatureFlowImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMinMaxCurvatureFlowImageFilterID3ID3 in _itkMinMaxCurvatureFlowImageFilterPython:
_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3_swigregister(itkMinMaxCurvatureFlowImageFilterID3ID3)
itkMinMaxCurvatureFlowImageFilterID3ID3___New_orig__ = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3___New_orig__
itkMinMaxCurvatureFlowImageFilterID3ID3_cast = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3_cast

class itkMinMaxCurvatureFlowImageFilterIF2IF2(itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF2IF2):
    r"""Proxy of C++ itkMinMaxCurvatureFlowImageFilterIF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_Clone)
    SetStencilRadius = _swig_new_instance_method(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_SetStencilRadius)
    GetStencilRadius = _swig_new_instance_method(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_GetStencilRadius)
    UnsignedLongConvertibleToOutputCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_UnsignedLongConvertibleToOutputCheck
    
    OutputLessThanComparableCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_OutputLessThanComparableCheck
    
    LongConvertibleToOutputCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_LongConvertibleToOutputCheck
    
    OutputDoubleComparableCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_OutputDoubleComparableCheck
    
    OutputDoubleMultiplyAndAssignOperatorCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_OutputDoubleMultiplyAndAssignOperatorCheck
    
    OutputGreaterThanUnsignedLongCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_OutputGreaterThanUnsignedLongCheck
    
    UnsignedLongOutputAditiveOperatorsCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_UnsignedLongOutputAditiveOperatorsCheck
    
    __swig_destroy__ = _itkMinMaxCurvatureFlowImageFilterPython.delete_itkMinMaxCurvatureFlowImageFilterIF2IF2
    cast = _swig_new_static_method(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkMinMaxCurvatureFlowImageFilterIF2IF2

        Create a new object of the class itkMinMaxCurvatureFlowImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMinMaxCurvatureFlowImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMinMaxCurvatureFlowImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMinMaxCurvatureFlowImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMinMaxCurvatureFlowImageFilterIF2IF2 in _itkMinMaxCurvatureFlowImageFilterPython:
_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_swigregister(itkMinMaxCurvatureFlowImageFilterIF2IF2)
itkMinMaxCurvatureFlowImageFilterIF2IF2___New_orig__ = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2___New_orig__
itkMinMaxCurvatureFlowImageFilterIF2IF2_cast = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_cast

class itkMinMaxCurvatureFlowImageFilterIF3IF3(itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF3IF3):
    r"""Proxy of C++ itkMinMaxCurvatureFlowImageFilterIF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_Clone)
    SetStencilRadius = _swig_new_instance_method(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_SetStencilRadius)
    GetStencilRadius = _swig_new_instance_method(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_GetStencilRadius)
    UnsignedLongConvertibleToOutputCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_UnsignedLongConvertibleToOutputCheck
    
    OutputLessThanComparableCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_OutputLessThanComparableCheck
    
    LongConvertibleToOutputCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_LongConvertibleToOutputCheck
    
    OutputDoubleComparableCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_OutputDoubleComparableCheck
    
    OutputDoubleMultiplyAndAssignOperatorCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_OutputDoubleMultiplyAndAssignOperatorCheck
    
    OutputGreaterThanUnsignedLongCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_OutputGreaterThanUnsignedLongCheck
    
    UnsignedLongOutputAditiveOperatorsCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_UnsignedLongOutputAditiveOperatorsCheck
    
    __swig_destroy__ = _itkMinMaxCurvatureFlowImageFilterPython.delete_itkMinMaxCurvatureFlowImageFilterIF3IF3
    cast = _swig_new_static_method(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkMinMaxCurvatureFlowImageFilterIF3IF3

        Create a new object of the class itkMinMaxCurvatureFlowImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMinMaxCurvatureFlowImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMinMaxCurvatureFlowImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMinMaxCurvatureFlowImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMinMaxCurvatureFlowImageFilterIF3IF3 in _itkMinMaxCurvatureFlowImageFilterPython:
_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_swigregister(itkMinMaxCurvatureFlowImageFilterIF3IF3)
itkMinMaxCurvatureFlowImageFilterIF3IF3___New_orig__ = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3___New_orig__
itkMinMaxCurvatureFlowImageFilterIF3IF3_cast = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def min_max_curvature_flow_image_filter(*args, **kwargs):
    """Procedural interface for MinMaxCurvatureFlowImageFilter"""
    import itk
    instance = itk.MinMaxCurvatureFlowImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def min_max_curvature_flow_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.MinMaxCurvatureFlowImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.MinMaxCurvatureFlowImageFilter.values()[0]
    else:
        filter_object = itk.MinMaxCurvatureFlowImageFilter

    min_max_curvature_flow_image_filter.__doc__ = filter_object.__doc__
    min_max_curvature_flow_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    min_max_curvature_flow_image_filter.__doc__ += "Available Keyword Arguments:\n"
    min_max_curvature_flow_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



