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
    from . import _itkMinimumImageFilterPython
else:
    import _itkMinimumImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkMinimumImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkMinimumImageFilterPython.SWIG_PyStaticMethod_New

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
import itkCovariantVectorPython
import itkVectorPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkFixedArrayPython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkInPlaceImageFilterBPython
import itkImageToImageFilterBPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImagePython
import itkOffsetPython
import itkSizePython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkSymmetricSecondRankTensorPython
import itkImageRegionPython
import itkIndexPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkSimpleDataObjectDecoratorPython
import itkArrayPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterAPython

def itkMinimumImageFilterID3ID3ID3_New():
  return itkMinimumImageFilterID3ID3ID3.New()


def itkMinimumImageFilterID2ID2ID2_New():
  return itkMinimumImageFilterID2ID2ID2.New()


def itkMinimumImageFilterIF3IF3IF3_New():
  return itkMinimumImageFilterIF3IF3IF3.New()


def itkMinimumImageFilterIF2IF2IF2_New():
  return itkMinimumImageFilterIF2IF2IF2.New()


def itkMinimumImageFilterIUS3IUS3IUS3_New():
  return itkMinimumImageFilterIUS3IUS3IUS3.New()


def itkMinimumImageFilterIUS2IUS2IUS2_New():
  return itkMinimumImageFilterIUS2IUS2IUS2.New()


def itkMinimumImageFilterIUC3IUC3IUC3_New():
  return itkMinimumImageFilterIUC3IUC3IUC3.New()


def itkMinimumImageFilterIUC2IUC2IUC2_New():
  return itkMinimumImageFilterIUC2IUC2IUC2.New()


def itkMinimumImageFilterISS3ISS3ISS3_New():
  return itkMinimumImageFilterISS3ISS3ISS3.New()


def itkMinimumImageFilterISS2ISS2ISS2_New():
  return itkMinimumImageFilterISS2ISS2ISS2.New()

class itkMinimumImageFilterID2ID2ID2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterID2ID2ID2):
    r"""Proxy of C++ itkMinimumImageFilterID2ID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMinimumImageFilterPython.itkMinimumImageFilterID2ID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkMinimumImageFilterPython.itkMinimumImageFilterID2ID2ID2_Clone)
    Input1ConvertibleToInput2Check = _itkMinimumImageFilterPython.itkMinimumImageFilterID2ID2ID2_Input1ConvertibleToInput2Check
    
    Input2ConvertibleToOutputCheck = _itkMinimumImageFilterPython.itkMinimumImageFilterID2ID2ID2_Input2ConvertibleToOutputCheck
    
    Input1LessThanInput2Check = _itkMinimumImageFilterPython.itkMinimumImageFilterID2ID2ID2_Input1LessThanInput2Check
    
    __swig_destroy__ = _itkMinimumImageFilterPython.delete_itkMinimumImageFilterID2ID2ID2
    cast = _swig_new_static_method(_itkMinimumImageFilterPython.itkMinimumImageFilterID2ID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkMinimumImageFilterID2ID2ID2

        Create a new object of the class itkMinimumImageFilterID2ID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMinimumImageFilterID2ID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMinimumImageFilterID2ID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMinimumImageFilterID2ID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMinimumImageFilterID2ID2ID2 in _itkMinimumImageFilterPython:
_itkMinimumImageFilterPython.itkMinimumImageFilterID2ID2ID2_swigregister(itkMinimumImageFilterID2ID2ID2)
itkMinimumImageFilterID2ID2ID2___New_orig__ = _itkMinimumImageFilterPython.itkMinimumImageFilterID2ID2ID2___New_orig__
itkMinimumImageFilterID2ID2ID2_cast = _itkMinimumImageFilterPython.itkMinimumImageFilterID2ID2ID2_cast

class itkMinimumImageFilterID3ID3ID3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterID3ID3ID3):
    r"""Proxy of C++ itkMinimumImageFilterID3ID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMinimumImageFilterPython.itkMinimumImageFilterID3ID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkMinimumImageFilterPython.itkMinimumImageFilterID3ID3ID3_Clone)
    Input1ConvertibleToInput2Check = _itkMinimumImageFilterPython.itkMinimumImageFilterID3ID3ID3_Input1ConvertibleToInput2Check
    
    Input2ConvertibleToOutputCheck = _itkMinimumImageFilterPython.itkMinimumImageFilterID3ID3ID3_Input2ConvertibleToOutputCheck
    
    Input1LessThanInput2Check = _itkMinimumImageFilterPython.itkMinimumImageFilterID3ID3ID3_Input1LessThanInput2Check
    
    __swig_destroy__ = _itkMinimumImageFilterPython.delete_itkMinimumImageFilterID3ID3ID3
    cast = _swig_new_static_method(_itkMinimumImageFilterPython.itkMinimumImageFilterID3ID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkMinimumImageFilterID3ID3ID3

        Create a new object of the class itkMinimumImageFilterID3ID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMinimumImageFilterID3ID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMinimumImageFilterID3ID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMinimumImageFilterID3ID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMinimumImageFilterID3ID3ID3 in _itkMinimumImageFilterPython:
_itkMinimumImageFilterPython.itkMinimumImageFilterID3ID3ID3_swigregister(itkMinimumImageFilterID3ID3ID3)
itkMinimumImageFilterID3ID3ID3___New_orig__ = _itkMinimumImageFilterPython.itkMinimumImageFilterID3ID3ID3___New_orig__
itkMinimumImageFilterID3ID3ID3_cast = _itkMinimumImageFilterPython.itkMinimumImageFilterID3ID3ID3_cast

class itkMinimumImageFilterIF2IF2IF2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIF2IF2IF2):
    r"""Proxy of C++ itkMinimumImageFilterIF2IF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMinimumImageFilterPython.itkMinimumImageFilterIF2IF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkMinimumImageFilterPython.itkMinimumImageFilterIF2IF2IF2_Clone)
    Input1ConvertibleToInput2Check = _itkMinimumImageFilterPython.itkMinimumImageFilterIF2IF2IF2_Input1ConvertibleToInput2Check
    
    Input2ConvertibleToOutputCheck = _itkMinimumImageFilterPython.itkMinimumImageFilterIF2IF2IF2_Input2ConvertibleToOutputCheck
    
    Input1LessThanInput2Check = _itkMinimumImageFilterPython.itkMinimumImageFilterIF2IF2IF2_Input1LessThanInput2Check
    
    __swig_destroy__ = _itkMinimumImageFilterPython.delete_itkMinimumImageFilterIF2IF2IF2
    cast = _swig_new_static_method(_itkMinimumImageFilterPython.itkMinimumImageFilterIF2IF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkMinimumImageFilterIF2IF2IF2

        Create a new object of the class itkMinimumImageFilterIF2IF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMinimumImageFilterIF2IF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMinimumImageFilterIF2IF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMinimumImageFilterIF2IF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMinimumImageFilterIF2IF2IF2 in _itkMinimumImageFilterPython:
_itkMinimumImageFilterPython.itkMinimumImageFilterIF2IF2IF2_swigregister(itkMinimumImageFilterIF2IF2IF2)
itkMinimumImageFilterIF2IF2IF2___New_orig__ = _itkMinimumImageFilterPython.itkMinimumImageFilterIF2IF2IF2___New_orig__
itkMinimumImageFilterIF2IF2IF2_cast = _itkMinimumImageFilterPython.itkMinimumImageFilterIF2IF2IF2_cast

class itkMinimumImageFilterIF3IF3IF3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIF3IF3IF3):
    r"""Proxy of C++ itkMinimumImageFilterIF3IF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMinimumImageFilterPython.itkMinimumImageFilterIF3IF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkMinimumImageFilterPython.itkMinimumImageFilterIF3IF3IF3_Clone)
    Input1ConvertibleToInput2Check = _itkMinimumImageFilterPython.itkMinimumImageFilterIF3IF3IF3_Input1ConvertibleToInput2Check
    
    Input2ConvertibleToOutputCheck = _itkMinimumImageFilterPython.itkMinimumImageFilterIF3IF3IF3_Input2ConvertibleToOutputCheck
    
    Input1LessThanInput2Check = _itkMinimumImageFilterPython.itkMinimumImageFilterIF3IF3IF3_Input1LessThanInput2Check
    
    __swig_destroy__ = _itkMinimumImageFilterPython.delete_itkMinimumImageFilterIF3IF3IF3
    cast = _swig_new_static_method(_itkMinimumImageFilterPython.itkMinimumImageFilterIF3IF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkMinimumImageFilterIF3IF3IF3

        Create a new object of the class itkMinimumImageFilterIF3IF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMinimumImageFilterIF3IF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMinimumImageFilterIF3IF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMinimumImageFilterIF3IF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMinimumImageFilterIF3IF3IF3 in _itkMinimumImageFilterPython:
_itkMinimumImageFilterPython.itkMinimumImageFilterIF3IF3IF3_swigregister(itkMinimumImageFilterIF3IF3IF3)
itkMinimumImageFilterIF3IF3IF3___New_orig__ = _itkMinimumImageFilterPython.itkMinimumImageFilterIF3IF3IF3___New_orig__
itkMinimumImageFilterIF3IF3IF3_cast = _itkMinimumImageFilterPython.itkMinimumImageFilterIF3IF3IF3_cast

class itkMinimumImageFilterISS2ISS2ISS2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterISS2ISS2ISS2):
    r"""Proxy of C++ itkMinimumImageFilterISS2ISS2ISS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMinimumImageFilterPython.itkMinimumImageFilterISS2ISS2ISS2___New_orig__)
    Clone = _swig_new_instance_method(_itkMinimumImageFilterPython.itkMinimumImageFilterISS2ISS2ISS2_Clone)
    Input1ConvertibleToInput2Check = _itkMinimumImageFilterPython.itkMinimumImageFilterISS2ISS2ISS2_Input1ConvertibleToInput2Check
    
    Input2ConvertibleToOutputCheck = _itkMinimumImageFilterPython.itkMinimumImageFilterISS2ISS2ISS2_Input2ConvertibleToOutputCheck
    
    Input1LessThanInput2Check = _itkMinimumImageFilterPython.itkMinimumImageFilterISS2ISS2ISS2_Input1LessThanInput2Check
    
    __swig_destroy__ = _itkMinimumImageFilterPython.delete_itkMinimumImageFilterISS2ISS2ISS2
    cast = _swig_new_static_method(_itkMinimumImageFilterPython.itkMinimumImageFilterISS2ISS2ISS2_cast)

    def New(*args, **kargs):
        """New() -> itkMinimumImageFilterISS2ISS2ISS2

        Create a new object of the class itkMinimumImageFilterISS2ISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMinimumImageFilterISS2ISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMinimumImageFilterISS2ISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMinimumImageFilterISS2ISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMinimumImageFilterISS2ISS2ISS2 in _itkMinimumImageFilterPython:
_itkMinimumImageFilterPython.itkMinimumImageFilterISS2ISS2ISS2_swigregister(itkMinimumImageFilterISS2ISS2ISS2)
itkMinimumImageFilterISS2ISS2ISS2___New_orig__ = _itkMinimumImageFilterPython.itkMinimumImageFilterISS2ISS2ISS2___New_orig__
itkMinimumImageFilterISS2ISS2ISS2_cast = _itkMinimumImageFilterPython.itkMinimumImageFilterISS2ISS2ISS2_cast

class itkMinimumImageFilterISS3ISS3ISS3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterISS3ISS3ISS3):
    r"""Proxy of C++ itkMinimumImageFilterISS3ISS3ISS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMinimumImageFilterPython.itkMinimumImageFilterISS3ISS3ISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkMinimumImageFilterPython.itkMinimumImageFilterISS3ISS3ISS3_Clone)
    Input1ConvertibleToInput2Check = _itkMinimumImageFilterPython.itkMinimumImageFilterISS3ISS3ISS3_Input1ConvertibleToInput2Check
    
    Input2ConvertibleToOutputCheck = _itkMinimumImageFilterPython.itkMinimumImageFilterISS3ISS3ISS3_Input2ConvertibleToOutputCheck
    
    Input1LessThanInput2Check = _itkMinimumImageFilterPython.itkMinimumImageFilterISS3ISS3ISS3_Input1LessThanInput2Check
    
    __swig_destroy__ = _itkMinimumImageFilterPython.delete_itkMinimumImageFilterISS3ISS3ISS3
    cast = _swig_new_static_method(_itkMinimumImageFilterPython.itkMinimumImageFilterISS3ISS3ISS3_cast)

    def New(*args, **kargs):
        """New() -> itkMinimumImageFilterISS3ISS3ISS3

        Create a new object of the class itkMinimumImageFilterISS3ISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMinimumImageFilterISS3ISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMinimumImageFilterISS3ISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMinimumImageFilterISS3ISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMinimumImageFilterISS3ISS3ISS3 in _itkMinimumImageFilterPython:
_itkMinimumImageFilterPython.itkMinimumImageFilterISS3ISS3ISS3_swigregister(itkMinimumImageFilterISS3ISS3ISS3)
itkMinimumImageFilterISS3ISS3ISS3___New_orig__ = _itkMinimumImageFilterPython.itkMinimumImageFilterISS3ISS3ISS3___New_orig__
itkMinimumImageFilterISS3ISS3ISS3_cast = _itkMinimumImageFilterPython.itkMinimumImageFilterISS3ISS3ISS3_cast

class itkMinimumImageFilterIUC2IUC2IUC2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUC2IUC2IUC2):
    r"""Proxy of C++ itkMinimumImageFilterIUC2IUC2IUC2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMinimumImageFilterPython.itkMinimumImageFilterIUC2IUC2IUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkMinimumImageFilterPython.itkMinimumImageFilterIUC2IUC2IUC2_Clone)
    Input1ConvertibleToInput2Check = _itkMinimumImageFilterPython.itkMinimumImageFilterIUC2IUC2IUC2_Input1ConvertibleToInput2Check
    
    Input2ConvertibleToOutputCheck = _itkMinimumImageFilterPython.itkMinimumImageFilterIUC2IUC2IUC2_Input2ConvertibleToOutputCheck
    
    Input1LessThanInput2Check = _itkMinimumImageFilterPython.itkMinimumImageFilterIUC2IUC2IUC2_Input1LessThanInput2Check
    
    __swig_destroy__ = _itkMinimumImageFilterPython.delete_itkMinimumImageFilterIUC2IUC2IUC2
    cast = _swig_new_static_method(_itkMinimumImageFilterPython.itkMinimumImageFilterIUC2IUC2IUC2_cast)

    def New(*args, **kargs):
        """New() -> itkMinimumImageFilterIUC2IUC2IUC2

        Create a new object of the class itkMinimumImageFilterIUC2IUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMinimumImageFilterIUC2IUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMinimumImageFilterIUC2IUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMinimumImageFilterIUC2IUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMinimumImageFilterIUC2IUC2IUC2 in _itkMinimumImageFilterPython:
_itkMinimumImageFilterPython.itkMinimumImageFilterIUC2IUC2IUC2_swigregister(itkMinimumImageFilterIUC2IUC2IUC2)
itkMinimumImageFilterIUC2IUC2IUC2___New_orig__ = _itkMinimumImageFilterPython.itkMinimumImageFilterIUC2IUC2IUC2___New_orig__
itkMinimumImageFilterIUC2IUC2IUC2_cast = _itkMinimumImageFilterPython.itkMinimumImageFilterIUC2IUC2IUC2_cast

class itkMinimumImageFilterIUC3IUC3IUC3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUC3IUC3IUC3):
    r"""Proxy of C++ itkMinimumImageFilterIUC3IUC3IUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMinimumImageFilterPython.itkMinimumImageFilterIUC3IUC3IUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkMinimumImageFilterPython.itkMinimumImageFilterIUC3IUC3IUC3_Clone)
    Input1ConvertibleToInput2Check = _itkMinimumImageFilterPython.itkMinimumImageFilterIUC3IUC3IUC3_Input1ConvertibleToInput2Check
    
    Input2ConvertibleToOutputCheck = _itkMinimumImageFilterPython.itkMinimumImageFilterIUC3IUC3IUC3_Input2ConvertibleToOutputCheck
    
    Input1LessThanInput2Check = _itkMinimumImageFilterPython.itkMinimumImageFilterIUC3IUC3IUC3_Input1LessThanInput2Check
    
    __swig_destroy__ = _itkMinimumImageFilterPython.delete_itkMinimumImageFilterIUC3IUC3IUC3
    cast = _swig_new_static_method(_itkMinimumImageFilterPython.itkMinimumImageFilterIUC3IUC3IUC3_cast)

    def New(*args, **kargs):
        """New() -> itkMinimumImageFilterIUC3IUC3IUC3

        Create a new object of the class itkMinimumImageFilterIUC3IUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMinimumImageFilterIUC3IUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMinimumImageFilterIUC3IUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMinimumImageFilterIUC3IUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMinimumImageFilterIUC3IUC3IUC3 in _itkMinimumImageFilterPython:
_itkMinimumImageFilterPython.itkMinimumImageFilterIUC3IUC3IUC3_swigregister(itkMinimumImageFilterIUC3IUC3IUC3)
itkMinimumImageFilterIUC3IUC3IUC3___New_orig__ = _itkMinimumImageFilterPython.itkMinimumImageFilterIUC3IUC3IUC3___New_orig__
itkMinimumImageFilterIUC3IUC3IUC3_cast = _itkMinimumImageFilterPython.itkMinimumImageFilterIUC3IUC3IUC3_cast

class itkMinimumImageFilterIUS2IUS2IUS2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUS2IUS2IUS2):
    r"""Proxy of C++ itkMinimumImageFilterIUS2IUS2IUS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMinimumImageFilterPython.itkMinimumImageFilterIUS2IUS2IUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkMinimumImageFilterPython.itkMinimumImageFilterIUS2IUS2IUS2_Clone)
    Input1ConvertibleToInput2Check = _itkMinimumImageFilterPython.itkMinimumImageFilterIUS2IUS2IUS2_Input1ConvertibleToInput2Check
    
    Input2ConvertibleToOutputCheck = _itkMinimumImageFilterPython.itkMinimumImageFilterIUS2IUS2IUS2_Input2ConvertibleToOutputCheck
    
    Input1LessThanInput2Check = _itkMinimumImageFilterPython.itkMinimumImageFilterIUS2IUS2IUS2_Input1LessThanInput2Check
    
    __swig_destroy__ = _itkMinimumImageFilterPython.delete_itkMinimumImageFilterIUS2IUS2IUS2
    cast = _swig_new_static_method(_itkMinimumImageFilterPython.itkMinimumImageFilterIUS2IUS2IUS2_cast)

    def New(*args, **kargs):
        """New() -> itkMinimumImageFilterIUS2IUS2IUS2

        Create a new object of the class itkMinimumImageFilterIUS2IUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMinimumImageFilterIUS2IUS2IUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMinimumImageFilterIUS2IUS2IUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMinimumImageFilterIUS2IUS2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMinimumImageFilterIUS2IUS2IUS2 in _itkMinimumImageFilterPython:
_itkMinimumImageFilterPython.itkMinimumImageFilterIUS2IUS2IUS2_swigregister(itkMinimumImageFilterIUS2IUS2IUS2)
itkMinimumImageFilterIUS2IUS2IUS2___New_orig__ = _itkMinimumImageFilterPython.itkMinimumImageFilterIUS2IUS2IUS2___New_orig__
itkMinimumImageFilterIUS2IUS2IUS2_cast = _itkMinimumImageFilterPython.itkMinimumImageFilterIUS2IUS2IUS2_cast

class itkMinimumImageFilterIUS3IUS3IUS3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUS3IUS3IUS3):
    r"""Proxy of C++ itkMinimumImageFilterIUS3IUS3IUS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkMinimumImageFilterPython.itkMinimumImageFilterIUS3IUS3IUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkMinimumImageFilterPython.itkMinimumImageFilterIUS3IUS3IUS3_Clone)
    Input1ConvertibleToInput2Check = _itkMinimumImageFilterPython.itkMinimumImageFilterIUS3IUS3IUS3_Input1ConvertibleToInput2Check
    
    Input2ConvertibleToOutputCheck = _itkMinimumImageFilterPython.itkMinimumImageFilterIUS3IUS3IUS3_Input2ConvertibleToOutputCheck
    
    Input1LessThanInput2Check = _itkMinimumImageFilterPython.itkMinimumImageFilterIUS3IUS3IUS3_Input1LessThanInput2Check
    
    __swig_destroy__ = _itkMinimumImageFilterPython.delete_itkMinimumImageFilterIUS3IUS3IUS3
    cast = _swig_new_static_method(_itkMinimumImageFilterPython.itkMinimumImageFilterIUS3IUS3IUS3_cast)

    def New(*args, **kargs):
        """New() -> itkMinimumImageFilterIUS3IUS3IUS3

        Create a new object of the class itkMinimumImageFilterIUS3IUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMinimumImageFilterIUS3IUS3IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMinimumImageFilterIUS3IUS3IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMinimumImageFilterIUS3IUS3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkMinimumImageFilterIUS3IUS3IUS3 in _itkMinimumImageFilterPython:
_itkMinimumImageFilterPython.itkMinimumImageFilterIUS3IUS3IUS3_swigregister(itkMinimumImageFilterIUS3IUS3IUS3)
itkMinimumImageFilterIUS3IUS3IUS3___New_orig__ = _itkMinimumImageFilterPython.itkMinimumImageFilterIUS3IUS3IUS3___New_orig__
itkMinimumImageFilterIUS3IUS3IUS3_cast = _itkMinimumImageFilterPython.itkMinimumImageFilterIUS3IUS3IUS3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def minimum_image_filter(*args, **kwargs):
    """Procedural interface for MinimumImageFilter"""
    import itk
    instance = itk.MinimumImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def minimum_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.MinimumImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.MinimumImageFilter.values()[0]
    else:
        filter_object = itk.MinimumImageFilter

    minimum_image_filter.__doc__ = filter_object.__doc__
    minimum_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    minimum_image_filter.__doc__ += "Available Keyword Arguments:\n"
    minimum_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



