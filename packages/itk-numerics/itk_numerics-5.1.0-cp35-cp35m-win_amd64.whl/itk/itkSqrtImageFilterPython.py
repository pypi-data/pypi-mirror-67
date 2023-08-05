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
    from . import _itkSqrtImageFilterPython
else:
    import _itkSqrtImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkSqrtImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkSqrtImageFilterPython.SWIG_PyStaticMethod_New

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
import itkUnaryGeneratorImageFilterPython
import itkInPlaceImageFilterBPython
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
import itkInPlaceImageFilterAPython
import itkImageToImageFilterAPython

def itkSqrtImageFilterID3ID3_New():
  return itkSqrtImageFilterID3ID3.New()


def itkSqrtImageFilterID2ID2_New():
  return itkSqrtImageFilterID2ID2.New()


def itkSqrtImageFilterIF3IF3_New():
  return itkSqrtImageFilterIF3IF3.New()


def itkSqrtImageFilterIF2IF2_New():
  return itkSqrtImageFilterIF2IF2.New()


def itkSqrtImageFilterIUS3IUS3_New():
  return itkSqrtImageFilterIUS3IUS3.New()


def itkSqrtImageFilterIUS2IUS2_New():
  return itkSqrtImageFilterIUS2IUS2.New()


def itkSqrtImageFilterIUC3IUC3_New():
  return itkSqrtImageFilterIUC3IUC3.New()


def itkSqrtImageFilterIUC2IUC2_New():
  return itkSqrtImageFilterIUC2IUC2.New()


def itkSqrtImageFilterISS3ISS3_New():
  return itkSqrtImageFilterISS3ISS3.New()


def itkSqrtImageFilterISS2ISS2_New():
  return itkSqrtImageFilterISS2ISS2.New()

class itkSqrtImageFilterID2ID2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID2ID2):
    r"""Proxy of C++ itkSqrtImageFilterID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSqrtImageFilterPython.itkSqrtImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkSqrtImageFilterPython.itkSqrtImageFilterID2ID2_Clone)
    InputConvertibleToDoubleCheck = _itkSqrtImageFilterPython.itkSqrtImageFilterID2ID2_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkSqrtImageFilterPython.itkSqrtImageFilterID2ID2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSqrtImageFilterPython.delete_itkSqrtImageFilterID2ID2
    cast = _swig_new_static_method(_itkSqrtImageFilterPython.itkSqrtImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkSqrtImageFilterID2ID2

        Create a new object of the class itkSqrtImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSqrtImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSqrtImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSqrtImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSqrtImageFilterID2ID2 in _itkSqrtImageFilterPython:
_itkSqrtImageFilterPython.itkSqrtImageFilterID2ID2_swigregister(itkSqrtImageFilterID2ID2)
itkSqrtImageFilterID2ID2___New_orig__ = _itkSqrtImageFilterPython.itkSqrtImageFilterID2ID2___New_orig__
itkSqrtImageFilterID2ID2_cast = _itkSqrtImageFilterPython.itkSqrtImageFilterID2ID2_cast

class itkSqrtImageFilterID3ID3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID3ID3):
    r"""Proxy of C++ itkSqrtImageFilterID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSqrtImageFilterPython.itkSqrtImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkSqrtImageFilterPython.itkSqrtImageFilterID3ID3_Clone)
    InputConvertibleToDoubleCheck = _itkSqrtImageFilterPython.itkSqrtImageFilterID3ID3_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkSqrtImageFilterPython.itkSqrtImageFilterID3ID3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSqrtImageFilterPython.delete_itkSqrtImageFilterID3ID3
    cast = _swig_new_static_method(_itkSqrtImageFilterPython.itkSqrtImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkSqrtImageFilterID3ID3

        Create a new object of the class itkSqrtImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSqrtImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSqrtImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSqrtImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSqrtImageFilterID3ID3 in _itkSqrtImageFilterPython:
_itkSqrtImageFilterPython.itkSqrtImageFilterID3ID3_swigregister(itkSqrtImageFilterID3ID3)
itkSqrtImageFilterID3ID3___New_orig__ = _itkSqrtImageFilterPython.itkSqrtImageFilterID3ID3___New_orig__
itkSqrtImageFilterID3ID3_cast = _itkSqrtImageFilterPython.itkSqrtImageFilterID3ID3_cast

class itkSqrtImageFilterIF2IF2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF2IF2):
    r"""Proxy of C++ itkSqrtImageFilterIF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSqrtImageFilterPython.itkSqrtImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkSqrtImageFilterPython.itkSqrtImageFilterIF2IF2_Clone)
    InputConvertibleToDoubleCheck = _itkSqrtImageFilterPython.itkSqrtImageFilterIF2IF2_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkSqrtImageFilterPython.itkSqrtImageFilterIF2IF2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSqrtImageFilterPython.delete_itkSqrtImageFilterIF2IF2
    cast = _swig_new_static_method(_itkSqrtImageFilterPython.itkSqrtImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkSqrtImageFilterIF2IF2

        Create a new object of the class itkSqrtImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSqrtImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSqrtImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSqrtImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSqrtImageFilterIF2IF2 in _itkSqrtImageFilterPython:
_itkSqrtImageFilterPython.itkSqrtImageFilterIF2IF2_swigregister(itkSqrtImageFilterIF2IF2)
itkSqrtImageFilterIF2IF2___New_orig__ = _itkSqrtImageFilterPython.itkSqrtImageFilterIF2IF2___New_orig__
itkSqrtImageFilterIF2IF2_cast = _itkSqrtImageFilterPython.itkSqrtImageFilterIF2IF2_cast

class itkSqrtImageFilterIF3IF3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF3IF3):
    r"""Proxy of C++ itkSqrtImageFilterIF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSqrtImageFilterPython.itkSqrtImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkSqrtImageFilterPython.itkSqrtImageFilterIF3IF3_Clone)
    InputConvertibleToDoubleCheck = _itkSqrtImageFilterPython.itkSqrtImageFilterIF3IF3_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkSqrtImageFilterPython.itkSqrtImageFilterIF3IF3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSqrtImageFilterPython.delete_itkSqrtImageFilterIF3IF3
    cast = _swig_new_static_method(_itkSqrtImageFilterPython.itkSqrtImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkSqrtImageFilterIF3IF3

        Create a new object of the class itkSqrtImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSqrtImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSqrtImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSqrtImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSqrtImageFilterIF3IF3 in _itkSqrtImageFilterPython:
_itkSqrtImageFilterPython.itkSqrtImageFilterIF3IF3_swigregister(itkSqrtImageFilterIF3IF3)
itkSqrtImageFilterIF3IF3___New_orig__ = _itkSqrtImageFilterPython.itkSqrtImageFilterIF3IF3___New_orig__
itkSqrtImageFilterIF3IF3_cast = _itkSqrtImageFilterPython.itkSqrtImageFilterIF3IF3_cast

class itkSqrtImageFilterISS2ISS2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterISS2ISS2):
    r"""Proxy of C++ itkSqrtImageFilterISS2ISS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSqrtImageFilterPython.itkSqrtImageFilterISS2ISS2___New_orig__)
    Clone = _swig_new_instance_method(_itkSqrtImageFilterPython.itkSqrtImageFilterISS2ISS2_Clone)
    InputConvertibleToDoubleCheck = _itkSqrtImageFilterPython.itkSqrtImageFilterISS2ISS2_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkSqrtImageFilterPython.itkSqrtImageFilterISS2ISS2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSqrtImageFilterPython.delete_itkSqrtImageFilterISS2ISS2
    cast = _swig_new_static_method(_itkSqrtImageFilterPython.itkSqrtImageFilterISS2ISS2_cast)

    def New(*args, **kargs):
        """New() -> itkSqrtImageFilterISS2ISS2

        Create a new object of the class itkSqrtImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSqrtImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSqrtImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSqrtImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSqrtImageFilterISS2ISS2 in _itkSqrtImageFilterPython:
_itkSqrtImageFilterPython.itkSqrtImageFilterISS2ISS2_swigregister(itkSqrtImageFilterISS2ISS2)
itkSqrtImageFilterISS2ISS2___New_orig__ = _itkSqrtImageFilterPython.itkSqrtImageFilterISS2ISS2___New_orig__
itkSqrtImageFilterISS2ISS2_cast = _itkSqrtImageFilterPython.itkSqrtImageFilterISS2ISS2_cast

class itkSqrtImageFilterISS3ISS3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterISS3ISS3):
    r"""Proxy of C++ itkSqrtImageFilterISS3ISS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSqrtImageFilterPython.itkSqrtImageFilterISS3ISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkSqrtImageFilterPython.itkSqrtImageFilterISS3ISS3_Clone)
    InputConvertibleToDoubleCheck = _itkSqrtImageFilterPython.itkSqrtImageFilterISS3ISS3_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkSqrtImageFilterPython.itkSqrtImageFilterISS3ISS3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSqrtImageFilterPython.delete_itkSqrtImageFilterISS3ISS3
    cast = _swig_new_static_method(_itkSqrtImageFilterPython.itkSqrtImageFilterISS3ISS3_cast)

    def New(*args, **kargs):
        """New() -> itkSqrtImageFilterISS3ISS3

        Create a new object of the class itkSqrtImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSqrtImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSqrtImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSqrtImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSqrtImageFilterISS3ISS3 in _itkSqrtImageFilterPython:
_itkSqrtImageFilterPython.itkSqrtImageFilterISS3ISS3_swigregister(itkSqrtImageFilterISS3ISS3)
itkSqrtImageFilterISS3ISS3___New_orig__ = _itkSqrtImageFilterPython.itkSqrtImageFilterISS3ISS3___New_orig__
itkSqrtImageFilterISS3ISS3_cast = _itkSqrtImageFilterPython.itkSqrtImageFilterISS3ISS3_cast

class itkSqrtImageFilterIUC2IUC2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUC2IUC2):
    r"""Proxy of C++ itkSqrtImageFilterIUC2IUC2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSqrtImageFilterPython.itkSqrtImageFilterIUC2IUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkSqrtImageFilterPython.itkSqrtImageFilterIUC2IUC2_Clone)
    InputConvertibleToDoubleCheck = _itkSqrtImageFilterPython.itkSqrtImageFilterIUC2IUC2_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkSqrtImageFilterPython.itkSqrtImageFilterIUC2IUC2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSqrtImageFilterPython.delete_itkSqrtImageFilterIUC2IUC2
    cast = _swig_new_static_method(_itkSqrtImageFilterPython.itkSqrtImageFilterIUC2IUC2_cast)

    def New(*args, **kargs):
        """New() -> itkSqrtImageFilterIUC2IUC2

        Create a new object of the class itkSqrtImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSqrtImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSqrtImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSqrtImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSqrtImageFilterIUC2IUC2 in _itkSqrtImageFilterPython:
_itkSqrtImageFilterPython.itkSqrtImageFilterIUC2IUC2_swigregister(itkSqrtImageFilterIUC2IUC2)
itkSqrtImageFilterIUC2IUC2___New_orig__ = _itkSqrtImageFilterPython.itkSqrtImageFilterIUC2IUC2___New_orig__
itkSqrtImageFilterIUC2IUC2_cast = _itkSqrtImageFilterPython.itkSqrtImageFilterIUC2IUC2_cast

class itkSqrtImageFilterIUC3IUC3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUC3IUC3):
    r"""Proxy of C++ itkSqrtImageFilterIUC3IUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSqrtImageFilterPython.itkSqrtImageFilterIUC3IUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkSqrtImageFilterPython.itkSqrtImageFilterIUC3IUC3_Clone)
    InputConvertibleToDoubleCheck = _itkSqrtImageFilterPython.itkSqrtImageFilterIUC3IUC3_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkSqrtImageFilterPython.itkSqrtImageFilterIUC3IUC3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSqrtImageFilterPython.delete_itkSqrtImageFilterIUC3IUC3
    cast = _swig_new_static_method(_itkSqrtImageFilterPython.itkSqrtImageFilterIUC3IUC3_cast)

    def New(*args, **kargs):
        """New() -> itkSqrtImageFilterIUC3IUC3

        Create a new object of the class itkSqrtImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSqrtImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSqrtImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSqrtImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSqrtImageFilterIUC3IUC3 in _itkSqrtImageFilterPython:
_itkSqrtImageFilterPython.itkSqrtImageFilterIUC3IUC3_swigregister(itkSqrtImageFilterIUC3IUC3)
itkSqrtImageFilterIUC3IUC3___New_orig__ = _itkSqrtImageFilterPython.itkSqrtImageFilterIUC3IUC3___New_orig__
itkSqrtImageFilterIUC3IUC3_cast = _itkSqrtImageFilterPython.itkSqrtImageFilterIUC3IUC3_cast

class itkSqrtImageFilterIUS2IUS2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUS2IUS2):
    r"""Proxy of C++ itkSqrtImageFilterIUS2IUS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSqrtImageFilterPython.itkSqrtImageFilterIUS2IUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkSqrtImageFilterPython.itkSqrtImageFilterIUS2IUS2_Clone)
    InputConvertibleToDoubleCheck = _itkSqrtImageFilterPython.itkSqrtImageFilterIUS2IUS2_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkSqrtImageFilterPython.itkSqrtImageFilterIUS2IUS2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSqrtImageFilterPython.delete_itkSqrtImageFilterIUS2IUS2
    cast = _swig_new_static_method(_itkSqrtImageFilterPython.itkSqrtImageFilterIUS2IUS2_cast)

    def New(*args, **kargs):
        """New() -> itkSqrtImageFilterIUS2IUS2

        Create a new object of the class itkSqrtImageFilterIUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSqrtImageFilterIUS2IUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSqrtImageFilterIUS2IUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSqrtImageFilterIUS2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSqrtImageFilterIUS2IUS2 in _itkSqrtImageFilterPython:
_itkSqrtImageFilterPython.itkSqrtImageFilterIUS2IUS2_swigregister(itkSqrtImageFilterIUS2IUS2)
itkSqrtImageFilterIUS2IUS2___New_orig__ = _itkSqrtImageFilterPython.itkSqrtImageFilterIUS2IUS2___New_orig__
itkSqrtImageFilterIUS2IUS2_cast = _itkSqrtImageFilterPython.itkSqrtImageFilterIUS2IUS2_cast

class itkSqrtImageFilterIUS3IUS3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUS3IUS3):
    r"""Proxy of C++ itkSqrtImageFilterIUS3IUS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSqrtImageFilterPython.itkSqrtImageFilterIUS3IUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkSqrtImageFilterPython.itkSqrtImageFilterIUS3IUS3_Clone)
    InputConvertibleToDoubleCheck = _itkSqrtImageFilterPython.itkSqrtImageFilterIUS3IUS3_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkSqrtImageFilterPython.itkSqrtImageFilterIUS3IUS3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkSqrtImageFilterPython.delete_itkSqrtImageFilterIUS3IUS3
    cast = _swig_new_static_method(_itkSqrtImageFilterPython.itkSqrtImageFilterIUS3IUS3_cast)

    def New(*args, **kargs):
        """New() -> itkSqrtImageFilterIUS3IUS3

        Create a new object of the class itkSqrtImageFilterIUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSqrtImageFilterIUS3IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSqrtImageFilterIUS3IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSqrtImageFilterIUS3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSqrtImageFilterIUS3IUS3 in _itkSqrtImageFilterPython:
_itkSqrtImageFilterPython.itkSqrtImageFilterIUS3IUS3_swigregister(itkSqrtImageFilterIUS3IUS3)
itkSqrtImageFilterIUS3IUS3___New_orig__ = _itkSqrtImageFilterPython.itkSqrtImageFilterIUS3IUS3___New_orig__
itkSqrtImageFilterIUS3IUS3_cast = _itkSqrtImageFilterPython.itkSqrtImageFilterIUS3IUS3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def sqrt_image_filter(*args, **kwargs):
    """Procedural interface for SqrtImageFilter"""
    import itk
    instance = itk.SqrtImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def sqrt_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.SqrtImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.SqrtImageFilter.values()[0]
    else:
        filter_object = itk.SqrtImageFilter

    sqrt_image_filter.__doc__ = filter_object.__doc__
    sqrt_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    sqrt_image_filter.__doc__ += "Available Keyword Arguments:\n"
    sqrt_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



