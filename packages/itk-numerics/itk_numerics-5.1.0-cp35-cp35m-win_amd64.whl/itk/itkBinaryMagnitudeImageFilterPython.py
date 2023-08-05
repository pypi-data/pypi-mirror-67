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
    from . import _itkBinaryMagnitudeImageFilterPython
else:
    import _itkBinaryMagnitudeImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkBinaryMagnitudeImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkBinaryMagnitudeImageFilterPython.SWIG_PyStaticMethod_New

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

def itkBinaryMagnitudeImageFilterID3ID3ID3_New():
  return itkBinaryMagnitudeImageFilterID3ID3ID3.New()


def itkBinaryMagnitudeImageFilterID2ID2ID2_New():
  return itkBinaryMagnitudeImageFilterID2ID2ID2.New()


def itkBinaryMagnitudeImageFilterIF3IF3IF3_New():
  return itkBinaryMagnitudeImageFilterIF3IF3IF3.New()


def itkBinaryMagnitudeImageFilterIF2IF2IF2_New():
  return itkBinaryMagnitudeImageFilterIF2IF2IF2.New()


def itkBinaryMagnitudeImageFilterIUS3IUS3IUS3_New():
  return itkBinaryMagnitudeImageFilterIUS3IUS3IUS3.New()


def itkBinaryMagnitudeImageFilterIUS2IUS2IUS2_New():
  return itkBinaryMagnitudeImageFilterIUS2IUS2IUS2.New()


def itkBinaryMagnitudeImageFilterIUC3IUC3IUC3_New():
  return itkBinaryMagnitudeImageFilterIUC3IUC3IUC3.New()


def itkBinaryMagnitudeImageFilterIUC2IUC2IUC2_New():
  return itkBinaryMagnitudeImageFilterIUC2IUC2IUC2.New()


def itkBinaryMagnitudeImageFilterISS3ISS3ISS3_New():
  return itkBinaryMagnitudeImageFilterISS3ISS3ISS3.New()


def itkBinaryMagnitudeImageFilterISS2ISS2ISS2_New():
  return itkBinaryMagnitudeImageFilterISS2ISS2ISS2.New()

class itkBinaryMagnitudeImageFilterID2ID2ID2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterID2ID2ID2):
    r"""Proxy of C++ itkBinaryMagnitudeImageFilterID2ID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterID2ID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterID2ID2ID2_Clone)
    Input1ConvertibleToDoubleCheck = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterID2ID2ID2_Input1ConvertibleToDoubleCheck
    
    Input2ConvertibleToDoubleCheck = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterID2ID2ID2_Input2ConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterID2ID2ID2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkBinaryMagnitudeImageFilterPython.delete_itkBinaryMagnitudeImageFilterID2ID2ID2
    cast = _swig_new_static_method(_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterID2ID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryMagnitudeImageFilterID2ID2ID2

        Create a new object of the class itkBinaryMagnitudeImageFilterID2ID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryMagnitudeImageFilterID2ID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryMagnitudeImageFilterID2ID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryMagnitudeImageFilterID2ID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryMagnitudeImageFilterID2ID2ID2 in _itkBinaryMagnitudeImageFilterPython:
_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterID2ID2ID2_swigregister(itkBinaryMagnitudeImageFilterID2ID2ID2)
itkBinaryMagnitudeImageFilterID2ID2ID2___New_orig__ = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterID2ID2ID2___New_orig__
itkBinaryMagnitudeImageFilterID2ID2ID2_cast = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterID2ID2ID2_cast

class itkBinaryMagnitudeImageFilterID3ID3ID3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterID3ID3ID3):
    r"""Proxy of C++ itkBinaryMagnitudeImageFilterID3ID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterID3ID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterID3ID3ID3_Clone)
    Input1ConvertibleToDoubleCheck = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterID3ID3ID3_Input1ConvertibleToDoubleCheck
    
    Input2ConvertibleToDoubleCheck = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterID3ID3ID3_Input2ConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterID3ID3ID3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkBinaryMagnitudeImageFilterPython.delete_itkBinaryMagnitudeImageFilterID3ID3ID3
    cast = _swig_new_static_method(_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterID3ID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryMagnitudeImageFilterID3ID3ID3

        Create a new object of the class itkBinaryMagnitudeImageFilterID3ID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryMagnitudeImageFilterID3ID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryMagnitudeImageFilterID3ID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryMagnitudeImageFilterID3ID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryMagnitudeImageFilterID3ID3ID3 in _itkBinaryMagnitudeImageFilterPython:
_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterID3ID3ID3_swigregister(itkBinaryMagnitudeImageFilterID3ID3ID3)
itkBinaryMagnitudeImageFilterID3ID3ID3___New_orig__ = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterID3ID3ID3___New_orig__
itkBinaryMagnitudeImageFilterID3ID3ID3_cast = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterID3ID3ID3_cast

class itkBinaryMagnitudeImageFilterIF2IF2IF2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIF2IF2IF2):
    r"""Proxy of C++ itkBinaryMagnitudeImageFilterIF2IF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIF2IF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIF2IF2IF2_Clone)
    Input1ConvertibleToDoubleCheck = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIF2IF2IF2_Input1ConvertibleToDoubleCheck
    
    Input2ConvertibleToDoubleCheck = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIF2IF2IF2_Input2ConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIF2IF2IF2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkBinaryMagnitudeImageFilterPython.delete_itkBinaryMagnitudeImageFilterIF2IF2IF2
    cast = _swig_new_static_method(_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIF2IF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryMagnitudeImageFilterIF2IF2IF2

        Create a new object of the class itkBinaryMagnitudeImageFilterIF2IF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryMagnitudeImageFilterIF2IF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryMagnitudeImageFilterIF2IF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryMagnitudeImageFilterIF2IF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryMagnitudeImageFilterIF2IF2IF2 in _itkBinaryMagnitudeImageFilterPython:
_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIF2IF2IF2_swigregister(itkBinaryMagnitudeImageFilterIF2IF2IF2)
itkBinaryMagnitudeImageFilterIF2IF2IF2___New_orig__ = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIF2IF2IF2___New_orig__
itkBinaryMagnitudeImageFilterIF2IF2IF2_cast = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIF2IF2IF2_cast

class itkBinaryMagnitudeImageFilterIF3IF3IF3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIF3IF3IF3):
    r"""Proxy of C++ itkBinaryMagnitudeImageFilterIF3IF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIF3IF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIF3IF3IF3_Clone)
    Input1ConvertibleToDoubleCheck = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIF3IF3IF3_Input1ConvertibleToDoubleCheck
    
    Input2ConvertibleToDoubleCheck = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIF3IF3IF3_Input2ConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIF3IF3IF3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkBinaryMagnitudeImageFilterPython.delete_itkBinaryMagnitudeImageFilterIF3IF3IF3
    cast = _swig_new_static_method(_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIF3IF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryMagnitudeImageFilterIF3IF3IF3

        Create a new object of the class itkBinaryMagnitudeImageFilterIF3IF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryMagnitudeImageFilterIF3IF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryMagnitudeImageFilterIF3IF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryMagnitudeImageFilterIF3IF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryMagnitudeImageFilterIF3IF3IF3 in _itkBinaryMagnitudeImageFilterPython:
_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIF3IF3IF3_swigregister(itkBinaryMagnitudeImageFilterIF3IF3IF3)
itkBinaryMagnitudeImageFilterIF3IF3IF3___New_orig__ = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIF3IF3IF3___New_orig__
itkBinaryMagnitudeImageFilterIF3IF3IF3_cast = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIF3IF3IF3_cast

class itkBinaryMagnitudeImageFilterISS2ISS2ISS2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterISS2ISS2ISS2):
    r"""Proxy of C++ itkBinaryMagnitudeImageFilterISS2ISS2ISS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterISS2ISS2ISS2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterISS2ISS2ISS2_Clone)
    Input1ConvertibleToDoubleCheck = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterISS2ISS2ISS2_Input1ConvertibleToDoubleCheck
    
    Input2ConvertibleToDoubleCheck = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterISS2ISS2ISS2_Input2ConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterISS2ISS2ISS2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkBinaryMagnitudeImageFilterPython.delete_itkBinaryMagnitudeImageFilterISS2ISS2ISS2
    cast = _swig_new_static_method(_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterISS2ISS2ISS2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryMagnitudeImageFilterISS2ISS2ISS2

        Create a new object of the class itkBinaryMagnitudeImageFilterISS2ISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryMagnitudeImageFilterISS2ISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryMagnitudeImageFilterISS2ISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryMagnitudeImageFilterISS2ISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryMagnitudeImageFilterISS2ISS2ISS2 in _itkBinaryMagnitudeImageFilterPython:
_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterISS2ISS2ISS2_swigregister(itkBinaryMagnitudeImageFilterISS2ISS2ISS2)
itkBinaryMagnitudeImageFilterISS2ISS2ISS2___New_orig__ = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterISS2ISS2ISS2___New_orig__
itkBinaryMagnitudeImageFilterISS2ISS2ISS2_cast = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterISS2ISS2ISS2_cast

class itkBinaryMagnitudeImageFilterISS3ISS3ISS3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterISS3ISS3ISS3):
    r"""Proxy of C++ itkBinaryMagnitudeImageFilterISS3ISS3ISS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterISS3ISS3ISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterISS3ISS3ISS3_Clone)
    Input1ConvertibleToDoubleCheck = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterISS3ISS3ISS3_Input1ConvertibleToDoubleCheck
    
    Input2ConvertibleToDoubleCheck = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterISS3ISS3ISS3_Input2ConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterISS3ISS3ISS3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkBinaryMagnitudeImageFilterPython.delete_itkBinaryMagnitudeImageFilterISS3ISS3ISS3
    cast = _swig_new_static_method(_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterISS3ISS3ISS3_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryMagnitudeImageFilterISS3ISS3ISS3

        Create a new object of the class itkBinaryMagnitudeImageFilterISS3ISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryMagnitudeImageFilterISS3ISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryMagnitudeImageFilterISS3ISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryMagnitudeImageFilterISS3ISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryMagnitudeImageFilterISS3ISS3ISS3 in _itkBinaryMagnitudeImageFilterPython:
_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterISS3ISS3ISS3_swigregister(itkBinaryMagnitudeImageFilterISS3ISS3ISS3)
itkBinaryMagnitudeImageFilterISS3ISS3ISS3___New_orig__ = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterISS3ISS3ISS3___New_orig__
itkBinaryMagnitudeImageFilterISS3ISS3ISS3_cast = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterISS3ISS3ISS3_cast

class itkBinaryMagnitudeImageFilterIUC2IUC2IUC2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUC2IUC2IUC2):
    r"""Proxy of C++ itkBinaryMagnitudeImageFilterIUC2IUC2IUC2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUC2IUC2IUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUC2IUC2IUC2_Clone)
    Input1ConvertibleToDoubleCheck = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUC2IUC2IUC2_Input1ConvertibleToDoubleCheck
    
    Input2ConvertibleToDoubleCheck = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUC2IUC2IUC2_Input2ConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUC2IUC2IUC2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkBinaryMagnitudeImageFilterPython.delete_itkBinaryMagnitudeImageFilterIUC2IUC2IUC2
    cast = _swig_new_static_method(_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUC2IUC2IUC2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryMagnitudeImageFilterIUC2IUC2IUC2

        Create a new object of the class itkBinaryMagnitudeImageFilterIUC2IUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryMagnitudeImageFilterIUC2IUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryMagnitudeImageFilterIUC2IUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryMagnitudeImageFilterIUC2IUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryMagnitudeImageFilterIUC2IUC2IUC2 in _itkBinaryMagnitudeImageFilterPython:
_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUC2IUC2IUC2_swigregister(itkBinaryMagnitudeImageFilterIUC2IUC2IUC2)
itkBinaryMagnitudeImageFilterIUC2IUC2IUC2___New_orig__ = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUC2IUC2IUC2___New_orig__
itkBinaryMagnitudeImageFilterIUC2IUC2IUC2_cast = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUC2IUC2IUC2_cast

class itkBinaryMagnitudeImageFilterIUC3IUC3IUC3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUC3IUC3IUC3):
    r"""Proxy of C++ itkBinaryMagnitudeImageFilterIUC3IUC3IUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUC3IUC3IUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUC3IUC3IUC3_Clone)
    Input1ConvertibleToDoubleCheck = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUC3IUC3IUC3_Input1ConvertibleToDoubleCheck
    
    Input2ConvertibleToDoubleCheck = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUC3IUC3IUC3_Input2ConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUC3IUC3IUC3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkBinaryMagnitudeImageFilterPython.delete_itkBinaryMagnitudeImageFilterIUC3IUC3IUC3
    cast = _swig_new_static_method(_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUC3IUC3IUC3_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryMagnitudeImageFilterIUC3IUC3IUC3

        Create a new object of the class itkBinaryMagnitudeImageFilterIUC3IUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryMagnitudeImageFilterIUC3IUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryMagnitudeImageFilterIUC3IUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryMagnitudeImageFilterIUC3IUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryMagnitudeImageFilterIUC3IUC3IUC3 in _itkBinaryMagnitudeImageFilterPython:
_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUC3IUC3IUC3_swigregister(itkBinaryMagnitudeImageFilterIUC3IUC3IUC3)
itkBinaryMagnitudeImageFilterIUC3IUC3IUC3___New_orig__ = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUC3IUC3IUC3___New_orig__
itkBinaryMagnitudeImageFilterIUC3IUC3IUC3_cast = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUC3IUC3IUC3_cast

class itkBinaryMagnitudeImageFilterIUS2IUS2IUS2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUS2IUS2IUS2):
    r"""Proxy of C++ itkBinaryMagnitudeImageFilterIUS2IUS2IUS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUS2IUS2IUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUS2IUS2IUS2_Clone)
    Input1ConvertibleToDoubleCheck = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUS2IUS2IUS2_Input1ConvertibleToDoubleCheck
    
    Input2ConvertibleToDoubleCheck = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUS2IUS2IUS2_Input2ConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUS2IUS2IUS2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkBinaryMagnitudeImageFilterPython.delete_itkBinaryMagnitudeImageFilterIUS2IUS2IUS2
    cast = _swig_new_static_method(_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUS2IUS2IUS2_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryMagnitudeImageFilterIUS2IUS2IUS2

        Create a new object of the class itkBinaryMagnitudeImageFilterIUS2IUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryMagnitudeImageFilterIUS2IUS2IUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryMagnitudeImageFilterIUS2IUS2IUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryMagnitudeImageFilterIUS2IUS2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryMagnitudeImageFilterIUS2IUS2IUS2 in _itkBinaryMagnitudeImageFilterPython:
_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUS2IUS2IUS2_swigregister(itkBinaryMagnitudeImageFilterIUS2IUS2IUS2)
itkBinaryMagnitudeImageFilterIUS2IUS2IUS2___New_orig__ = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUS2IUS2IUS2___New_orig__
itkBinaryMagnitudeImageFilterIUS2IUS2IUS2_cast = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUS2IUS2IUS2_cast

class itkBinaryMagnitudeImageFilterIUS3IUS3IUS3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUS3IUS3IUS3):
    r"""Proxy of C++ itkBinaryMagnitudeImageFilterIUS3IUS3IUS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUS3IUS3IUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUS3IUS3IUS3_Clone)
    Input1ConvertibleToDoubleCheck = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUS3IUS3IUS3_Input1ConvertibleToDoubleCheck
    
    Input2ConvertibleToDoubleCheck = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUS3IUS3IUS3_Input2ConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUS3IUS3IUS3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkBinaryMagnitudeImageFilterPython.delete_itkBinaryMagnitudeImageFilterIUS3IUS3IUS3
    cast = _swig_new_static_method(_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUS3IUS3IUS3_cast)

    def New(*args, **kargs):
        """New() -> itkBinaryMagnitudeImageFilterIUS3IUS3IUS3

        Create a new object of the class itkBinaryMagnitudeImageFilterIUS3IUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryMagnitudeImageFilterIUS3IUS3IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryMagnitudeImageFilterIUS3IUS3IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryMagnitudeImageFilterIUS3IUS3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBinaryMagnitudeImageFilterIUS3IUS3IUS3 in _itkBinaryMagnitudeImageFilterPython:
_itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUS3IUS3IUS3_swigregister(itkBinaryMagnitudeImageFilterIUS3IUS3IUS3)
itkBinaryMagnitudeImageFilterIUS3IUS3IUS3___New_orig__ = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUS3IUS3IUS3___New_orig__
itkBinaryMagnitudeImageFilterIUS3IUS3IUS3_cast = _itkBinaryMagnitudeImageFilterPython.itkBinaryMagnitudeImageFilterIUS3IUS3IUS3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def binary_magnitude_image_filter(*args, **kwargs):
    """Procedural interface for BinaryMagnitudeImageFilter"""
    import itk
    instance = itk.BinaryMagnitudeImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def binary_magnitude_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.BinaryMagnitudeImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.BinaryMagnitudeImageFilter.values()[0]
    else:
        filter_object = itk.BinaryMagnitudeImageFilter

    binary_magnitude_image_filter.__doc__ = filter_object.__doc__
    binary_magnitude_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    binary_magnitude_image_filter.__doc__ += "Available Keyword Arguments:\n"
    binary_magnitude_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



