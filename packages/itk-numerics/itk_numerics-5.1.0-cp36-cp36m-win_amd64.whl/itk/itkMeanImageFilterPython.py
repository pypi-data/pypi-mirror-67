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
    from . import _itkMeanImageFilterPython
else:
    import _itkMeanImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkMeanImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkMeanImageFilterPython.SWIG_PyStaticMethod_New

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


import itkBoxImageFilterPython
import itkImageToImageFilterAPython
import itkImageToImageFilterCommonPython
import pyBasePython
import ITKCommonBasePython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageRegionPython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkImagePython
import itkFixedArrayPython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkVectorPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import itkCovariantVectorPython
import itkPointPython
import vnl_matrix_fixedPython
import itkVectorImagePython
import itkVariableLengthVectorPython

def itkMeanImageFilterID3ID3_New():
  return itkMeanImageFilterID3ID3.New()


def itkMeanImageFilterID2ID2_New():
  return itkMeanImageFilterID2ID2.New()


def itkMeanImageFilterIF3IF3_New():
  return itkMeanImageFilterIF3IF3.New()


def itkMeanImageFilterIF2IF2_New():
  return itkMeanImageFilterIF2IF2.New()


def itkMeanImageFilterIUS3IUS3_New():
  return itkMeanImageFilterIUS3IUS3.New()


def itkMeanImageFilterIUS2IUS2_New():
  return itkMeanImageFilterIUS2IUS2.New()


def itkMeanImageFilterIUC3IUC3_New():
  return itkMeanImageFilterIUC3IUC3.New()


def itkMeanImageFilterIUC2IUC2_New():
  return itkMeanImageFilterIUC2IUC2.New()


def itkMeanImageFilterISS3ISS3_New():
  return itkMeanImageFilterISS3ISS3.New()


def itkMeanImageFilterISS2ISS2_New():
  return itkMeanImageFilterISS2ISS2.New()

class itkMeanImageFilterID2ID2(itkBoxImageFilterPython.itkBoxImageFilterID2ID2):
    r"""Proxy of C++ itkMeanImageFilterID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMeanImageFilterPython.itkMeanImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkMeanImageFilterPython.itkMeanImageFilterID2ID2_Clone)
    InputHasNumericTraitsCheck = _itkMeanImageFilterPython.itkMeanImageFilterID2ID2_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkMeanImageFilterPython.delete_itkMeanImageFilterID2ID2
    cast = _swig_new_static_method(_itkMeanImageFilterPython.itkMeanImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkMeanImageFilterID2ID2

        Create a new object of the class itkMeanImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeanImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeanImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeanImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMeanImageFilterID2ID2 in _itkMeanImageFilterPython:
_itkMeanImageFilterPython.itkMeanImageFilterID2ID2_swigregister(itkMeanImageFilterID2ID2)
itkMeanImageFilterID2ID2___New_orig__ = _itkMeanImageFilterPython.itkMeanImageFilterID2ID2___New_orig__
itkMeanImageFilterID2ID2_cast = _itkMeanImageFilterPython.itkMeanImageFilterID2ID2_cast

class itkMeanImageFilterID3ID3(itkBoxImageFilterPython.itkBoxImageFilterID3ID3):
    r"""Proxy of C++ itkMeanImageFilterID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMeanImageFilterPython.itkMeanImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkMeanImageFilterPython.itkMeanImageFilterID3ID3_Clone)
    InputHasNumericTraitsCheck = _itkMeanImageFilterPython.itkMeanImageFilterID3ID3_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkMeanImageFilterPython.delete_itkMeanImageFilterID3ID3
    cast = _swig_new_static_method(_itkMeanImageFilterPython.itkMeanImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkMeanImageFilterID3ID3

        Create a new object of the class itkMeanImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeanImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeanImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeanImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMeanImageFilterID3ID3 in _itkMeanImageFilterPython:
_itkMeanImageFilterPython.itkMeanImageFilterID3ID3_swigregister(itkMeanImageFilterID3ID3)
itkMeanImageFilterID3ID3___New_orig__ = _itkMeanImageFilterPython.itkMeanImageFilterID3ID3___New_orig__
itkMeanImageFilterID3ID3_cast = _itkMeanImageFilterPython.itkMeanImageFilterID3ID3_cast

class itkMeanImageFilterIF2IF2(itkBoxImageFilterPython.itkBoxImageFilterIF2IF2):
    r"""Proxy of C++ itkMeanImageFilterIF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMeanImageFilterPython.itkMeanImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkMeanImageFilterPython.itkMeanImageFilterIF2IF2_Clone)
    InputHasNumericTraitsCheck = _itkMeanImageFilterPython.itkMeanImageFilterIF2IF2_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkMeanImageFilterPython.delete_itkMeanImageFilterIF2IF2
    cast = _swig_new_static_method(_itkMeanImageFilterPython.itkMeanImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkMeanImageFilterIF2IF2

        Create a new object of the class itkMeanImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeanImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeanImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeanImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMeanImageFilterIF2IF2 in _itkMeanImageFilterPython:
_itkMeanImageFilterPython.itkMeanImageFilterIF2IF2_swigregister(itkMeanImageFilterIF2IF2)
itkMeanImageFilterIF2IF2___New_orig__ = _itkMeanImageFilterPython.itkMeanImageFilterIF2IF2___New_orig__
itkMeanImageFilterIF2IF2_cast = _itkMeanImageFilterPython.itkMeanImageFilterIF2IF2_cast

class itkMeanImageFilterIF3IF3(itkBoxImageFilterPython.itkBoxImageFilterIF3IF3):
    r"""Proxy of C++ itkMeanImageFilterIF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMeanImageFilterPython.itkMeanImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkMeanImageFilterPython.itkMeanImageFilterIF3IF3_Clone)
    InputHasNumericTraitsCheck = _itkMeanImageFilterPython.itkMeanImageFilterIF3IF3_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkMeanImageFilterPython.delete_itkMeanImageFilterIF3IF3
    cast = _swig_new_static_method(_itkMeanImageFilterPython.itkMeanImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkMeanImageFilterIF3IF3

        Create a new object of the class itkMeanImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeanImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeanImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeanImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMeanImageFilterIF3IF3 in _itkMeanImageFilterPython:
_itkMeanImageFilterPython.itkMeanImageFilterIF3IF3_swigregister(itkMeanImageFilterIF3IF3)
itkMeanImageFilterIF3IF3___New_orig__ = _itkMeanImageFilterPython.itkMeanImageFilterIF3IF3___New_orig__
itkMeanImageFilterIF3IF3_cast = _itkMeanImageFilterPython.itkMeanImageFilterIF3IF3_cast

class itkMeanImageFilterISS2ISS2(itkBoxImageFilterPython.itkBoxImageFilterISS2ISS2):
    r"""Proxy of C++ itkMeanImageFilterISS2ISS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMeanImageFilterPython.itkMeanImageFilterISS2ISS2___New_orig__)
    Clone = _swig_new_instance_method(_itkMeanImageFilterPython.itkMeanImageFilterISS2ISS2_Clone)
    InputHasNumericTraitsCheck = _itkMeanImageFilterPython.itkMeanImageFilterISS2ISS2_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkMeanImageFilterPython.delete_itkMeanImageFilterISS2ISS2
    cast = _swig_new_static_method(_itkMeanImageFilterPython.itkMeanImageFilterISS2ISS2_cast)

    def New(*args, **kargs):
        """New() -> itkMeanImageFilterISS2ISS2

        Create a new object of the class itkMeanImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeanImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeanImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeanImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMeanImageFilterISS2ISS2 in _itkMeanImageFilterPython:
_itkMeanImageFilterPython.itkMeanImageFilterISS2ISS2_swigregister(itkMeanImageFilterISS2ISS2)
itkMeanImageFilterISS2ISS2___New_orig__ = _itkMeanImageFilterPython.itkMeanImageFilterISS2ISS2___New_orig__
itkMeanImageFilterISS2ISS2_cast = _itkMeanImageFilterPython.itkMeanImageFilterISS2ISS2_cast

class itkMeanImageFilterISS3ISS3(itkBoxImageFilterPython.itkBoxImageFilterISS3ISS3):
    r"""Proxy of C++ itkMeanImageFilterISS3ISS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMeanImageFilterPython.itkMeanImageFilterISS3ISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkMeanImageFilterPython.itkMeanImageFilterISS3ISS3_Clone)
    InputHasNumericTraitsCheck = _itkMeanImageFilterPython.itkMeanImageFilterISS3ISS3_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkMeanImageFilterPython.delete_itkMeanImageFilterISS3ISS3
    cast = _swig_new_static_method(_itkMeanImageFilterPython.itkMeanImageFilterISS3ISS3_cast)

    def New(*args, **kargs):
        """New() -> itkMeanImageFilterISS3ISS3

        Create a new object of the class itkMeanImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeanImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeanImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeanImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMeanImageFilterISS3ISS3 in _itkMeanImageFilterPython:
_itkMeanImageFilterPython.itkMeanImageFilterISS3ISS3_swigregister(itkMeanImageFilterISS3ISS3)
itkMeanImageFilterISS3ISS3___New_orig__ = _itkMeanImageFilterPython.itkMeanImageFilterISS3ISS3___New_orig__
itkMeanImageFilterISS3ISS3_cast = _itkMeanImageFilterPython.itkMeanImageFilterISS3ISS3_cast

class itkMeanImageFilterIUC2IUC2(itkBoxImageFilterPython.itkBoxImageFilterIUC2IUC2):
    r"""Proxy of C++ itkMeanImageFilterIUC2IUC2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMeanImageFilterPython.itkMeanImageFilterIUC2IUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkMeanImageFilterPython.itkMeanImageFilterIUC2IUC2_Clone)
    InputHasNumericTraitsCheck = _itkMeanImageFilterPython.itkMeanImageFilterIUC2IUC2_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkMeanImageFilterPython.delete_itkMeanImageFilterIUC2IUC2
    cast = _swig_new_static_method(_itkMeanImageFilterPython.itkMeanImageFilterIUC2IUC2_cast)

    def New(*args, **kargs):
        """New() -> itkMeanImageFilterIUC2IUC2

        Create a new object of the class itkMeanImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeanImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeanImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeanImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMeanImageFilterIUC2IUC2 in _itkMeanImageFilterPython:
_itkMeanImageFilterPython.itkMeanImageFilterIUC2IUC2_swigregister(itkMeanImageFilterIUC2IUC2)
itkMeanImageFilterIUC2IUC2___New_orig__ = _itkMeanImageFilterPython.itkMeanImageFilterIUC2IUC2___New_orig__
itkMeanImageFilterIUC2IUC2_cast = _itkMeanImageFilterPython.itkMeanImageFilterIUC2IUC2_cast

class itkMeanImageFilterIUC3IUC3(itkBoxImageFilterPython.itkBoxImageFilterIUC3IUC3):
    r"""Proxy of C++ itkMeanImageFilterIUC3IUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMeanImageFilterPython.itkMeanImageFilterIUC3IUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkMeanImageFilterPython.itkMeanImageFilterIUC3IUC3_Clone)
    InputHasNumericTraitsCheck = _itkMeanImageFilterPython.itkMeanImageFilterIUC3IUC3_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkMeanImageFilterPython.delete_itkMeanImageFilterIUC3IUC3
    cast = _swig_new_static_method(_itkMeanImageFilterPython.itkMeanImageFilterIUC3IUC3_cast)

    def New(*args, **kargs):
        """New() -> itkMeanImageFilterIUC3IUC3

        Create a new object of the class itkMeanImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeanImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeanImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeanImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMeanImageFilterIUC3IUC3 in _itkMeanImageFilterPython:
_itkMeanImageFilterPython.itkMeanImageFilterIUC3IUC3_swigregister(itkMeanImageFilterIUC3IUC3)
itkMeanImageFilterIUC3IUC3___New_orig__ = _itkMeanImageFilterPython.itkMeanImageFilterIUC3IUC3___New_orig__
itkMeanImageFilterIUC3IUC3_cast = _itkMeanImageFilterPython.itkMeanImageFilterIUC3IUC3_cast

class itkMeanImageFilterIUS2IUS2(itkBoxImageFilterPython.itkBoxImageFilterIUS2IUS2):
    r"""Proxy of C++ itkMeanImageFilterIUS2IUS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMeanImageFilterPython.itkMeanImageFilterIUS2IUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkMeanImageFilterPython.itkMeanImageFilterIUS2IUS2_Clone)
    InputHasNumericTraitsCheck = _itkMeanImageFilterPython.itkMeanImageFilterIUS2IUS2_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkMeanImageFilterPython.delete_itkMeanImageFilterIUS2IUS2
    cast = _swig_new_static_method(_itkMeanImageFilterPython.itkMeanImageFilterIUS2IUS2_cast)

    def New(*args, **kargs):
        """New() -> itkMeanImageFilterIUS2IUS2

        Create a new object of the class itkMeanImageFilterIUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeanImageFilterIUS2IUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeanImageFilterIUS2IUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeanImageFilterIUS2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMeanImageFilterIUS2IUS2 in _itkMeanImageFilterPython:
_itkMeanImageFilterPython.itkMeanImageFilterIUS2IUS2_swigregister(itkMeanImageFilterIUS2IUS2)
itkMeanImageFilterIUS2IUS2___New_orig__ = _itkMeanImageFilterPython.itkMeanImageFilterIUS2IUS2___New_orig__
itkMeanImageFilterIUS2IUS2_cast = _itkMeanImageFilterPython.itkMeanImageFilterIUS2IUS2_cast

class itkMeanImageFilterIUS3IUS3(itkBoxImageFilterPython.itkBoxImageFilterIUS3IUS3):
    r"""Proxy of C++ itkMeanImageFilterIUS3IUS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMeanImageFilterPython.itkMeanImageFilterIUS3IUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkMeanImageFilterPython.itkMeanImageFilterIUS3IUS3_Clone)
    InputHasNumericTraitsCheck = _itkMeanImageFilterPython.itkMeanImageFilterIUS3IUS3_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkMeanImageFilterPython.delete_itkMeanImageFilterIUS3IUS3
    cast = _swig_new_static_method(_itkMeanImageFilterPython.itkMeanImageFilterIUS3IUS3_cast)

    def New(*args, **kargs):
        """New() -> itkMeanImageFilterIUS3IUS3

        Create a new object of the class itkMeanImageFilterIUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMeanImageFilterIUS3IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMeanImageFilterIUS3IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMeanImageFilterIUS3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMeanImageFilterIUS3IUS3 in _itkMeanImageFilterPython:
_itkMeanImageFilterPython.itkMeanImageFilterIUS3IUS3_swigregister(itkMeanImageFilterIUS3IUS3)
itkMeanImageFilterIUS3IUS3___New_orig__ = _itkMeanImageFilterPython.itkMeanImageFilterIUS3IUS3___New_orig__
itkMeanImageFilterIUS3IUS3_cast = _itkMeanImageFilterPython.itkMeanImageFilterIUS3IUS3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def mean_image_filter(*args, **kwargs):
    """Procedural interface for MeanImageFilter"""
    import itk
    instance = itk.MeanImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def mean_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.MeanImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.MeanImageFilter.values()[0]
    else:
        filter_object = itk.MeanImageFilter

    mean_image_filter.__doc__ = filter_object.__doc__
    mean_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    mean_image_filter.__doc__ += "Available Keyword Arguments:\n"
    mean_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



