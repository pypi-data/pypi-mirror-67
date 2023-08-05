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
    from . import _itkEigenAnalysis2DImageFilterPython
else:
    import _itkEigenAnalysis2DImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkEigenAnalysis2DImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkEigenAnalysis2DImageFilterPython.SWIG_PyStaticMethod_New

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
import itkImagePython
import itkFixedArrayPython
import itkRGBAPixelPython
import itkRGBPixelPython
import itkVectorPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkSizePython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import itkCovariantVectorPython
import itkPointPython
import vnl_matrix_fixedPython
import itkIndexPython
import itkOffsetPython
import itkImageRegionPython
import itkImageToImageFilterAPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython

def itkEigenAnalysis2DImageFilterID2ID2IVF42_New():
  return itkEigenAnalysis2DImageFilterID2ID2IVF42.New()


def itkEigenAnalysis2DImageFilterID2ID2IVF32_New():
  return itkEigenAnalysis2DImageFilterID2ID2IVF32.New()


def itkEigenAnalysis2DImageFilterID2ID2IVF22_New():
  return itkEigenAnalysis2DImageFilterID2ID2IVF22.New()


def itkEigenAnalysis2DImageFilterIF2IF2IVF42_New():
  return itkEigenAnalysis2DImageFilterIF2IF2IVF42.New()


def itkEigenAnalysis2DImageFilterIF2IF2IVF32_New():
  return itkEigenAnalysis2DImageFilterIF2IF2IVF32.New()


def itkEigenAnalysis2DImageFilterIF2IF2IVF22_New():
  return itkEigenAnalysis2DImageFilterIF2IF2IVF22.New()

class itkEigenAnalysis2DImageFilterID2ID2IVF22(itkImageToImageFilterAPython.itkImageToImageFilterID2ID2):
    r"""Proxy of C++ itkEigenAnalysis2DImageFilterID2ID2IVF22 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF22___New_orig__)
    Clone = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF22_Clone)
    SetInput1 = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF22_SetInput1)
    SetInput2 = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF22_SetInput2)
    SetInput3 = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF22_SetInput3)
    GetMaxEigenValue = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF22_GetMaxEigenValue)
    GetMinEigenValue = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF22_GetMinEigenValue)
    GetMaxEigenVector = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF22_GetMaxEigenVector)
    VectorComponentHasNumericTraitsCheck = _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF22_VectorComponentHasNumericTraitsCheck
    
    __swig_destroy__ = _itkEigenAnalysis2DImageFilterPython.delete_itkEigenAnalysis2DImageFilterID2ID2IVF22
    cast = _swig_new_static_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF22_cast)

    def New(*args, **kargs):
        """New() -> itkEigenAnalysis2DImageFilterID2ID2IVF22

        Create a new object of the class itkEigenAnalysis2DImageFilterID2ID2IVF22 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkEigenAnalysis2DImageFilterID2ID2IVF22.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkEigenAnalysis2DImageFilterID2ID2IVF22.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkEigenAnalysis2DImageFilterID2ID2IVF22.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkEigenAnalysis2DImageFilterID2ID2IVF22 in _itkEigenAnalysis2DImageFilterPython:
_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF22_swigregister(itkEigenAnalysis2DImageFilterID2ID2IVF22)
itkEigenAnalysis2DImageFilterID2ID2IVF22___New_orig__ = _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF22___New_orig__
itkEigenAnalysis2DImageFilterID2ID2IVF22_cast = _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF22_cast

class itkEigenAnalysis2DImageFilterID2ID2IVF32(itkImageToImageFilterAPython.itkImageToImageFilterID2ID2):
    r"""Proxy of C++ itkEigenAnalysis2DImageFilterID2ID2IVF32 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF32___New_orig__)
    Clone = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF32_Clone)
    SetInput1 = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF32_SetInput1)
    SetInput2 = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF32_SetInput2)
    SetInput3 = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF32_SetInput3)
    GetMaxEigenValue = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF32_GetMaxEigenValue)
    GetMinEigenValue = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF32_GetMinEigenValue)
    GetMaxEigenVector = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF32_GetMaxEigenVector)
    VectorComponentHasNumericTraitsCheck = _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF32_VectorComponentHasNumericTraitsCheck
    
    __swig_destroy__ = _itkEigenAnalysis2DImageFilterPython.delete_itkEigenAnalysis2DImageFilterID2ID2IVF32
    cast = _swig_new_static_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF32_cast)

    def New(*args, **kargs):
        """New() -> itkEigenAnalysis2DImageFilterID2ID2IVF32

        Create a new object of the class itkEigenAnalysis2DImageFilterID2ID2IVF32 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkEigenAnalysis2DImageFilterID2ID2IVF32.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkEigenAnalysis2DImageFilterID2ID2IVF32.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkEigenAnalysis2DImageFilterID2ID2IVF32.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkEigenAnalysis2DImageFilterID2ID2IVF32 in _itkEigenAnalysis2DImageFilterPython:
_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF32_swigregister(itkEigenAnalysis2DImageFilterID2ID2IVF32)
itkEigenAnalysis2DImageFilterID2ID2IVF32___New_orig__ = _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF32___New_orig__
itkEigenAnalysis2DImageFilterID2ID2IVF32_cast = _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF32_cast

class itkEigenAnalysis2DImageFilterID2ID2IVF42(itkImageToImageFilterAPython.itkImageToImageFilterID2ID2):
    r"""Proxy of C++ itkEigenAnalysis2DImageFilterID2ID2IVF42 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF42___New_orig__)
    Clone = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF42_Clone)
    SetInput1 = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF42_SetInput1)
    SetInput2 = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF42_SetInput2)
    SetInput3 = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF42_SetInput3)
    GetMaxEigenValue = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF42_GetMaxEigenValue)
    GetMinEigenValue = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF42_GetMinEigenValue)
    GetMaxEigenVector = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF42_GetMaxEigenVector)
    VectorComponentHasNumericTraitsCheck = _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF42_VectorComponentHasNumericTraitsCheck
    
    __swig_destroy__ = _itkEigenAnalysis2DImageFilterPython.delete_itkEigenAnalysis2DImageFilterID2ID2IVF42
    cast = _swig_new_static_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF42_cast)

    def New(*args, **kargs):
        """New() -> itkEigenAnalysis2DImageFilterID2ID2IVF42

        Create a new object of the class itkEigenAnalysis2DImageFilterID2ID2IVF42 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkEigenAnalysis2DImageFilterID2ID2IVF42.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkEigenAnalysis2DImageFilterID2ID2IVF42.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkEigenAnalysis2DImageFilterID2ID2IVF42.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkEigenAnalysis2DImageFilterID2ID2IVF42 in _itkEigenAnalysis2DImageFilterPython:
_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF42_swigregister(itkEigenAnalysis2DImageFilterID2ID2IVF42)
itkEigenAnalysis2DImageFilterID2ID2IVF42___New_orig__ = _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF42___New_orig__
itkEigenAnalysis2DImageFilterID2ID2IVF42_cast = _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterID2ID2IVF42_cast

class itkEigenAnalysis2DImageFilterIF2IF2IVF22(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    r"""Proxy of C++ itkEigenAnalysis2DImageFilterIF2IF2IVF22 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22___New_orig__)
    Clone = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22_Clone)
    SetInput1 = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22_SetInput1)
    SetInput2 = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22_SetInput2)
    SetInput3 = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22_SetInput3)
    GetMaxEigenValue = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22_GetMaxEigenValue)
    GetMinEigenValue = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22_GetMinEigenValue)
    GetMaxEigenVector = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22_GetMaxEigenVector)
    VectorComponentHasNumericTraitsCheck = _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22_VectorComponentHasNumericTraitsCheck
    
    __swig_destroy__ = _itkEigenAnalysis2DImageFilterPython.delete_itkEigenAnalysis2DImageFilterIF2IF2IVF22
    cast = _swig_new_static_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22_cast)

    def New(*args, **kargs):
        """New() -> itkEigenAnalysis2DImageFilterIF2IF2IVF22

        Create a new object of the class itkEigenAnalysis2DImageFilterIF2IF2IVF22 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkEigenAnalysis2DImageFilterIF2IF2IVF22.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkEigenAnalysis2DImageFilterIF2IF2IVF22.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkEigenAnalysis2DImageFilterIF2IF2IVF22.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkEigenAnalysis2DImageFilterIF2IF2IVF22 in _itkEigenAnalysis2DImageFilterPython:
_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22_swigregister(itkEigenAnalysis2DImageFilterIF2IF2IVF22)
itkEigenAnalysis2DImageFilterIF2IF2IVF22___New_orig__ = _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22___New_orig__
itkEigenAnalysis2DImageFilterIF2IF2IVF22_cast = _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF22_cast

class itkEigenAnalysis2DImageFilterIF2IF2IVF32(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    r"""Proxy of C++ itkEigenAnalysis2DImageFilterIF2IF2IVF32 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32___New_orig__)
    Clone = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32_Clone)
    SetInput1 = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32_SetInput1)
    SetInput2 = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32_SetInput2)
    SetInput3 = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32_SetInput3)
    GetMaxEigenValue = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32_GetMaxEigenValue)
    GetMinEigenValue = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32_GetMinEigenValue)
    GetMaxEigenVector = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32_GetMaxEigenVector)
    VectorComponentHasNumericTraitsCheck = _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32_VectorComponentHasNumericTraitsCheck
    
    __swig_destroy__ = _itkEigenAnalysis2DImageFilterPython.delete_itkEigenAnalysis2DImageFilterIF2IF2IVF32
    cast = _swig_new_static_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32_cast)

    def New(*args, **kargs):
        """New() -> itkEigenAnalysis2DImageFilterIF2IF2IVF32

        Create a new object of the class itkEigenAnalysis2DImageFilterIF2IF2IVF32 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkEigenAnalysis2DImageFilterIF2IF2IVF32.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkEigenAnalysis2DImageFilterIF2IF2IVF32.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkEigenAnalysis2DImageFilterIF2IF2IVF32.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkEigenAnalysis2DImageFilterIF2IF2IVF32 in _itkEigenAnalysis2DImageFilterPython:
_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32_swigregister(itkEigenAnalysis2DImageFilterIF2IF2IVF32)
itkEigenAnalysis2DImageFilterIF2IF2IVF32___New_orig__ = _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32___New_orig__
itkEigenAnalysis2DImageFilterIF2IF2IVF32_cast = _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF32_cast

class itkEigenAnalysis2DImageFilterIF2IF2IVF42(itkImageToImageFilterAPython.itkImageToImageFilterIF2IF2):
    r"""Proxy of C++ itkEigenAnalysis2DImageFilterIF2IF2IVF42 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42___New_orig__)
    Clone = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42_Clone)
    SetInput1 = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42_SetInput1)
    SetInput2 = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42_SetInput2)
    SetInput3 = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42_SetInput3)
    GetMaxEigenValue = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42_GetMaxEigenValue)
    GetMinEigenValue = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42_GetMinEigenValue)
    GetMaxEigenVector = _swig_new_instance_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42_GetMaxEigenVector)
    VectorComponentHasNumericTraitsCheck = _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42_VectorComponentHasNumericTraitsCheck
    
    __swig_destroy__ = _itkEigenAnalysis2DImageFilterPython.delete_itkEigenAnalysis2DImageFilterIF2IF2IVF42
    cast = _swig_new_static_method(_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42_cast)

    def New(*args, **kargs):
        """New() -> itkEigenAnalysis2DImageFilterIF2IF2IVF42

        Create a new object of the class itkEigenAnalysis2DImageFilterIF2IF2IVF42 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkEigenAnalysis2DImageFilterIF2IF2IVF42.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkEigenAnalysis2DImageFilterIF2IF2IVF42.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkEigenAnalysis2DImageFilterIF2IF2IVF42.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkEigenAnalysis2DImageFilterIF2IF2IVF42 in _itkEigenAnalysis2DImageFilterPython:
_itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42_swigregister(itkEigenAnalysis2DImageFilterIF2IF2IVF42)
itkEigenAnalysis2DImageFilterIF2IF2IVF42___New_orig__ = _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42___New_orig__
itkEigenAnalysis2DImageFilterIF2IF2IVF42_cast = _itkEigenAnalysis2DImageFilterPython.itkEigenAnalysis2DImageFilterIF2IF2IVF42_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def eigen_analysis2_d_image_filter(*args, **kwargs):
    """Procedural interface for EigenAnalysis2DImageFilter"""
    import itk
    instance = itk.EigenAnalysis2DImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def eigen_analysis2_d_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.EigenAnalysis2DImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.EigenAnalysis2DImageFilter.values()[0]
    else:
        filter_object = itk.EigenAnalysis2DImageFilter

    eigen_analysis2_d_image_filter.__doc__ = filter_object.__doc__
    eigen_analysis2_d_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    eigen_analysis2_d_image_filter.__doc__ += "Available Keyword Arguments:\n"
    eigen_analysis2_d_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



