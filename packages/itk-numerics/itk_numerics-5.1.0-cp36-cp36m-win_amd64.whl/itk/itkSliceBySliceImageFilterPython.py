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
    from . import _itkSliceBySliceImageFilterPython
else:
    import _itkSliceBySliceImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkSliceBySliceImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkSliceBySliceImageFilterPython.SWIG_PyStaticMethod_New

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


import itkImageToImageFilterBPython
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
import itkImageToImageFilterAPython

def itkSliceBySliceImageFilterICF3ICF3_New():
  return itkSliceBySliceImageFilterICF3ICF3.New()


def itkSliceBySliceImageFilterIRGBUC3IRGBUC3_New():
  return itkSliceBySliceImageFilterIRGBUC3IRGBUC3.New()


def itkSliceBySliceImageFilterID3ID3_New():
  return itkSliceBySliceImageFilterID3ID3.New()


def itkSliceBySliceImageFilterIF3IF3_New():
  return itkSliceBySliceImageFilterIF3IF3.New()


def itkSliceBySliceImageFilterIUS3IUS3_New():
  return itkSliceBySliceImageFilterIUS3IUS3.New()


def itkSliceBySliceImageFilterIUC3IUC3_New():
  return itkSliceBySliceImageFilterIUC3IUC3.New()


def itkSliceBySliceImageFilterISS3ISS3_New():
  return itkSliceBySliceImageFilterISS3ISS3.New()

class itkSliceBySliceImageFilterICF3ICF3(itkImageToImageFilterBPython.itkImageToImageFilterICF3ICF3):
    r"""Proxy of C++ itkSliceBySliceImageFilterICF3ICF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterICF3ICF3___New_orig__)
    Clone = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterICF3ICF3_Clone)
    SetDimension = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterICF3ICF3_SetDimension)
    GetDimension = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterICF3ICF3_GetDimension)
    SetFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterICF3ICF3_SetFilter)
    GetFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterICF3ICF3_GetFilter)
    SetInputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterICF3ICF3_SetInputFilter)
    GetModifiableInputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterICF3ICF3_GetModifiableInputFilter)
    GetInputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterICF3ICF3_GetInputFilter)
    SetOutputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterICF3ICF3_SetOutputFilter)
    GetModifiableOutputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterICF3ICF3_GetModifiableOutputFilter)
    GetOutputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterICF3ICF3_GetOutputFilter)
    GetSliceIndex = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterICF3ICF3_GetSliceIndex)
    __swig_destroy__ = _itkSliceBySliceImageFilterPython.delete_itkSliceBySliceImageFilterICF3ICF3
    cast = _swig_new_static_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterICF3ICF3_cast)

    def New(*args, **kargs):
        """New() -> itkSliceBySliceImageFilterICF3ICF3

        Create a new object of the class itkSliceBySliceImageFilterICF3ICF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSliceBySliceImageFilterICF3ICF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSliceBySliceImageFilterICF3ICF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSliceBySliceImageFilterICF3ICF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSliceBySliceImageFilterICF3ICF3 in _itkSliceBySliceImageFilterPython:
_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterICF3ICF3_swigregister(itkSliceBySliceImageFilterICF3ICF3)
itkSliceBySliceImageFilterICF3ICF3___New_orig__ = _itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterICF3ICF3___New_orig__
itkSliceBySliceImageFilterICF3ICF3_cast = _itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterICF3ICF3_cast

class itkSliceBySliceImageFilterID3ID3(itkImageToImageFilterAPython.itkImageToImageFilterID3ID3):
    r"""Proxy of C++ itkSliceBySliceImageFilterID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterID3ID3_Clone)
    SetDimension = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterID3ID3_SetDimension)
    GetDimension = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterID3ID3_GetDimension)
    SetFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterID3ID3_SetFilter)
    GetFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterID3ID3_GetFilter)
    SetInputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterID3ID3_SetInputFilter)
    GetModifiableInputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterID3ID3_GetModifiableInputFilter)
    GetInputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterID3ID3_GetInputFilter)
    SetOutputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterID3ID3_SetOutputFilter)
    GetModifiableOutputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterID3ID3_GetModifiableOutputFilter)
    GetOutputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterID3ID3_GetOutputFilter)
    GetSliceIndex = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterID3ID3_GetSliceIndex)
    __swig_destroy__ = _itkSliceBySliceImageFilterPython.delete_itkSliceBySliceImageFilterID3ID3
    cast = _swig_new_static_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkSliceBySliceImageFilterID3ID3

        Create a new object of the class itkSliceBySliceImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSliceBySliceImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSliceBySliceImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSliceBySliceImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSliceBySliceImageFilterID3ID3 in _itkSliceBySliceImageFilterPython:
_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterID3ID3_swigregister(itkSliceBySliceImageFilterID3ID3)
itkSliceBySliceImageFilterID3ID3___New_orig__ = _itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterID3ID3___New_orig__
itkSliceBySliceImageFilterID3ID3_cast = _itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterID3ID3_cast

class itkSliceBySliceImageFilterIF3IF3(itkImageToImageFilterAPython.itkImageToImageFilterIF3IF3):
    r"""Proxy of C++ itkSliceBySliceImageFilterIF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIF3IF3_Clone)
    SetDimension = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIF3IF3_SetDimension)
    GetDimension = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIF3IF3_GetDimension)
    SetFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIF3IF3_SetFilter)
    GetFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIF3IF3_GetFilter)
    SetInputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIF3IF3_SetInputFilter)
    GetModifiableInputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIF3IF3_GetModifiableInputFilter)
    GetInputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIF3IF3_GetInputFilter)
    SetOutputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIF3IF3_SetOutputFilter)
    GetModifiableOutputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIF3IF3_GetModifiableOutputFilter)
    GetOutputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIF3IF3_GetOutputFilter)
    GetSliceIndex = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIF3IF3_GetSliceIndex)
    __swig_destroy__ = _itkSliceBySliceImageFilterPython.delete_itkSliceBySliceImageFilterIF3IF3
    cast = _swig_new_static_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkSliceBySliceImageFilterIF3IF3

        Create a new object of the class itkSliceBySliceImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSliceBySliceImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSliceBySliceImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSliceBySliceImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSliceBySliceImageFilterIF3IF3 in _itkSliceBySliceImageFilterPython:
_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIF3IF3_swigregister(itkSliceBySliceImageFilterIF3IF3)
itkSliceBySliceImageFilterIF3IF3___New_orig__ = _itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIF3IF3___New_orig__
itkSliceBySliceImageFilterIF3IF3_cast = _itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIF3IF3_cast

class itkSliceBySliceImageFilterIRGBUC3IRGBUC3(itkImageToImageFilterAPython.itkImageToImageFilterIRGBUC3IRGBUC3):
    r"""Proxy of C++ itkSliceBySliceImageFilterIRGBUC3IRGBUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIRGBUC3IRGBUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIRGBUC3IRGBUC3_Clone)
    SetDimension = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIRGBUC3IRGBUC3_SetDimension)
    GetDimension = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIRGBUC3IRGBUC3_GetDimension)
    SetFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIRGBUC3IRGBUC3_SetFilter)
    GetFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIRGBUC3IRGBUC3_GetFilter)
    SetInputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIRGBUC3IRGBUC3_SetInputFilter)
    GetModifiableInputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIRGBUC3IRGBUC3_GetModifiableInputFilter)
    GetInputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIRGBUC3IRGBUC3_GetInputFilter)
    SetOutputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIRGBUC3IRGBUC3_SetOutputFilter)
    GetModifiableOutputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIRGBUC3IRGBUC3_GetModifiableOutputFilter)
    GetOutputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIRGBUC3IRGBUC3_GetOutputFilter)
    GetSliceIndex = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIRGBUC3IRGBUC3_GetSliceIndex)
    __swig_destroy__ = _itkSliceBySliceImageFilterPython.delete_itkSliceBySliceImageFilterIRGBUC3IRGBUC3
    cast = _swig_new_static_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIRGBUC3IRGBUC3_cast)

    def New(*args, **kargs):
        """New() -> itkSliceBySliceImageFilterIRGBUC3IRGBUC3

        Create a new object of the class itkSliceBySliceImageFilterIRGBUC3IRGBUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSliceBySliceImageFilterIRGBUC3IRGBUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSliceBySliceImageFilterIRGBUC3IRGBUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSliceBySliceImageFilterIRGBUC3IRGBUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSliceBySliceImageFilterIRGBUC3IRGBUC3 in _itkSliceBySliceImageFilterPython:
_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIRGBUC3IRGBUC3_swigregister(itkSliceBySliceImageFilterIRGBUC3IRGBUC3)
itkSliceBySliceImageFilterIRGBUC3IRGBUC3___New_orig__ = _itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIRGBUC3IRGBUC3___New_orig__
itkSliceBySliceImageFilterIRGBUC3IRGBUC3_cast = _itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIRGBUC3IRGBUC3_cast

class itkSliceBySliceImageFilterISS3ISS3(itkImageToImageFilterAPython.itkImageToImageFilterISS3ISS3):
    r"""Proxy of C++ itkSliceBySliceImageFilterISS3ISS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterISS3ISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterISS3ISS3_Clone)
    SetDimension = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterISS3ISS3_SetDimension)
    GetDimension = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterISS3ISS3_GetDimension)
    SetFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterISS3ISS3_SetFilter)
    GetFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterISS3ISS3_GetFilter)
    SetInputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterISS3ISS3_SetInputFilter)
    GetModifiableInputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterISS3ISS3_GetModifiableInputFilter)
    GetInputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterISS3ISS3_GetInputFilter)
    SetOutputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterISS3ISS3_SetOutputFilter)
    GetModifiableOutputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterISS3ISS3_GetModifiableOutputFilter)
    GetOutputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterISS3ISS3_GetOutputFilter)
    GetSliceIndex = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterISS3ISS3_GetSliceIndex)
    __swig_destroy__ = _itkSliceBySliceImageFilterPython.delete_itkSliceBySliceImageFilterISS3ISS3
    cast = _swig_new_static_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterISS3ISS3_cast)

    def New(*args, **kargs):
        """New() -> itkSliceBySliceImageFilterISS3ISS3

        Create a new object of the class itkSliceBySliceImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSliceBySliceImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSliceBySliceImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSliceBySliceImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSliceBySliceImageFilterISS3ISS3 in _itkSliceBySliceImageFilterPython:
_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterISS3ISS3_swigregister(itkSliceBySliceImageFilterISS3ISS3)
itkSliceBySliceImageFilterISS3ISS3___New_orig__ = _itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterISS3ISS3___New_orig__
itkSliceBySliceImageFilterISS3ISS3_cast = _itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterISS3ISS3_cast

class itkSliceBySliceImageFilterIUC3IUC3(itkImageToImageFilterAPython.itkImageToImageFilterIUC3IUC3):
    r"""Proxy of C++ itkSliceBySliceImageFilterIUC3IUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUC3IUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUC3IUC3_Clone)
    SetDimension = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUC3IUC3_SetDimension)
    GetDimension = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUC3IUC3_GetDimension)
    SetFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUC3IUC3_SetFilter)
    GetFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUC3IUC3_GetFilter)
    SetInputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUC3IUC3_SetInputFilter)
    GetModifiableInputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUC3IUC3_GetModifiableInputFilter)
    GetInputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUC3IUC3_GetInputFilter)
    SetOutputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUC3IUC3_SetOutputFilter)
    GetModifiableOutputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUC3IUC3_GetModifiableOutputFilter)
    GetOutputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUC3IUC3_GetOutputFilter)
    GetSliceIndex = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUC3IUC3_GetSliceIndex)
    __swig_destroy__ = _itkSliceBySliceImageFilterPython.delete_itkSliceBySliceImageFilterIUC3IUC3
    cast = _swig_new_static_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUC3IUC3_cast)

    def New(*args, **kargs):
        """New() -> itkSliceBySliceImageFilterIUC3IUC3

        Create a new object of the class itkSliceBySliceImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSliceBySliceImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSliceBySliceImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSliceBySliceImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSliceBySliceImageFilterIUC3IUC3 in _itkSliceBySliceImageFilterPython:
_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUC3IUC3_swigregister(itkSliceBySliceImageFilterIUC3IUC3)
itkSliceBySliceImageFilterIUC3IUC3___New_orig__ = _itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUC3IUC3___New_orig__
itkSliceBySliceImageFilterIUC3IUC3_cast = _itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUC3IUC3_cast

class itkSliceBySliceImageFilterIUS3IUS3(itkImageToImageFilterAPython.itkImageToImageFilterIUS3IUS3):
    r"""Proxy of C++ itkSliceBySliceImageFilterIUS3IUS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUS3IUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUS3IUS3_Clone)
    SetDimension = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUS3IUS3_SetDimension)
    GetDimension = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUS3IUS3_GetDimension)
    SetFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUS3IUS3_SetFilter)
    GetFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUS3IUS3_GetFilter)
    SetInputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUS3IUS3_SetInputFilter)
    GetModifiableInputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUS3IUS3_GetModifiableInputFilter)
    GetInputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUS3IUS3_GetInputFilter)
    SetOutputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUS3IUS3_SetOutputFilter)
    GetModifiableOutputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUS3IUS3_GetModifiableOutputFilter)
    GetOutputFilter = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUS3IUS3_GetOutputFilter)
    GetSliceIndex = _swig_new_instance_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUS3IUS3_GetSliceIndex)
    __swig_destroy__ = _itkSliceBySliceImageFilterPython.delete_itkSliceBySliceImageFilterIUS3IUS3
    cast = _swig_new_static_method(_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUS3IUS3_cast)

    def New(*args, **kargs):
        """New() -> itkSliceBySliceImageFilterIUS3IUS3

        Create a new object of the class itkSliceBySliceImageFilterIUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSliceBySliceImageFilterIUS3IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSliceBySliceImageFilterIUS3IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSliceBySliceImageFilterIUS3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSliceBySliceImageFilterIUS3IUS3 in _itkSliceBySliceImageFilterPython:
_itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUS3IUS3_swigregister(itkSliceBySliceImageFilterIUS3IUS3)
itkSliceBySliceImageFilterIUS3IUS3___New_orig__ = _itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUS3IUS3___New_orig__
itkSliceBySliceImageFilterIUS3IUS3_cast = _itkSliceBySliceImageFilterPython.itkSliceBySliceImageFilterIUS3IUS3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def slice_by_slice_image_filter(*args, **kwargs):
    """Procedural interface for SliceBySliceImageFilter"""
    import itk
    instance = itk.SliceBySliceImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def slice_by_slice_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.SliceBySliceImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.SliceBySliceImageFilter.values()[0]
    else:
        filter_object = itk.SliceBySliceImageFilter

    slice_by_slice_image_filter.__doc__ = filter_object.__doc__
    slice_by_slice_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    slice_by_slice_image_filter.__doc__ += "Available Keyword Arguments:\n"
    slice_by_slice_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



