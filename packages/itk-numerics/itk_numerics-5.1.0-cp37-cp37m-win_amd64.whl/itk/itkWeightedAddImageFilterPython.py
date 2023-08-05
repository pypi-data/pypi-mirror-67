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
    from . import _itkWeightedAddImageFilterPython
else:
    import _itkWeightedAddImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkWeightedAddImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkWeightedAddImageFilterPython.SWIG_PyStaticMethod_New

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
import itkCovariantVectorPython
import itkVectorPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkFixedArrayPython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkInPlaceImageFilterBPython
import itkImageToImageFilterBPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImagePython
import itkOffsetPython
import itkSizePython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkSymmetricSecondRankTensorPython
import itkImageRegionPython
import itkIndexPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkSimpleDataObjectDecoratorPython
import itkArrayPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterAPython

def itkWeightedAddImageFilterID3ID3ID3_New():
  return itkWeightedAddImageFilterID3ID3ID3.New()


def itkWeightedAddImageFilterID2ID2ID2_New():
  return itkWeightedAddImageFilterID2ID2ID2.New()


def itkWeightedAddImageFilterIF3IF3IF3_New():
  return itkWeightedAddImageFilterIF3IF3IF3.New()


def itkWeightedAddImageFilterIF2IF2IF2_New():
  return itkWeightedAddImageFilterIF2IF2IF2.New()


def itkWeightedAddImageFilterIUS3IUS3IUS3_New():
  return itkWeightedAddImageFilterIUS3IUS3IUS3.New()


def itkWeightedAddImageFilterIUS2IUS2IUS2_New():
  return itkWeightedAddImageFilterIUS2IUS2IUS2.New()


def itkWeightedAddImageFilterIUC3IUC3IUC3_New():
  return itkWeightedAddImageFilterIUC3IUC3IUC3.New()


def itkWeightedAddImageFilterIUC2IUC2IUC2_New():
  return itkWeightedAddImageFilterIUC2IUC2IUC2.New()


def itkWeightedAddImageFilterISS3ISS3ISS3_New():
  return itkWeightedAddImageFilterISS3ISS3ISS3.New()


def itkWeightedAddImageFilterISS2ISS2ISS2_New():
  return itkWeightedAddImageFilterISS2ISS2ISS2.New()

class itkWeightedAddImageFilterID2ID2ID2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterID2ID2ID2):
    r"""Proxy of C++ itkWeightedAddImageFilterID2ID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterID2ID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterID2ID2ID2_Clone)
    SetAlpha = _swig_new_instance_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterID2ID2ID2_SetAlpha)
    GetAlpha = _swig_new_instance_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterID2ID2ID2_GetAlpha)
    Input1HasNumericTraitsCheck = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterID2ID2ID2_Input1HasNumericTraitsCheck
    
    Input1RealTypeMultiplyCheck = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterID2ID2ID2_Input1RealTypeMultiplyCheck
    
    Input2RealTypeMultiplyCheck = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterID2ID2ID2_Input2RealTypeMultiplyCheck
    
    __swig_destroy__ = _itkWeightedAddImageFilterPython.delete_itkWeightedAddImageFilterID2ID2ID2
    cast = _swig_new_static_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterID2ID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkWeightedAddImageFilterID2ID2ID2

        Create a new object of the class itkWeightedAddImageFilterID2ID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkWeightedAddImageFilterID2ID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkWeightedAddImageFilterID2ID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkWeightedAddImageFilterID2ID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkWeightedAddImageFilterID2ID2ID2 in _itkWeightedAddImageFilterPython:
_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterID2ID2ID2_swigregister(itkWeightedAddImageFilterID2ID2ID2)
itkWeightedAddImageFilterID2ID2ID2___New_orig__ = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterID2ID2ID2___New_orig__
itkWeightedAddImageFilterID2ID2ID2_cast = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterID2ID2ID2_cast

class itkWeightedAddImageFilterID3ID3ID3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterID3ID3ID3):
    r"""Proxy of C++ itkWeightedAddImageFilterID3ID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterID3ID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterID3ID3ID3_Clone)
    SetAlpha = _swig_new_instance_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterID3ID3ID3_SetAlpha)
    GetAlpha = _swig_new_instance_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterID3ID3ID3_GetAlpha)
    Input1HasNumericTraitsCheck = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterID3ID3ID3_Input1HasNumericTraitsCheck
    
    Input1RealTypeMultiplyCheck = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterID3ID3ID3_Input1RealTypeMultiplyCheck
    
    Input2RealTypeMultiplyCheck = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterID3ID3ID3_Input2RealTypeMultiplyCheck
    
    __swig_destroy__ = _itkWeightedAddImageFilterPython.delete_itkWeightedAddImageFilterID3ID3ID3
    cast = _swig_new_static_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterID3ID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkWeightedAddImageFilterID3ID3ID3

        Create a new object of the class itkWeightedAddImageFilterID3ID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkWeightedAddImageFilterID3ID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkWeightedAddImageFilterID3ID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkWeightedAddImageFilterID3ID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkWeightedAddImageFilterID3ID3ID3 in _itkWeightedAddImageFilterPython:
_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterID3ID3ID3_swigregister(itkWeightedAddImageFilterID3ID3ID3)
itkWeightedAddImageFilterID3ID3ID3___New_orig__ = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterID3ID3ID3___New_orig__
itkWeightedAddImageFilterID3ID3ID3_cast = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterID3ID3ID3_cast

class itkWeightedAddImageFilterIF2IF2IF2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIF2IF2IF2):
    r"""Proxy of C++ itkWeightedAddImageFilterIF2IF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIF2IF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIF2IF2IF2_Clone)
    SetAlpha = _swig_new_instance_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIF2IF2IF2_SetAlpha)
    GetAlpha = _swig_new_instance_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIF2IF2IF2_GetAlpha)
    Input1HasNumericTraitsCheck = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIF2IF2IF2_Input1HasNumericTraitsCheck
    
    Input1RealTypeMultiplyCheck = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIF2IF2IF2_Input1RealTypeMultiplyCheck
    
    Input2RealTypeMultiplyCheck = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIF2IF2IF2_Input2RealTypeMultiplyCheck
    
    __swig_destroy__ = _itkWeightedAddImageFilterPython.delete_itkWeightedAddImageFilterIF2IF2IF2
    cast = _swig_new_static_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIF2IF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkWeightedAddImageFilterIF2IF2IF2

        Create a new object of the class itkWeightedAddImageFilterIF2IF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkWeightedAddImageFilterIF2IF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkWeightedAddImageFilterIF2IF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkWeightedAddImageFilterIF2IF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkWeightedAddImageFilterIF2IF2IF2 in _itkWeightedAddImageFilterPython:
_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIF2IF2IF2_swigregister(itkWeightedAddImageFilterIF2IF2IF2)
itkWeightedAddImageFilterIF2IF2IF2___New_orig__ = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIF2IF2IF2___New_orig__
itkWeightedAddImageFilterIF2IF2IF2_cast = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIF2IF2IF2_cast

class itkWeightedAddImageFilterIF3IF3IF3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIF3IF3IF3):
    r"""Proxy of C++ itkWeightedAddImageFilterIF3IF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIF3IF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIF3IF3IF3_Clone)
    SetAlpha = _swig_new_instance_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIF3IF3IF3_SetAlpha)
    GetAlpha = _swig_new_instance_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIF3IF3IF3_GetAlpha)
    Input1HasNumericTraitsCheck = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIF3IF3IF3_Input1HasNumericTraitsCheck
    
    Input1RealTypeMultiplyCheck = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIF3IF3IF3_Input1RealTypeMultiplyCheck
    
    Input2RealTypeMultiplyCheck = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIF3IF3IF3_Input2RealTypeMultiplyCheck
    
    __swig_destroy__ = _itkWeightedAddImageFilterPython.delete_itkWeightedAddImageFilterIF3IF3IF3
    cast = _swig_new_static_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIF3IF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkWeightedAddImageFilterIF3IF3IF3

        Create a new object of the class itkWeightedAddImageFilterIF3IF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkWeightedAddImageFilterIF3IF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkWeightedAddImageFilterIF3IF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkWeightedAddImageFilterIF3IF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkWeightedAddImageFilterIF3IF3IF3 in _itkWeightedAddImageFilterPython:
_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIF3IF3IF3_swigregister(itkWeightedAddImageFilterIF3IF3IF3)
itkWeightedAddImageFilterIF3IF3IF3___New_orig__ = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIF3IF3IF3___New_orig__
itkWeightedAddImageFilterIF3IF3IF3_cast = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIF3IF3IF3_cast

class itkWeightedAddImageFilterISS2ISS2ISS2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterISS2ISS2ISS2):
    r"""Proxy of C++ itkWeightedAddImageFilterISS2ISS2ISS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterISS2ISS2ISS2___New_orig__)
    Clone = _swig_new_instance_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterISS2ISS2ISS2_Clone)
    SetAlpha = _swig_new_instance_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterISS2ISS2ISS2_SetAlpha)
    GetAlpha = _swig_new_instance_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterISS2ISS2ISS2_GetAlpha)
    Input1HasNumericTraitsCheck = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterISS2ISS2ISS2_Input1HasNumericTraitsCheck
    
    Input1RealTypeMultiplyCheck = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterISS2ISS2ISS2_Input1RealTypeMultiplyCheck
    
    Input2RealTypeMultiplyCheck = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterISS2ISS2ISS2_Input2RealTypeMultiplyCheck
    
    __swig_destroy__ = _itkWeightedAddImageFilterPython.delete_itkWeightedAddImageFilterISS2ISS2ISS2
    cast = _swig_new_static_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterISS2ISS2ISS2_cast)

    def New(*args, **kargs):
        """New() -> itkWeightedAddImageFilterISS2ISS2ISS2

        Create a new object of the class itkWeightedAddImageFilterISS2ISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkWeightedAddImageFilterISS2ISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkWeightedAddImageFilterISS2ISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkWeightedAddImageFilterISS2ISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkWeightedAddImageFilterISS2ISS2ISS2 in _itkWeightedAddImageFilterPython:
_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterISS2ISS2ISS2_swigregister(itkWeightedAddImageFilterISS2ISS2ISS2)
itkWeightedAddImageFilterISS2ISS2ISS2___New_orig__ = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterISS2ISS2ISS2___New_orig__
itkWeightedAddImageFilterISS2ISS2ISS2_cast = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterISS2ISS2ISS2_cast

class itkWeightedAddImageFilterISS3ISS3ISS3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterISS3ISS3ISS3):
    r"""Proxy of C++ itkWeightedAddImageFilterISS3ISS3ISS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterISS3ISS3ISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterISS3ISS3ISS3_Clone)
    SetAlpha = _swig_new_instance_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterISS3ISS3ISS3_SetAlpha)
    GetAlpha = _swig_new_instance_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterISS3ISS3ISS3_GetAlpha)
    Input1HasNumericTraitsCheck = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterISS3ISS3ISS3_Input1HasNumericTraitsCheck
    
    Input1RealTypeMultiplyCheck = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterISS3ISS3ISS3_Input1RealTypeMultiplyCheck
    
    Input2RealTypeMultiplyCheck = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterISS3ISS3ISS3_Input2RealTypeMultiplyCheck
    
    __swig_destroy__ = _itkWeightedAddImageFilterPython.delete_itkWeightedAddImageFilterISS3ISS3ISS3
    cast = _swig_new_static_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterISS3ISS3ISS3_cast)

    def New(*args, **kargs):
        """New() -> itkWeightedAddImageFilterISS3ISS3ISS3

        Create a new object of the class itkWeightedAddImageFilterISS3ISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkWeightedAddImageFilterISS3ISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkWeightedAddImageFilterISS3ISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkWeightedAddImageFilterISS3ISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkWeightedAddImageFilterISS3ISS3ISS3 in _itkWeightedAddImageFilterPython:
_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterISS3ISS3ISS3_swigregister(itkWeightedAddImageFilterISS3ISS3ISS3)
itkWeightedAddImageFilterISS3ISS3ISS3___New_orig__ = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterISS3ISS3ISS3___New_orig__
itkWeightedAddImageFilterISS3ISS3ISS3_cast = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterISS3ISS3ISS3_cast

class itkWeightedAddImageFilterIUC2IUC2IUC2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUC2IUC2IUC2):
    r"""Proxy of C++ itkWeightedAddImageFilterIUC2IUC2IUC2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUC2IUC2IUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUC2IUC2IUC2_Clone)
    SetAlpha = _swig_new_instance_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUC2IUC2IUC2_SetAlpha)
    GetAlpha = _swig_new_instance_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUC2IUC2IUC2_GetAlpha)
    Input1HasNumericTraitsCheck = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUC2IUC2IUC2_Input1HasNumericTraitsCheck
    
    Input1RealTypeMultiplyCheck = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUC2IUC2IUC2_Input1RealTypeMultiplyCheck
    
    Input2RealTypeMultiplyCheck = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUC2IUC2IUC2_Input2RealTypeMultiplyCheck
    
    __swig_destroy__ = _itkWeightedAddImageFilterPython.delete_itkWeightedAddImageFilterIUC2IUC2IUC2
    cast = _swig_new_static_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUC2IUC2IUC2_cast)

    def New(*args, **kargs):
        """New() -> itkWeightedAddImageFilterIUC2IUC2IUC2

        Create a new object of the class itkWeightedAddImageFilterIUC2IUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkWeightedAddImageFilterIUC2IUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkWeightedAddImageFilterIUC2IUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkWeightedAddImageFilterIUC2IUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkWeightedAddImageFilterIUC2IUC2IUC2 in _itkWeightedAddImageFilterPython:
_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUC2IUC2IUC2_swigregister(itkWeightedAddImageFilterIUC2IUC2IUC2)
itkWeightedAddImageFilterIUC2IUC2IUC2___New_orig__ = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUC2IUC2IUC2___New_orig__
itkWeightedAddImageFilterIUC2IUC2IUC2_cast = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUC2IUC2IUC2_cast

class itkWeightedAddImageFilterIUC3IUC3IUC3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUC3IUC3IUC3):
    r"""Proxy of C++ itkWeightedAddImageFilterIUC3IUC3IUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUC3IUC3IUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUC3IUC3IUC3_Clone)
    SetAlpha = _swig_new_instance_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUC3IUC3IUC3_SetAlpha)
    GetAlpha = _swig_new_instance_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUC3IUC3IUC3_GetAlpha)
    Input1HasNumericTraitsCheck = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUC3IUC3IUC3_Input1HasNumericTraitsCheck
    
    Input1RealTypeMultiplyCheck = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUC3IUC3IUC3_Input1RealTypeMultiplyCheck
    
    Input2RealTypeMultiplyCheck = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUC3IUC3IUC3_Input2RealTypeMultiplyCheck
    
    __swig_destroy__ = _itkWeightedAddImageFilterPython.delete_itkWeightedAddImageFilterIUC3IUC3IUC3
    cast = _swig_new_static_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUC3IUC3IUC3_cast)

    def New(*args, **kargs):
        """New() -> itkWeightedAddImageFilterIUC3IUC3IUC3

        Create a new object of the class itkWeightedAddImageFilterIUC3IUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkWeightedAddImageFilterIUC3IUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkWeightedAddImageFilterIUC3IUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkWeightedAddImageFilterIUC3IUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkWeightedAddImageFilterIUC3IUC3IUC3 in _itkWeightedAddImageFilterPython:
_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUC3IUC3IUC3_swigregister(itkWeightedAddImageFilterIUC3IUC3IUC3)
itkWeightedAddImageFilterIUC3IUC3IUC3___New_orig__ = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUC3IUC3IUC3___New_orig__
itkWeightedAddImageFilterIUC3IUC3IUC3_cast = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUC3IUC3IUC3_cast

class itkWeightedAddImageFilterIUS2IUS2IUS2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUS2IUS2IUS2):
    r"""Proxy of C++ itkWeightedAddImageFilterIUS2IUS2IUS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUS2IUS2IUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUS2IUS2IUS2_Clone)
    SetAlpha = _swig_new_instance_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUS2IUS2IUS2_SetAlpha)
    GetAlpha = _swig_new_instance_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUS2IUS2IUS2_GetAlpha)
    Input1HasNumericTraitsCheck = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUS2IUS2IUS2_Input1HasNumericTraitsCheck
    
    Input1RealTypeMultiplyCheck = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUS2IUS2IUS2_Input1RealTypeMultiplyCheck
    
    Input2RealTypeMultiplyCheck = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUS2IUS2IUS2_Input2RealTypeMultiplyCheck
    
    __swig_destroy__ = _itkWeightedAddImageFilterPython.delete_itkWeightedAddImageFilterIUS2IUS2IUS2
    cast = _swig_new_static_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUS2IUS2IUS2_cast)

    def New(*args, **kargs):
        """New() -> itkWeightedAddImageFilterIUS2IUS2IUS2

        Create a new object of the class itkWeightedAddImageFilterIUS2IUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkWeightedAddImageFilterIUS2IUS2IUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkWeightedAddImageFilterIUS2IUS2IUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkWeightedAddImageFilterIUS2IUS2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkWeightedAddImageFilterIUS2IUS2IUS2 in _itkWeightedAddImageFilterPython:
_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUS2IUS2IUS2_swigregister(itkWeightedAddImageFilterIUS2IUS2IUS2)
itkWeightedAddImageFilterIUS2IUS2IUS2___New_orig__ = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUS2IUS2IUS2___New_orig__
itkWeightedAddImageFilterIUS2IUS2IUS2_cast = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUS2IUS2IUS2_cast

class itkWeightedAddImageFilterIUS3IUS3IUS3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUS3IUS3IUS3):
    r"""Proxy of C++ itkWeightedAddImageFilterIUS3IUS3IUS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUS3IUS3IUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUS3IUS3IUS3_Clone)
    SetAlpha = _swig_new_instance_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUS3IUS3IUS3_SetAlpha)
    GetAlpha = _swig_new_instance_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUS3IUS3IUS3_GetAlpha)
    Input1HasNumericTraitsCheck = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUS3IUS3IUS3_Input1HasNumericTraitsCheck
    
    Input1RealTypeMultiplyCheck = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUS3IUS3IUS3_Input1RealTypeMultiplyCheck
    
    Input2RealTypeMultiplyCheck = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUS3IUS3IUS3_Input2RealTypeMultiplyCheck
    
    __swig_destroy__ = _itkWeightedAddImageFilterPython.delete_itkWeightedAddImageFilterIUS3IUS3IUS3
    cast = _swig_new_static_method(_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUS3IUS3IUS3_cast)

    def New(*args, **kargs):
        """New() -> itkWeightedAddImageFilterIUS3IUS3IUS3

        Create a new object of the class itkWeightedAddImageFilterIUS3IUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkWeightedAddImageFilterIUS3IUS3IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkWeightedAddImageFilterIUS3IUS3IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkWeightedAddImageFilterIUS3IUS3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkWeightedAddImageFilterIUS3IUS3IUS3 in _itkWeightedAddImageFilterPython:
_itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUS3IUS3IUS3_swigregister(itkWeightedAddImageFilterIUS3IUS3IUS3)
itkWeightedAddImageFilterIUS3IUS3IUS3___New_orig__ = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUS3IUS3IUS3___New_orig__
itkWeightedAddImageFilterIUS3IUS3IUS3_cast = _itkWeightedAddImageFilterPython.itkWeightedAddImageFilterIUS3IUS3IUS3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def weighted_add_image_filter(*args, **kwargs):
    """Procedural interface for WeightedAddImageFilter"""
    import itk
    instance = itk.WeightedAddImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def weighted_add_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.WeightedAddImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.WeightedAddImageFilter.values()[0]
    else:
        filter_object = itk.WeightedAddImageFilter

    weighted_add_image_filter.__doc__ = filter_object.__doc__
    weighted_add_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    weighted_add_image_filter.__doc__ += "Available Keyword Arguments:\n"
    weighted_add_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



