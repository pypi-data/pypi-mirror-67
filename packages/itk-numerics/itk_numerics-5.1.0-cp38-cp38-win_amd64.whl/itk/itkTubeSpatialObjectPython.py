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
    from . import _itkTubeSpatialObjectPython
else:
    import _itkTubeSpatialObjectPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkTubeSpatialObjectPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkTubeSpatialObjectPython.SWIG_PyStaticMethod_New

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
import itkSpatialObjectBasePython
import itkAffineTransformPython
import itkVectorPython
import itkFixedArrayPython
import vnl_vector_refPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkCovariantVectorPython
import itkTransformBasePython
import itkSymmetricSecondRankTensorPython
import itkArrayPython
import itkDiffusionTensor3DPython
import itkOptimizerParametersPython
import itkArray2DPython
import itkVariableLengthVectorPython
import itkMatrixOffsetTransformBasePython
import itkSpatialObjectPropertyPython
import itkRGBAPixelPython
import itkBoundingBoxPython
import itkMapContainerPython
import itkVectorContainerPython
import itkContinuousIndexPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkImageRegionPython
import itkTubeSpatialObjectPointPython
import itkSpatialObjectPointPython

def itkTubeSpatialObject3_New():
  return itkTubeSpatialObject3.New()


def itkTubeSpatialObject2_New():
  return itkTubeSpatialObject2.New()


def itkPointBasedSpatialObjectTube3_New():
  return itkPointBasedSpatialObjectTube3.New()


def itkPointBasedSpatialObjectTube2_New():
  return itkPointBasedSpatialObjectTube2.New()

class listitkPointBasedSpatialObjectTube2_Pointer(object):
    r"""Proxy of C++ std::list< itkPointBasedSpatialObjectTube2_Pointer > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer___nonzero__)
    __bool__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer___bool__)
    __len__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer___len__)
    __getslice__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer___getslice__)
    __setslice__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer___setslice__)
    __delslice__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer___delslice__)
    __delitem__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer___delitem__)
    __getitem__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer___getitem__)
    __setitem__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer___setitem__)
    pop = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer_pop)
    append = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer_append)
    empty = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer_empty)
    size = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer_size)
    swap = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer_swap)
    begin = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer_begin)
    end = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer_end)
    rbegin = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer_rbegin)
    rend = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer_rend)
    clear = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer_clear)
    get_allocator = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer_get_allocator)
    pop_back = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer_pop_back)
    erase = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer_erase)

    def __init__(self, *args):
        r"""
        __init__(listitkPointBasedSpatialObjectTube2_Pointer self) -> listitkPointBasedSpatialObjectTube2_Pointer
        __init__(listitkPointBasedSpatialObjectTube2_Pointer self, listitkPointBasedSpatialObjectTube2_Pointer other) -> listitkPointBasedSpatialObjectTube2_Pointer
        __init__(listitkPointBasedSpatialObjectTube2_Pointer self, std::list< itkPointBasedSpatialObjectTube2_Pointer >::size_type size) -> listitkPointBasedSpatialObjectTube2_Pointer
        __init__(listitkPointBasedSpatialObjectTube2_Pointer self, std::list< itkPointBasedSpatialObjectTube2_Pointer >::size_type size, std::list< itkPointBasedSpatialObjectTube2_Pointer >::value_type const & value) -> listitkPointBasedSpatialObjectTube2_Pointer
        """
        _itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer_swiginit(self, _itkTubeSpatialObjectPython.new_listitkPointBasedSpatialObjectTube2_Pointer(*args))
    push_back = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer_push_back)
    front = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer_front)
    back = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer_back)
    assign = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer_assign)
    resize = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer_resize)
    insert = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer_insert)
    pop_front = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer_pop_front)
    push_front = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer_push_front)
    reverse = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer_reverse)
    __swig_destroy__ = _itkTubeSpatialObjectPython.delete_listitkPointBasedSpatialObjectTube2_Pointer

# Register listitkPointBasedSpatialObjectTube2_Pointer in _itkTubeSpatialObjectPython:
_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube2_Pointer_swigregister(listitkPointBasedSpatialObjectTube2_Pointer)

class listitkPointBasedSpatialObjectTube3_Pointer(object):
    r"""Proxy of C++ std::list< itkPointBasedSpatialObjectTube3_Pointer > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer___nonzero__)
    __bool__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer___bool__)
    __len__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer___len__)
    __getslice__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer___getslice__)
    __setslice__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer___setslice__)
    __delslice__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer___delslice__)
    __delitem__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer___delitem__)
    __getitem__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer___getitem__)
    __setitem__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer___setitem__)
    pop = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer_pop)
    append = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer_append)
    empty = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer_empty)
    size = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer_size)
    swap = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer_swap)
    begin = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer_begin)
    end = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer_end)
    rbegin = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer_rbegin)
    rend = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer_rend)
    clear = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer_clear)
    get_allocator = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer_get_allocator)
    pop_back = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer_pop_back)
    erase = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer_erase)

    def __init__(self, *args):
        r"""
        __init__(listitkPointBasedSpatialObjectTube3_Pointer self) -> listitkPointBasedSpatialObjectTube3_Pointer
        __init__(listitkPointBasedSpatialObjectTube3_Pointer self, listitkPointBasedSpatialObjectTube3_Pointer other) -> listitkPointBasedSpatialObjectTube3_Pointer
        __init__(listitkPointBasedSpatialObjectTube3_Pointer self, std::list< itkPointBasedSpatialObjectTube3_Pointer >::size_type size) -> listitkPointBasedSpatialObjectTube3_Pointer
        __init__(listitkPointBasedSpatialObjectTube3_Pointer self, std::list< itkPointBasedSpatialObjectTube3_Pointer >::size_type size, std::list< itkPointBasedSpatialObjectTube3_Pointer >::value_type const & value) -> listitkPointBasedSpatialObjectTube3_Pointer
        """
        _itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer_swiginit(self, _itkTubeSpatialObjectPython.new_listitkPointBasedSpatialObjectTube3_Pointer(*args))
    push_back = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer_push_back)
    front = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer_front)
    back = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer_back)
    assign = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer_assign)
    resize = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer_resize)
    insert = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer_insert)
    pop_front = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer_pop_front)
    push_front = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer_push_front)
    reverse = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer_reverse)
    __swig_destroy__ = _itkTubeSpatialObjectPython.delete_listitkPointBasedSpatialObjectTube3_Pointer

# Register listitkPointBasedSpatialObjectTube3_Pointer in _itkTubeSpatialObjectPython:
_itkTubeSpatialObjectPython.listitkPointBasedSpatialObjectTube3_Pointer_swigregister(listitkPointBasedSpatialObjectTube3_Pointer)

class listitkTubeSpatialObject2_Pointer(object):
    r"""Proxy of C++ std::list< itkTubeSpatialObject2_Pointer > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer___nonzero__)
    __bool__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer___bool__)
    __len__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer___len__)
    __getslice__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer___getslice__)
    __setslice__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer___setslice__)
    __delslice__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer___delslice__)
    __delitem__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer___delitem__)
    __getitem__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer___getitem__)
    __setitem__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer___setitem__)
    pop = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer_pop)
    append = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer_append)
    empty = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer_empty)
    size = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer_size)
    swap = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer_swap)
    begin = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer_begin)
    end = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer_end)
    rbegin = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer_rbegin)
    rend = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer_rend)
    clear = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer_clear)
    get_allocator = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer_get_allocator)
    pop_back = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer_pop_back)
    erase = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer_erase)

    def __init__(self, *args):
        r"""
        __init__(listitkTubeSpatialObject2_Pointer self) -> listitkTubeSpatialObject2_Pointer
        __init__(listitkTubeSpatialObject2_Pointer self, listitkTubeSpatialObject2_Pointer other) -> listitkTubeSpatialObject2_Pointer
        __init__(listitkTubeSpatialObject2_Pointer self, std::list< itkTubeSpatialObject2_Pointer >::size_type size) -> listitkTubeSpatialObject2_Pointer
        __init__(listitkTubeSpatialObject2_Pointer self, std::list< itkTubeSpatialObject2_Pointer >::size_type size, std::list< itkTubeSpatialObject2_Pointer >::value_type const & value) -> listitkTubeSpatialObject2_Pointer
        """
        _itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer_swiginit(self, _itkTubeSpatialObjectPython.new_listitkTubeSpatialObject2_Pointer(*args))
    push_back = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer_push_back)
    front = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer_front)
    back = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer_back)
    assign = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer_assign)
    resize = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer_resize)
    insert = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer_insert)
    pop_front = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer_pop_front)
    push_front = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer_push_front)
    reverse = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer_reverse)
    __swig_destroy__ = _itkTubeSpatialObjectPython.delete_listitkTubeSpatialObject2_Pointer

# Register listitkTubeSpatialObject2_Pointer in _itkTubeSpatialObjectPython:
_itkTubeSpatialObjectPython.listitkTubeSpatialObject2_Pointer_swigregister(listitkTubeSpatialObject2_Pointer)

class listitkTubeSpatialObject3_Pointer(object):
    r"""Proxy of C++ std::list< itkTubeSpatialObject3_Pointer > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer___nonzero__)
    __bool__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer___bool__)
    __len__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer___len__)
    __getslice__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer___getslice__)
    __setslice__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer___setslice__)
    __delslice__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer___delslice__)
    __delitem__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer___delitem__)
    __getitem__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer___getitem__)
    __setitem__ = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer___setitem__)
    pop = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer_pop)
    append = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer_append)
    empty = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer_empty)
    size = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer_size)
    swap = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer_swap)
    begin = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer_begin)
    end = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer_end)
    rbegin = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer_rbegin)
    rend = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer_rend)
    clear = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer_clear)
    get_allocator = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer_get_allocator)
    pop_back = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer_pop_back)
    erase = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer_erase)

    def __init__(self, *args):
        r"""
        __init__(listitkTubeSpatialObject3_Pointer self) -> listitkTubeSpatialObject3_Pointer
        __init__(listitkTubeSpatialObject3_Pointer self, listitkTubeSpatialObject3_Pointer other) -> listitkTubeSpatialObject3_Pointer
        __init__(listitkTubeSpatialObject3_Pointer self, std::list< itkTubeSpatialObject3_Pointer >::size_type size) -> listitkTubeSpatialObject3_Pointer
        __init__(listitkTubeSpatialObject3_Pointer self, std::list< itkTubeSpatialObject3_Pointer >::size_type size, std::list< itkTubeSpatialObject3_Pointer >::value_type const & value) -> listitkTubeSpatialObject3_Pointer
        """
        _itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer_swiginit(self, _itkTubeSpatialObjectPython.new_listitkTubeSpatialObject3_Pointer(*args))
    push_back = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer_push_back)
    front = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer_front)
    back = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer_back)
    assign = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer_assign)
    resize = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer_resize)
    insert = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer_insert)
    pop_front = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer_pop_front)
    push_front = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer_push_front)
    reverse = _swig_new_instance_method(_itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer_reverse)
    __swig_destroy__ = _itkTubeSpatialObjectPython.delete_listitkTubeSpatialObject3_Pointer

# Register listitkTubeSpatialObject3_Pointer in _itkTubeSpatialObjectPython:
_itkTubeSpatialObjectPython.listitkTubeSpatialObject3_Pointer_swigregister(listitkTubeSpatialObject3_Pointer)

class itkPointBasedSpatialObjectTube2(itkSpatialObjectBasePython.itkSpatialObject2):
    r"""Proxy of C++ itkPointBasedSpatialObjectTube2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkTubeSpatialObjectPython.itkPointBasedSpatialObjectTube2___New_orig__)
    Clone = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkPointBasedSpatialObjectTube2_Clone)
    AddPoint = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkPointBasedSpatialObjectTube2_AddPoint)
    RemovePoint = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkPointBasedSpatialObjectTube2_RemovePoint)
    SetPoints = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkPointBasedSpatialObjectTube2_SetPoints)
    GetPoints = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkPointBasedSpatialObjectTube2_GetPoints)
    GetPoint = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkPointBasedSpatialObjectTube2_GetPoint)
    GetNumberOfPoints = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkPointBasedSpatialObjectTube2_GetNumberOfPoints)
    ClosestPointInWorldSpace = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkPointBasedSpatialObjectTube2_ClosestPointInWorldSpace)
    ClosestPointInObjectSpace = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkPointBasedSpatialObjectTube2_ClosestPointInObjectSpace)
    __swig_destroy__ = _itkTubeSpatialObjectPython.delete_itkPointBasedSpatialObjectTube2
    cast = _swig_new_static_method(_itkTubeSpatialObjectPython.itkPointBasedSpatialObjectTube2_cast)

    def New(*args, **kargs):
        """New() -> itkPointBasedSpatialObjectTube2

        Create a new object of the class itkPointBasedSpatialObjectTube2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPointBasedSpatialObjectTube2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkPointBasedSpatialObjectTube2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkPointBasedSpatialObjectTube2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPointBasedSpatialObjectTube2 in _itkTubeSpatialObjectPython:
_itkTubeSpatialObjectPython.itkPointBasedSpatialObjectTube2_swigregister(itkPointBasedSpatialObjectTube2)
itkPointBasedSpatialObjectTube2___New_orig__ = _itkTubeSpatialObjectPython.itkPointBasedSpatialObjectTube2___New_orig__
itkPointBasedSpatialObjectTube2_cast = _itkTubeSpatialObjectPython.itkPointBasedSpatialObjectTube2_cast

class itkPointBasedSpatialObjectTube3(itkSpatialObjectBasePython.itkSpatialObject3):
    r"""Proxy of C++ itkPointBasedSpatialObjectTube3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkTubeSpatialObjectPython.itkPointBasedSpatialObjectTube3___New_orig__)
    Clone = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkPointBasedSpatialObjectTube3_Clone)
    AddPoint = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkPointBasedSpatialObjectTube3_AddPoint)
    RemovePoint = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkPointBasedSpatialObjectTube3_RemovePoint)
    SetPoints = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkPointBasedSpatialObjectTube3_SetPoints)
    GetPoints = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkPointBasedSpatialObjectTube3_GetPoints)
    GetPoint = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkPointBasedSpatialObjectTube3_GetPoint)
    GetNumberOfPoints = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkPointBasedSpatialObjectTube3_GetNumberOfPoints)
    ClosestPointInWorldSpace = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkPointBasedSpatialObjectTube3_ClosestPointInWorldSpace)
    ClosestPointInObjectSpace = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkPointBasedSpatialObjectTube3_ClosestPointInObjectSpace)
    __swig_destroy__ = _itkTubeSpatialObjectPython.delete_itkPointBasedSpatialObjectTube3
    cast = _swig_new_static_method(_itkTubeSpatialObjectPython.itkPointBasedSpatialObjectTube3_cast)

    def New(*args, **kargs):
        """New() -> itkPointBasedSpatialObjectTube3

        Create a new object of the class itkPointBasedSpatialObjectTube3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkPointBasedSpatialObjectTube3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkPointBasedSpatialObjectTube3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkPointBasedSpatialObjectTube3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkPointBasedSpatialObjectTube3 in _itkTubeSpatialObjectPython:
_itkTubeSpatialObjectPython.itkPointBasedSpatialObjectTube3_swigregister(itkPointBasedSpatialObjectTube3)
itkPointBasedSpatialObjectTube3___New_orig__ = _itkTubeSpatialObjectPython.itkPointBasedSpatialObjectTube3___New_orig__
itkPointBasedSpatialObjectTube3_cast = _itkTubeSpatialObjectPython.itkPointBasedSpatialObjectTube3_cast

class itkTubeSpatialObject2(itkPointBasedSpatialObjectTube2):
    r"""Proxy of C++ itkTubeSpatialObject2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkTubeSpatialObjectPython.itkTubeSpatialObject2___New_orig__)
    Clone = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkTubeSpatialObject2_Clone)
    SetEndRounded = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkTubeSpatialObject2_SetEndRounded)
    GetEndRounded = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkTubeSpatialObject2_GetEndRounded)
    ComputeTangentAndNormals = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkTubeSpatialObject2_ComputeTangentAndNormals)
    RemoveDuplicatePointsInObjectSpace = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkTubeSpatialObject2_RemoveDuplicatePointsInObjectSpace)
    SetParentPoint = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkTubeSpatialObject2_SetParentPoint)
    GetParentPoint = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkTubeSpatialObject2_GetParentPoint)
    SetRoot = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkTubeSpatialObject2_SetRoot)
    GetRoot = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkTubeSpatialObject2_GetRoot)
    __swig_destroy__ = _itkTubeSpatialObjectPython.delete_itkTubeSpatialObject2
    cast = _swig_new_static_method(_itkTubeSpatialObjectPython.itkTubeSpatialObject2_cast)

    def New(*args, **kargs):
        """New() -> itkTubeSpatialObject2

        Create a new object of the class itkTubeSpatialObject2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTubeSpatialObject2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTubeSpatialObject2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTubeSpatialObject2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTubeSpatialObject2 in _itkTubeSpatialObjectPython:
_itkTubeSpatialObjectPython.itkTubeSpatialObject2_swigregister(itkTubeSpatialObject2)
itkTubeSpatialObject2___New_orig__ = _itkTubeSpatialObjectPython.itkTubeSpatialObject2___New_orig__
itkTubeSpatialObject2_cast = _itkTubeSpatialObjectPython.itkTubeSpatialObject2_cast

class itkTubeSpatialObject3(itkPointBasedSpatialObjectTube3):
    r"""Proxy of C++ itkTubeSpatialObject3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkTubeSpatialObjectPython.itkTubeSpatialObject3___New_orig__)
    Clone = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkTubeSpatialObject3_Clone)
    SetEndRounded = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkTubeSpatialObject3_SetEndRounded)
    GetEndRounded = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkTubeSpatialObject3_GetEndRounded)
    ComputeTangentAndNormals = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkTubeSpatialObject3_ComputeTangentAndNormals)
    RemoveDuplicatePointsInObjectSpace = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkTubeSpatialObject3_RemoveDuplicatePointsInObjectSpace)
    SetParentPoint = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkTubeSpatialObject3_SetParentPoint)
    GetParentPoint = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkTubeSpatialObject3_GetParentPoint)
    SetRoot = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkTubeSpatialObject3_SetRoot)
    GetRoot = _swig_new_instance_method(_itkTubeSpatialObjectPython.itkTubeSpatialObject3_GetRoot)
    __swig_destroy__ = _itkTubeSpatialObjectPython.delete_itkTubeSpatialObject3
    cast = _swig_new_static_method(_itkTubeSpatialObjectPython.itkTubeSpatialObject3_cast)

    def New(*args, **kargs):
        """New() -> itkTubeSpatialObject3

        Create a new object of the class itkTubeSpatialObject3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTubeSpatialObject3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTubeSpatialObject3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTubeSpatialObject3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkTubeSpatialObject3 in _itkTubeSpatialObjectPython:
_itkTubeSpatialObjectPython.itkTubeSpatialObject3_swigregister(itkTubeSpatialObject3)
itkTubeSpatialObject3___New_orig__ = _itkTubeSpatialObjectPython.itkTubeSpatialObject3___New_orig__
itkTubeSpatialObject3_cast = _itkTubeSpatialObjectPython.itkTubeSpatialObject3_cast



