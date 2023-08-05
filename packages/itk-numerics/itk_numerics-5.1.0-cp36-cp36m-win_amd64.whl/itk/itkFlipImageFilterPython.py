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
    from . import _itkFlipImageFilterPython
else:
    import _itkFlipImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkFlipImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkFlipImageFilterPython.SWIG_PyStaticMethod_New

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

def itkFlipImageFilterID3_New():
  return itkFlipImageFilterID3.New()


def itkFlipImageFilterID2_New():
  return itkFlipImageFilterID2.New()


def itkFlipImageFilterIF3_New():
  return itkFlipImageFilterIF3.New()


def itkFlipImageFilterIF2_New():
  return itkFlipImageFilterIF2.New()


def itkFlipImageFilterIUS3_New():
  return itkFlipImageFilterIUS3.New()


def itkFlipImageFilterIUS2_New():
  return itkFlipImageFilterIUS2.New()


def itkFlipImageFilterIUC3_New():
  return itkFlipImageFilterIUC3.New()


def itkFlipImageFilterIUC2_New():
  return itkFlipImageFilterIUC2.New()


def itkFlipImageFilterISS3_New():
  return itkFlipImageFilterISS3.New()


def itkFlipImageFilterISS2_New():
  return itkFlipImageFilterISS2.New()

class itkFlipImageFilterID2(itkImageToImageFilterAPython.itkImageToImageFilterID2ID2):
    r"""Proxy of C++ itkFlipImageFilterID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFlipImageFilterPython.itkFlipImageFilterID2___New_orig__)
    Clone = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterID2_Clone)
    SetFlipAxes = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterID2_SetFlipAxes)
    GetFlipAxes = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterID2_GetFlipAxes)
    FlipAboutOriginOn = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterID2_FlipAboutOriginOn)
    FlipAboutOriginOff = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterID2_FlipAboutOriginOff)
    GetFlipAboutOrigin = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterID2_GetFlipAboutOrigin)
    SetFlipAboutOrigin = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterID2_SetFlipAboutOrigin)
    GenerateOutputInformation = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterID2_GenerateOutputInformation)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterID2_GenerateInputRequestedRegion)
    __swig_destroy__ = _itkFlipImageFilterPython.delete_itkFlipImageFilterID2
    cast = _swig_new_static_method(_itkFlipImageFilterPython.itkFlipImageFilterID2_cast)

    def New(*args, **kargs):
        """New() -> itkFlipImageFilterID2

        Create a new object of the class itkFlipImageFilterID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFlipImageFilterID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFlipImageFilterID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFlipImageFilterID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFlipImageFilterID2 in _itkFlipImageFilterPython:
_itkFlipImageFilterPython.itkFlipImageFilterID2_swigregister(itkFlipImageFilterID2)
itkFlipImageFilterID2___New_orig__ = _itkFlipImageFilterPython.itkFlipImageFilterID2___New_orig__
itkFlipImageFilterID2_cast = _itkFlipImageFilterPython.itkFlipImageFilterID2_cast

class itkFlipImageFilterID3(itkImageToImageFilterAPython.itkImageToImageFilterID3ID3):
    r"""Proxy of C++ itkFlipImageFilterID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFlipImageFilterPython.itkFlipImageFilterID3___New_orig__)
    Clone = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterID3_Clone)
    SetFlipAxes = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterID3_SetFlipAxes)
    GetFlipAxes = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterID3_GetFlipAxes)
    FlipAboutOriginOn = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterID3_FlipAboutOriginOn)
    FlipAboutOriginOff = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterID3_FlipAboutOriginOff)
    GetFlipAboutOrigin = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterID3_GetFlipAboutOrigin)
    SetFlipAboutOrigin = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterID3_SetFlipAboutOrigin)
    GenerateOutputInformation = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterID3_GenerateOutputInformation)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterID3_GenerateInputRequestedRegion)
    __swig_destroy__ = _itkFlipImageFilterPython.delete_itkFlipImageFilterID3
    cast = _swig_new_static_method(_itkFlipImageFilterPython.itkFlipImageFilterID3_cast)

    def New(*args, **kargs):
        """New() -> itkFlipImageFilterID3

        Create a new object of the class itkFlipImageFilterID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFlipImageFilterID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFlipImageFilterID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFlipImageFilterID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFlipImageFilterID3 in _itkFlipImageFilterPython:
_itkFlipImageFilterPython.itkFlipImageFilterID3_swigregister(itkFlipImageFilterID3)
itkFlipImageFilterID3___New_orig__ = _itkFlipImageFilterPython.itkFlipImageFilterID3___New_orig__
itkFlipImageFilterID3_cast = _itkFlipImageFilterPython.itkFlipImageFilterID3_cast

class itkFlipImageFilterIF2(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    r"""Proxy of C++ itkFlipImageFilterIF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFlipImageFilterPython.itkFlipImageFilterIF2___New_orig__)
    Clone = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIF2_Clone)
    SetFlipAxes = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIF2_SetFlipAxes)
    GetFlipAxes = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIF2_GetFlipAxes)
    FlipAboutOriginOn = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIF2_FlipAboutOriginOn)
    FlipAboutOriginOff = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIF2_FlipAboutOriginOff)
    GetFlipAboutOrigin = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIF2_GetFlipAboutOrigin)
    SetFlipAboutOrigin = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIF2_SetFlipAboutOrigin)
    GenerateOutputInformation = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIF2_GenerateOutputInformation)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIF2_GenerateInputRequestedRegion)
    __swig_destroy__ = _itkFlipImageFilterPython.delete_itkFlipImageFilterIF2
    cast = _swig_new_static_method(_itkFlipImageFilterPython.itkFlipImageFilterIF2_cast)

    def New(*args, **kargs):
        """New() -> itkFlipImageFilterIF2

        Create a new object of the class itkFlipImageFilterIF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFlipImageFilterIF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFlipImageFilterIF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFlipImageFilterIF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFlipImageFilterIF2 in _itkFlipImageFilterPython:
_itkFlipImageFilterPython.itkFlipImageFilterIF2_swigregister(itkFlipImageFilterIF2)
itkFlipImageFilterIF2___New_orig__ = _itkFlipImageFilterPython.itkFlipImageFilterIF2___New_orig__
itkFlipImageFilterIF2_cast = _itkFlipImageFilterPython.itkFlipImageFilterIF2_cast

class itkFlipImageFilterIF3(itkImageToImageFilterAPython.itkImageToImageFilterIF3IF3):
    r"""Proxy of C++ itkFlipImageFilterIF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFlipImageFilterPython.itkFlipImageFilterIF3___New_orig__)
    Clone = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIF3_Clone)
    SetFlipAxes = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIF3_SetFlipAxes)
    GetFlipAxes = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIF3_GetFlipAxes)
    FlipAboutOriginOn = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIF3_FlipAboutOriginOn)
    FlipAboutOriginOff = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIF3_FlipAboutOriginOff)
    GetFlipAboutOrigin = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIF3_GetFlipAboutOrigin)
    SetFlipAboutOrigin = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIF3_SetFlipAboutOrigin)
    GenerateOutputInformation = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIF3_GenerateOutputInformation)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIF3_GenerateInputRequestedRegion)
    __swig_destroy__ = _itkFlipImageFilterPython.delete_itkFlipImageFilterIF3
    cast = _swig_new_static_method(_itkFlipImageFilterPython.itkFlipImageFilterIF3_cast)

    def New(*args, **kargs):
        """New() -> itkFlipImageFilterIF3

        Create a new object of the class itkFlipImageFilterIF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFlipImageFilterIF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFlipImageFilterIF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFlipImageFilterIF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFlipImageFilterIF3 in _itkFlipImageFilterPython:
_itkFlipImageFilterPython.itkFlipImageFilterIF3_swigregister(itkFlipImageFilterIF3)
itkFlipImageFilterIF3___New_orig__ = _itkFlipImageFilterPython.itkFlipImageFilterIF3___New_orig__
itkFlipImageFilterIF3_cast = _itkFlipImageFilterPython.itkFlipImageFilterIF3_cast

class itkFlipImageFilterISS2(itkImageToImageFilterAPython.itkImageToImageFilterISS2ISS2):
    r"""Proxy of C++ itkFlipImageFilterISS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFlipImageFilterPython.itkFlipImageFilterISS2___New_orig__)
    Clone = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterISS2_Clone)
    SetFlipAxes = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterISS2_SetFlipAxes)
    GetFlipAxes = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterISS2_GetFlipAxes)
    FlipAboutOriginOn = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterISS2_FlipAboutOriginOn)
    FlipAboutOriginOff = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterISS2_FlipAboutOriginOff)
    GetFlipAboutOrigin = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterISS2_GetFlipAboutOrigin)
    SetFlipAboutOrigin = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterISS2_SetFlipAboutOrigin)
    GenerateOutputInformation = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterISS2_GenerateOutputInformation)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterISS2_GenerateInputRequestedRegion)
    __swig_destroy__ = _itkFlipImageFilterPython.delete_itkFlipImageFilterISS2
    cast = _swig_new_static_method(_itkFlipImageFilterPython.itkFlipImageFilterISS2_cast)

    def New(*args, **kargs):
        """New() -> itkFlipImageFilterISS2

        Create a new object of the class itkFlipImageFilterISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFlipImageFilterISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFlipImageFilterISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFlipImageFilterISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFlipImageFilterISS2 in _itkFlipImageFilterPython:
_itkFlipImageFilterPython.itkFlipImageFilterISS2_swigregister(itkFlipImageFilterISS2)
itkFlipImageFilterISS2___New_orig__ = _itkFlipImageFilterPython.itkFlipImageFilterISS2___New_orig__
itkFlipImageFilterISS2_cast = _itkFlipImageFilterPython.itkFlipImageFilterISS2_cast

class itkFlipImageFilterISS3(itkImageToImageFilterAPython.itkImageToImageFilterISS3ISS3):
    r"""Proxy of C++ itkFlipImageFilterISS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFlipImageFilterPython.itkFlipImageFilterISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterISS3_Clone)
    SetFlipAxes = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterISS3_SetFlipAxes)
    GetFlipAxes = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterISS3_GetFlipAxes)
    FlipAboutOriginOn = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterISS3_FlipAboutOriginOn)
    FlipAboutOriginOff = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterISS3_FlipAboutOriginOff)
    GetFlipAboutOrigin = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterISS3_GetFlipAboutOrigin)
    SetFlipAboutOrigin = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterISS3_SetFlipAboutOrigin)
    GenerateOutputInformation = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterISS3_GenerateOutputInformation)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterISS3_GenerateInputRequestedRegion)
    __swig_destroy__ = _itkFlipImageFilterPython.delete_itkFlipImageFilterISS3
    cast = _swig_new_static_method(_itkFlipImageFilterPython.itkFlipImageFilterISS3_cast)

    def New(*args, **kargs):
        """New() -> itkFlipImageFilterISS3

        Create a new object of the class itkFlipImageFilterISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFlipImageFilterISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFlipImageFilterISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFlipImageFilterISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFlipImageFilterISS3 in _itkFlipImageFilterPython:
_itkFlipImageFilterPython.itkFlipImageFilterISS3_swigregister(itkFlipImageFilterISS3)
itkFlipImageFilterISS3___New_orig__ = _itkFlipImageFilterPython.itkFlipImageFilterISS3___New_orig__
itkFlipImageFilterISS3_cast = _itkFlipImageFilterPython.itkFlipImageFilterISS3_cast

class itkFlipImageFilterIUC2(itkImageToImageFilterAPython.itkImageToImageFilterIUC2IUC2):
    r"""Proxy of C++ itkFlipImageFilterIUC2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFlipImageFilterPython.itkFlipImageFilterIUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUC2_Clone)
    SetFlipAxes = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUC2_SetFlipAxes)
    GetFlipAxes = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUC2_GetFlipAxes)
    FlipAboutOriginOn = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUC2_FlipAboutOriginOn)
    FlipAboutOriginOff = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUC2_FlipAboutOriginOff)
    GetFlipAboutOrigin = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUC2_GetFlipAboutOrigin)
    SetFlipAboutOrigin = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUC2_SetFlipAboutOrigin)
    GenerateOutputInformation = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUC2_GenerateOutputInformation)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUC2_GenerateInputRequestedRegion)
    __swig_destroy__ = _itkFlipImageFilterPython.delete_itkFlipImageFilterIUC2
    cast = _swig_new_static_method(_itkFlipImageFilterPython.itkFlipImageFilterIUC2_cast)

    def New(*args, **kargs):
        """New() -> itkFlipImageFilterIUC2

        Create a new object of the class itkFlipImageFilterIUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFlipImageFilterIUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFlipImageFilterIUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFlipImageFilterIUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFlipImageFilterIUC2 in _itkFlipImageFilterPython:
_itkFlipImageFilterPython.itkFlipImageFilterIUC2_swigregister(itkFlipImageFilterIUC2)
itkFlipImageFilterIUC2___New_orig__ = _itkFlipImageFilterPython.itkFlipImageFilterIUC2___New_orig__
itkFlipImageFilterIUC2_cast = _itkFlipImageFilterPython.itkFlipImageFilterIUC2_cast

class itkFlipImageFilterIUC3(itkImageToImageFilterAPython.itkImageToImageFilterIUC3IUC3):
    r"""Proxy of C++ itkFlipImageFilterIUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFlipImageFilterPython.itkFlipImageFilterIUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUC3_Clone)
    SetFlipAxes = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUC3_SetFlipAxes)
    GetFlipAxes = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUC3_GetFlipAxes)
    FlipAboutOriginOn = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUC3_FlipAboutOriginOn)
    FlipAboutOriginOff = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUC3_FlipAboutOriginOff)
    GetFlipAboutOrigin = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUC3_GetFlipAboutOrigin)
    SetFlipAboutOrigin = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUC3_SetFlipAboutOrigin)
    GenerateOutputInformation = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUC3_GenerateOutputInformation)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUC3_GenerateInputRequestedRegion)
    __swig_destroy__ = _itkFlipImageFilterPython.delete_itkFlipImageFilterIUC3
    cast = _swig_new_static_method(_itkFlipImageFilterPython.itkFlipImageFilterIUC3_cast)

    def New(*args, **kargs):
        """New() -> itkFlipImageFilterIUC3

        Create a new object of the class itkFlipImageFilterIUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFlipImageFilterIUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFlipImageFilterIUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFlipImageFilterIUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFlipImageFilterIUC3 in _itkFlipImageFilterPython:
_itkFlipImageFilterPython.itkFlipImageFilterIUC3_swigregister(itkFlipImageFilterIUC3)
itkFlipImageFilterIUC3___New_orig__ = _itkFlipImageFilterPython.itkFlipImageFilterIUC3___New_orig__
itkFlipImageFilterIUC3_cast = _itkFlipImageFilterPython.itkFlipImageFilterIUC3_cast

class itkFlipImageFilterIUS2(itkImageToImageFilterAPython.itkImageToImageFilterIUS2IUS2):
    r"""Proxy of C++ itkFlipImageFilterIUS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFlipImageFilterPython.itkFlipImageFilterIUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUS2_Clone)
    SetFlipAxes = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUS2_SetFlipAxes)
    GetFlipAxes = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUS2_GetFlipAxes)
    FlipAboutOriginOn = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUS2_FlipAboutOriginOn)
    FlipAboutOriginOff = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUS2_FlipAboutOriginOff)
    GetFlipAboutOrigin = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUS2_GetFlipAboutOrigin)
    SetFlipAboutOrigin = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUS2_SetFlipAboutOrigin)
    GenerateOutputInformation = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUS2_GenerateOutputInformation)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUS2_GenerateInputRequestedRegion)
    __swig_destroy__ = _itkFlipImageFilterPython.delete_itkFlipImageFilterIUS2
    cast = _swig_new_static_method(_itkFlipImageFilterPython.itkFlipImageFilterIUS2_cast)

    def New(*args, **kargs):
        """New() -> itkFlipImageFilterIUS2

        Create a new object of the class itkFlipImageFilterIUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFlipImageFilterIUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFlipImageFilterIUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFlipImageFilterIUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFlipImageFilterIUS2 in _itkFlipImageFilterPython:
_itkFlipImageFilterPython.itkFlipImageFilterIUS2_swigregister(itkFlipImageFilterIUS2)
itkFlipImageFilterIUS2___New_orig__ = _itkFlipImageFilterPython.itkFlipImageFilterIUS2___New_orig__
itkFlipImageFilterIUS2_cast = _itkFlipImageFilterPython.itkFlipImageFilterIUS2_cast

class itkFlipImageFilterIUS3(itkImageToImageFilterAPython.itkImageToImageFilterIUS3IUS3):
    r"""Proxy of C++ itkFlipImageFilterIUS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkFlipImageFilterPython.itkFlipImageFilterIUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUS3_Clone)
    SetFlipAxes = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUS3_SetFlipAxes)
    GetFlipAxes = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUS3_GetFlipAxes)
    FlipAboutOriginOn = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUS3_FlipAboutOriginOn)
    FlipAboutOriginOff = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUS3_FlipAboutOriginOff)
    GetFlipAboutOrigin = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUS3_GetFlipAboutOrigin)
    SetFlipAboutOrigin = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUS3_SetFlipAboutOrigin)
    GenerateOutputInformation = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUS3_GenerateOutputInformation)
    GenerateInputRequestedRegion = _swig_new_instance_method(_itkFlipImageFilterPython.itkFlipImageFilterIUS3_GenerateInputRequestedRegion)
    __swig_destroy__ = _itkFlipImageFilterPython.delete_itkFlipImageFilterIUS3
    cast = _swig_new_static_method(_itkFlipImageFilterPython.itkFlipImageFilterIUS3_cast)

    def New(*args, **kargs):
        """New() -> itkFlipImageFilterIUS3

        Create a new object of the class itkFlipImageFilterIUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkFlipImageFilterIUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkFlipImageFilterIUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkFlipImageFilterIUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkFlipImageFilterIUS3 in _itkFlipImageFilterPython:
_itkFlipImageFilterPython.itkFlipImageFilterIUS3_swigregister(itkFlipImageFilterIUS3)
itkFlipImageFilterIUS3___New_orig__ = _itkFlipImageFilterPython.itkFlipImageFilterIUS3___New_orig__
itkFlipImageFilterIUS3_cast = _itkFlipImageFilterPython.itkFlipImageFilterIUS3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def flip_image_filter(*args, **kwargs):
    """Procedural interface for FlipImageFilter"""
    import itk
    instance = itk.FlipImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def flip_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.FlipImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.FlipImageFilter.values()[0]
    else:
        filter_object = itk.FlipImageFilter

    flip_image_filter.__doc__ = filter_object.__doc__
    flip_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    flip_image_filter.__doc__ += "Available Keyword Arguments:\n"
    flip_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



