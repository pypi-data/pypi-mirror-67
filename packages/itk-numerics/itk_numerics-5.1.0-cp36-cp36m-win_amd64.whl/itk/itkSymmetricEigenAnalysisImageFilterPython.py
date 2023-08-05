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
    from . import _itkSymmetricEigenAnalysisImageFilterPython
else:
    import _itkSymmetricEigenAnalysisImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkSymmetricEigenAnalysisImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkSymmetricEigenAnalysisImageFilterPython.SWIG_PyStaticMethod_New

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


import itkImageRegionPython
import ITKCommonBasePython
import pyBasePython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkImageToImageFilterBPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkImageSourceCommonPython
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

def itkSymmetricEigenAnalysisImageFilterISSRTD33_New():
  return itkSymmetricEigenAnalysisImageFilterISSRTD33.New()


def itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_New():
  return itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass.New()


def itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass_New():
  return itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass.New()


def itkSymmetricEigenAnalysisImageFilterISSRTD22_New():
  return itkSymmetricEigenAnalysisImageFilterISSRTD22.New()


def itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_New():
  return itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass.New()


def itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass_New():
  return itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass.New()

class itkSymmetricEigenAnalysisEnums(object):
    r"""Proxy of C++ itkSymmetricEigenAnalysisEnums class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    EigenValueOrder_OrderByValue = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisEnums_EigenValueOrder_OrderByValue
    
    EigenValueOrder_OrderByMagnitude = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisEnums_EigenValueOrder_OrderByMagnitude
    
    EigenValueOrder_DoNotOrder = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisEnums_EigenValueOrder_DoNotOrder
    

    def __init__(self, *args):
        r"""
        __init__(itkSymmetricEigenAnalysisEnums self) -> itkSymmetricEigenAnalysisEnums
        __init__(itkSymmetricEigenAnalysisEnums self, itkSymmetricEigenAnalysisEnums arg0) -> itkSymmetricEigenAnalysisEnums
        """
        _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisEnums_swiginit(self, _itkSymmetricEigenAnalysisImageFilterPython.new_itkSymmetricEigenAnalysisEnums(*args))
    __swig_destroy__ = _itkSymmetricEigenAnalysisImageFilterPython.delete_itkSymmetricEigenAnalysisEnums

# Register itkSymmetricEigenAnalysisEnums in _itkSymmetricEigenAnalysisImageFilterPython:
_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisEnums_swigregister(itkSymmetricEigenAnalysisEnums)

class itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass(itkImageToImageFilterBPython.itkImageToImageFilterISSRTD22ISSRTD22):
    r"""Proxy of C++ itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetInPlace = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass_SetInPlace)
    GetInPlace = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass_GetInPlace)
    InPlaceOn = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass_InPlaceOn)
    InPlaceOff = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass_InPlaceOff)
    CanRunInPlace = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass_CanRunInPlace)
    __swig_destroy__ = _itkSymmetricEigenAnalysisImageFilterPython.delete_itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass
    cast = _swig_new_static_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass_cast)

    def New(*args, **kargs):
        """New() -> itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass

        Create a new object of the class itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass in _itkSymmetricEigenAnalysisImageFilterPython:
_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass_swigregister(itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass)
itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass_cast = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass_cast

class itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass(itkImageToImageFilterBPython.itkImageToImageFilterISSRTD33ISSRTD33):
    r"""Proxy of C++ itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetInPlace = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass_SetInPlace)
    GetInPlace = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass_GetInPlace)
    InPlaceOn = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass_InPlaceOn)
    InPlaceOff = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass_InPlaceOff)
    CanRunInPlace = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass_CanRunInPlace)
    __swig_destroy__ = _itkSymmetricEigenAnalysisImageFilterPython.delete_itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass
    cast = _swig_new_static_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass_cast)

    def New(*args, **kargs):
        """New() -> itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass

        Create a new object of the class itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass in _itkSymmetricEigenAnalysisImageFilterPython:
_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass_swigregister(itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass)
itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass_cast = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass_cast

class itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass(itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Superclass):
    r"""Proxy of C++ itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass___New_orig__)
    Clone = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_Clone)
    GetFunctor = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_GetFunctor)
    SetFunctor = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_SetFunctor)
    __swig_destroy__ = _itkSymmetricEigenAnalysisImageFilterPython.delete_itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass
    cast = _swig_new_static_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_cast)

    def New(*args, **kargs):
        """New() -> itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass

        Create a new object of the class itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass in _itkSymmetricEigenAnalysisImageFilterPython:
_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_swigregister(itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass)
itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass___New_orig__ = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass___New_orig__
itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_cast = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass_cast

class itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass(itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Superclass):
    r"""Proxy of C++ itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass___New_orig__)
    Clone = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_Clone)
    GetFunctor = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_GetFunctor)
    SetFunctor = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_SetFunctor)
    __swig_destroy__ = _itkSymmetricEigenAnalysisImageFilterPython.delete_itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass
    cast = _swig_new_static_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_cast)

    def New(*args, **kargs):
        """New() -> itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass

        Create a new object of the class itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass in _itkSymmetricEigenAnalysisImageFilterPython:
_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_swigregister(itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass)
itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass___New_orig__ = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass___New_orig__
itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_cast = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass_cast

class itkSymmetricEigenAnalysisImageFilterISSRTD22(itkSymmetricEigenAnalysisImageFilterISSRTD22_Superclass):
    r"""Proxy of C++ itkSymmetricEigenAnalysisImageFilterISSRTD22 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    OrderEigenValuesBy = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_OrderEigenValuesBy)
    __New_orig__ = _swig_new_static_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22___New_orig__)
    Clone = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_Clone)
    PrintSelf = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_PrintSelf)
    SetDimension = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_SetDimension)
    GetDimension = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_GetDimension)
    InputHasNumericTraitsCheck = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkSymmetricEigenAnalysisImageFilterPython.delete_itkSymmetricEigenAnalysisImageFilterISSRTD22
    cast = _swig_new_static_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_cast)

    def New(*args, **kargs):
        """New() -> itkSymmetricEigenAnalysisImageFilterISSRTD22

        Create a new object of the class itkSymmetricEigenAnalysisImageFilterISSRTD22 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSymmetricEigenAnalysisImageFilterISSRTD22.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSymmetricEigenAnalysisImageFilterISSRTD22.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSymmetricEigenAnalysisImageFilterISSRTD22.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSymmetricEigenAnalysisImageFilterISSRTD22 in _itkSymmetricEigenAnalysisImageFilterPython:
_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_swigregister(itkSymmetricEigenAnalysisImageFilterISSRTD22)
itkSymmetricEigenAnalysisImageFilterISSRTD22___New_orig__ = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22___New_orig__
itkSymmetricEigenAnalysisImageFilterISSRTD22_cast = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD22_cast

class itkSymmetricEigenAnalysisImageFilterISSRTD33(itkSymmetricEigenAnalysisImageFilterISSRTD33_Superclass):
    r"""Proxy of C++ itkSymmetricEigenAnalysisImageFilterISSRTD33 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    OrderEigenValuesBy = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_OrderEigenValuesBy)
    __New_orig__ = _swig_new_static_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33___New_orig__)
    Clone = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_Clone)
    PrintSelf = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_PrintSelf)
    SetDimension = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_SetDimension)
    GetDimension = _swig_new_instance_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_GetDimension)
    InputHasNumericTraitsCheck = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_InputHasNumericTraitsCheck
    
    __swig_destroy__ = _itkSymmetricEigenAnalysisImageFilterPython.delete_itkSymmetricEigenAnalysisImageFilterISSRTD33
    cast = _swig_new_static_method(_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_cast)

    def New(*args, **kargs):
        """New() -> itkSymmetricEigenAnalysisImageFilterISSRTD33

        Create a new object of the class itkSymmetricEigenAnalysisImageFilterISSRTD33 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSymmetricEigenAnalysisImageFilterISSRTD33.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSymmetricEigenAnalysisImageFilterISSRTD33.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSymmetricEigenAnalysisImageFilterISSRTD33.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkSymmetricEigenAnalysisImageFilterISSRTD33 in _itkSymmetricEigenAnalysisImageFilterPython:
_itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_swigregister(itkSymmetricEigenAnalysisImageFilterISSRTD33)
itkSymmetricEigenAnalysisImageFilterISSRTD33___New_orig__ = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33___New_orig__
itkSymmetricEigenAnalysisImageFilterISSRTD33_cast = _itkSymmetricEigenAnalysisImageFilterPython.itkSymmetricEigenAnalysisImageFilterISSRTD33_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def in_place_image_filter(*args, **kwargs):
    """Procedural interface for InPlaceImageFilter"""
    import itk
    instance = itk.InPlaceImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def in_place_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.InPlaceImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.InPlaceImageFilter.values()[0]
    else:
        filter_object = itk.InPlaceImageFilter

    in_place_image_filter.__doc__ = filter_object.__doc__
    in_place_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    in_place_image_filter.__doc__ += "Available Keyword Arguments:\n"
    in_place_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])
import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def symmetric_eigen_analysis_image_filter(*args, **kwargs):
    """Procedural interface for SymmetricEigenAnalysisImageFilter"""
    import itk
    instance = itk.SymmetricEigenAnalysisImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def symmetric_eigen_analysis_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.SymmetricEigenAnalysisImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.SymmetricEigenAnalysisImageFilter.values()[0]
    else:
        filter_object = itk.SymmetricEigenAnalysisImageFilter

    symmetric_eigen_analysis_image_filter.__doc__ = filter_object.__doc__
    symmetric_eigen_analysis_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    symmetric_eigen_analysis_image_filter.__doc__ += "Available Keyword Arguments:\n"
    symmetric_eigen_analysis_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])
import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def unary_functor_image_filter(*args, **kwargs):
    """Procedural interface for UnaryFunctorImageFilter"""
    import itk
    instance = itk.UnaryFunctorImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def unary_functor_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.UnaryFunctorImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.UnaryFunctorImageFilter.values()[0]
    else:
        filter_object = itk.UnaryFunctorImageFilter

    unary_functor_image_filter.__doc__ = filter_object.__doc__
    unary_functor_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    unary_functor_image_filter.__doc__ += "Available Keyword Arguments:\n"
    unary_functor_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



