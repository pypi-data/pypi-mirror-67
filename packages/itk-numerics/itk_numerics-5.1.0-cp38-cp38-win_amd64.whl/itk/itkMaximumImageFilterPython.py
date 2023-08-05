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
    from . import _itkMaximumImageFilterPython
else:
    import _itkMaximumImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkMaximumImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkMaximumImageFilterPython.SWIG_PyStaticMethod_New

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
import itkRGBAPixelPython
import itkFixedArrayPython
import itkVectorPython
import vnl_vector_refPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import itkImagePython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkCovariantVectorPython
import itkSymmetricSecondRankTensorPython
import itkRGBPixelPython
import itkImageRegionPython
import itkInPlaceImageFilterBPython
import itkImageToImageFilterBPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkSimpleDataObjectDecoratorPython
import itkArrayPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterAPython

def itkMaximumImageFilterID3ID3ID3_New():
  return itkMaximumImageFilterID3ID3ID3.New()


def itkMaximumImageFilterID2ID2ID2_New():
  return itkMaximumImageFilterID2ID2ID2.New()


def itkMaximumImageFilterIF3IF3IF3_New():
  return itkMaximumImageFilterIF3IF3IF3.New()


def itkMaximumImageFilterIF2IF2IF2_New():
  return itkMaximumImageFilterIF2IF2IF2.New()


def itkMaximumImageFilterIUS3IUS3IUS3_New():
  return itkMaximumImageFilterIUS3IUS3IUS3.New()


def itkMaximumImageFilterIUS2IUS2IUS2_New():
  return itkMaximumImageFilterIUS2IUS2IUS2.New()


def itkMaximumImageFilterIUC3IUC3IUC3_New():
  return itkMaximumImageFilterIUC3IUC3IUC3.New()


def itkMaximumImageFilterIUC2IUC2IUC2_New():
  return itkMaximumImageFilterIUC2IUC2IUC2.New()


def itkMaximumImageFilterISS3ISS3ISS3_New():
  return itkMaximumImageFilterISS3ISS3ISS3.New()


def itkMaximumImageFilterISS2ISS2ISS2_New():
  return itkMaximumImageFilterISS2ISS2ISS2.New()

class itkMaximumImageFilterID2ID2ID2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterID2ID2ID2):
    r"""Proxy of C++ itkMaximumImageFilterID2ID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMaximumImageFilterPython.itkMaximumImageFilterID2ID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkMaximumImageFilterPython.itkMaximumImageFilterID2ID2ID2_Clone)
    Input1ConvertibleToOutputCheck = _itkMaximumImageFilterPython.itkMaximumImageFilterID2ID2ID2_Input1ConvertibleToOutputCheck
    
    Input2ConvertibleToOutputCheck = _itkMaximumImageFilterPython.itkMaximumImageFilterID2ID2ID2_Input2ConvertibleToOutputCheck
    
    Input1GreaterThanInput2Check = _itkMaximumImageFilterPython.itkMaximumImageFilterID2ID2ID2_Input1GreaterThanInput2Check
    
    __swig_destroy__ = _itkMaximumImageFilterPython.delete_itkMaximumImageFilterID2ID2ID2
    cast = _swig_new_static_method(_itkMaximumImageFilterPython.itkMaximumImageFilterID2ID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkMaximumImageFilterID2ID2ID2

        Create a new object of the class itkMaximumImageFilterID2ID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMaximumImageFilterID2ID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMaximumImageFilterID2ID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMaximumImageFilterID2ID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMaximumImageFilterID2ID2ID2 in _itkMaximumImageFilterPython:
_itkMaximumImageFilterPython.itkMaximumImageFilterID2ID2ID2_swigregister(itkMaximumImageFilterID2ID2ID2)
itkMaximumImageFilterID2ID2ID2___New_orig__ = _itkMaximumImageFilterPython.itkMaximumImageFilterID2ID2ID2___New_orig__
itkMaximumImageFilterID2ID2ID2_cast = _itkMaximumImageFilterPython.itkMaximumImageFilterID2ID2ID2_cast

class itkMaximumImageFilterID3ID3ID3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterID3ID3ID3):
    r"""Proxy of C++ itkMaximumImageFilterID3ID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMaximumImageFilterPython.itkMaximumImageFilterID3ID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkMaximumImageFilterPython.itkMaximumImageFilterID3ID3ID3_Clone)
    Input1ConvertibleToOutputCheck = _itkMaximumImageFilterPython.itkMaximumImageFilterID3ID3ID3_Input1ConvertibleToOutputCheck
    
    Input2ConvertibleToOutputCheck = _itkMaximumImageFilterPython.itkMaximumImageFilterID3ID3ID3_Input2ConvertibleToOutputCheck
    
    Input1GreaterThanInput2Check = _itkMaximumImageFilterPython.itkMaximumImageFilterID3ID3ID3_Input1GreaterThanInput2Check
    
    __swig_destroy__ = _itkMaximumImageFilterPython.delete_itkMaximumImageFilterID3ID3ID3
    cast = _swig_new_static_method(_itkMaximumImageFilterPython.itkMaximumImageFilterID3ID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkMaximumImageFilterID3ID3ID3

        Create a new object of the class itkMaximumImageFilterID3ID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMaximumImageFilterID3ID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMaximumImageFilterID3ID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMaximumImageFilterID3ID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMaximumImageFilterID3ID3ID3 in _itkMaximumImageFilterPython:
_itkMaximumImageFilterPython.itkMaximumImageFilterID3ID3ID3_swigregister(itkMaximumImageFilterID3ID3ID3)
itkMaximumImageFilterID3ID3ID3___New_orig__ = _itkMaximumImageFilterPython.itkMaximumImageFilterID3ID3ID3___New_orig__
itkMaximumImageFilterID3ID3ID3_cast = _itkMaximumImageFilterPython.itkMaximumImageFilterID3ID3ID3_cast

class itkMaximumImageFilterIF2IF2IF2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIF2IF2IF2):
    r"""Proxy of C++ itkMaximumImageFilterIF2IF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMaximumImageFilterPython.itkMaximumImageFilterIF2IF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkMaximumImageFilterPython.itkMaximumImageFilterIF2IF2IF2_Clone)
    Input1ConvertibleToOutputCheck = _itkMaximumImageFilterPython.itkMaximumImageFilterIF2IF2IF2_Input1ConvertibleToOutputCheck
    
    Input2ConvertibleToOutputCheck = _itkMaximumImageFilterPython.itkMaximumImageFilterIF2IF2IF2_Input2ConvertibleToOutputCheck
    
    Input1GreaterThanInput2Check = _itkMaximumImageFilterPython.itkMaximumImageFilterIF2IF2IF2_Input1GreaterThanInput2Check
    
    __swig_destroy__ = _itkMaximumImageFilterPython.delete_itkMaximumImageFilterIF2IF2IF2
    cast = _swig_new_static_method(_itkMaximumImageFilterPython.itkMaximumImageFilterIF2IF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkMaximumImageFilterIF2IF2IF2

        Create a new object of the class itkMaximumImageFilterIF2IF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMaximumImageFilterIF2IF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMaximumImageFilterIF2IF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMaximumImageFilterIF2IF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMaximumImageFilterIF2IF2IF2 in _itkMaximumImageFilterPython:
_itkMaximumImageFilterPython.itkMaximumImageFilterIF2IF2IF2_swigregister(itkMaximumImageFilterIF2IF2IF2)
itkMaximumImageFilterIF2IF2IF2___New_orig__ = _itkMaximumImageFilterPython.itkMaximumImageFilterIF2IF2IF2___New_orig__
itkMaximumImageFilterIF2IF2IF2_cast = _itkMaximumImageFilterPython.itkMaximumImageFilterIF2IF2IF2_cast

class itkMaximumImageFilterIF3IF3IF3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIF3IF3IF3):
    r"""Proxy of C++ itkMaximumImageFilterIF3IF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMaximumImageFilterPython.itkMaximumImageFilterIF3IF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkMaximumImageFilterPython.itkMaximumImageFilterIF3IF3IF3_Clone)
    Input1ConvertibleToOutputCheck = _itkMaximumImageFilterPython.itkMaximumImageFilterIF3IF3IF3_Input1ConvertibleToOutputCheck
    
    Input2ConvertibleToOutputCheck = _itkMaximumImageFilterPython.itkMaximumImageFilterIF3IF3IF3_Input2ConvertibleToOutputCheck
    
    Input1GreaterThanInput2Check = _itkMaximumImageFilterPython.itkMaximumImageFilterIF3IF3IF3_Input1GreaterThanInput2Check
    
    __swig_destroy__ = _itkMaximumImageFilterPython.delete_itkMaximumImageFilterIF3IF3IF3
    cast = _swig_new_static_method(_itkMaximumImageFilterPython.itkMaximumImageFilterIF3IF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkMaximumImageFilterIF3IF3IF3

        Create a new object of the class itkMaximumImageFilterIF3IF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMaximumImageFilterIF3IF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMaximumImageFilterIF3IF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMaximumImageFilterIF3IF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMaximumImageFilterIF3IF3IF3 in _itkMaximumImageFilterPython:
_itkMaximumImageFilterPython.itkMaximumImageFilterIF3IF3IF3_swigregister(itkMaximumImageFilterIF3IF3IF3)
itkMaximumImageFilterIF3IF3IF3___New_orig__ = _itkMaximumImageFilterPython.itkMaximumImageFilterIF3IF3IF3___New_orig__
itkMaximumImageFilterIF3IF3IF3_cast = _itkMaximumImageFilterPython.itkMaximumImageFilterIF3IF3IF3_cast

class itkMaximumImageFilterISS2ISS2ISS2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterISS2ISS2ISS2):
    r"""Proxy of C++ itkMaximumImageFilterISS2ISS2ISS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMaximumImageFilterPython.itkMaximumImageFilterISS2ISS2ISS2___New_orig__)
    Clone = _swig_new_instance_method(_itkMaximumImageFilterPython.itkMaximumImageFilterISS2ISS2ISS2_Clone)
    Input1ConvertibleToOutputCheck = _itkMaximumImageFilterPython.itkMaximumImageFilterISS2ISS2ISS2_Input1ConvertibleToOutputCheck
    
    Input2ConvertibleToOutputCheck = _itkMaximumImageFilterPython.itkMaximumImageFilterISS2ISS2ISS2_Input2ConvertibleToOutputCheck
    
    Input1GreaterThanInput2Check = _itkMaximumImageFilterPython.itkMaximumImageFilterISS2ISS2ISS2_Input1GreaterThanInput2Check
    
    __swig_destroy__ = _itkMaximumImageFilterPython.delete_itkMaximumImageFilterISS2ISS2ISS2
    cast = _swig_new_static_method(_itkMaximumImageFilterPython.itkMaximumImageFilterISS2ISS2ISS2_cast)

    def New(*args, **kargs):
        """New() -> itkMaximumImageFilterISS2ISS2ISS2

        Create a new object of the class itkMaximumImageFilterISS2ISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMaximumImageFilterISS2ISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMaximumImageFilterISS2ISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMaximumImageFilterISS2ISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMaximumImageFilterISS2ISS2ISS2 in _itkMaximumImageFilterPython:
_itkMaximumImageFilterPython.itkMaximumImageFilterISS2ISS2ISS2_swigregister(itkMaximumImageFilterISS2ISS2ISS2)
itkMaximumImageFilterISS2ISS2ISS2___New_orig__ = _itkMaximumImageFilterPython.itkMaximumImageFilterISS2ISS2ISS2___New_orig__
itkMaximumImageFilterISS2ISS2ISS2_cast = _itkMaximumImageFilterPython.itkMaximumImageFilterISS2ISS2ISS2_cast

class itkMaximumImageFilterISS3ISS3ISS3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterISS3ISS3ISS3):
    r"""Proxy of C++ itkMaximumImageFilterISS3ISS3ISS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMaximumImageFilterPython.itkMaximumImageFilterISS3ISS3ISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkMaximumImageFilterPython.itkMaximumImageFilterISS3ISS3ISS3_Clone)
    Input1ConvertibleToOutputCheck = _itkMaximumImageFilterPython.itkMaximumImageFilterISS3ISS3ISS3_Input1ConvertibleToOutputCheck
    
    Input2ConvertibleToOutputCheck = _itkMaximumImageFilterPython.itkMaximumImageFilterISS3ISS3ISS3_Input2ConvertibleToOutputCheck
    
    Input1GreaterThanInput2Check = _itkMaximumImageFilterPython.itkMaximumImageFilterISS3ISS3ISS3_Input1GreaterThanInput2Check
    
    __swig_destroy__ = _itkMaximumImageFilterPython.delete_itkMaximumImageFilterISS3ISS3ISS3
    cast = _swig_new_static_method(_itkMaximumImageFilterPython.itkMaximumImageFilterISS3ISS3ISS3_cast)

    def New(*args, **kargs):
        """New() -> itkMaximumImageFilterISS3ISS3ISS3

        Create a new object of the class itkMaximumImageFilterISS3ISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMaximumImageFilterISS3ISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMaximumImageFilterISS3ISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMaximumImageFilterISS3ISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMaximumImageFilterISS3ISS3ISS3 in _itkMaximumImageFilterPython:
_itkMaximumImageFilterPython.itkMaximumImageFilterISS3ISS3ISS3_swigregister(itkMaximumImageFilterISS3ISS3ISS3)
itkMaximumImageFilterISS3ISS3ISS3___New_orig__ = _itkMaximumImageFilterPython.itkMaximumImageFilterISS3ISS3ISS3___New_orig__
itkMaximumImageFilterISS3ISS3ISS3_cast = _itkMaximumImageFilterPython.itkMaximumImageFilterISS3ISS3ISS3_cast

class itkMaximumImageFilterIUC2IUC2IUC2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUC2IUC2IUC2):
    r"""Proxy of C++ itkMaximumImageFilterIUC2IUC2IUC2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMaximumImageFilterPython.itkMaximumImageFilterIUC2IUC2IUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkMaximumImageFilterPython.itkMaximumImageFilterIUC2IUC2IUC2_Clone)
    Input1ConvertibleToOutputCheck = _itkMaximumImageFilterPython.itkMaximumImageFilterIUC2IUC2IUC2_Input1ConvertibleToOutputCheck
    
    Input2ConvertibleToOutputCheck = _itkMaximumImageFilterPython.itkMaximumImageFilterIUC2IUC2IUC2_Input2ConvertibleToOutputCheck
    
    Input1GreaterThanInput2Check = _itkMaximumImageFilterPython.itkMaximumImageFilterIUC2IUC2IUC2_Input1GreaterThanInput2Check
    
    __swig_destroy__ = _itkMaximumImageFilterPython.delete_itkMaximumImageFilterIUC2IUC2IUC2
    cast = _swig_new_static_method(_itkMaximumImageFilterPython.itkMaximumImageFilterIUC2IUC2IUC2_cast)

    def New(*args, **kargs):
        """New() -> itkMaximumImageFilterIUC2IUC2IUC2

        Create a new object of the class itkMaximumImageFilterIUC2IUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMaximumImageFilterIUC2IUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMaximumImageFilterIUC2IUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMaximumImageFilterIUC2IUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMaximumImageFilterIUC2IUC2IUC2 in _itkMaximumImageFilterPython:
_itkMaximumImageFilterPython.itkMaximumImageFilterIUC2IUC2IUC2_swigregister(itkMaximumImageFilterIUC2IUC2IUC2)
itkMaximumImageFilterIUC2IUC2IUC2___New_orig__ = _itkMaximumImageFilterPython.itkMaximumImageFilterIUC2IUC2IUC2___New_orig__
itkMaximumImageFilterIUC2IUC2IUC2_cast = _itkMaximumImageFilterPython.itkMaximumImageFilterIUC2IUC2IUC2_cast

class itkMaximumImageFilterIUC3IUC3IUC3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUC3IUC3IUC3):
    r"""Proxy of C++ itkMaximumImageFilterIUC3IUC3IUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMaximumImageFilterPython.itkMaximumImageFilterIUC3IUC3IUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkMaximumImageFilterPython.itkMaximumImageFilterIUC3IUC3IUC3_Clone)
    Input1ConvertibleToOutputCheck = _itkMaximumImageFilterPython.itkMaximumImageFilterIUC3IUC3IUC3_Input1ConvertibleToOutputCheck
    
    Input2ConvertibleToOutputCheck = _itkMaximumImageFilterPython.itkMaximumImageFilterIUC3IUC3IUC3_Input2ConvertibleToOutputCheck
    
    Input1GreaterThanInput2Check = _itkMaximumImageFilterPython.itkMaximumImageFilterIUC3IUC3IUC3_Input1GreaterThanInput2Check
    
    __swig_destroy__ = _itkMaximumImageFilterPython.delete_itkMaximumImageFilterIUC3IUC3IUC3
    cast = _swig_new_static_method(_itkMaximumImageFilterPython.itkMaximumImageFilterIUC3IUC3IUC3_cast)

    def New(*args, **kargs):
        """New() -> itkMaximumImageFilterIUC3IUC3IUC3

        Create a new object of the class itkMaximumImageFilterIUC3IUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMaximumImageFilterIUC3IUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMaximumImageFilterIUC3IUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMaximumImageFilterIUC3IUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMaximumImageFilterIUC3IUC3IUC3 in _itkMaximumImageFilterPython:
_itkMaximumImageFilterPython.itkMaximumImageFilterIUC3IUC3IUC3_swigregister(itkMaximumImageFilterIUC3IUC3IUC3)
itkMaximumImageFilterIUC3IUC3IUC3___New_orig__ = _itkMaximumImageFilterPython.itkMaximumImageFilterIUC3IUC3IUC3___New_orig__
itkMaximumImageFilterIUC3IUC3IUC3_cast = _itkMaximumImageFilterPython.itkMaximumImageFilterIUC3IUC3IUC3_cast

class itkMaximumImageFilterIUS2IUS2IUS2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUS2IUS2IUS2):
    r"""Proxy of C++ itkMaximumImageFilterIUS2IUS2IUS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMaximumImageFilterPython.itkMaximumImageFilterIUS2IUS2IUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkMaximumImageFilterPython.itkMaximumImageFilterIUS2IUS2IUS2_Clone)
    Input1ConvertibleToOutputCheck = _itkMaximumImageFilterPython.itkMaximumImageFilterIUS2IUS2IUS2_Input1ConvertibleToOutputCheck
    
    Input2ConvertibleToOutputCheck = _itkMaximumImageFilterPython.itkMaximumImageFilterIUS2IUS2IUS2_Input2ConvertibleToOutputCheck
    
    Input1GreaterThanInput2Check = _itkMaximumImageFilterPython.itkMaximumImageFilterIUS2IUS2IUS2_Input1GreaterThanInput2Check
    
    __swig_destroy__ = _itkMaximumImageFilterPython.delete_itkMaximumImageFilterIUS2IUS2IUS2
    cast = _swig_new_static_method(_itkMaximumImageFilterPython.itkMaximumImageFilterIUS2IUS2IUS2_cast)

    def New(*args, **kargs):
        """New() -> itkMaximumImageFilterIUS2IUS2IUS2

        Create a new object of the class itkMaximumImageFilterIUS2IUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMaximumImageFilterIUS2IUS2IUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMaximumImageFilterIUS2IUS2IUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMaximumImageFilterIUS2IUS2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMaximumImageFilterIUS2IUS2IUS2 in _itkMaximumImageFilterPython:
_itkMaximumImageFilterPython.itkMaximumImageFilterIUS2IUS2IUS2_swigregister(itkMaximumImageFilterIUS2IUS2IUS2)
itkMaximumImageFilterIUS2IUS2IUS2___New_orig__ = _itkMaximumImageFilterPython.itkMaximumImageFilterIUS2IUS2IUS2___New_orig__
itkMaximumImageFilterIUS2IUS2IUS2_cast = _itkMaximumImageFilterPython.itkMaximumImageFilterIUS2IUS2IUS2_cast

class itkMaximumImageFilterIUS3IUS3IUS3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUS3IUS3IUS3):
    r"""Proxy of C++ itkMaximumImageFilterIUS3IUS3IUS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMaximumImageFilterPython.itkMaximumImageFilterIUS3IUS3IUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkMaximumImageFilterPython.itkMaximumImageFilterIUS3IUS3IUS3_Clone)
    Input1ConvertibleToOutputCheck = _itkMaximumImageFilterPython.itkMaximumImageFilterIUS3IUS3IUS3_Input1ConvertibleToOutputCheck
    
    Input2ConvertibleToOutputCheck = _itkMaximumImageFilterPython.itkMaximumImageFilterIUS3IUS3IUS3_Input2ConvertibleToOutputCheck
    
    Input1GreaterThanInput2Check = _itkMaximumImageFilterPython.itkMaximumImageFilterIUS3IUS3IUS3_Input1GreaterThanInput2Check
    
    __swig_destroy__ = _itkMaximumImageFilterPython.delete_itkMaximumImageFilterIUS3IUS3IUS3
    cast = _swig_new_static_method(_itkMaximumImageFilterPython.itkMaximumImageFilterIUS3IUS3IUS3_cast)

    def New(*args, **kargs):
        """New() -> itkMaximumImageFilterIUS3IUS3IUS3

        Create a new object of the class itkMaximumImageFilterIUS3IUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMaximumImageFilterIUS3IUS3IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMaximumImageFilterIUS3IUS3IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMaximumImageFilterIUS3IUS3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMaximumImageFilterIUS3IUS3IUS3 in _itkMaximumImageFilterPython:
_itkMaximumImageFilterPython.itkMaximumImageFilterIUS3IUS3IUS3_swigregister(itkMaximumImageFilterIUS3IUS3IUS3)
itkMaximumImageFilterIUS3IUS3IUS3___New_orig__ = _itkMaximumImageFilterPython.itkMaximumImageFilterIUS3IUS3IUS3___New_orig__
itkMaximumImageFilterIUS3IUS3IUS3_cast = _itkMaximumImageFilterPython.itkMaximumImageFilterIUS3IUS3IUS3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def maximum_image_filter(*args, **kwargs):
    """Procedural interface for MaximumImageFilter"""
    import itk
    instance = itk.MaximumImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def maximum_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.MaximumImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.MaximumImageFilter.values()[0]
    else:
        filter_object = itk.MaximumImageFilter

    maximum_image_filter.__doc__ = filter_object.__doc__
    maximum_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    maximum_image_filter.__doc__ += "Available Keyword Arguments:\n"
    maximum_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



