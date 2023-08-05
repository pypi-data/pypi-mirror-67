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
    from . import _itkAbsImageFilterPython
else:
    import _itkAbsImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkAbsImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkAbsImageFilterPython.SWIG_PyStaticMethod_New

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

def itkAbsImageFilterID3ID3_New():
  return itkAbsImageFilterID3ID3.New()


def itkAbsImageFilterID2ID2_New():
  return itkAbsImageFilterID2ID2.New()


def itkAbsImageFilterIF3IF3_New():
  return itkAbsImageFilterIF3IF3.New()


def itkAbsImageFilterIF2IF2_New():
  return itkAbsImageFilterIF2IF2.New()


def itkAbsImageFilterIUS3IUS3_New():
  return itkAbsImageFilterIUS3IUS3.New()


def itkAbsImageFilterIUS2IUS2_New():
  return itkAbsImageFilterIUS2IUS2.New()


def itkAbsImageFilterIUC3IUC3_New():
  return itkAbsImageFilterIUC3IUC3.New()


def itkAbsImageFilterIUC2IUC2_New():
  return itkAbsImageFilterIUC2IUC2.New()


def itkAbsImageFilterISS3ISS3_New():
  return itkAbsImageFilterISS3ISS3.New()


def itkAbsImageFilterISS2ISS2_New():
  return itkAbsImageFilterISS2ISS2.New()

class itkAbsImageFilterID2ID2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID2ID2):
    r"""Proxy of C++ itkAbsImageFilterID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAbsImageFilterPython.itkAbsImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkAbsImageFilterPython.itkAbsImageFilterID2ID2_Clone)
    ConvertibleCheck = _itkAbsImageFilterPython.itkAbsImageFilterID2ID2_ConvertibleCheck
    
    InputGreaterThanIntCheck = _itkAbsImageFilterPython.itkAbsImageFilterID2ID2_InputGreaterThanIntCheck
    
    __swig_destroy__ = _itkAbsImageFilterPython.delete_itkAbsImageFilterID2ID2
    cast = _swig_new_static_method(_itkAbsImageFilterPython.itkAbsImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkAbsImageFilterID2ID2

        Create a new object of the class itkAbsImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAbsImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAbsImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAbsImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAbsImageFilterID2ID2 in _itkAbsImageFilterPython:
_itkAbsImageFilterPython.itkAbsImageFilterID2ID2_swigregister(itkAbsImageFilterID2ID2)
itkAbsImageFilterID2ID2___New_orig__ = _itkAbsImageFilterPython.itkAbsImageFilterID2ID2___New_orig__
itkAbsImageFilterID2ID2_cast = _itkAbsImageFilterPython.itkAbsImageFilterID2ID2_cast

class itkAbsImageFilterID3ID3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID3ID3):
    r"""Proxy of C++ itkAbsImageFilterID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAbsImageFilterPython.itkAbsImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkAbsImageFilterPython.itkAbsImageFilterID3ID3_Clone)
    ConvertibleCheck = _itkAbsImageFilterPython.itkAbsImageFilterID3ID3_ConvertibleCheck
    
    InputGreaterThanIntCheck = _itkAbsImageFilterPython.itkAbsImageFilterID3ID3_InputGreaterThanIntCheck
    
    __swig_destroy__ = _itkAbsImageFilterPython.delete_itkAbsImageFilterID3ID3
    cast = _swig_new_static_method(_itkAbsImageFilterPython.itkAbsImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkAbsImageFilterID3ID3

        Create a new object of the class itkAbsImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAbsImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAbsImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAbsImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAbsImageFilterID3ID3 in _itkAbsImageFilterPython:
_itkAbsImageFilterPython.itkAbsImageFilterID3ID3_swigregister(itkAbsImageFilterID3ID3)
itkAbsImageFilterID3ID3___New_orig__ = _itkAbsImageFilterPython.itkAbsImageFilterID3ID3___New_orig__
itkAbsImageFilterID3ID3_cast = _itkAbsImageFilterPython.itkAbsImageFilterID3ID3_cast

class itkAbsImageFilterIF2IF2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF2IF2):
    r"""Proxy of C++ itkAbsImageFilterIF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAbsImageFilterPython.itkAbsImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkAbsImageFilterPython.itkAbsImageFilterIF2IF2_Clone)
    ConvertibleCheck = _itkAbsImageFilterPython.itkAbsImageFilterIF2IF2_ConvertibleCheck
    
    InputGreaterThanIntCheck = _itkAbsImageFilterPython.itkAbsImageFilterIF2IF2_InputGreaterThanIntCheck
    
    __swig_destroy__ = _itkAbsImageFilterPython.delete_itkAbsImageFilterIF2IF2
    cast = _swig_new_static_method(_itkAbsImageFilterPython.itkAbsImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkAbsImageFilterIF2IF2

        Create a new object of the class itkAbsImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAbsImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAbsImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAbsImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAbsImageFilterIF2IF2 in _itkAbsImageFilterPython:
_itkAbsImageFilterPython.itkAbsImageFilterIF2IF2_swigregister(itkAbsImageFilterIF2IF2)
itkAbsImageFilterIF2IF2___New_orig__ = _itkAbsImageFilterPython.itkAbsImageFilterIF2IF2___New_orig__
itkAbsImageFilterIF2IF2_cast = _itkAbsImageFilterPython.itkAbsImageFilterIF2IF2_cast

class itkAbsImageFilterIF3IF3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF3IF3):
    r"""Proxy of C++ itkAbsImageFilterIF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAbsImageFilterPython.itkAbsImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkAbsImageFilterPython.itkAbsImageFilterIF3IF3_Clone)
    ConvertibleCheck = _itkAbsImageFilterPython.itkAbsImageFilterIF3IF3_ConvertibleCheck
    
    InputGreaterThanIntCheck = _itkAbsImageFilterPython.itkAbsImageFilterIF3IF3_InputGreaterThanIntCheck
    
    __swig_destroy__ = _itkAbsImageFilterPython.delete_itkAbsImageFilterIF3IF3
    cast = _swig_new_static_method(_itkAbsImageFilterPython.itkAbsImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkAbsImageFilterIF3IF3

        Create a new object of the class itkAbsImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAbsImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAbsImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAbsImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAbsImageFilterIF3IF3 in _itkAbsImageFilterPython:
_itkAbsImageFilterPython.itkAbsImageFilterIF3IF3_swigregister(itkAbsImageFilterIF3IF3)
itkAbsImageFilterIF3IF3___New_orig__ = _itkAbsImageFilterPython.itkAbsImageFilterIF3IF3___New_orig__
itkAbsImageFilterIF3IF3_cast = _itkAbsImageFilterPython.itkAbsImageFilterIF3IF3_cast

class itkAbsImageFilterISS2ISS2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterISS2ISS2):
    r"""Proxy of C++ itkAbsImageFilterISS2ISS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAbsImageFilterPython.itkAbsImageFilterISS2ISS2___New_orig__)
    Clone = _swig_new_instance_method(_itkAbsImageFilterPython.itkAbsImageFilterISS2ISS2_Clone)
    ConvertibleCheck = _itkAbsImageFilterPython.itkAbsImageFilterISS2ISS2_ConvertibleCheck
    
    InputGreaterThanIntCheck = _itkAbsImageFilterPython.itkAbsImageFilterISS2ISS2_InputGreaterThanIntCheck
    
    __swig_destroy__ = _itkAbsImageFilterPython.delete_itkAbsImageFilterISS2ISS2
    cast = _swig_new_static_method(_itkAbsImageFilterPython.itkAbsImageFilterISS2ISS2_cast)

    def New(*args, **kargs):
        """New() -> itkAbsImageFilterISS2ISS2

        Create a new object of the class itkAbsImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAbsImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAbsImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAbsImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAbsImageFilterISS2ISS2 in _itkAbsImageFilterPython:
_itkAbsImageFilterPython.itkAbsImageFilterISS2ISS2_swigregister(itkAbsImageFilterISS2ISS2)
itkAbsImageFilterISS2ISS2___New_orig__ = _itkAbsImageFilterPython.itkAbsImageFilterISS2ISS2___New_orig__
itkAbsImageFilterISS2ISS2_cast = _itkAbsImageFilterPython.itkAbsImageFilterISS2ISS2_cast

class itkAbsImageFilterISS3ISS3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterISS3ISS3):
    r"""Proxy of C++ itkAbsImageFilterISS3ISS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAbsImageFilterPython.itkAbsImageFilterISS3ISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkAbsImageFilterPython.itkAbsImageFilterISS3ISS3_Clone)
    ConvertibleCheck = _itkAbsImageFilterPython.itkAbsImageFilterISS3ISS3_ConvertibleCheck
    
    InputGreaterThanIntCheck = _itkAbsImageFilterPython.itkAbsImageFilterISS3ISS3_InputGreaterThanIntCheck
    
    __swig_destroy__ = _itkAbsImageFilterPython.delete_itkAbsImageFilterISS3ISS3
    cast = _swig_new_static_method(_itkAbsImageFilterPython.itkAbsImageFilterISS3ISS3_cast)

    def New(*args, **kargs):
        """New() -> itkAbsImageFilterISS3ISS3

        Create a new object of the class itkAbsImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAbsImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAbsImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAbsImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAbsImageFilterISS3ISS3 in _itkAbsImageFilterPython:
_itkAbsImageFilterPython.itkAbsImageFilterISS3ISS3_swigregister(itkAbsImageFilterISS3ISS3)
itkAbsImageFilterISS3ISS3___New_orig__ = _itkAbsImageFilterPython.itkAbsImageFilterISS3ISS3___New_orig__
itkAbsImageFilterISS3ISS3_cast = _itkAbsImageFilterPython.itkAbsImageFilterISS3ISS3_cast

class itkAbsImageFilterIUC2IUC2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUC2IUC2):
    r"""Proxy of C++ itkAbsImageFilterIUC2IUC2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAbsImageFilterPython.itkAbsImageFilterIUC2IUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkAbsImageFilterPython.itkAbsImageFilterIUC2IUC2_Clone)
    ConvertibleCheck = _itkAbsImageFilterPython.itkAbsImageFilterIUC2IUC2_ConvertibleCheck
    
    InputGreaterThanIntCheck = _itkAbsImageFilterPython.itkAbsImageFilterIUC2IUC2_InputGreaterThanIntCheck
    
    __swig_destroy__ = _itkAbsImageFilterPython.delete_itkAbsImageFilterIUC2IUC2
    cast = _swig_new_static_method(_itkAbsImageFilterPython.itkAbsImageFilterIUC2IUC2_cast)

    def New(*args, **kargs):
        """New() -> itkAbsImageFilterIUC2IUC2

        Create a new object of the class itkAbsImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAbsImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAbsImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAbsImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAbsImageFilterIUC2IUC2 in _itkAbsImageFilterPython:
_itkAbsImageFilterPython.itkAbsImageFilterIUC2IUC2_swigregister(itkAbsImageFilterIUC2IUC2)
itkAbsImageFilterIUC2IUC2___New_orig__ = _itkAbsImageFilterPython.itkAbsImageFilterIUC2IUC2___New_orig__
itkAbsImageFilterIUC2IUC2_cast = _itkAbsImageFilterPython.itkAbsImageFilterIUC2IUC2_cast

class itkAbsImageFilterIUC3IUC3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUC3IUC3):
    r"""Proxy of C++ itkAbsImageFilterIUC3IUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAbsImageFilterPython.itkAbsImageFilterIUC3IUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkAbsImageFilterPython.itkAbsImageFilterIUC3IUC3_Clone)
    ConvertibleCheck = _itkAbsImageFilterPython.itkAbsImageFilterIUC3IUC3_ConvertibleCheck
    
    InputGreaterThanIntCheck = _itkAbsImageFilterPython.itkAbsImageFilterIUC3IUC3_InputGreaterThanIntCheck
    
    __swig_destroy__ = _itkAbsImageFilterPython.delete_itkAbsImageFilterIUC3IUC3
    cast = _swig_new_static_method(_itkAbsImageFilterPython.itkAbsImageFilterIUC3IUC3_cast)

    def New(*args, **kargs):
        """New() -> itkAbsImageFilterIUC3IUC3

        Create a new object of the class itkAbsImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAbsImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAbsImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAbsImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAbsImageFilterIUC3IUC3 in _itkAbsImageFilterPython:
_itkAbsImageFilterPython.itkAbsImageFilterIUC3IUC3_swigregister(itkAbsImageFilterIUC3IUC3)
itkAbsImageFilterIUC3IUC3___New_orig__ = _itkAbsImageFilterPython.itkAbsImageFilterIUC3IUC3___New_orig__
itkAbsImageFilterIUC3IUC3_cast = _itkAbsImageFilterPython.itkAbsImageFilterIUC3IUC3_cast

class itkAbsImageFilterIUS2IUS2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUS2IUS2):
    r"""Proxy of C++ itkAbsImageFilterIUS2IUS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAbsImageFilterPython.itkAbsImageFilterIUS2IUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkAbsImageFilterPython.itkAbsImageFilterIUS2IUS2_Clone)
    ConvertibleCheck = _itkAbsImageFilterPython.itkAbsImageFilterIUS2IUS2_ConvertibleCheck
    
    InputGreaterThanIntCheck = _itkAbsImageFilterPython.itkAbsImageFilterIUS2IUS2_InputGreaterThanIntCheck
    
    __swig_destroy__ = _itkAbsImageFilterPython.delete_itkAbsImageFilterIUS2IUS2
    cast = _swig_new_static_method(_itkAbsImageFilterPython.itkAbsImageFilterIUS2IUS2_cast)

    def New(*args, **kargs):
        """New() -> itkAbsImageFilterIUS2IUS2

        Create a new object of the class itkAbsImageFilterIUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAbsImageFilterIUS2IUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAbsImageFilterIUS2IUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAbsImageFilterIUS2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAbsImageFilterIUS2IUS2 in _itkAbsImageFilterPython:
_itkAbsImageFilterPython.itkAbsImageFilterIUS2IUS2_swigregister(itkAbsImageFilterIUS2IUS2)
itkAbsImageFilterIUS2IUS2___New_orig__ = _itkAbsImageFilterPython.itkAbsImageFilterIUS2IUS2___New_orig__
itkAbsImageFilterIUS2IUS2_cast = _itkAbsImageFilterPython.itkAbsImageFilterIUS2IUS2_cast

class itkAbsImageFilterIUS3IUS3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUS3IUS3):
    r"""Proxy of C++ itkAbsImageFilterIUS3IUS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAbsImageFilterPython.itkAbsImageFilterIUS3IUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkAbsImageFilterPython.itkAbsImageFilterIUS3IUS3_Clone)
    ConvertibleCheck = _itkAbsImageFilterPython.itkAbsImageFilterIUS3IUS3_ConvertibleCheck
    
    InputGreaterThanIntCheck = _itkAbsImageFilterPython.itkAbsImageFilterIUS3IUS3_InputGreaterThanIntCheck
    
    __swig_destroy__ = _itkAbsImageFilterPython.delete_itkAbsImageFilterIUS3IUS3
    cast = _swig_new_static_method(_itkAbsImageFilterPython.itkAbsImageFilterIUS3IUS3_cast)

    def New(*args, **kargs):
        """New() -> itkAbsImageFilterIUS3IUS3

        Create a new object of the class itkAbsImageFilterIUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAbsImageFilterIUS3IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAbsImageFilterIUS3IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAbsImageFilterIUS3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAbsImageFilterIUS3IUS3 in _itkAbsImageFilterPython:
_itkAbsImageFilterPython.itkAbsImageFilterIUS3IUS3_swigregister(itkAbsImageFilterIUS3IUS3)
itkAbsImageFilterIUS3IUS3___New_orig__ = _itkAbsImageFilterPython.itkAbsImageFilterIUS3IUS3___New_orig__
itkAbsImageFilterIUS3IUS3_cast = _itkAbsImageFilterPython.itkAbsImageFilterIUS3IUS3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def abs_image_filter(*args, **kwargs):
    """Procedural interface for AbsImageFilter"""
    import itk
    instance = itk.AbsImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def abs_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.AbsImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.AbsImageFilter.values()[0]
    else:
        filter_object = itk.AbsImageFilter

    abs_image_filter.__doc__ = filter_object.__doc__
    abs_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    abs_image_filter.__doc__ += "Available Keyword Arguments:\n"
    abs_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



