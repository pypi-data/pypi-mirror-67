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
    from . import _itkLandmarkSpatialObjectPython
else:
    import _itkLandmarkSpatialObjectPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkLandmarkSpatialObjectPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkLandmarkSpatialObjectPython.SWIG_PyStaticMethod_New

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


import itkPointBasedSpatialObjectPython
import itkSpatialObjectBasePython
import itkSpatialObjectPropertyPython
import itkRGBAPixelPython
import itkFixedArrayPython
import pyBasePython
import ITKCommonBasePython
import itkCovariantVectorPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import itkVectorPython
import itkImageRegionPython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkAffineTransformPython
import itkMatrixPython
import itkPointPython
import vnl_matrix_fixedPython
import itkTransformBasePython
import itkSymmetricSecondRankTensorPython
import itkArrayPython
import itkDiffusionTensor3DPython
import itkArray2DPython
import itkVariableLengthVectorPython
import itkOptimizerParametersPython
import itkMatrixOffsetTransformBasePython
import itkBoundingBoxPython
import itkMapContainerPython
import itkVectorContainerPython
import itkContinuousIndexPython
import itkSpatialObjectPointPython

def itkLandmarkSpatialObject3_New():
  return itkLandmarkSpatialObject3.New()


def itkLandmarkSpatialObject2_New():
  return itkLandmarkSpatialObject2.New()

class listitkLandmarkSpatialObject2_Pointer(object):
    r"""Proxy of C++ std::list< itkLandmarkSpatialObject2_Pointer > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer___nonzero__)
    __bool__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer___bool__)
    __len__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer___len__)
    __getslice__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer___getslice__)
    __setslice__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer___setslice__)
    __delslice__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer___delslice__)
    __delitem__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer___delitem__)
    __getitem__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer___getitem__)
    __setitem__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer___setitem__)
    pop = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_pop)
    append = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_append)
    empty = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_empty)
    size = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_size)
    swap = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_swap)
    begin = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_begin)
    end = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_end)
    rbegin = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_rbegin)
    rend = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_rend)
    clear = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_clear)
    get_allocator = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_get_allocator)
    pop_back = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_pop_back)
    erase = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_erase)

    def __init__(self, *args):
        r"""
        __init__(listitkLandmarkSpatialObject2_Pointer self) -> listitkLandmarkSpatialObject2_Pointer
        __init__(listitkLandmarkSpatialObject2_Pointer self, listitkLandmarkSpatialObject2_Pointer other) -> listitkLandmarkSpatialObject2_Pointer
        __init__(listitkLandmarkSpatialObject2_Pointer self, std::list< itkLandmarkSpatialObject2_Pointer >::size_type size) -> listitkLandmarkSpatialObject2_Pointer
        __init__(listitkLandmarkSpatialObject2_Pointer self, std::list< itkLandmarkSpatialObject2_Pointer >::size_type size, std::list< itkLandmarkSpatialObject2_Pointer >::value_type const & value) -> listitkLandmarkSpatialObject2_Pointer
        """
        _itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_swiginit(self, _itkLandmarkSpatialObjectPython.new_listitkLandmarkSpatialObject2_Pointer(*args))
    push_back = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_push_back)
    front = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_front)
    back = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_back)
    assign = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_assign)
    resize = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_resize)
    insert = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_insert)
    pop_front = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_pop_front)
    push_front = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_push_front)
    reverse = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_reverse)
    __swig_destroy__ = _itkLandmarkSpatialObjectPython.delete_listitkLandmarkSpatialObject2_Pointer

# Register listitkLandmarkSpatialObject2_Pointer in _itkLandmarkSpatialObjectPython:
_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject2_Pointer_swigregister(listitkLandmarkSpatialObject2_Pointer)

class listitkLandmarkSpatialObject3_Pointer(object):
    r"""Proxy of C++ std::list< itkLandmarkSpatialObject3_Pointer > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer___nonzero__)
    __bool__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer___bool__)
    __len__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer___len__)
    __getslice__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer___getslice__)
    __setslice__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer___setslice__)
    __delslice__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer___delslice__)
    __delitem__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer___delitem__)
    __getitem__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer___getitem__)
    __setitem__ = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer___setitem__)
    pop = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_pop)
    append = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_append)
    empty = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_empty)
    size = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_size)
    swap = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_swap)
    begin = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_begin)
    end = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_end)
    rbegin = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_rbegin)
    rend = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_rend)
    clear = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_clear)
    get_allocator = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_get_allocator)
    pop_back = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_pop_back)
    erase = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_erase)

    def __init__(self, *args):
        r"""
        __init__(listitkLandmarkSpatialObject3_Pointer self) -> listitkLandmarkSpatialObject3_Pointer
        __init__(listitkLandmarkSpatialObject3_Pointer self, listitkLandmarkSpatialObject3_Pointer other) -> listitkLandmarkSpatialObject3_Pointer
        __init__(listitkLandmarkSpatialObject3_Pointer self, std::list< itkLandmarkSpatialObject3_Pointer >::size_type size) -> listitkLandmarkSpatialObject3_Pointer
        __init__(listitkLandmarkSpatialObject3_Pointer self, std::list< itkLandmarkSpatialObject3_Pointer >::size_type size, std::list< itkLandmarkSpatialObject3_Pointer >::value_type const & value) -> listitkLandmarkSpatialObject3_Pointer
        """
        _itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_swiginit(self, _itkLandmarkSpatialObjectPython.new_listitkLandmarkSpatialObject3_Pointer(*args))
    push_back = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_push_back)
    front = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_front)
    back = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_back)
    assign = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_assign)
    resize = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_resize)
    insert = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_insert)
    pop_front = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_pop_front)
    push_front = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_push_front)
    reverse = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_reverse)
    __swig_destroy__ = _itkLandmarkSpatialObjectPython.delete_listitkLandmarkSpatialObject3_Pointer

# Register listitkLandmarkSpatialObject3_Pointer in _itkLandmarkSpatialObjectPython:
_itkLandmarkSpatialObjectPython.listitkLandmarkSpatialObject3_Pointer_swigregister(listitkLandmarkSpatialObject3_Pointer)

class itkLandmarkSpatialObject2(itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject2):
    r"""Proxy of C++ itkLandmarkSpatialObject2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject2___New_orig__)
    Clone = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject2_Clone)
    __swig_destroy__ = _itkLandmarkSpatialObjectPython.delete_itkLandmarkSpatialObject2
    cast = _swig_new_static_method(_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject2_cast)

    def New(*args, **kargs):
        """New() -> itkLandmarkSpatialObject2

        Create a new object of the class itkLandmarkSpatialObject2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLandmarkSpatialObject2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLandmarkSpatialObject2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLandmarkSpatialObject2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLandmarkSpatialObject2 in _itkLandmarkSpatialObjectPython:
_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject2_swigregister(itkLandmarkSpatialObject2)
itkLandmarkSpatialObject2___New_orig__ = _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject2___New_orig__
itkLandmarkSpatialObject2_cast = _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject2_cast

class itkLandmarkSpatialObject3(itkPointBasedSpatialObjectPython.itkPointBasedSpatialObject3):
    r"""Proxy of C++ itkLandmarkSpatialObject3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject3___New_orig__)
    Clone = _swig_new_instance_method(_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject3_Clone)
    __swig_destroy__ = _itkLandmarkSpatialObjectPython.delete_itkLandmarkSpatialObject3
    cast = _swig_new_static_method(_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject3_cast)

    def New(*args, **kargs):
        """New() -> itkLandmarkSpatialObject3

        Create a new object of the class itkLandmarkSpatialObject3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLandmarkSpatialObject3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkLandmarkSpatialObject3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkLandmarkSpatialObject3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLandmarkSpatialObject3 in _itkLandmarkSpatialObjectPython:
_itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject3_swigregister(itkLandmarkSpatialObject3)
itkLandmarkSpatialObject3___New_orig__ = _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject3___New_orig__
itkLandmarkSpatialObject3_cast = _itkLandmarkSpatialObjectPython.itkLandmarkSpatialObject3_cast



