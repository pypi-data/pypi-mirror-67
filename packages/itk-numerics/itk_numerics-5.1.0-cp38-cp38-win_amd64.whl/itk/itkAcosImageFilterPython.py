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
    from . import _itkAcosImageFilterPython
else:
    import _itkAcosImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkAcosImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkAcosImageFilterPython.SWIG_PyStaticMethod_New

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

def itkAcosImageFilterID3ID3_New():
  return itkAcosImageFilterID3ID3.New()


def itkAcosImageFilterID2ID2_New():
  return itkAcosImageFilterID2ID2.New()


def itkAcosImageFilterIF3IF3_New():
  return itkAcosImageFilterIF3IF3.New()


def itkAcosImageFilterIF2IF2_New():
  return itkAcosImageFilterIF2IF2.New()


def itkAcosImageFilterIUS3IUS3_New():
  return itkAcosImageFilterIUS3IUS3.New()


def itkAcosImageFilterIUS2IUS2_New():
  return itkAcosImageFilterIUS2IUS2.New()


def itkAcosImageFilterIUC3IUC3_New():
  return itkAcosImageFilterIUC3IUC3.New()


def itkAcosImageFilterIUC2IUC2_New():
  return itkAcosImageFilterIUC2IUC2.New()


def itkAcosImageFilterISS3ISS3_New():
  return itkAcosImageFilterISS3ISS3.New()


def itkAcosImageFilterISS2ISS2_New():
  return itkAcosImageFilterISS2ISS2.New()

class itkAcosImageFilterID2ID2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID2ID2):
    r"""Proxy of C++ itkAcosImageFilterID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAcosImageFilterPython.itkAcosImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkAcosImageFilterPython.itkAcosImageFilterID2ID2_Clone)
    InputCovertibleToDoubleCheck = _itkAcosImageFilterPython.itkAcosImageFilterID2ID2_InputCovertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkAcosImageFilterPython.itkAcosImageFilterID2ID2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkAcosImageFilterPython.delete_itkAcosImageFilterID2ID2
    cast = _swig_new_static_method(_itkAcosImageFilterPython.itkAcosImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkAcosImageFilterID2ID2

        Create a new object of the class itkAcosImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAcosImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAcosImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAcosImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAcosImageFilterID2ID2 in _itkAcosImageFilterPython:
_itkAcosImageFilterPython.itkAcosImageFilterID2ID2_swigregister(itkAcosImageFilterID2ID2)
itkAcosImageFilterID2ID2___New_orig__ = _itkAcosImageFilterPython.itkAcosImageFilterID2ID2___New_orig__
itkAcosImageFilterID2ID2_cast = _itkAcosImageFilterPython.itkAcosImageFilterID2ID2_cast

class itkAcosImageFilterID3ID3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID3ID3):
    r"""Proxy of C++ itkAcosImageFilterID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAcosImageFilterPython.itkAcosImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkAcosImageFilterPython.itkAcosImageFilterID3ID3_Clone)
    InputCovertibleToDoubleCheck = _itkAcosImageFilterPython.itkAcosImageFilterID3ID3_InputCovertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkAcosImageFilterPython.itkAcosImageFilterID3ID3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkAcosImageFilterPython.delete_itkAcosImageFilterID3ID3
    cast = _swig_new_static_method(_itkAcosImageFilterPython.itkAcosImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkAcosImageFilterID3ID3

        Create a new object of the class itkAcosImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAcosImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAcosImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAcosImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAcosImageFilterID3ID3 in _itkAcosImageFilterPython:
_itkAcosImageFilterPython.itkAcosImageFilterID3ID3_swigregister(itkAcosImageFilterID3ID3)
itkAcosImageFilterID3ID3___New_orig__ = _itkAcosImageFilterPython.itkAcosImageFilterID3ID3___New_orig__
itkAcosImageFilterID3ID3_cast = _itkAcosImageFilterPython.itkAcosImageFilterID3ID3_cast

class itkAcosImageFilterIF2IF2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF2IF2):
    r"""Proxy of C++ itkAcosImageFilterIF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAcosImageFilterPython.itkAcosImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkAcosImageFilterPython.itkAcosImageFilterIF2IF2_Clone)
    InputCovertibleToDoubleCheck = _itkAcosImageFilterPython.itkAcosImageFilterIF2IF2_InputCovertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkAcosImageFilterPython.itkAcosImageFilterIF2IF2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkAcosImageFilterPython.delete_itkAcosImageFilterIF2IF2
    cast = _swig_new_static_method(_itkAcosImageFilterPython.itkAcosImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkAcosImageFilterIF2IF2

        Create a new object of the class itkAcosImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAcosImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAcosImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAcosImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAcosImageFilterIF2IF2 in _itkAcosImageFilterPython:
_itkAcosImageFilterPython.itkAcosImageFilterIF2IF2_swigregister(itkAcosImageFilterIF2IF2)
itkAcosImageFilterIF2IF2___New_orig__ = _itkAcosImageFilterPython.itkAcosImageFilterIF2IF2___New_orig__
itkAcosImageFilterIF2IF2_cast = _itkAcosImageFilterPython.itkAcosImageFilterIF2IF2_cast

class itkAcosImageFilterIF3IF3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF3IF3):
    r"""Proxy of C++ itkAcosImageFilterIF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAcosImageFilterPython.itkAcosImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkAcosImageFilterPython.itkAcosImageFilterIF3IF3_Clone)
    InputCovertibleToDoubleCheck = _itkAcosImageFilterPython.itkAcosImageFilterIF3IF3_InputCovertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkAcosImageFilterPython.itkAcosImageFilterIF3IF3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkAcosImageFilterPython.delete_itkAcosImageFilterIF3IF3
    cast = _swig_new_static_method(_itkAcosImageFilterPython.itkAcosImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkAcosImageFilterIF3IF3

        Create a new object of the class itkAcosImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAcosImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAcosImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAcosImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAcosImageFilterIF3IF3 in _itkAcosImageFilterPython:
_itkAcosImageFilterPython.itkAcosImageFilterIF3IF3_swigregister(itkAcosImageFilterIF3IF3)
itkAcosImageFilterIF3IF3___New_orig__ = _itkAcosImageFilterPython.itkAcosImageFilterIF3IF3___New_orig__
itkAcosImageFilterIF3IF3_cast = _itkAcosImageFilterPython.itkAcosImageFilterIF3IF3_cast

class itkAcosImageFilterISS2ISS2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterISS2ISS2):
    r"""Proxy of C++ itkAcosImageFilterISS2ISS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAcosImageFilterPython.itkAcosImageFilterISS2ISS2___New_orig__)
    Clone = _swig_new_instance_method(_itkAcosImageFilterPython.itkAcosImageFilterISS2ISS2_Clone)
    InputCovertibleToDoubleCheck = _itkAcosImageFilterPython.itkAcosImageFilterISS2ISS2_InputCovertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkAcosImageFilterPython.itkAcosImageFilterISS2ISS2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkAcosImageFilterPython.delete_itkAcosImageFilterISS2ISS2
    cast = _swig_new_static_method(_itkAcosImageFilterPython.itkAcosImageFilterISS2ISS2_cast)

    def New(*args, **kargs):
        """New() -> itkAcosImageFilterISS2ISS2

        Create a new object of the class itkAcosImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAcosImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAcosImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAcosImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAcosImageFilterISS2ISS2 in _itkAcosImageFilterPython:
_itkAcosImageFilterPython.itkAcosImageFilterISS2ISS2_swigregister(itkAcosImageFilterISS2ISS2)
itkAcosImageFilterISS2ISS2___New_orig__ = _itkAcosImageFilterPython.itkAcosImageFilterISS2ISS2___New_orig__
itkAcosImageFilterISS2ISS2_cast = _itkAcosImageFilterPython.itkAcosImageFilterISS2ISS2_cast

class itkAcosImageFilterISS3ISS3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterISS3ISS3):
    r"""Proxy of C++ itkAcosImageFilterISS3ISS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAcosImageFilterPython.itkAcosImageFilterISS3ISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkAcosImageFilterPython.itkAcosImageFilterISS3ISS3_Clone)
    InputCovertibleToDoubleCheck = _itkAcosImageFilterPython.itkAcosImageFilterISS3ISS3_InputCovertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkAcosImageFilterPython.itkAcosImageFilterISS3ISS3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkAcosImageFilterPython.delete_itkAcosImageFilterISS3ISS3
    cast = _swig_new_static_method(_itkAcosImageFilterPython.itkAcosImageFilterISS3ISS3_cast)

    def New(*args, **kargs):
        """New() -> itkAcosImageFilterISS3ISS3

        Create a new object of the class itkAcosImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAcosImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAcosImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAcosImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAcosImageFilterISS3ISS3 in _itkAcosImageFilterPython:
_itkAcosImageFilterPython.itkAcosImageFilterISS3ISS3_swigregister(itkAcosImageFilterISS3ISS3)
itkAcosImageFilterISS3ISS3___New_orig__ = _itkAcosImageFilterPython.itkAcosImageFilterISS3ISS3___New_orig__
itkAcosImageFilterISS3ISS3_cast = _itkAcosImageFilterPython.itkAcosImageFilterISS3ISS3_cast

class itkAcosImageFilterIUC2IUC2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUC2IUC2):
    r"""Proxy of C++ itkAcosImageFilterIUC2IUC2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAcosImageFilterPython.itkAcosImageFilterIUC2IUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkAcosImageFilterPython.itkAcosImageFilterIUC2IUC2_Clone)
    InputCovertibleToDoubleCheck = _itkAcosImageFilterPython.itkAcosImageFilterIUC2IUC2_InputCovertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkAcosImageFilterPython.itkAcosImageFilterIUC2IUC2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkAcosImageFilterPython.delete_itkAcosImageFilterIUC2IUC2
    cast = _swig_new_static_method(_itkAcosImageFilterPython.itkAcosImageFilterIUC2IUC2_cast)

    def New(*args, **kargs):
        """New() -> itkAcosImageFilterIUC2IUC2

        Create a new object of the class itkAcosImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAcosImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAcosImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAcosImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAcosImageFilterIUC2IUC2 in _itkAcosImageFilterPython:
_itkAcosImageFilterPython.itkAcosImageFilterIUC2IUC2_swigregister(itkAcosImageFilterIUC2IUC2)
itkAcosImageFilterIUC2IUC2___New_orig__ = _itkAcosImageFilterPython.itkAcosImageFilterIUC2IUC2___New_orig__
itkAcosImageFilterIUC2IUC2_cast = _itkAcosImageFilterPython.itkAcosImageFilterIUC2IUC2_cast

class itkAcosImageFilterIUC3IUC3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUC3IUC3):
    r"""Proxy of C++ itkAcosImageFilterIUC3IUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAcosImageFilterPython.itkAcosImageFilterIUC3IUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkAcosImageFilterPython.itkAcosImageFilterIUC3IUC3_Clone)
    InputCovertibleToDoubleCheck = _itkAcosImageFilterPython.itkAcosImageFilterIUC3IUC3_InputCovertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkAcosImageFilterPython.itkAcosImageFilterIUC3IUC3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkAcosImageFilterPython.delete_itkAcosImageFilterIUC3IUC3
    cast = _swig_new_static_method(_itkAcosImageFilterPython.itkAcosImageFilterIUC3IUC3_cast)

    def New(*args, **kargs):
        """New() -> itkAcosImageFilterIUC3IUC3

        Create a new object of the class itkAcosImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAcosImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAcosImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAcosImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAcosImageFilterIUC3IUC3 in _itkAcosImageFilterPython:
_itkAcosImageFilterPython.itkAcosImageFilterIUC3IUC3_swigregister(itkAcosImageFilterIUC3IUC3)
itkAcosImageFilterIUC3IUC3___New_orig__ = _itkAcosImageFilterPython.itkAcosImageFilterIUC3IUC3___New_orig__
itkAcosImageFilterIUC3IUC3_cast = _itkAcosImageFilterPython.itkAcosImageFilterIUC3IUC3_cast

class itkAcosImageFilterIUS2IUS2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUS2IUS2):
    r"""Proxy of C++ itkAcosImageFilterIUS2IUS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAcosImageFilterPython.itkAcosImageFilterIUS2IUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkAcosImageFilterPython.itkAcosImageFilterIUS2IUS2_Clone)
    InputCovertibleToDoubleCheck = _itkAcosImageFilterPython.itkAcosImageFilterIUS2IUS2_InputCovertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkAcosImageFilterPython.itkAcosImageFilterIUS2IUS2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkAcosImageFilterPython.delete_itkAcosImageFilterIUS2IUS2
    cast = _swig_new_static_method(_itkAcosImageFilterPython.itkAcosImageFilterIUS2IUS2_cast)

    def New(*args, **kargs):
        """New() -> itkAcosImageFilterIUS2IUS2

        Create a new object of the class itkAcosImageFilterIUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAcosImageFilterIUS2IUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAcosImageFilterIUS2IUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAcosImageFilterIUS2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAcosImageFilterIUS2IUS2 in _itkAcosImageFilterPython:
_itkAcosImageFilterPython.itkAcosImageFilterIUS2IUS2_swigregister(itkAcosImageFilterIUS2IUS2)
itkAcosImageFilterIUS2IUS2___New_orig__ = _itkAcosImageFilterPython.itkAcosImageFilterIUS2IUS2___New_orig__
itkAcosImageFilterIUS2IUS2_cast = _itkAcosImageFilterPython.itkAcosImageFilterIUS2IUS2_cast

class itkAcosImageFilterIUS3IUS3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUS3IUS3):
    r"""Proxy of C++ itkAcosImageFilterIUS3IUS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAcosImageFilterPython.itkAcosImageFilterIUS3IUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkAcosImageFilterPython.itkAcosImageFilterIUS3IUS3_Clone)
    InputCovertibleToDoubleCheck = _itkAcosImageFilterPython.itkAcosImageFilterIUS3IUS3_InputCovertibleToDoubleCheck
    
    DoubleConvertibleToOutputCheck = _itkAcosImageFilterPython.itkAcosImageFilterIUS3IUS3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkAcosImageFilterPython.delete_itkAcosImageFilterIUS3IUS3
    cast = _swig_new_static_method(_itkAcosImageFilterPython.itkAcosImageFilterIUS3IUS3_cast)

    def New(*args, **kargs):
        """New() -> itkAcosImageFilterIUS3IUS3

        Create a new object of the class itkAcosImageFilterIUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAcosImageFilterIUS3IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAcosImageFilterIUS3IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAcosImageFilterIUS3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAcosImageFilterIUS3IUS3 in _itkAcosImageFilterPython:
_itkAcosImageFilterPython.itkAcosImageFilterIUS3IUS3_swigregister(itkAcosImageFilterIUS3IUS3)
itkAcosImageFilterIUS3IUS3___New_orig__ = _itkAcosImageFilterPython.itkAcosImageFilterIUS3IUS3___New_orig__
itkAcosImageFilterIUS3IUS3_cast = _itkAcosImageFilterPython.itkAcosImageFilterIUS3IUS3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def acos_image_filter(*args, **kwargs):
    """Procedural interface for AcosImageFilter"""
    import itk
    instance = itk.AcosImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def acos_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.AcosImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.AcosImageFilter.values()[0]
    else:
        filter_object = itk.AcosImageFilter

    acos_image_filter.__doc__ = filter_object.__doc__
    acos_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    acos_image_filter.__doc__ += "Available Keyword Arguments:\n"
    acos_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



