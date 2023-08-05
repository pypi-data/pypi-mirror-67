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
    from . import _itkBSplineUpsampleImageFilterPython
else:
    import _itkBSplineUpsampleImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkBSplineUpsampleImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkBSplineUpsampleImageFilterPython.SWIG_PyStaticMethod_New

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
import itkBSplineDownsampleImageFilterPython
import itkSizePython
import itkImageToImageFilterAPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImagePython
import stdcomplexPython
import itkVectorPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import itkFixedArrayPython
import itkOffsetPython
import itkCovariantVectorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkSymmetricSecondRankTensorPython
import itkRGBAPixelPython
import itkImageRegionPython
import itkIndexPython
import itkRGBPixelPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython

def itkBSplineUpsampleImageFilterID3ID3_New():
  return itkBSplineUpsampleImageFilterID3ID3.New()


def itkBSplineUpsampleImageFilterID2ID2_New():
  return itkBSplineUpsampleImageFilterID2ID2.New()


def itkBSplineUpsampleImageFilterIF3IF3_New():
  return itkBSplineUpsampleImageFilterIF3IF3.New()


def itkBSplineUpsampleImageFilterIF2IF2_New():
  return itkBSplineUpsampleImageFilterIF2IF2.New()


def itkBSplineUpsampleImageFilterIUS3IUS3_New():
  return itkBSplineUpsampleImageFilterIUS3IUS3.New()


def itkBSplineUpsampleImageFilterIUS2IUS2_New():
  return itkBSplineUpsampleImageFilterIUS2IUS2.New()


def itkBSplineUpsampleImageFilterIUC3IUC3_New():
  return itkBSplineUpsampleImageFilterIUC3IUC3.New()


def itkBSplineUpsampleImageFilterIUC2IUC2_New():
  return itkBSplineUpsampleImageFilterIUC2IUC2.New()


def itkBSplineUpsampleImageFilterISS3ISS3_New():
  return itkBSplineUpsampleImageFilterISS3ISS3.New()


def itkBSplineUpsampleImageFilterISS2ISS2_New():
  return itkBSplineUpsampleImageFilterISS2ISS2.New()

class itkBSplineUpsampleImageFilterID2ID2(itkBSplineDownsampleImageFilterPython.itkBSplineDownsampleImageFilterID2ID2_Superclass):
    r"""Proxy of C++ itkBSplineUpsampleImageFilterID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterID2ID2_Clone)
    GenerateOutputInformation = _swig_new_instance_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterID2ID2_GenerateOutputInformation)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterID2ID2_GenerateInputRequestedRegion)
    DoubleConvertibleToOutputCheck = _itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterID2ID2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkBSplineUpsampleImageFilterPython.delete_itkBSplineUpsampleImageFilterID2ID2
    cast = _swig_new_static_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineUpsampleImageFilterID2ID2

        Create a new object of the class itkBSplineUpsampleImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineUpsampleImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineUpsampleImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineUpsampleImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineUpsampleImageFilterID2ID2 in _itkBSplineUpsampleImageFilterPython:
_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterID2ID2_swigregister(itkBSplineUpsampleImageFilterID2ID2)
itkBSplineUpsampleImageFilterID2ID2___New_orig__ = _itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterID2ID2___New_orig__
itkBSplineUpsampleImageFilterID2ID2_cast = _itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterID2ID2_cast

class itkBSplineUpsampleImageFilterID3ID3(itkBSplineDownsampleImageFilterPython.itkBSplineDownsampleImageFilterID3ID3_Superclass):
    r"""Proxy of C++ itkBSplineUpsampleImageFilterID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterID3ID3_Clone)
    GenerateOutputInformation = _swig_new_instance_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterID3ID3_GenerateOutputInformation)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterID3ID3_GenerateInputRequestedRegion)
    DoubleConvertibleToOutputCheck = _itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterID3ID3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkBSplineUpsampleImageFilterPython.delete_itkBSplineUpsampleImageFilterID3ID3
    cast = _swig_new_static_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineUpsampleImageFilterID3ID3

        Create a new object of the class itkBSplineUpsampleImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineUpsampleImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineUpsampleImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineUpsampleImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineUpsampleImageFilterID3ID3 in _itkBSplineUpsampleImageFilterPython:
_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterID3ID3_swigregister(itkBSplineUpsampleImageFilterID3ID3)
itkBSplineUpsampleImageFilterID3ID3___New_orig__ = _itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterID3ID3___New_orig__
itkBSplineUpsampleImageFilterID3ID3_cast = _itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterID3ID3_cast

class itkBSplineUpsampleImageFilterIF2IF2(itkBSplineDownsampleImageFilterPython.itkBSplineDownsampleImageFilterIF2IF2_Superclass):
    r"""Proxy of C++ itkBSplineUpsampleImageFilterIF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIF2IF2_Clone)
    GenerateOutputInformation = _swig_new_instance_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIF2IF2_GenerateOutputInformation)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIF2IF2_GenerateInputRequestedRegion)
    DoubleConvertibleToOutputCheck = _itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIF2IF2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkBSplineUpsampleImageFilterPython.delete_itkBSplineUpsampleImageFilterIF2IF2
    cast = _swig_new_static_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineUpsampleImageFilterIF2IF2

        Create a new object of the class itkBSplineUpsampleImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineUpsampleImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineUpsampleImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineUpsampleImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineUpsampleImageFilterIF2IF2 in _itkBSplineUpsampleImageFilterPython:
_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIF2IF2_swigregister(itkBSplineUpsampleImageFilterIF2IF2)
itkBSplineUpsampleImageFilterIF2IF2___New_orig__ = _itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIF2IF2___New_orig__
itkBSplineUpsampleImageFilterIF2IF2_cast = _itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIF2IF2_cast

class itkBSplineUpsampleImageFilterIF3IF3(itkBSplineDownsampleImageFilterPython.itkBSplineDownsampleImageFilterIF3IF3_Superclass):
    r"""Proxy of C++ itkBSplineUpsampleImageFilterIF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIF3IF3_Clone)
    GenerateOutputInformation = _swig_new_instance_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIF3IF3_GenerateOutputInformation)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIF3IF3_GenerateInputRequestedRegion)
    DoubleConvertibleToOutputCheck = _itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIF3IF3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkBSplineUpsampleImageFilterPython.delete_itkBSplineUpsampleImageFilterIF3IF3
    cast = _swig_new_static_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineUpsampleImageFilterIF3IF3

        Create a new object of the class itkBSplineUpsampleImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineUpsampleImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineUpsampleImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineUpsampleImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineUpsampleImageFilterIF3IF3 in _itkBSplineUpsampleImageFilterPython:
_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIF3IF3_swigregister(itkBSplineUpsampleImageFilterIF3IF3)
itkBSplineUpsampleImageFilterIF3IF3___New_orig__ = _itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIF3IF3___New_orig__
itkBSplineUpsampleImageFilterIF3IF3_cast = _itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIF3IF3_cast

class itkBSplineUpsampleImageFilterISS2ISS2(itkBSplineDownsampleImageFilterPython.itkBSplineDownsampleImageFilterISS2ISS2_Superclass):
    r"""Proxy of C++ itkBSplineUpsampleImageFilterISS2ISS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterISS2ISS2___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterISS2ISS2_Clone)
    GenerateOutputInformation = _swig_new_instance_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterISS2ISS2_GenerateOutputInformation)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterISS2ISS2_GenerateInputRequestedRegion)
    DoubleConvertibleToOutputCheck = _itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterISS2ISS2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkBSplineUpsampleImageFilterPython.delete_itkBSplineUpsampleImageFilterISS2ISS2
    cast = _swig_new_static_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterISS2ISS2_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineUpsampleImageFilterISS2ISS2

        Create a new object of the class itkBSplineUpsampleImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineUpsampleImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineUpsampleImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineUpsampleImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineUpsampleImageFilterISS2ISS2 in _itkBSplineUpsampleImageFilterPython:
_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterISS2ISS2_swigregister(itkBSplineUpsampleImageFilterISS2ISS2)
itkBSplineUpsampleImageFilterISS2ISS2___New_orig__ = _itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterISS2ISS2___New_orig__
itkBSplineUpsampleImageFilterISS2ISS2_cast = _itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterISS2ISS2_cast

class itkBSplineUpsampleImageFilterISS3ISS3(itkBSplineDownsampleImageFilterPython.itkBSplineDownsampleImageFilterISS3ISS3_Superclass):
    r"""Proxy of C++ itkBSplineUpsampleImageFilterISS3ISS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterISS3ISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterISS3ISS3_Clone)
    GenerateOutputInformation = _swig_new_instance_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterISS3ISS3_GenerateOutputInformation)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterISS3ISS3_GenerateInputRequestedRegion)
    DoubleConvertibleToOutputCheck = _itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterISS3ISS3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkBSplineUpsampleImageFilterPython.delete_itkBSplineUpsampleImageFilterISS3ISS3
    cast = _swig_new_static_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterISS3ISS3_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineUpsampleImageFilterISS3ISS3

        Create a new object of the class itkBSplineUpsampleImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineUpsampleImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineUpsampleImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineUpsampleImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineUpsampleImageFilterISS3ISS3 in _itkBSplineUpsampleImageFilterPython:
_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterISS3ISS3_swigregister(itkBSplineUpsampleImageFilterISS3ISS3)
itkBSplineUpsampleImageFilterISS3ISS3___New_orig__ = _itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterISS3ISS3___New_orig__
itkBSplineUpsampleImageFilterISS3ISS3_cast = _itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterISS3ISS3_cast

class itkBSplineUpsampleImageFilterIUC2IUC2(itkBSplineDownsampleImageFilterPython.itkBSplineDownsampleImageFilterIUC2IUC2_Superclass):
    r"""Proxy of C++ itkBSplineUpsampleImageFilterIUC2IUC2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUC2IUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUC2IUC2_Clone)
    GenerateOutputInformation = _swig_new_instance_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUC2IUC2_GenerateOutputInformation)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUC2IUC2_GenerateInputRequestedRegion)
    DoubleConvertibleToOutputCheck = _itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUC2IUC2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkBSplineUpsampleImageFilterPython.delete_itkBSplineUpsampleImageFilterIUC2IUC2
    cast = _swig_new_static_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUC2IUC2_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineUpsampleImageFilterIUC2IUC2

        Create a new object of the class itkBSplineUpsampleImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineUpsampleImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineUpsampleImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineUpsampleImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineUpsampleImageFilterIUC2IUC2 in _itkBSplineUpsampleImageFilterPython:
_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUC2IUC2_swigregister(itkBSplineUpsampleImageFilterIUC2IUC2)
itkBSplineUpsampleImageFilterIUC2IUC2___New_orig__ = _itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUC2IUC2___New_orig__
itkBSplineUpsampleImageFilterIUC2IUC2_cast = _itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUC2IUC2_cast

class itkBSplineUpsampleImageFilterIUC3IUC3(itkBSplineDownsampleImageFilterPython.itkBSplineDownsampleImageFilterIUC3IUC3_Superclass):
    r"""Proxy of C++ itkBSplineUpsampleImageFilterIUC3IUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUC3IUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUC3IUC3_Clone)
    GenerateOutputInformation = _swig_new_instance_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUC3IUC3_GenerateOutputInformation)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUC3IUC3_GenerateInputRequestedRegion)
    DoubleConvertibleToOutputCheck = _itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUC3IUC3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkBSplineUpsampleImageFilterPython.delete_itkBSplineUpsampleImageFilterIUC3IUC3
    cast = _swig_new_static_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUC3IUC3_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineUpsampleImageFilterIUC3IUC3

        Create a new object of the class itkBSplineUpsampleImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineUpsampleImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineUpsampleImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineUpsampleImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineUpsampleImageFilterIUC3IUC3 in _itkBSplineUpsampleImageFilterPython:
_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUC3IUC3_swigregister(itkBSplineUpsampleImageFilterIUC3IUC3)
itkBSplineUpsampleImageFilterIUC3IUC3___New_orig__ = _itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUC3IUC3___New_orig__
itkBSplineUpsampleImageFilterIUC3IUC3_cast = _itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUC3IUC3_cast

class itkBSplineUpsampleImageFilterIUS2IUS2(itkBSplineDownsampleImageFilterPython.itkBSplineDownsampleImageFilterIUS2IUS2_Superclass):
    r"""Proxy of C++ itkBSplineUpsampleImageFilterIUS2IUS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUS2IUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUS2IUS2_Clone)
    GenerateOutputInformation = _swig_new_instance_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUS2IUS2_GenerateOutputInformation)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUS2IUS2_GenerateInputRequestedRegion)
    DoubleConvertibleToOutputCheck = _itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUS2IUS2_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkBSplineUpsampleImageFilterPython.delete_itkBSplineUpsampleImageFilterIUS2IUS2
    cast = _swig_new_static_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUS2IUS2_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineUpsampleImageFilterIUS2IUS2

        Create a new object of the class itkBSplineUpsampleImageFilterIUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineUpsampleImageFilterIUS2IUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineUpsampleImageFilterIUS2IUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineUpsampleImageFilterIUS2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineUpsampleImageFilterIUS2IUS2 in _itkBSplineUpsampleImageFilterPython:
_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUS2IUS2_swigregister(itkBSplineUpsampleImageFilterIUS2IUS2)
itkBSplineUpsampleImageFilterIUS2IUS2___New_orig__ = _itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUS2IUS2___New_orig__
itkBSplineUpsampleImageFilterIUS2IUS2_cast = _itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUS2IUS2_cast

class itkBSplineUpsampleImageFilterIUS3IUS3(itkBSplineDownsampleImageFilterPython.itkBSplineDownsampleImageFilterIUS3IUS3_Superclass):
    r"""Proxy of C++ itkBSplineUpsampleImageFilterIUS3IUS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUS3IUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUS3IUS3_Clone)
    GenerateOutputInformation = _swig_new_instance_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUS3IUS3_GenerateOutputInformation)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUS3IUS3_GenerateInputRequestedRegion)
    DoubleConvertibleToOutputCheck = _itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUS3IUS3_DoubleConvertibleToOutputCheck
    
    __swig_destroy__ = _itkBSplineUpsampleImageFilterPython.delete_itkBSplineUpsampleImageFilterIUS3IUS3
    cast = _swig_new_static_method(_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUS3IUS3_cast)

    def New(*args, **kargs):
        """New() -> itkBSplineUpsampleImageFilterIUS3IUS3

        Create a new object of the class itkBSplineUpsampleImageFilterIUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBSplineUpsampleImageFilterIUS3IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBSplineUpsampleImageFilterIUS3IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBSplineUpsampleImageFilterIUS3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBSplineUpsampleImageFilterIUS3IUS3 in _itkBSplineUpsampleImageFilterPython:
_itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUS3IUS3_swigregister(itkBSplineUpsampleImageFilterIUS3IUS3)
itkBSplineUpsampleImageFilterIUS3IUS3___New_orig__ = _itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUS3IUS3___New_orig__
itkBSplineUpsampleImageFilterIUS3IUS3_cast = _itkBSplineUpsampleImageFilterPython.itkBSplineUpsampleImageFilterIUS3IUS3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def b_spline_upsample_image_filter(*args, **kwargs):
    """Procedural interface for BSplineUpsampleImageFilter"""
    import itk
    instance = itk.BSplineUpsampleImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def b_spline_upsample_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.BSplineUpsampleImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.BSplineUpsampleImageFilter.values()[0]
    else:
        filter_object = itk.BSplineUpsampleImageFilter

    b_spline_upsample_image_filter.__doc__ = filter_object.__doc__
    b_spline_upsample_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    b_spline_upsample_image_filter.__doc__ += "Available Keyword Arguments:\n"
    b_spline_upsample_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



