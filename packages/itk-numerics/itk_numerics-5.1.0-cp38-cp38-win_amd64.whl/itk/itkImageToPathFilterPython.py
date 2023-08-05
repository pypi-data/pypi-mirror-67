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
    from . import _itkImageToPathFilterPython
else:
    import _itkImageToPathFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkImageToPathFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkImageToPathFilterPython.SWIG_PyStaticMethod_New

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


import itkImagePython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import pyBasePython
import ITKCommonBasePython
import itkMatrixPython
import vnl_matrixPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrix_fixedPython
import itkPointPython
import itkFixedArrayPython
import itkVectorPython
import vnl_vector_refPython
import itkCovariantVectorPython
import itkSymmetricSecondRankTensorPython
import itkRGBPixelPython
import itkRGBAPixelPython
import itkImageRegionPython
import itkPathSourcePython
import itkPolyLineParametricPathPython
import itkContinuousIndexPython
import itkVectorContainerPython
import itkParametricPathPython
import itkPathBasePython

def itkImageToPathFilterID3PLPP3_New():
  return itkImageToPathFilterID3PLPP3.New()


def itkImageToPathFilterIF3PLPP3_New():
  return itkImageToPathFilterIF3PLPP3.New()


def itkImageToPathFilterIUS3PLPP3_New():
  return itkImageToPathFilterIUS3PLPP3.New()


def itkImageToPathFilterIUC3PLPP3_New():
  return itkImageToPathFilterIUC3PLPP3.New()


def itkImageToPathFilterISS3PLPP3_New():
  return itkImageToPathFilterISS3PLPP3.New()


def itkImageToPathFilterID2PLPP2_New():
  return itkImageToPathFilterID2PLPP2.New()


def itkImageToPathFilterIF2PLPP2_New():
  return itkImageToPathFilterIF2PLPP2.New()


def itkImageToPathFilterIUS2PLPP2_New():
  return itkImageToPathFilterIUS2PLPP2.New()


def itkImageToPathFilterIUC2PLPP2_New():
  return itkImageToPathFilterIUC2PLPP2.New()


def itkImageToPathFilterISS2PLPP2_New():
  return itkImageToPathFilterISS2PLPP2.New()

class itkImageToPathFilterID2PLPP2(itkPathSourcePython.itkPathSourcePLPP2):
    r"""Proxy of C++ itkImageToPathFilterID2PLPP2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetInput = _swig_new_instance_method(_itkImageToPathFilterPython.itkImageToPathFilterID2PLPP2_SetInput)
    GetInput = _swig_new_instance_method(_itkImageToPathFilterPython.itkImageToPathFilterID2PLPP2_GetInput)
    __swig_destroy__ = _itkImageToPathFilterPython.delete_itkImageToPathFilterID2PLPP2
    cast = _swig_new_static_method(_itkImageToPathFilterPython.itkImageToPathFilterID2PLPP2_cast)

    def New(*args, **kargs):
        """New() -> itkImageToPathFilterID2PLPP2

        Create a new object of the class itkImageToPathFilterID2PLPP2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToPathFilterID2PLPP2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImageToPathFilterID2PLPP2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImageToPathFilterID2PLPP2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImageToPathFilterID2PLPP2 in _itkImageToPathFilterPython:
_itkImageToPathFilterPython.itkImageToPathFilterID2PLPP2_swigregister(itkImageToPathFilterID2PLPP2)
itkImageToPathFilterID2PLPP2_cast = _itkImageToPathFilterPython.itkImageToPathFilterID2PLPP2_cast

class itkImageToPathFilterID3PLPP3(itkPathSourcePython.itkPathSourcePLPP3):
    r"""Proxy of C++ itkImageToPathFilterID3PLPP3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetInput = _swig_new_instance_method(_itkImageToPathFilterPython.itkImageToPathFilterID3PLPP3_SetInput)
    GetInput = _swig_new_instance_method(_itkImageToPathFilterPython.itkImageToPathFilterID3PLPP3_GetInput)
    __swig_destroy__ = _itkImageToPathFilterPython.delete_itkImageToPathFilterID3PLPP3
    cast = _swig_new_static_method(_itkImageToPathFilterPython.itkImageToPathFilterID3PLPP3_cast)

    def New(*args, **kargs):
        """New() -> itkImageToPathFilterID3PLPP3

        Create a new object of the class itkImageToPathFilterID3PLPP3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToPathFilterID3PLPP3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImageToPathFilterID3PLPP3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImageToPathFilterID3PLPP3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImageToPathFilterID3PLPP3 in _itkImageToPathFilterPython:
_itkImageToPathFilterPython.itkImageToPathFilterID3PLPP3_swigregister(itkImageToPathFilterID3PLPP3)
itkImageToPathFilterID3PLPP3_cast = _itkImageToPathFilterPython.itkImageToPathFilterID3PLPP3_cast

class itkImageToPathFilterIF2PLPP2(itkPathSourcePython.itkPathSourcePLPP2):
    r"""Proxy of C++ itkImageToPathFilterIF2PLPP2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetInput = _swig_new_instance_method(_itkImageToPathFilterPython.itkImageToPathFilterIF2PLPP2_SetInput)
    GetInput = _swig_new_instance_method(_itkImageToPathFilterPython.itkImageToPathFilterIF2PLPP2_GetInput)
    __swig_destroy__ = _itkImageToPathFilterPython.delete_itkImageToPathFilterIF2PLPP2
    cast = _swig_new_static_method(_itkImageToPathFilterPython.itkImageToPathFilterIF2PLPP2_cast)

    def New(*args, **kargs):
        """New() -> itkImageToPathFilterIF2PLPP2

        Create a new object of the class itkImageToPathFilterIF2PLPP2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToPathFilterIF2PLPP2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImageToPathFilterIF2PLPP2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImageToPathFilterIF2PLPP2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImageToPathFilterIF2PLPP2 in _itkImageToPathFilterPython:
_itkImageToPathFilterPython.itkImageToPathFilterIF2PLPP2_swigregister(itkImageToPathFilterIF2PLPP2)
itkImageToPathFilterIF2PLPP2_cast = _itkImageToPathFilterPython.itkImageToPathFilterIF2PLPP2_cast

class itkImageToPathFilterIF3PLPP3(itkPathSourcePython.itkPathSourcePLPP3):
    r"""Proxy of C++ itkImageToPathFilterIF3PLPP3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetInput = _swig_new_instance_method(_itkImageToPathFilterPython.itkImageToPathFilterIF3PLPP3_SetInput)
    GetInput = _swig_new_instance_method(_itkImageToPathFilterPython.itkImageToPathFilterIF3PLPP3_GetInput)
    __swig_destroy__ = _itkImageToPathFilterPython.delete_itkImageToPathFilterIF3PLPP3
    cast = _swig_new_static_method(_itkImageToPathFilterPython.itkImageToPathFilterIF3PLPP3_cast)

    def New(*args, **kargs):
        """New() -> itkImageToPathFilterIF3PLPP3

        Create a new object of the class itkImageToPathFilterIF3PLPP3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToPathFilterIF3PLPP3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImageToPathFilterIF3PLPP3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImageToPathFilterIF3PLPP3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImageToPathFilterIF3PLPP3 in _itkImageToPathFilterPython:
_itkImageToPathFilterPython.itkImageToPathFilterIF3PLPP3_swigregister(itkImageToPathFilterIF3PLPP3)
itkImageToPathFilterIF3PLPP3_cast = _itkImageToPathFilterPython.itkImageToPathFilterIF3PLPP3_cast

class itkImageToPathFilterISS2PLPP2(itkPathSourcePython.itkPathSourcePLPP2):
    r"""Proxy of C++ itkImageToPathFilterISS2PLPP2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetInput = _swig_new_instance_method(_itkImageToPathFilterPython.itkImageToPathFilterISS2PLPP2_SetInput)
    GetInput = _swig_new_instance_method(_itkImageToPathFilterPython.itkImageToPathFilterISS2PLPP2_GetInput)
    __swig_destroy__ = _itkImageToPathFilterPython.delete_itkImageToPathFilterISS2PLPP2
    cast = _swig_new_static_method(_itkImageToPathFilterPython.itkImageToPathFilterISS2PLPP2_cast)

    def New(*args, **kargs):
        """New() -> itkImageToPathFilterISS2PLPP2

        Create a new object of the class itkImageToPathFilterISS2PLPP2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToPathFilterISS2PLPP2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImageToPathFilterISS2PLPP2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImageToPathFilterISS2PLPP2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImageToPathFilterISS2PLPP2 in _itkImageToPathFilterPython:
_itkImageToPathFilterPython.itkImageToPathFilterISS2PLPP2_swigregister(itkImageToPathFilterISS2PLPP2)
itkImageToPathFilterISS2PLPP2_cast = _itkImageToPathFilterPython.itkImageToPathFilterISS2PLPP2_cast

class itkImageToPathFilterISS3PLPP3(itkPathSourcePython.itkPathSourcePLPP3):
    r"""Proxy of C++ itkImageToPathFilterISS3PLPP3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetInput = _swig_new_instance_method(_itkImageToPathFilterPython.itkImageToPathFilterISS3PLPP3_SetInput)
    GetInput = _swig_new_instance_method(_itkImageToPathFilterPython.itkImageToPathFilterISS3PLPP3_GetInput)
    __swig_destroy__ = _itkImageToPathFilterPython.delete_itkImageToPathFilterISS3PLPP3
    cast = _swig_new_static_method(_itkImageToPathFilterPython.itkImageToPathFilterISS3PLPP3_cast)

    def New(*args, **kargs):
        """New() -> itkImageToPathFilterISS3PLPP3

        Create a new object of the class itkImageToPathFilterISS3PLPP3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToPathFilterISS3PLPP3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImageToPathFilterISS3PLPP3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImageToPathFilterISS3PLPP3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImageToPathFilterISS3PLPP3 in _itkImageToPathFilterPython:
_itkImageToPathFilterPython.itkImageToPathFilterISS3PLPP3_swigregister(itkImageToPathFilterISS3PLPP3)
itkImageToPathFilterISS3PLPP3_cast = _itkImageToPathFilterPython.itkImageToPathFilterISS3PLPP3_cast

class itkImageToPathFilterIUC2PLPP2(itkPathSourcePython.itkPathSourcePLPP2):
    r"""Proxy of C++ itkImageToPathFilterIUC2PLPP2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetInput = _swig_new_instance_method(_itkImageToPathFilterPython.itkImageToPathFilterIUC2PLPP2_SetInput)
    GetInput = _swig_new_instance_method(_itkImageToPathFilterPython.itkImageToPathFilterIUC2PLPP2_GetInput)
    __swig_destroy__ = _itkImageToPathFilterPython.delete_itkImageToPathFilterIUC2PLPP2
    cast = _swig_new_static_method(_itkImageToPathFilterPython.itkImageToPathFilterIUC2PLPP2_cast)

    def New(*args, **kargs):
        """New() -> itkImageToPathFilterIUC2PLPP2

        Create a new object of the class itkImageToPathFilterIUC2PLPP2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToPathFilterIUC2PLPP2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImageToPathFilterIUC2PLPP2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImageToPathFilterIUC2PLPP2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImageToPathFilterIUC2PLPP2 in _itkImageToPathFilterPython:
_itkImageToPathFilterPython.itkImageToPathFilterIUC2PLPP2_swigregister(itkImageToPathFilterIUC2PLPP2)
itkImageToPathFilterIUC2PLPP2_cast = _itkImageToPathFilterPython.itkImageToPathFilterIUC2PLPP2_cast

class itkImageToPathFilterIUC3PLPP3(itkPathSourcePython.itkPathSourcePLPP3):
    r"""Proxy of C++ itkImageToPathFilterIUC3PLPP3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetInput = _swig_new_instance_method(_itkImageToPathFilterPython.itkImageToPathFilterIUC3PLPP3_SetInput)
    GetInput = _swig_new_instance_method(_itkImageToPathFilterPython.itkImageToPathFilterIUC3PLPP3_GetInput)
    __swig_destroy__ = _itkImageToPathFilterPython.delete_itkImageToPathFilterIUC3PLPP3
    cast = _swig_new_static_method(_itkImageToPathFilterPython.itkImageToPathFilterIUC3PLPP3_cast)

    def New(*args, **kargs):
        """New() -> itkImageToPathFilterIUC3PLPP3

        Create a new object of the class itkImageToPathFilterIUC3PLPP3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToPathFilterIUC3PLPP3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImageToPathFilterIUC3PLPP3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImageToPathFilterIUC3PLPP3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImageToPathFilterIUC3PLPP3 in _itkImageToPathFilterPython:
_itkImageToPathFilterPython.itkImageToPathFilterIUC3PLPP3_swigregister(itkImageToPathFilterIUC3PLPP3)
itkImageToPathFilterIUC3PLPP3_cast = _itkImageToPathFilterPython.itkImageToPathFilterIUC3PLPP3_cast

class itkImageToPathFilterIUS2PLPP2(itkPathSourcePython.itkPathSourcePLPP2):
    r"""Proxy of C++ itkImageToPathFilterIUS2PLPP2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetInput = _swig_new_instance_method(_itkImageToPathFilterPython.itkImageToPathFilterIUS2PLPP2_SetInput)
    GetInput = _swig_new_instance_method(_itkImageToPathFilterPython.itkImageToPathFilterIUS2PLPP2_GetInput)
    __swig_destroy__ = _itkImageToPathFilterPython.delete_itkImageToPathFilterIUS2PLPP2
    cast = _swig_new_static_method(_itkImageToPathFilterPython.itkImageToPathFilterIUS2PLPP2_cast)

    def New(*args, **kargs):
        """New() -> itkImageToPathFilterIUS2PLPP2

        Create a new object of the class itkImageToPathFilterIUS2PLPP2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToPathFilterIUS2PLPP2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImageToPathFilterIUS2PLPP2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImageToPathFilterIUS2PLPP2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImageToPathFilterIUS2PLPP2 in _itkImageToPathFilterPython:
_itkImageToPathFilterPython.itkImageToPathFilterIUS2PLPP2_swigregister(itkImageToPathFilterIUS2PLPP2)
itkImageToPathFilterIUS2PLPP2_cast = _itkImageToPathFilterPython.itkImageToPathFilterIUS2PLPP2_cast

class itkImageToPathFilterIUS3PLPP3(itkPathSourcePython.itkPathSourcePLPP3):
    r"""Proxy of C++ itkImageToPathFilterIUS3PLPP3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    SetInput = _swig_new_instance_method(_itkImageToPathFilterPython.itkImageToPathFilterIUS3PLPP3_SetInput)
    GetInput = _swig_new_instance_method(_itkImageToPathFilterPython.itkImageToPathFilterIUS3PLPP3_GetInput)
    __swig_destroy__ = _itkImageToPathFilterPython.delete_itkImageToPathFilterIUS3PLPP3
    cast = _swig_new_static_method(_itkImageToPathFilterPython.itkImageToPathFilterIUS3PLPP3_cast)

    def New(*args, **kargs):
        """New() -> itkImageToPathFilterIUS3PLPP3

        Create a new object of the class itkImageToPathFilterIUS3PLPP3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkImageToPathFilterIUS3PLPP3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkImageToPathFilterIUS3PLPP3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkImageToPathFilterIUS3PLPP3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkImageToPathFilterIUS3PLPP3 in _itkImageToPathFilterPython:
_itkImageToPathFilterPython.itkImageToPathFilterIUS3PLPP3_swigregister(itkImageToPathFilterIUS3PLPP3)
itkImageToPathFilterIUS3PLPP3_cast = _itkImageToPathFilterPython.itkImageToPathFilterIUS3PLPP3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def image_to_path_filter(*args, **kwargs):
    """Procedural interface for ImageToPathFilter"""
    import itk
    instance = itk.ImageToPathFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def image_to_path_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.ImageToPathFilter, itkTemplate.itkTemplate):
        filter_object = itk.ImageToPathFilter.values()[0]
    else:
        filter_object = itk.ImageToPathFilter

    image_to_path_filter.__doc__ = filter_object.__doc__
    image_to_path_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    image_to_path_filter.__doc__ += "Available Keyword Arguments:\n"
    image_to_path_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



