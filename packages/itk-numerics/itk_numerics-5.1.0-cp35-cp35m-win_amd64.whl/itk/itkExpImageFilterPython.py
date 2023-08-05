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
    from . import _itkExpImageFilterPython
else:
    import _itkExpImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkExpImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkExpImageFilterPython.SWIG_PyStaticMethod_New

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
import itkInPlaceImageFilterBPython
import itkImageToImageFilterBPython
import itkImagePython
import itkPointPython
import itkFixedArrayPython
import pyBasePython
import itkVectorPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import vnl_vector_refPython
import itkRGBAPixelPython
import ITKCommonBasePython
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

def itkExpImageFilterID3ID3_New():
  return itkExpImageFilterID3ID3.New()


def itkExpImageFilterID2ID2_New():
  return itkExpImageFilterID2ID2.New()


def itkExpImageFilterIF3IF3_New():
  return itkExpImageFilterIF3IF3.New()


def itkExpImageFilterIF2IF2_New():
  return itkExpImageFilterIF2IF2.New()


def itkExpImageFilterIUS3IUS3_New():
  return itkExpImageFilterIUS3IUS3.New()


def itkExpImageFilterIUS2IUS2_New():
  return itkExpImageFilterIUS2IUS2.New()


def itkExpImageFilterIUC3IUC3_New():
  return itkExpImageFilterIUC3IUC3.New()


def itkExpImageFilterIUC2IUC2_New():
  return itkExpImageFilterIUC2IUC2.New()


def itkExpImageFilterISS3ISS3_New():
  return itkExpImageFilterISS3ISS3.New()


def itkExpImageFilterISS2ISS2_New():
  return itkExpImageFilterISS2ISS2.New()

class itkExpImageFilterID2ID2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID2ID2):
    r"""Proxy of C++ itkExpImageFilterID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkExpImageFilterPython.itkExpImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkExpImageFilterPython.itkExpImageFilterID2ID2_Clone)
    InputConvertibleToDoubleCheck = _itkExpImageFilterPython.itkExpImageFilterID2ID2_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkExpImageFilterPython.itkExpImageFilterID2ID2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkExpImageFilterPython.delete_itkExpImageFilterID2ID2
    cast = _swig_new_static_method(_itkExpImageFilterPython.itkExpImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkExpImageFilterID2ID2

        Create a new object of the class itkExpImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExpImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkExpImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkExpImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkExpImageFilterID2ID2 in _itkExpImageFilterPython:
_itkExpImageFilterPython.itkExpImageFilterID2ID2_swigregister(itkExpImageFilterID2ID2)
itkExpImageFilterID2ID2___New_orig__ = _itkExpImageFilterPython.itkExpImageFilterID2ID2___New_orig__
itkExpImageFilterID2ID2_cast = _itkExpImageFilterPython.itkExpImageFilterID2ID2_cast

class itkExpImageFilterID3ID3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID3ID3):
    r"""Proxy of C++ itkExpImageFilterID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkExpImageFilterPython.itkExpImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkExpImageFilterPython.itkExpImageFilterID3ID3_Clone)
    InputConvertibleToDoubleCheck = _itkExpImageFilterPython.itkExpImageFilterID3ID3_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkExpImageFilterPython.itkExpImageFilterID3ID3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkExpImageFilterPython.delete_itkExpImageFilterID3ID3
    cast = _swig_new_static_method(_itkExpImageFilterPython.itkExpImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkExpImageFilterID3ID3

        Create a new object of the class itkExpImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExpImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkExpImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkExpImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkExpImageFilterID3ID3 in _itkExpImageFilterPython:
_itkExpImageFilterPython.itkExpImageFilterID3ID3_swigregister(itkExpImageFilterID3ID3)
itkExpImageFilterID3ID3___New_orig__ = _itkExpImageFilterPython.itkExpImageFilterID3ID3___New_orig__
itkExpImageFilterID3ID3_cast = _itkExpImageFilterPython.itkExpImageFilterID3ID3_cast

class itkExpImageFilterIF2IF2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF2IF2):
    r"""Proxy of C++ itkExpImageFilterIF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkExpImageFilterPython.itkExpImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkExpImageFilterPython.itkExpImageFilterIF2IF2_Clone)
    InputConvertibleToDoubleCheck = _itkExpImageFilterPython.itkExpImageFilterIF2IF2_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkExpImageFilterPython.itkExpImageFilterIF2IF2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkExpImageFilterPython.delete_itkExpImageFilterIF2IF2
    cast = _swig_new_static_method(_itkExpImageFilterPython.itkExpImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkExpImageFilterIF2IF2

        Create a new object of the class itkExpImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExpImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkExpImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkExpImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkExpImageFilterIF2IF2 in _itkExpImageFilterPython:
_itkExpImageFilterPython.itkExpImageFilterIF2IF2_swigregister(itkExpImageFilterIF2IF2)
itkExpImageFilterIF2IF2___New_orig__ = _itkExpImageFilterPython.itkExpImageFilterIF2IF2___New_orig__
itkExpImageFilterIF2IF2_cast = _itkExpImageFilterPython.itkExpImageFilterIF2IF2_cast

class itkExpImageFilterIF3IF3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF3IF3):
    r"""Proxy of C++ itkExpImageFilterIF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkExpImageFilterPython.itkExpImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkExpImageFilterPython.itkExpImageFilterIF3IF3_Clone)
    InputConvertibleToDoubleCheck = _itkExpImageFilterPython.itkExpImageFilterIF3IF3_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkExpImageFilterPython.itkExpImageFilterIF3IF3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkExpImageFilterPython.delete_itkExpImageFilterIF3IF3
    cast = _swig_new_static_method(_itkExpImageFilterPython.itkExpImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkExpImageFilterIF3IF3

        Create a new object of the class itkExpImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExpImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkExpImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkExpImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkExpImageFilterIF3IF3 in _itkExpImageFilterPython:
_itkExpImageFilterPython.itkExpImageFilterIF3IF3_swigregister(itkExpImageFilterIF3IF3)
itkExpImageFilterIF3IF3___New_orig__ = _itkExpImageFilterPython.itkExpImageFilterIF3IF3___New_orig__
itkExpImageFilterIF3IF3_cast = _itkExpImageFilterPython.itkExpImageFilterIF3IF3_cast

class itkExpImageFilterISS2ISS2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterISS2ISS2):
    r"""Proxy of C++ itkExpImageFilterISS2ISS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkExpImageFilterPython.itkExpImageFilterISS2ISS2___New_orig__)
    Clone = _swig_new_instance_method(_itkExpImageFilterPython.itkExpImageFilterISS2ISS2_Clone)
    InputConvertibleToDoubleCheck = _itkExpImageFilterPython.itkExpImageFilterISS2ISS2_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkExpImageFilterPython.itkExpImageFilterISS2ISS2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkExpImageFilterPython.delete_itkExpImageFilterISS2ISS2
    cast = _swig_new_static_method(_itkExpImageFilterPython.itkExpImageFilterISS2ISS2_cast)

    def New(*args, **kargs):
        """New() -> itkExpImageFilterISS2ISS2

        Create a new object of the class itkExpImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExpImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkExpImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkExpImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkExpImageFilterISS2ISS2 in _itkExpImageFilterPython:
_itkExpImageFilterPython.itkExpImageFilterISS2ISS2_swigregister(itkExpImageFilterISS2ISS2)
itkExpImageFilterISS2ISS2___New_orig__ = _itkExpImageFilterPython.itkExpImageFilterISS2ISS2___New_orig__
itkExpImageFilterISS2ISS2_cast = _itkExpImageFilterPython.itkExpImageFilterISS2ISS2_cast

class itkExpImageFilterISS3ISS3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterISS3ISS3):
    r"""Proxy of C++ itkExpImageFilterISS3ISS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkExpImageFilterPython.itkExpImageFilterISS3ISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkExpImageFilterPython.itkExpImageFilterISS3ISS3_Clone)
    InputConvertibleToDoubleCheck = _itkExpImageFilterPython.itkExpImageFilterISS3ISS3_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkExpImageFilterPython.itkExpImageFilterISS3ISS3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkExpImageFilterPython.delete_itkExpImageFilterISS3ISS3
    cast = _swig_new_static_method(_itkExpImageFilterPython.itkExpImageFilterISS3ISS3_cast)

    def New(*args, **kargs):
        """New() -> itkExpImageFilterISS3ISS3

        Create a new object of the class itkExpImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExpImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkExpImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkExpImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkExpImageFilterISS3ISS3 in _itkExpImageFilterPython:
_itkExpImageFilterPython.itkExpImageFilterISS3ISS3_swigregister(itkExpImageFilterISS3ISS3)
itkExpImageFilterISS3ISS3___New_orig__ = _itkExpImageFilterPython.itkExpImageFilterISS3ISS3___New_orig__
itkExpImageFilterISS3ISS3_cast = _itkExpImageFilterPython.itkExpImageFilterISS3ISS3_cast

class itkExpImageFilterIUC2IUC2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUC2IUC2):
    r"""Proxy of C++ itkExpImageFilterIUC2IUC2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkExpImageFilterPython.itkExpImageFilterIUC2IUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkExpImageFilterPython.itkExpImageFilterIUC2IUC2_Clone)
    InputConvertibleToDoubleCheck = _itkExpImageFilterPython.itkExpImageFilterIUC2IUC2_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkExpImageFilterPython.itkExpImageFilterIUC2IUC2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkExpImageFilterPython.delete_itkExpImageFilterIUC2IUC2
    cast = _swig_new_static_method(_itkExpImageFilterPython.itkExpImageFilterIUC2IUC2_cast)

    def New(*args, **kargs):
        """New() -> itkExpImageFilterIUC2IUC2

        Create a new object of the class itkExpImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExpImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkExpImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkExpImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkExpImageFilterIUC2IUC2 in _itkExpImageFilterPython:
_itkExpImageFilterPython.itkExpImageFilterIUC2IUC2_swigregister(itkExpImageFilterIUC2IUC2)
itkExpImageFilterIUC2IUC2___New_orig__ = _itkExpImageFilterPython.itkExpImageFilterIUC2IUC2___New_orig__
itkExpImageFilterIUC2IUC2_cast = _itkExpImageFilterPython.itkExpImageFilterIUC2IUC2_cast

class itkExpImageFilterIUC3IUC3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUC3IUC3):
    r"""Proxy of C++ itkExpImageFilterIUC3IUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkExpImageFilterPython.itkExpImageFilterIUC3IUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkExpImageFilterPython.itkExpImageFilterIUC3IUC3_Clone)
    InputConvertibleToDoubleCheck = _itkExpImageFilterPython.itkExpImageFilterIUC3IUC3_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkExpImageFilterPython.itkExpImageFilterIUC3IUC3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkExpImageFilterPython.delete_itkExpImageFilterIUC3IUC3
    cast = _swig_new_static_method(_itkExpImageFilterPython.itkExpImageFilterIUC3IUC3_cast)

    def New(*args, **kargs):
        """New() -> itkExpImageFilterIUC3IUC3

        Create a new object of the class itkExpImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExpImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkExpImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkExpImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkExpImageFilterIUC3IUC3 in _itkExpImageFilterPython:
_itkExpImageFilterPython.itkExpImageFilterIUC3IUC3_swigregister(itkExpImageFilterIUC3IUC3)
itkExpImageFilterIUC3IUC3___New_orig__ = _itkExpImageFilterPython.itkExpImageFilterIUC3IUC3___New_orig__
itkExpImageFilterIUC3IUC3_cast = _itkExpImageFilterPython.itkExpImageFilterIUC3IUC3_cast

class itkExpImageFilterIUS2IUS2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUS2IUS2):
    r"""Proxy of C++ itkExpImageFilterIUS2IUS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkExpImageFilterPython.itkExpImageFilterIUS2IUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkExpImageFilterPython.itkExpImageFilterIUS2IUS2_Clone)
    InputConvertibleToDoubleCheck = _itkExpImageFilterPython.itkExpImageFilterIUS2IUS2_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkExpImageFilterPython.itkExpImageFilterIUS2IUS2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkExpImageFilterPython.delete_itkExpImageFilterIUS2IUS2
    cast = _swig_new_static_method(_itkExpImageFilterPython.itkExpImageFilterIUS2IUS2_cast)

    def New(*args, **kargs):
        """New() -> itkExpImageFilterIUS2IUS2

        Create a new object of the class itkExpImageFilterIUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExpImageFilterIUS2IUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkExpImageFilterIUS2IUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkExpImageFilterIUS2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkExpImageFilterIUS2IUS2 in _itkExpImageFilterPython:
_itkExpImageFilterPython.itkExpImageFilterIUS2IUS2_swigregister(itkExpImageFilterIUS2IUS2)
itkExpImageFilterIUS2IUS2___New_orig__ = _itkExpImageFilterPython.itkExpImageFilterIUS2IUS2___New_orig__
itkExpImageFilterIUS2IUS2_cast = _itkExpImageFilterPython.itkExpImageFilterIUS2IUS2_cast

class itkExpImageFilterIUS3IUS3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUS3IUS3):
    r"""Proxy of C++ itkExpImageFilterIUS3IUS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkExpImageFilterPython.itkExpImageFilterIUS3IUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkExpImageFilterPython.itkExpImageFilterIUS3IUS3_Clone)
    InputConvertibleToDoubleCheck = _itkExpImageFilterPython.itkExpImageFilterIUS3IUS3_InputConvertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkExpImageFilterPython.itkExpImageFilterIUS3IUS3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkExpImageFilterPython.delete_itkExpImageFilterIUS3IUS3
    cast = _swig_new_static_method(_itkExpImageFilterPython.itkExpImageFilterIUS3IUS3_cast)

    def New(*args, **kargs):
        """New() -> itkExpImageFilterIUS3IUS3

        Create a new object of the class itkExpImageFilterIUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkExpImageFilterIUS3IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkExpImageFilterIUS3IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkExpImageFilterIUS3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkExpImageFilterIUS3IUS3 in _itkExpImageFilterPython:
_itkExpImageFilterPython.itkExpImageFilterIUS3IUS3_swigregister(itkExpImageFilterIUS3IUS3)
itkExpImageFilterIUS3IUS3___New_orig__ = _itkExpImageFilterPython.itkExpImageFilterIUS3IUS3___New_orig__
itkExpImageFilterIUS3IUS3_cast = _itkExpImageFilterPython.itkExpImageFilterIUS3IUS3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def exp_image_filter(*args, **kwargs):
    """Procedural interface for ExpImageFilter"""
    import itk
    instance = itk.ExpImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def exp_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.ExpImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.ExpImageFilter.values()[0]
    else:
        filter_object = itk.ExpImageFilter

    exp_image_filter.__doc__ = filter_object.__doc__
    exp_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    exp_image_filter.__doc__ += "Available Keyword Arguments:\n"
    exp_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



