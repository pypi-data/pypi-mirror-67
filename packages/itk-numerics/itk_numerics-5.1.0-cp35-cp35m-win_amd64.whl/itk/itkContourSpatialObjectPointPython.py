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
    from . import _itkContourSpatialObjectPointPython
else:
    import _itkContourSpatialObjectPointPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkContourSpatialObjectPointPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkContourSpatialObjectPointPython.SWIG_PyStaticMethod_New

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
import itkSpatialObjectPointPython
import itkSpatialObjectBasePython
import itkSpatialObjectPropertyPython
import itkRGBAPixelPython
import itkFixedArrayPython
import itkCovariantVectorPython
import itkVectorPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import vnl_vector_refPython
import itkImageRegionPython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import itkBoundingBoxPython
import itkPointPython
import itkVectorContainerPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkContinuousIndexPython
import itkMapContainerPython
import itkAffineTransformPython
import itkTransformBasePython
import itkSymmetricSecondRankTensorPython
import itkArray2DPython
import itkArrayPython
import itkVariableLengthVectorPython
import itkDiffusionTensor3DPython
import itkOptimizerParametersPython
import itkMatrixOffsetTransformBasePython
class vectoritkContourSpatialObjectPoint2(object):
    r"""Proxy of C++ std::vector< itkContourSpatialObjectPoint2 > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint2_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint2___nonzero__)
    __bool__ = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint2___bool__)
    __len__ = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint2___len__)
    __getslice__ = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint2___getslice__)
    __setslice__ = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint2___setslice__)
    __delslice__ = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint2___delslice__)
    __delitem__ = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint2___delitem__)
    __getitem__ = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint2___getitem__)
    __setitem__ = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint2___setitem__)
    pop = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint2_pop)
    append = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint2_append)
    empty = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint2_empty)
    size = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint2_size)
    swap = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint2_swap)
    begin = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint2_begin)
    end = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint2_end)
    rbegin = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint2_rbegin)
    rend = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint2_rend)
    clear = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint2_clear)
    get_allocator = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint2_get_allocator)
    pop_back = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint2_pop_back)
    erase = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint2_erase)

    def __init__(self, *args):
        r"""
        __init__(vectoritkContourSpatialObjectPoint2 self) -> vectoritkContourSpatialObjectPoint2
        __init__(vectoritkContourSpatialObjectPoint2 self, vectoritkContourSpatialObjectPoint2 other) -> vectoritkContourSpatialObjectPoint2
        __init__(vectoritkContourSpatialObjectPoint2 self, std::vector< itkContourSpatialObjectPoint2 >::size_type size) -> vectoritkContourSpatialObjectPoint2
        __init__(vectoritkContourSpatialObjectPoint2 self, std::vector< itkContourSpatialObjectPoint2 >::size_type size, itkContourSpatialObjectPoint2 value) -> vectoritkContourSpatialObjectPoint2
        """
        _itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint2_swiginit(self, _itkContourSpatialObjectPointPython.new_vectoritkContourSpatialObjectPoint2(*args))
    push_back = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint2_push_back)
    front = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint2_front)
    back = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint2_back)
    assign = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint2_assign)
    resize = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint2_resize)
    insert = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint2_insert)
    reserve = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint2_reserve)
    capacity = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint2_capacity)
    __swig_destroy__ = _itkContourSpatialObjectPointPython.delete_vectoritkContourSpatialObjectPoint2

# Register vectoritkContourSpatialObjectPoint2 in _itkContourSpatialObjectPointPython:
_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint2_swigregister(vectoritkContourSpatialObjectPoint2)

class vectoritkContourSpatialObjectPoint3(object):
    r"""Proxy of C++ std::vector< itkContourSpatialObjectPoint3 > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint3_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint3___nonzero__)
    __bool__ = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint3___bool__)
    __len__ = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint3___len__)
    __getslice__ = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint3___getslice__)
    __setslice__ = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint3___setslice__)
    __delslice__ = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint3___delslice__)
    __delitem__ = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint3___delitem__)
    __getitem__ = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint3___getitem__)
    __setitem__ = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint3___setitem__)
    pop = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint3_pop)
    append = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint3_append)
    empty = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint3_empty)
    size = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint3_size)
    swap = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint3_swap)
    begin = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint3_begin)
    end = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint3_end)
    rbegin = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint3_rbegin)
    rend = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint3_rend)
    clear = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint3_clear)
    get_allocator = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint3_get_allocator)
    pop_back = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint3_pop_back)
    erase = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint3_erase)

    def __init__(self, *args):
        r"""
        __init__(vectoritkContourSpatialObjectPoint3 self) -> vectoritkContourSpatialObjectPoint3
        __init__(vectoritkContourSpatialObjectPoint3 self, vectoritkContourSpatialObjectPoint3 other) -> vectoritkContourSpatialObjectPoint3
        __init__(vectoritkContourSpatialObjectPoint3 self, std::vector< itkContourSpatialObjectPoint3 >::size_type size) -> vectoritkContourSpatialObjectPoint3
        __init__(vectoritkContourSpatialObjectPoint3 self, std::vector< itkContourSpatialObjectPoint3 >::size_type size, itkContourSpatialObjectPoint3 value) -> vectoritkContourSpatialObjectPoint3
        """
        _itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint3_swiginit(self, _itkContourSpatialObjectPointPython.new_vectoritkContourSpatialObjectPoint3(*args))
    push_back = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint3_push_back)
    front = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint3_front)
    back = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint3_back)
    assign = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint3_assign)
    resize = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint3_resize)
    insert = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint3_insert)
    reserve = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint3_reserve)
    capacity = _swig_new_instance_method(_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint3_capacity)
    __swig_destroy__ = _itkContourSpatialObjectPointPython.delete_vectoritkContourSpatialObjectPoint3

# Register vectoritkContourSpatialObjectPoint3 in _itkContourSpatialObjectPointPython:
_itkContourSpatialObjectPointPython.vectoritkContourSpatialObjectPoint3_swigregister(vectoritkContourSpatialObjectPoint3)

class itkContourSpatialObjectPoint2(itkSpatialObjectPointPython.itkSpatialObjectPoint2):
    r"""Proxy of C++ itkContourSpatialObjectPoint2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkContourSpatialObjectPointPython.delete_itkContourSpatialObjectPoint2
    GetPickedPointInObjectSpace = _swig_new_instance_method(_itkContourSpatialObjectPointPython.itkContourSpatialObjectPoint2_GetPickedPointInObjectSpace)
    SetPickedPointInObjectSpace = _swig_new_instance_method(_itkContourSpatialObjectPointPython.itkContourSpatialObjectPoint2_SetPickedPointInObjectSpace)
    GetNormalInObjectSpace = _swig_new_instance_method(_itkContourSpatialObjectPointPython.itkContourSpatialObjectPoint2_GetNormalInObjectSpace)
    SetNormalInObjectSpace = _swig_new_instance_method(_itkContourSpatialObjectPointPython.itkContourSpatialObjectPoint2_SetNormalInObjectSpace)

    def __init__(self, *args):
        r"""
        __init__(itkContourSpatialObjectPoint2 self) -> itkContourSpatialObjectPoint2
        __init__(itkContourSpatialObjectPoint2 self, itkContourSpatialObjectPoint2 arg0) -> itkContourSpatialObjectPoint2
        """
        _itkContourSpatialObjectPointPython.itkContourSpatialObjectPoint2_swiginit(self, _itkContourSpatialObjectPointPython.new_itkContourSpatialObjectPoint2(*args))

# Register itkContourSpatialObjectPoint2 in _itkContourSpatialObjectPointPython:
_itkContourSpatialObjectPointPython.itkContourSpatialObjectPoint2_swigregister(itkContourSpatialObjectPoint2)

class itkContourSpatialObjectPoint3(itkSpatialObjectPointPython.itkSpatialObjectPoint3):
    r"""Proxy of C++ itkContourSpatialObjectPoint3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _itkContourSpatialObjectPointPython.delete_itkContourSpatialObjectPoint3
    GetPickedPointInObjectSpace = _swig_new_instance_method(_itkContourSpatialObjectPointPython.itkContourSpatialObjectPoint3_GetPickedPointInObjectSpace)
    SetPickedPointInObjectSpace = _swig_new_instance_method(_itkContourSpatialObjectPointPython.itkContourSpatialObjectPoint3_SetPickedPointInObjectSpace)
    GetNormalInObjectSpace = _swig_new_instance_method(_itkContourSpatialObjectPointPython.itkContourSpatialObjectPoint3_GetNormalInObjectSpace)
    SetNormalInObjectSpace = _swig_new_instance_method(_itkContourSpatialObjectPointPython.itkContourSpatialObjectPoint3_SetNormalInObjectSpace)

    def __init__(self, *args):
        r"""
        __init__(itkContourSpatialObjectPoint3 self) -> itkContourSpatialObjectPoint3
        __init__(itkContourSpatialObjectPoint3 self, itkContourSpatialObjectPoint3 arg0) -> itkContourSpatialObjectPoint3
        """
        _itkContourSpatialObjectPointPython.itkContourSpatialObjectPoint3_swiginit(self, _itkContourSpatialObjectPointPython.new_itkContourSpatialObjectPoint3(*args))

# Register itkContourSpatialObjectPoint3 in _itkContourSpatialObjectPointPython:
_itkContourSpatialObjectPointPython.itkContourSpatialObjectPoint3_swigregister(itkContourSpatialObjectPoint3)



