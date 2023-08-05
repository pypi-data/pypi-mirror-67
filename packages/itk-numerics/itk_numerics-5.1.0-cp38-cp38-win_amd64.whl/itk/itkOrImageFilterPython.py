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
    from . import _itkOrImageFilterPython
else:
    import _itkOrImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkOrImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkOrImageFilterPython.SWIG_PyStaticMethod_New

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

def itkOrImageFilterISS3ISS3ISS3_New():
  return itkOrImageFilterISS3ISS3ISS3.New()


def itkOrImageFilterISS2ISS2ISS2_New():
  return itkOrImageFilterISS2ISS2ISS2.New()


def itkOrImageFilterIUS3IUS3IUS3_New():
  return itkOrImageFilterIUS3IUS3IUS3.New()


def itkOrImageFilterIUS2IUS2IUS2_New():
  return itkOrImageFilterIUS2IUS2IUS2.New()


def itkOrImageFilterIUC3IUC3IUC3_New():
  return itkOrImageFilterIUC3IUC3IUC3.New()


def itkOrImageFilterIUC2IUC2IUC2_New():
  return itkOrImageFilterIUC2IUC2IUC2.New()

class itkOrImageFilterISS2ISS2ISS2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterISS2ISS2ISS2):
    r"""Proxy of C++ itkOrImageFilterISS2ISS2ISS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkOrImageFilterPython.itkOrImageFilterISS2ISS2ISS2___New_orig__)
    Clone = _swig_new_instance_method(_itkOrImageFilterPython.itkOrImageFilterISS2ISS2ISS2_Clone)
    Input1Input2OutputBitwiseOperatorsCheck = _itkOrImageFilterPython.itkOrImageFilterISS2ISS2ISS2_Input1Input2OutputBitwiseOperatorsCheck
    
    __swig_destroy__ = _itkOrImageFilterPython.delete_itkOrImageFilterISS2ISS2ISS2
    cast = _swig_new_static_method(_itkOrImageFilterPython.itkOrImageFilterISS2ISS2ISS2_cast)

    def New(*args, **kargs):
        """New() -> itkOrImageFilterISS2ISS2ISS2

        Create a new object of the class itkOrImageFilterISS2ISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkOrImageFilterISS2ISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkOrImageFilterISS2ISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkOrImageFilterISS2ISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkOrImageFilterISS2ISS2ISS2 in _itkOrImageFilterPython:
_itkOrImageFilterPython.itkOrImageFilterISS2ISS2ISS2_swigregister(itkOrImageFilterISS2ISS2ISS2)
itkOrImageFilterISS2ISS2ISS2___New_orig__ = _itkOrImageFilterPython.itkOrImageFilterISS2ISS2ISS2___New_orig__
itkOrImageFilterISS2ISS2ISS2_cast = _itkOrImageFilterPython.itkOrImageFilterISS2ISS2ISS2_cast

class itkOrImageFilterISS3ISS3ISS3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterISS3ISS3ISS3):
    r"""Proxy of C++ itkOrImageFilterISS3ISS3ISS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkOrImageFilterPython.itkOrImageFilterISS3ISS3ISS3___New_orig__)
    Clone = _swig_new_instance_method(_itkOrImageFilterPython.itkOrImageFilterISS3ISS3ISS3_Clone)
    Input1Input2OutputBitwiseOperatorsCheck = _itkOrImageFilterPython.itkOrImageFilterISS3ISS3ISS3_Input1Input2OutputBitwiseOperatorsCheck
    
    __swig_destroy__ = _itkOrImageFilterPython.delete_itkOrImageFilterISS3ISS3ISS3
    cast = _swig_new_static_method(_itkOrImageFilterPython.itkOrImageFilterISS3ISS3ISS3_cast)

    def New(*args, **kargs):
        """New() -> itkOrImageFilterISS3ISS3ISS3

        Create a new object of the class itkOrImageFilterISS3ISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkOrImageFilterISS3ISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkOrImageFilterISS3ISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkOrImageFilterISS3ISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkOrImageFilterISS3ISS3ISS3 in _itkOrImageFilterPython:
_itkOrImageFilterPython.itkOrImageFilterISS3ISS3ISS3_swigregister(itkOrImageFilterISS3ISS3ISS3)
itkOrImageFilterISS3ISS3ISS3___New_orig__ = _itkOrImageFilterPython.itkOrImageFilterISS3ISS3ISS3___New_orig__
itkOrImageFilterISS3ISS3ISS3_cast = _itkOrImageFilterPython.itkOrImageFilterISS3ISS3ISS3_cast

class itkOrImageFilterIUC2IUC2IUC2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUC2IUC2IUC2):
    r"""Proxy of C++ itkOrImageFilterIUC2IUC2IUC2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkOrImageFilterPython.itkOrImageFilterIUC2IUC2IUC2___New_orig__)
    Clone = _swig_new_instance_method(_itkOrImageFilterPython.itkOrImageFilterIUC2IUC2IUC2_Clone)
    Input1Input2OutputBitwiseOperatorsCheck = _itkOrImageFilterPython.itkOrImageFilterIUC2IUC2IUC2_Input1Input2OutputBitwiseOperatorsCheck
    
    __swig_destroy__ = _itkOrImageFilterPython.delete_itkOrImageFilterIUC2IUC2IUC2
    cast = _swig_new_static_method(_itkOrImageFilterPython.itkOrImageFilterIUC2IUC2IUC2_cast)

    def New(*args, **kargs):
        """New() -> itkOrImageFilterIUC2IUC2IUC2

        Create a new object of the class itkOrImageFilterIUC2IUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkOrImageFilterIUC2IUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkOrImageFilterIUC2IUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkOrImageFilterIUC2IUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkOrImageFilterIUC2IUC2IUC2 in _itkOrImageFilterPython:
_itkOrImageFilterPython.itkOrImageFilterIUC2IUC2IUC2_swigregister(itkOrImageFilterIUC2IUC2IUC2)
itkOrImageFilterIUC2IUC2IUC2___New_orig__ = _itkOrImageFilterPython.itkOrImageFilterIUC2IUC2IUC2___New_orig__
itkOrImageFilterIUC2IUC2IUC2_cast = _itkOrImageFilterPython.itkOrImageFilterIUC2IUC2IUC2_cast

class itkOrImageFilterIUC3IUC3IUC3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUC3IUC3IUC3):
    r"""Proxy of C++ itkOrImageFilterIUC3IUC3IUC3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkOrImageFilterPython.itkOrImageFilterIUC3IUC3IUC3___New_orig__)
    Clone = _swig_new_instance_method(_itkOrImageFilterPython.itkOrImageFilterIUC3IUC3IUC3_Clone)
    Input1Input2OutputBitwiseOperatorsCheck = _itkOrImageFilterPython.itkOrImageFilterIUC3IUC3IUC3_Input1Input2OutputBitwiseOperatorsCheck
    
    __swig_destroy__ = _itkOrImageFilterPython.delete_itkOrImageFilterIUC3IUC3IUC3
    cast = _swig_new_static_method(_itkOrImageFilterPython.itkOrImageFilterIUC3IUC3IUC3_cast)

    def New(*args, **kargs):
        """New() -> itkOrImageFilterIUC3IUC3IUC3

        Create a new object of the class itkOrImageFilterIUC3IUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkOrImageFilterIUC3IUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkOrImageFilterIUC3IUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkOrImageFilterIUC3IUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkOrImageFilterIUC3IUC3IUC3 in _itkOrImageFilterPython:
_itkOrImageFilterPython.itkOrImageFilterIUC3IUC3IUC3_swigregister(itkOrImageFilterIUC3IUC3IUC3)
itkOrImageFilterIUC3IUC3IUC3___New_orig__ = _itkOrImageFilterPython.itkOrImageFilterIUC3IUC3IUC3___New_orig__
itkOrImageFilterIUC3IUC3IUC3_cast = _itkOrImageFilterPython.itkOrImageFilterIUC3IUC3IUC3_cast

class itkOrImageFilterIUS2IUS2IUS2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUS2IUS2IUS2):
    r"""Proxy of C++ itkOrImageFilterIUS2IUS2IUS2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkOrImageFilterPython.itkOrImageFilterIUS2IUS2IUS2___New_orig__)
    Clone = _swig_new_instance_method(_itkOrImageFilterPython.itkOrImageFilterIUS2IUS2IUS2_Clone)
    Input1Input2OutputBitwiseOperatorsCheck = _itkOrImageFilterPython.itkOrImageFilterIUS2IUS2IUS2_Input1Input2OutputBitwiseOperatorsCheck
    
    __swig_destroy__ = _itkOrImageFilterPython.delete_itkOrImageFilterIUS2IUS2IUS2
    cast = _swig_new_static_method(_itkOrImageFilterPython.itkOrImageFilterIUS2IUS2IUS2_cast)

    def New(*args, **kargs):
        """New() -> itkOrImageFilterIUS2IUS2IUS2

        Create a new object of the class itkOrImageFilterIUS2IUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkOrImageFilterIUS2IUS2IUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkOrImageFilterIUS2IUS2IUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkOrImageFilterIUS2IUS2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkOrImageFilterIUS2IUS2IUS2 in _itkOrImageFilterPython:
_itkOrImageFilterPython.itkOrImageFilterIUS2IUS2IUS2_swigregister(itkOrImageFilterIUS2IUS2IUS2)
itkOrImageFilterIUS2IUS2IUS2___New_orig__ = _itkOrImageFilterPython.itkOrImageFilterIUS2IUS2IUS2___New_orig__
itkOrImageFilterIUS2IUS2IUS2_cast = _itkOrImageFilterPython.itkOrImageFilterIUS2IUS2IUS2_cast

class itkOrImageFilterIUS3IUS3IUS3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUS3IUS3IUS3):
    r"""Proxy of C++ itkOrImageFilterIUS3IUS3IUS3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkOrImageFilterPython.itkOrImageFilterIUS3IUS3IUS3___New_orig__)
    Clone = _swig_new_instance_method(_itkOrImageFilterPython.itkOrImageFilterIUS3IUS3IUS3_Clone)
    Input1Input2OutputBitwiseOperatorsCheck = _itkOrImageFilterPython.itkOrImageFilterIUS3IUS3IUS3_Input1Input2OutputBitwiseOperatorsCheck
    
    __swig_destroy__ = _itkOrImageFilterPython.delete_itkOrImageFilterIUS3IUS3IUS3
    cast = _swig_new_static_method(_itkOrImageFilterPython.itkOrImageFilterIUS3IUS3IUS3_cast)

    def New(*args, **kargs):
        """New() -> itkOrImageFilterIUS3IUS3IUS3

        Create a new object of the class itkOrImageFilterIUS3IUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkOrImageFilterIUS3IUS3IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkOrImageFilterIUS3IUS3IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkOrImageFilterIUS3IUS3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkOrImageFilterIUS3IUS3IUS3 in _itkOrImageFilterPython:
_itkOrImageFilterPython.itkOrImageFilterIUS3IUS3IUS3_swigregister(itkOrImageFilterIUS3IUS3IUS3)
itkOrImageFilterIUS3IUS3IUS3___New_orig__ = _itkOrImageFilterPython.itkOrImageFilterIUS3IUS3IUS3___New_orig__
itkOrImageFilterIUS3IUS3IUS3_cast = _itkOrImageFilterPython.itkOrImageFilterIUS3IUS3IUS3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def or_image_filter(*args, **kwargs):
    """Procedural interface for OrImageFilter"""
    import itk
    instance = itk.OrImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def or_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.OrImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.OrImageFilter.values()[0]
    else:
        filter_object = itk.OrImageFilter

    or_image_filter.__doc__ = filter_object.__doc__
    or_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    or_image_filter.__doc__ += "Available Keyword Arguments:\n"
    or_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



