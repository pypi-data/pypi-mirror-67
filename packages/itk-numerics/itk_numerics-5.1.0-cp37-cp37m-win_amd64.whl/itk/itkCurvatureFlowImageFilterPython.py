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
    from . import _itkCurvatureFlowImageFilterPython
else:
    import _itkCurvatureFlowImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkCurvatureFlowImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkCurvatureFlowImageFilterPython.SWIG_PyStaticMethod_New

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


import itkDenseFiniteDifferenceImageFilterPython
import itkImageRegionPython
import ITKCommonBasePython
import pyBasePython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkImagePython
import stdcomplexPython
import itkVectorPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import itkFixedArrayPython
import itkCovariantVectorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkSymmetricSecondRankTensorPython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkFiniteDifferenceImageFilterPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterAPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkImageToImageFilterBPython
import itkFiniteDifferenceFunctionPython

def itkCurvatureFlowImageFilterID3ID3_New():
  return itkCurvatureFlowImageFilterID3ID3.New()


def itkCurvatureFlowImageFilterID2ID2_New():
  return itkCurvatureFlowImageFilterID2ID2.New()


def itkCurvatureFlowImageFilterIF3IF3_New():
  return itkCurvatureFlowImageFilterIF3IF3.New()


def itkCurvatureFlowImageFilterIF2IF2_New():
  return itkCurvatureFlowImageFilterIF2IF2.New()

class itkCurvatureFlowImageFilterID2ID2(itkDenseFiniteDifferenceImageFilterPython.itkDenseFiniteDifferenceImageFilterID2ID2):
    r"""Proxy of C++ itkCurvatureFlowImageFilterID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID2ID2_Clone)
    SetTimeStep = _swig_new_instance_method(_itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID2ID2_SetTimeStep)
    GetTimeStep = _swig_new_instance_method(_itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID2ID2_GetTimeStep)
    DoubleConvertibleToOutputCheck = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID2ID2_DoubleConvertibleToOutputCheck
    
    OutputConvertibleToDoubleCheck = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID2ID2_OutputConvertibleToDoubleCheck
    
    OutputDivisionOperatorsCheck = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID2ID2_OutputDivisionOperatorsCheck
    
    DoubleOutputMultiplyOperatorCheck = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID2ID2_DoubleOutputMultiplyOperatorCheck
    
    IntOutputMultiplyOperatorCheck = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID2ID2_IntOutputMultiplyOperatorCheck
    
    OutputLessThanDoubleCheck = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID2ID2_OutputLessThanDoubleCheck
    
    OutputDoubleAdditiveOperatorsCheck = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID2ID2_OutputDoubleAdditiveOperatorsCheck
    
    __swig_destroy__ = _itkCurvatureFlowImageFilterPython.delete_itkCurvatureFlowImageFilterID2ID2
    cast = _swig_new_static_method(_itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkCurvatureFlowImageFilterID2ID2

        Create a new object of the class itkCurvatureFlowImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCurvatureFlowImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCurvatureFlowImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCurvatureFlowImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCurvatureFlowImageFilterID2ID2 in _itkCurvatureFlowImageFilterPython:
_itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID2ID2_swigregister(itkCurvatureFlowImageFilterID2ID2)
itkCurvatureFlowImageFilterID2ID2___New_orig__ = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID2ID2___New_orig__
itkCurvatureFlowImageFilterID2ID2_cast = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID2ID2_cast

class itkCurvatureFlowImageFilterID3ID3(itkDenseFiniteDifferenceImageFilterPython.itkDenseFiniteDifferenceImageFilterID3ID3):
    r"""Proxy of C++ itkCurvatureFlowImageFilterID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID3ID3_Clone)
    SetTimeStep = _swig_new_instance_method(_itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID3ID3_SetTimeStep)
    GetTimeStep = _swig_new_instance_method(_itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID3ID3_GetTimeStep)
    DoubleConvertibleToOutputCheck = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID3ID3_DoubleConvertibleToOutputCheck
    
    OutputConvertibleToDoubleCheck = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID3ID3_OutputConvertibleToDoubleCheck
    
    OutputDivisionOperatorsCheck = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID3ID3_OutputDivisionOperatorsCheck
    
    DoubleOutputMultiplyOperatorCheck = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID3ID3_DoubleOutputMultiplyOperatorCheck
    
    IntOutputMultiplyOperatorCheck = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID3ID3_IntOutputMultiplyOperatorCheck
    
    OutputLessThanDoubleCheck = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID3ID3_OutputLessThanDoubleCheck
    
    OutputDoubleAdditiveOperatorsCheck = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID3ID3_OutputDoubleAdditiveOperatorsCheck
    
    __swig_destroy__ = _itkCurvatureFlowImageFilterPython.delete_itkCurvatureFlowImageFilterID3ID3
    cast = _swig_new_static_method(_itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkCurvatureFlowImageFilterID3ID3

        Create a new object of the class itkCurvatureFlowImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCurvatureFlowImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCurvatureFlowImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCurvatureFlowImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCurvatureFlowImageFilterID3ID3 in _itkCurvatureFlowImageFilterPython:
_itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID3ID3_swigregister(itkCurvatureFlowImageFilterID3ID3)
itkCurvatureFlowImageFilterID3ID3___New_orig__ = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID3ID3___New_orig__
itkCurvatureFlowImageFilterID3ID3_cast = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID3ID3_cast

class itkCurvatureFlowImageFilterIF2IF2(itkDenseFiniteDifferenceImageFilterPython.itkDenseFiniteDifferenceImageFilterIF2IF2):
    r"""Proxy of C++ itkCurvatureFlowImageFilterIF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF2IF2_Clone)
    SetTimeStep = _swig_new_instance_method(_itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF2IF2_SetTimeStep)
    GetTimeStep = _swig_new_instance_method(_itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF2IF2_GetTimeStep)
    DoubleConvertibleToOutputCheck = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF2IF2_DoubleConvertibleToOutputCheck
    
    OutputConvertibleToDoubleCheck = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF2IF2_OutputConvertibleToDoubleCheck
    
    OutputDivisionOperatorsCheck = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF2IF2_OutputDivisionOperatorsCheck
    
    DoubleOutputMultiplyOperatorCheck = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF2IF2_DoubleOutputMultiplyOperatorCheck
    
    IntOutputMultiplyOperatorCheck = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF2IF2_IntOutputMultiplyOperatorCheck
    
    OutputLessThanDoubleCheck = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF2IF2_OutputLessThanDoubleCheck
    
    OutputDoubleAdditiveOperatorsCheck = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF2IF2_OutputDoubleAdditiveOperatorsCheck
    
    __swig_destroy__ = _itkCurvatureFlowImageFilterPython.delete_itkCurvatureFlowImageFilterIF2IF2
    cast = _swig_new_static_method(_itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkCurvatureFlowImageFilterIF2IF2

        Create a new object of the class itkCurvatureFlowImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCurvatureFlowImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCurvatureFlowImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCurvatureFlowImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCurvatureFlowImageFilterIF2IF2 in _itkCurvatureFlowImageFilterPython:
_itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF2IF2_swigregister(itkCurvatureFlowImageFilterIF2IF2)
itkCurvatureFlowImageFilterIF2IF2___New_orig__ = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF2IF2___New_orig__
itkCurvatureFlowImageFilterIF2IF2_cast = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF2IF2_cast

class itkCurvatureFlowImageFilterIF3IF3(itkDenseFiniteDifferenceImageFilterPython.itkDenseFiniteDifferenceImageFilterIF3IF3):
    r"""Proxy of C++ itkCurvatureFlowImageFilterIF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF3IF3_Clone)
    SetTimeStep = _swig_new_instance_method(_itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF3IF3_SetTimeStep)
    GetTimeStep = _swig_new_instance_method(_itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF3IF3_GetTimeStep)
    DoubleConvertibleToOutputCheck = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF3IF3_DoubleConvertibleToOutputCheck
    
    OutputConvertibleToDoubleCheck = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF3IF3_OutputConvertibleToDoubleCheck
    
    OutputDivisionOperatorsCheck = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF3IF3_OutputDivisionOperatorsCheck
    
    DoubleOutputMultiplyOperatorCheck = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF3IF3_DoubleOutputMultiplyOperatorCheck
    
    IntOutputMultiplyOperatorCheck = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF3IF3_IntOutputMultiplyOperatorCheck
    
    OutputLessThanDoubleCheck = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF3IF3_OutputLessThanDoubleCheck
    
    OutputDoubleAdditiveOperatorsCheck = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF3IF3_OutputDoubleAdditiveOperatorsCheck
    
    __swig_destroy__ = _itkCurvatureFlowImageFilterPython.delete_itkCurvatureFlowImageFilterIF3IF3
    cast = _swig_new_static_method(_itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkCurvatureFlowImageFilterIF3IF3

        Create a new object of the class itkCurvatureFlowImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCurvatureFlowImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCurvatureFlowImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCurvatureFlowImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkCurvatureFlowImageFilterIF3IF3 in _itkCurvatureFlowImageFilterPython:
_itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF3IF3_swigregister(itkCurvatureFlowImageFilterIF3IF3)
itkCurvatureFlowImageFilterIF3IF3___New_orig__ = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF3IF3___New_orig__
itkCurvatureFlowImageFilterIF3IF3_cast = _itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF3IF3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def curvature_flow_image_filter(*args, **kwargs):
    """Procedural interface for CurvatureFlowImageFilter"""
    import itk
    instance = itk.CurvatureFlowImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def curvature_flow_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.CurvatureFlowImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.CurvatureFlowImageFilter.values()[0]
    else:
        filter_object = itk.CurvatureFlowImageFilter

    curvature_flow_image_filter.__doc__ = filter_object.__doc__
    curvature_flow_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    curvature_flow_image_filter.__doc__ += "Available Keyword Arguments:\n"
    curvature_flow_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



