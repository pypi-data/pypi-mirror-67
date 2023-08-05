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
    from . import _itkAddImageFilterPython
else:
    import _itkAddImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkAddImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkAddImageFilterPython.SWIG_PyStaticMethod_New

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


import itkBinaryGeneratorImageFilterPython
import itkRGBPixelPython
import itkFixedArrayPython
import pyBasePython
import itkRGBAPixelPython
import itkImagePython
import itkVectorPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkSizePython
import ITKCommonBasePython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import itkCovariantVectorPython
import itkPointPython
import vnl_matrix_fixedPython
import itkIndexPython
import itkOffsetPython
import itkImageRegionPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterBPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterAPython
import itkSimpleDataObjectDecoratorPython
import itkArrayPython
import itkInPlaceImageFilterBPython

def itkAddImageFilterID3ID3ID3_New():
  return itkAddImageFilterID3ID3ID3.New()


def itkAddImageFilterID2ID2ID2_New():
  return itkAddImageFilterID2ID2ID2.New()


def itkAddImageFilterIF3IF3IF3_New():
  return itkAddImageFilterIF3IF3IF3.New()


def itkAddImageFilterIF2IF2IF2_New():
  return itkAddImageFilterIF2IF2IF2.New()


def itkAddImageFilterIUS3IUS3IUS3_New():
  return itkAddImageFilterIUS3IUS3IUS3.New()


def itkAddImageFilterIUS2IUS2IUS2_New():
  return itkAddImageFilterIUS2IUS2IUS2.New()


def itkAddImageFilterIUC3IUC3IUC3_New():
  return itkAddImageFilterIUC3IUC3IUC3.New()


def itkAddImageFilterIUC2IUC2IUC2_New():
  return itkAddImageFilterIUC2IUC2IUC2.New()


def itkAddImageFilterISS3ISS3ISS3_New():
  return itkAddImageFilterISS3ISS3ISS3.New()


def itkAddImageFilterISS2ISS2ISS2_New():
  return itkAddImageFilterISS2ISS2ISS2.New()

class itkAddImageFilterID2ID2ID2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterID2ID2ID2):
    r"""Proxy of C++ itkAddImageFilterID2ID2ID2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAddImageFilterPython.itkAddImageFilterID2ID2ID2___New_orig__)
    Clone = _swig_new_instance_method(_itkAddImageFilterPython.itkAddImageFilterID2ID2ID2_Clone)
    Input1Input2OutputAdditiveOperatorsCheck = _itkAddImageFilterPython.itkAddImageFilterID2ID2ID2_Input1Input2OutputAdditiveOperatorsCheck
    
    __swig_destroy__ = _itkAddImageFilterPython.delete_itkAddImageFilterID2ID2ID2
    cast = _swig_new_static_method(_itkAddImageFilterPython.itkAddImageFilterID2ID2ID2_cast)

    def New(*args, **kargs):
        """New() -> itkAddImageFilterID2ID2ID2

        Create a new object of the class itkAddImageFilterID2ID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAddImageFilterID2ID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAddImageFilterID2ID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAddImageFilterID2ID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAddImageFilterID2ID2ID2 in _itkAddImageFilterPython:
_itkAddImageFilterPython.itkAddImageFilterID2ID2ID2_swigregister(itkAddImageFilterID2ID2ID2)
itkAddImageFilterID2ID2ID2___New_orig__ = _itkAddImageFilterPython.itkAddImageFilterID2ID2ID2___New_orig__
itkAddImageFilterID2ID2ID2_cast = _itkAddImageFilterPython.itkAddImageFilterID2ID2ID2_cast

class itkAddImageFilterID3ID3ID3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterID3ID3ID3):
    r"""Proxy of C++ itkAddImageFilterID3ID3ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAddImageFilterPython.itkAddImageFilterID3ID3ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkAddImageFilterPython.itkAddImageFilterID3ID3ID3_Clone)
    Input1Input2OutputAdditiveOperatorsCheck = _itkAddImageFilterPython.itkAddImageFilterID3ID3ID3_Input1Input2OutputAdditiveOperatorsCheck
    
    __swig_destroy__ = _itkAddImageFilterPython.delete_itkAddImageFilterID3ID3ID3
    cast = _swig_new_static_method(_itkAddImageFilterPython.itkAddImageFilterID3ID3ID3_cast)

    def New(*args, **kargs):
        """New() -> itkAddImageFilterID3ID3ID3

        Create a new object of the class itkAddImageFilterID3ID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAddImageFilterID3ID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAddImageFilterID3ID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAddImageFilterID3ID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAddImageFilterID3ID3ID3 in _itkAddImageFilterPython:
_itkAddImageFilterPython.itkAddImageFilterID3ID3ID3_swigregister(itkAddImageFilterID3ID3ID3)
itkAddImageFilterID3ID3ID3___New_orig__ = _itkAddImageFilterPython.itkAddImageFilterID3ID3ID3___New_orig__
itkAddImageFilterID3ID3ID3_cast = _itkAddImageFilterPython.itkAddImageFilterID3ID3ID3_cast

class itkAddImageFilterIF2IF2IF2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIF2IF2IF2):
    r"""Proxy of C++ itkAddImageFilterIF2IF2IF2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAddImageFilterPython.itkAddImageFilterIF2IF2IF2___New_orig__)
    Clone = _swig_new_instance_method(_itkAddImageFilterPython.itkAddImageFilterIF2IF2IF2_Clone)
    Input1Input2OutputAdditiveOperatorsCheck = _itkAddImageFilterPython.itkAddImageFilterIF2IF2IF2_Input1Input2OutputAdditiveOperatorsCheck
    
    __swig_destroy__ = _itkAddImageFilterPython.delete_itkAddImageFilterIF2IF2IF2
    cast = _swig_new_static_method(_itkAddImageFilterPython.itkAddImageFilterIF2IF2IF2_cast)

    def New(*args, **kargs):
        """New() -> itkAddImageFilterIF2IF2IF2

        Create a new object of the class itkAddImageFilterIF2IF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAddImageFilterIF2IF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAddImageFilterIF2IF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAddImageFilterIF2IF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAddImageFilterIF2IF2IF2 in _itkAddImageFilterPython:
_itkAddImageFilterPython.itkAddImageFilterIF2IF2IF2_swigregister(itkAddImageFilterIF2IF2IF2)
itkAddImageFilterIF2IF2IF2___New_orig__ = _itkAddImageFilterPython.itkAddImageFilterIF2IF2IF2___New_orig__
itkAddImageFilterIF2IF2IF2_cast = _itkAddImageFilterPython.itkAddImageFilterIF2IF2IF2_cast

class itkAddImageFilterIF3IF3IF3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIF3IF3IF3):
    r"""Proxy of C++ itkAddImageFilterIF3IF3IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAddImageFilterPython.itkAddImageFilterIF3IF3IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkAddImageFilterPython.itkAddImageFilterIF3IF3IF3_Clone)
    Input1Input2OutputAdditiveOperatorsCheck = _itkAddImageFilterPython.itkAddImageFilterIF3IF3IF3_Input1Input2OutputAdditiveOperatorsCheck
    
    __swig_destroy__ = _itkAddImageFilterPython.delete_itkAddImageFilterIF3IF3IF3
    cast = _swig_new_static_method(_itkAddImageFilterPython.itkAddImageFilterIF3IF3IF3_cast)

    def New(*args, **kargs):
        """New() -> itkAddImageFilterIF3IF3IF3

        Create a new object of the class itkAddImageFilterIF3IF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAddImageFilterIF3IF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAddImageFilterIF3IF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAddImageFilterIF3IF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAddImageFilterIF3IF3IF3 in _itkAddImageFilterPython:
_itkAddImageFilterPython.itkAddImageFilterIF3IF3IF3_swigregister(itkAddImageFilterIF3IF3IF3)
itkAddImageFilterIF3IF3IF3___New_orig__ = _itkAddImageFilterPython.itkAddImageFilterIF3IF3IF3___New_orig__
itkAddImageFilterIF3IF3IF3_cast = _itkAddImageFilterPython.itkAddImageFilterIF3IF3IF3_cast

class itkAddImageFilterISS2ISS2ISS2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterISS2ISS2ISS2):
    r"""Proxy of C++ itkAddImageFilterISS2ISS2ISS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAddImageFilterPython.itkAddImageFilterISS2ISS2ISS2___New_orig__)
    Clone = _swig_new_instance_method(_itkAddImageFilterPython.itkAddImageFilterISS2ISS2ISS2_Clone)
    Input1Input2OutputAdditiveOperatorsCheck = _itkAddImageFilterPython.itkAddImageFilterISS2ISS2ISS2_Input1Input2OutputAdditiveOperatorsCheck
    
    __swig_destroy__ = _itkAddImageFilterPython.delete_itkAddImageFilterISS2ISS2ISS2
    cast = _swig_new_static_method(_itkAddImageFilterPython.itkAddImageFilterISS2ISS2ISS2_cast)

    def New(*args, **kargs):
        """New() -> itkAddImageFilterISS2ISS2ISS2

        Create a new object of the class itkAddImageFilterISS2ISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAddImageFilterISS2ISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAddImageFilterISS2ISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAddImageFilterISS2ISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAddImageFilterISS2ISS2ISS2 in _itkAddImageFilterPython:
_itkAddImageFilterPython.itkAddImageFilterISS2ISS2ISS2_swigregister(itkAddImageFilterISS2ISS2ISS2)
itkAddImageFilterISS2ISS2ISS2___New_orig__ = _itkAddImageFilterPython.itkAddImageFilterISS2ISS2ISS2___New_orig__
itkAddImageFilterISS2ISS2ISS2_cast = _itkAddImageFilterPython.itkAddImageFilterISS2ISS2ISS2_cast

class itkAddImageFilterISS3ISS3ISS3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterISS3ISS3ISS3):
    r"""Proxy of C++ itkAddImageFilterISS3ISS3ISS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAddImageFilterPython.itkAddImageFilterISS3ISS3ISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkAddImageFilterPython.itkAddImageFilterISS3ISS3ISS3_Clone)
    Input1Input2OutputAdditiveOperatorsCheck = _itkAddImageFilterPython.itkAddImageFilterISS3ISS3ISS3_Input1Input2OutputAdditiveOperatorsCheck
    
    __swig_destroy__ = _itkAddImageFilterPython.delete_itkAddImageFilterISS3ISS3ISS3
    cast = _swig_new_static_method(_itkAddImageFilterPython.itkAddImageFilterISS3ISS3ISS3_cast)

    def New(*args, **kargs):
        """New() -> itkAddImageFilterISS3ISS3ISS3

        Create a new object of the class itkAddImageFilterISS3ISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAddImageFilterISS3ISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAddImageFilterISS3ISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAddImageFilterISS3ISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAddImageFilterISS3ISS3ISS3 in _itkAddImageFilterPython:
_itkAddImageFilterPython.itkAddImageFilterISS3ISS3ISS3_swigregister(itkAddImageFilterISS3ISS3ISS3)
itkAddImageFilterISS3ISS3ISS3___New_orig__ = _itkAddImageFilterPython.itkAddImageFilterISS3ISS3ISS3___New_orig__
itkAddImageFilterISS3ISS3ISS3_cast = _itkAddImageFilterPython.itkAddImageFilterISS3ISS3ISS3_cast

class itkAddImageFilterIUC2IUC2IUC2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUC2IUC2IUC2):
    r"""Proxy of C++ itkAddImageFilterIUC2IUC2IUC2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAddImageFilterPython.itkAddImageFilterIUC2IUC2IUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkAddImageFilterPython.itkAddImageFilterIUC2IUC2IUC2_Clone)
    Input1Input2OutputAdditiveOperatorsCheck = _itkAddImageFilterPython.itkAddImageFilterIUC2IUC2IUC2_Input1Input2OutputAdditiveOperatorsCheck
    
    __swig_destroy__ = _itkAddImageFilterPython.delete_itkAddImageFilterIUC2IUC2IUC2
    cast = _swig_new_static_method(_itkAddImageFilterPython.itkAddImageFilterIUC2IUC2IUC2_cast)

    def New(*args, **kargs):
        """New() -> itkAddImageFilterIUC2IUC2IUC2

        Create a new object of the class itkAddImageFilterIUC2IUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAddImageFilterIUC2IUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAddImageFilterIUC2IUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAddImageFilterIUC2IUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAddImageFilterIUC2IUC2IUC2 in _itkAddImageFilterPython:
_itkAddImageFilterPython.itkAddImageFilterIUC2IUC2IUC2_swigregister(itkAddImageFilterIUC2IUC2IUC2)
itkAddImageFilterIUC2IUC2IUC2___New_orig__ = _itkAddImageFilterPython.itkAddImageFilterIUC2IUC2IUC2___New_orig__
itkAddImageFilterIUC2IUC2IUC2_cast = _itkAddImageFilterPython.itkAddImageFilterIUC2IUC2IUC2_cast

class itkAddImageFilterIUC3IUC3IUC3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUC3IUC3IUC3):
    r"""Proxy of C++ itkAddImageFilterIUC3IUC3IUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAddImageFilterPython.itkAddImageFilterIUC3IUC3IUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkAddImageFilterPython.itkAddImageFilterIUC3IUC3IUC3_Clone)
    Input1Input2OutputAdditiveOperatorsCheck = _itkAddImageFilterPython.itkAddImageFilterIUC3IUC3IUC3_Input1Input2OutputAdditiveOperatorsCheck
    
    __swig_destroy__ = _itkAddImageFilterPython.delete_itkAddImageFilterIUC3IUC3IUC3
    cast = _swig_new_static_method(_itkAddImageFilterPython.itkAddImageFilterIUC3IUC3IUC3_cast)

    def New(*args, **kargs):
        """New() -> itkAddImageFilterIUC3IUC3IUC3

        Create a new object of the class itkAddImageFilterIUC3IUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAddImageFilterIUC3IUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAddImageFilterIUC3IUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAddImageFilterIUC3IUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAddImageFilterIUC3IUC3IUC3 in _itkAddImageFilterPython:
_itkAddImageFilterPython.itkAddImageFilterIUC3IUC3IUC3_swigregister(itkAddImageFilterIUC3IUC3IUC3)
itkAddImageFilterIUC3IUC3IUC3___New_orig__ = _itkAddImageFilterPython.itkAddImageFilterIUC3IUC3IUC3___New_orig__
itkAddImageFilterIUC3IUC3IUC3_cast = _itkAddImageFilterPython.itkAddImageFilterIUC3IUC3IUC3_cast

class itkAddImageFilterIUS2IUS2IUS2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUS2IUS2IUS2):
    r"""Proxy of C++ itkAddImageFilterIUS2IUS2IUS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAddImageFilterPython.itkAddImageFilterIUS2IUS2IUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkAddImageFilterPython.itkAddImageFilterIUS2IUS2IUS2_Clone)
    Input1Input2OutputAdditiveOperatorsCheck = _itkAddImageFilterPython.itkAddImageFilterIUS2IUS2IUS2_Input1Input2OutputAdditiveOperatorsCheck
    
    __swig_destroy__ = _itkAddImageFilterPython.delete_itkAddImageFilterIUS2IUS2IUS2
    cast = _swig_new_static_method(_itkAddImageFilterPython.itkAddImageFilterIUS2IUS2IUS2_cast)

    def New(*args, **kargs):
        """New() -> itkAddImageFilterIUS2IUS2IUS2

        Create a new object of the class itkAddImageFilterIUS2IUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAddImageFilterIUS2IUS2IUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAddImageFilterIUS2IUS2IUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAddImageFilterIUS2IUS2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAddImageFilterIUS2IUS2IUS2 in _itkAddImageFilterPython:
_itkAddImageFilterPython.itkAddImageFilterIUS2IUS2IUS2_swigregister(itkAddImageFilterIUS2IUS2IUS2)
itkAddImageFilterIUS2IUS2IUS2___New_orig__ = _itkAddImageFilterPython.itkAddImageFilterIUS2IUS2IUS2___New_orig__
itkAddImageFilterIUS2IUS2IUS2_cast = _itkAddImageFilterPython.itkAddImageFilterIUS2IUS2IUS2_cast

class itkAddImageFilterIUS3IUS3IUS3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUS3IUS3IUS3):
    r"""Proxy of C++ itkAddImageFilterIUS3IUS3IUS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkAddImageFilterPython.itkAddImageFilterIUS3IUS3IUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkAddImageFilterPython.itkAddImageFilterIUS3IUS3IUS3_Clone)
    Input1Input2OutputAdditiveOperatorsCheck = _itkAddImageFilterPython.itkAddImageFilterIUS3IUS3IUS3_Input1Input2OutputAdditiveOperatorsCheck
    
    __swig_destroy__ = _itkAddImageFilterPython.delete_itkAddImageFilterIUS3IUS3IUS3
    cast = _swig_new_static_method(_itkAddImageFilterPython.itkAddImageFilterIUS3IUS3IUS3_cast)

    def New(*args, **kargs):
        """New() -> itkAddImageFilterIUS3IUS3IUS3

        Create a new object of the class itkAddImageFilterIUS3IUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAddImageFilterIUS3IUS3IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAddImageFilterIUS3IUS3IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAddImageFilterIUS3IUS3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkAddImageFilterIUS3IUS3IUS3 in _itkAddImageFilterPython:
_itkAddImageFilterPython.itkAddImageFilterIUS3IUS3IUS3_swigregister(itkAddImageFilterIUS3IUS3IUS3)
itkAddImageFilterIUS3IUS3IUS3___New_orig__ = _itkAddImageFilterPython.itkAddImageFilterIUS3IUS3IUS3___New_orig__
itkAddImageFilterIUS3IUS3IUS3_cast = _itkAddImageFilterPython.itkAddImageFilterIUS3IUS3IUS3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def add_image_filter(*args, **kwargs):
    """Procedural interface for AddImageFilter"""
    import itk
    instance = itk.AddImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def add_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.AddImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.AddImageFilter.values()[0]
    else:
        filter_object = itk.AddImageFilter

    add_image_filter.__doc__ = filter_object.__doc__
    add_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    add_image_filter.__doc__ += "Available Keyword Arguments:\n"
    add_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



