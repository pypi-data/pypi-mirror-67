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
    from . import _itkEdgePotentialImageFilterPython
else:
    import _itkEdgePotentialImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkEdgePotentialImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkEdgePotentialImageFilterPython.SWIG_PyStaticMethod_New

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


import itkVectorMagnitudeImageFilterPython
import itkInPlaceImageFilterBPython
import ITKCommonBasePython
import pyBasePython
import itkImageToImageFilterBPython
import itkImageToImageFilterCommonPython
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

def itkEdgePotentialImageFilterICVF43ID3_New():
  return itkEdgePotentialImageFilterICVF43ID3.New()


def itkEdgePotentialImageFilterICVF42ID2_New():
  return itkEdgePotentialImageFilterICVF42ID2.New()


def itkEdgePotentialImageFilterICVF33ID3_New():
  return itkEdgePotentialImageFilterICVF33ID3.New()


def itkEdgePotentialImageFilterICVF32ID2_New():
  return itkEdgePotentialImageFilterICVF32ID2.New()


def itkEdgePotentialImageFilterICVF23ID3_New():
  return itkEdgePotentialImageFilterICVF23ID3.New()


def itkEdgePotentialImageFilterICVF22ID2_New():
  return itkEdgePotentialImageFilterICVF22ID2.New()


def itkEdgePotentialImageFilterICVF43IF3_New():
  return itkEdgePotentialImageFilterICVF43IF3.New()


def itkEdgePotentialImageFilterICVF42IF2_New():
  return itkEdgePotentialImageFilterICVF42IF2.New()


def itkEdgePotentialImageFilterICVF33IF3_New():
  return itkEdgePotentialImageFilterICVF33IF3.New()


def itkEdgePotentialImageFilterICVF32IF2_New():
  return itkEdgePotentialImageFilterICVF32IF2.New()


def itkEdgePotentialImageFilterICVF23IF3_New():
  return itkEdgePotentialImageFilterICVF23IF3.New()


def itkEdgePotentialImageFilterICVF22IF2_New():
  return itkEdgePotentialImageFilterICVF22IF2.New()

class itkEdgePotentialImageFilterICVF22ID2(itkVectorMagnitudeImageFilterPython.itkVectorMagnitudeImageFilterICVF22ID2_Superclass):
    r"""Proxy of C++ itkEdgePotentialImageFilterICVF22ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF22ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF22ID2_Clone)
    InputHasNumericTraitsCheck = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF22ID2_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkEdgePotentialImageFilterPython.delete_itkEdgePotentialImageFilterICVF22ID2
    cast = _swig_new_static_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF22ID2_cast)

    def New(*args, **kargs):
        """New() -> itkEdgePotentialImageFilterICVF22ID2

        Create a new object of the class itkEdgePotentialImageFilterICVF22ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkEdgePotentialImageFilterICVF22ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkEdgePotentialImageFilterICVF22ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkEdgePotentialImageFilterICVF22ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkEdgePotentialImageFilterICVF22ID2 in _itkEdgePotentialImageFilterPython:
_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF22ID2_swigregister(itkEdgePotentialImageFilterICVF22ID2)
itkEdgePotentialImageFilterICVF22ID2___New_orig__ = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF22ID2___New_orig__
itkEdgePotentialImageFilterICVF22ID2_cast = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF22ID2_cast

class itkEdgePotentialImageFilterICVF22IF2(itkVectorMagnitudeImageFilterPython.itkVectorMagnitudeImageFilterICVF22IF2_Superclass):
    r"""Proxy of C++ itkEdgePotentialImageFilterICVF22IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF22IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF22IF2_Clone)
    InputHasNumericTraitsCheck = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF22IF2_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkEdgePotentialImageFilterPython.delete_itkEdgePotentialImageFilterICVF22IF2
    cast = _swig_new_static_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF22IF2_cast)

    def New(*args, **kargs):
        """New() -> itkEdgePotentialImageFilterICVF22IF2

        Create a new object of the class itkEdgePotentialImageFilterICVF22IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkEdgePotentialImageFilterICVF22IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkEdgePotentialImageFilterICVF22IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkEdgePotentialImageFilterICVF22IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkEdgePotentialImageFilterICVF22IF2 in _itkEdgePotentialImageFilterPython:
_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF22IF2_swigregister(itkEdgePotentialImageFilterICVF22IF2)
itkEdgePotentialImageFilterICVF22IF2___New_orig__ = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF22IF2___New_orig__
itkEdgePotentialImageFilterICVF22IF2_cast = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF22IF2_cast

class itkEdgePotentialImageFilterICVF23ID3(itkVectorMagnitudeImageFilterPython.itkVectorMagnitudeImageFilterICVF23ID3_Superclass):
    r"""Proxy of C++ itkEdgePotentialImageFilterICVF23ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF23ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF23ID3_Clone)
    InputHasNumericTraitsCheck = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF23ID3_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkEdgePotentialImageFilterPython.delete_itkEdgePotentialImageFilterICVF23ID3
    cast = _swig_new_static_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF23ID3_cast)

    def New(*args, **kargs):
        """New() -> itkEdgePotentialImageFilterICVF23ID3

        Create a new object of the class itkEdgePotentialImageFilterICVF23ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkEdgePotentialImageFilterICVF23ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkEdgePotentialImageFilterICVF23ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkEdgePotentialImageFilterICVF23ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkEdgePotentialImageFilterICVF23ID3 in _itkEdgePotentialImageFilterPython:
_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF23ID3_swigregister(itkEdgePotentialImageFilterICVF23ID3)
itkEdgePotentialImageFilterICVF23ID3___New_orig__ = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF23ID3___New_orig__
itkEdgePotentialImageFilterICVF23ID3_cast = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF23ID3_cast

class itkEdgePotentialImageFilterICVF23IF3(itkVectorMagnitudeImageFilterPython.itkVectorMagnitudeImageFilterICVF23IF3_Superclass):
    r"""Proxy of C++ itkEdgePotentialImageFilterICVF23IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF23IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF23IF3_Clone)
    InputHasNumericTraitsCheck = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF23IF3_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkEdgePotentialImageFilterPython.delete_itkEdgePotentialImageFilterICVF23IF3
    cast = _swig_new_static_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF23IF3_cast)

    def New(*args, **kargs):
        """New() -> itkEdgePotentialImageFilterICVF23IF3

        Create a new object of the class itkEdgePotentialImageFilterICVF23IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkEdgePotentialImageFilterICVF23IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkEdgePotentialImageFilterICVF23IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkEdgePotentialImageFilterICVF23IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkEdgePotentialImageFilterICVF23IF3 in _itkEdgePotentialImageFilterPython:
_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF23IF3_swigregister(itkEdgePotentialImageFilterICVF23IF3)
itkEdgePotentialImageFilterICVF23IF3___New_orig__ = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF23IF3___New_orig__
itkEdgePotentialImageFilterICVF23IF3_cast = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF23IF3_cast

class itkEdgePotentialImageFilterICVF32ID2(itkVectorMagnitudeImageFilterPython.itkVectorMagnitudeImageFilterICVF32ID2_Superclass):
    r"""Proxy of C++ itkEdgePotentialImageFilterICVF32ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF32ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF32ID2_Clone)
    InputHasNumericTraitsCheck = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF32ID2_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkEdgePotentialImageFilterPython.delete_itkEdgePotentialImageFilterICVF32ID2
    cast = _swig_new_static_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF32ID2_cast)

    def New(*args, **kargs):
        """New() -> itkEdgePotentialImageFilterICVF32ID2

        Create a new object of the class itkEdgePotentialImageFilterICVF32ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkEdgePotentialImageFilterICVF32ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkEdgePotentialImageFilterICVF32ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkEdgePotentialImageFilterICVF32ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkEdgePotentialImageFilterICVF32ID2 in _itkEdgePotentialImageFilterPython:
_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF32ID2_swigregister(itkEdgePotentialImageFilterICVF32ID2)
itkEdgePotentialImageFilterICVF32ID2___New_orig__ = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF32ID2___New_orig__
itkEdgePotentialImageFilterICVF32ID2_cast = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF32ID2_cast

class itkEdgePotentialImageFilterICVF32IF2(itkVectorMagnitudeImageFilterPython.itkVectorMagnitudeImageFilterICVF32IF2_Superclass):
    r"""Proxy of C++ itkEdgePotentialImageFilterICVF32IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF32IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF32IF2_Clone)
    InputHasNumericTraitsCheck = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF32IF2_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkEdgePotentialImageFilterPython.delete_itkEdgePotentialImageFilterICVF32IF2
    cast = _swig_new_static_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF32IF2_cast)

    def New(*args, **kargs):
        """New() -> itkEdgePotentialImageFilterICVF32IF2

        Create a new object of the class itkEdgePotentialImageFilterICVF32IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkEdgePotentialImageFilterICVF32IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkEdgePotentialImageFilterICVF32IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkEdgePotentialImageFilterICVF32IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkEdgePotentialImageFilterICVF32IF2 in _itkEdgePotentialImageFilterPython:
_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF32IF2_swigregister(itkEdgePotentialImageFilterICVF32IF2)
itkEdgePotentialImageFilterICVF32IF2___New_orig__ = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF32IF2___New_orig__
itkEdgePotentialImageFilterICVF32IF2_cast = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF32IF2_cast

class itkEdgePotentialImageFilterICVF33ID3(itkVectorMagnitudeImageFilterPython.itkVectorMagnitudeImageFilterICVF33ID3_Superclass):
    r"""Proxy of C++ itkEdgePotentialImageFilterICVF33ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF33ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF33ID3_Clone)
    InputHasNumericTraitsCheck = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF33ID3_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkEdgePotentialImageFilterPython.delete_itkEdgePotentialImageFilterICVF33ID3
    cast = _swig_new_static_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF33ID3_cast)

    def New(*args, **kargs):
        """New() -> itkEdgePotentialImageFilterICVF33ID3

        Create a new object of the class itkEdgePotentialImageFilterICVF33ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkEdgePotentialImageFilterICVF33ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkEdgePotentialImageFilterICVF33ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkEdgePotentialImageFilterICVF33ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkEdgePotentialImageFilterICVF33ID3 in _itkEdgePotentialImageFilterPython:
_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF33ID3_swigregister(itkEdgePotentialImageFilterICVF33ID3)
itkEdgePotentialImageFilterICVF33ID3___New_orig__ = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF33ID3___New_orig__
itkEdgePotentialImageFilterICVF33ID3_cast = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF33ID3_cast

class itkEdgePotentialImageFilterICVF33IF3(itkVectorMagnitudeImageFilterPython.itkVectorMagnitudeImageFilterICVF33IF3_Superclass):
    r"""Proxy of C++ itkEdgePotentialImageFilterICVF33IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF33IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF33IF3_Clone)
    InputHasNumericTraitsCheck = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF33IF3_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkEdgePotentialImageFilterPython.delete_itkEdgePotentialImageFilterICVF33IF3
    cast = _swig_new_static_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF33IF3_cast)

    def New(*args, **kargs):
        """New() -> itkEdgePotentialImageFilterICVF33IF3

        Create a new object of the class itkEdgePotentialImageFilterICVF33IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkEdgePotentialImageFilterICVF33IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkEdgePotentialImageFilterICVF33IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkEdgePotentialImageFilterICVF33IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkEdgePotentialImageFilterICVF33IF3 in _itkEdgePotentialImageFilterPython:
_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF33IF3_swigregister(itkEdgePotentialImageFilterICVF33IF3)
itkEdgePotentialImageFilterICVF33IF3___New_orig__ = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF33IF3___New_orig__
itkEdgePotentialImageFilterICVF33IF3_cast = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF33IF3_cast

class itkEdgePotentialImageFilterICVF42ID2(itkVectorMagnitudeImageFilterPython.itkVectorMagnitudeImageFilterICVF42ID2_Superclass):
    r"""Proxy of C++ itkEdgePotentialImageFilterICVF42ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF42ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF42ID2_Clone)
    InputHasNumericTraitsCheck = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF42ID2_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkEdgePotentialImageFilterPython.delete_itkEdgePotentialImageFilterICVF42ID2
    cast = _swig_new_static_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF42ID2_cast)

    def New(*args, **kargs):
        """New() -> itkEdgePotentialImageFilterICVF42ID2

        Create a new object of the class itkEdgePotentialImageFilterICVF42ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkEdgePotentialImageFilterICVF42ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkEdgePotentialImageFilterICVF42ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkEdgePotentialImageFilterICVF42ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkEdgePotentialImageFilterICVF42ID2 in _itkEdgePotentialImageFilterPython:
_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF42ID2_swigregister(itkEdgePotentialImageFilterICVF42ID2)
itkEdgePotentialImageFilterICVF42ID2___New_orig__ = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF42ID2___New_orig__
itkEdgePotentialImageFilterICVF42ID2_cast = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF42ID2_cast

class itkEdgePotentialImageFilterICVF42IF2(itkVectorMagnitudeImageFilterPython.itkVectorMagnitudeImageFilterICVF42IF2_Superclass):
    r"""Proxy of C++ itkEdgePotentialImageFilterICVF42IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF42IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF42IF2_Clone)
    InputHasNumericTraitsCheck = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF42IF2_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkEdgePotentialImageFilterPython.delete_itkEdgePotentialImageFilterICVF42IF2
    cast = _swig_new_static_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF42IF2_cast)

    def New(*args, **kargs):
        """New() -> itkEdgePotentialImageFilterICVF42IF2

        Create a new object of the class itkEdgePotentialImageFilterICVF42IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkEdgePotentialImageFilterICVF42IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkEdgePotentialImageFilterICVF42IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkEdgePotentialImageFilterICVF42IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkEdgePotentialImageFilterICVF42IF2 in _itkEdgePotentialImageFilterPython:
_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF42IF2_swigregister(itkEdgePotentialImageFilterICVF42IF2)
itkEdgePotentialImageFilterICVF42IF2___New_orig__ = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF42IF2___New_orig__
itkEdgePotentialImageFilterICVF42IF2_cast = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF42IF2_cast

class itkEdgePotentialImageFilterICVF43ID3(itkVectorMagnitudeImageFilterPython.itkVectorMagnitudeImageFilterICVF43ID3_Superclass):
    r"""Proxy of C++ itkEdgePotentialImageFilterICVF43ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF43ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF43ID3_Clone)
    InputHasNumericTraitsCheck = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF43ID3_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkEdgePotentialImageFilterPython.delete_itkEdgePotentialImageFilterICVF43ID3
    cast = _swig_new_static_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF43ID3_cast)

    def New(*args, **kargs):
        """New() -> itkEdgePotentialImageFilterICVF43ID3

        Create a new object of the class itkEdgePotentialImageFilterICVF43ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkEdgePotentialImageFilterICVF43ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkEdgePotentialImageFilterICVF43ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkEdgePotentialImageFilterICVF43ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkEdgePotentialImageFilterICVF43ID3 in _itkEdgePotentialImageFilterPython:
_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF43ID3_swigregister(itkEdgePotentialImageFilterICVF43ID3)
itkEdgePotentialImageFilterICVF43ID3___New_orig__ = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF43ID3___New_orig__
itkEdgePotentialImageFilterICVF43ID3_cast = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF43ID3_cast

class itkEdgePotentialImageFilterICVF43IF3(itkVectorMagnitudeImageFilterPython.itkVectorMagnitudeImageFilterICVF43IF3_Superclass):
    r"""Proxy of C++ itkEdgePotentialImageFilterICVF43IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF43IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF43IF3_Clone)
    InputHasNumericTraitsCheck = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF43IF3_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkEdgePotentialImageFilterPython.delete_itkEdgePotentialImageFilterICVF43IF3
    cast = _swig_new_static_method(_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF43IF3_cast)

    def New(*args, **kargs):
        """New() -> itkEdgePotentialImageFilterICVF43IF3

        Create a new object of the class itkEdgePotentialImageFilterICVF43IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkEdgePotentialImageFilterICVF43IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkEdgePotentialImageFilterICVF43IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkEdgePotentialImageFilterICVF43IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkEdgePotentialImageFilterICVF43IF3 in _itkEdgePotentialImageFilterPython:
_itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF43IF3_swigregister(itkEdgePotentialImageFilterICVF43IF3)
itkEdgePotentialImageFilterICVF43IF3___New_orig__ = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF43IF3___New_orig__
itkEdgePotentialImageFilterICVF43IF3_cast = _itkEdgePotentialImageFilterPython.itkEdgePotentialImageFilterICVF43IF3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def edge_potential_image_filter(*args, **kwargs):
    """Procedural interface for EdgePotentialImageFilter"""
    import itk
    instance = itk.EdgePotentialImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def edge_potential_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.EdgePotentialImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.EdgePotentialImageFilter.values()[0]
    else:
        filter_object = itk.EdgePotentialImageFilter

    edge_potential_image_filter.__doc__ = filter_object.__doc__
    edge_potential_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    edge_potential_image_filter.__doc__ += "Available Keyword Arguments:\n"
    edge_potential_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



