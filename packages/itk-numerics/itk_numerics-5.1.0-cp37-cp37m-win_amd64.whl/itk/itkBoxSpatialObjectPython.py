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
    from . import _itkBoxSpatialObjectPython
else:
    import _itkBoxSpatialObjectPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkBoxSpatialObjectPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkBoxSpatialObjectPython.SWIG_PyStaticMethod_New

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


import itkFixedArrayPython
import pyBasePython
import itkSpatialObjectBasePython
import itkBoundingBoxPython
import ITKCommonBasePython
import itkVectorContainerPython
import itkVectorPython
import vnl_vector_refPython
import stdcomplexPython
import vnl_vectorPython
import vnl_matrixPython
import itkOffsetPython
import itkSizePython
import itkMatrixPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import itkPointPython
import itkContinuousIndexPython
import itkIndexPython
import itkMapContainerPython
import itkImageRegionPython
import itkAffineTransformPython
import itkMatrixOffsetTransformBasePython
import itkArray2DPython
import itkOptimizerParametersPython
import itkArrayPython
import itkVariableLengthVectorPython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkTransformBasePython
import itkSpatialObjectPropertyPython
import itkRGBAPixelPython

def itkBoxSpatialObject3_New():
  return itkBoxSpatialObject3.New()


def itkBoxSpatialObject2_New():
  return itkBoxSpatialObject2.New()

class listitkBoxSpatialObject2_Pointer(object):
    r"""Proxy of C++ std::list< itkBoxSpatialObject2_Pointer > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer___nonzero__)
    __bool__ = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer___bool__)
    __len__ = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer___len__)
    __getslice__ = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer___getslice__)
    __setslice__ = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer___setslice__)
    __delslice__ = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer___delslice__)
    __delitem__ = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer___delitem__)
    __getitem__ = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer___getitem__)
    __setitem__ = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer___setitem__)
    pop = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer_pop)
    append = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer_append)
    empty = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer_empty)
    size = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer_size)
    swap = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer_swap)
    begin = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer_begin)
    end = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer_end)
    rbegin = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer_rbegin)
    rend = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer_rend)
    clear = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer_clear)
    get_allocator = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer_get_allocator)
    pop_back = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer_pop_back)
    erase = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer_erase)

    def __init__(self, *args):
        r"""
        __init__(listitkBoxSpatialObject2_Pointer self) -> listitkBoxSpatialObject2_Pointer
        __init__(listitkBoxSpatialObject2_Pointer self, listitkBoxSpatialObject2_Pointer other) -> listitkBoxSpatialObject2_Pointer
        __init__(listitkBoxSpatialObject2_Pointer self, std::list< itkBoxSpatialObject2_Pointer >::size_type size) -> listitkBoxSpatialObject2_Pointer
        __init__(listitkBoxSpatialObject2_Pointer self, std::list< itkBoxSpatialObject2_Pointer >::size_type size, std::list< itkBoxSpatialObject2_Pointer >::value_type const & value) -> listitkBoxSpatialObject2_Pointer
        """
        _itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer_swiginit(self, _itkBoxSpatialObjectPython.new_listitkBoxSpatialObject2_Pointer(*args))
    push_back = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer_push_back)
    front = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer_front)
    back = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer_back)
    assign = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer_assign)
    resize = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer_resize)
    insert = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer_insert)
    pop_front = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer_pop_front)
    push_front = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer_push_front)
    reverse = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer_reverse)
    __swig_destroy__ = _itkBoxSpatialObjectPython.delete_listitkBoxSpatialObject2_Pointer

# Register listitkBoxSpatialObject2_Pointer in _itkBoxSpatialObjectPython:
_itkBoxSpatialObjectPython.listitkBoxSpatialObject2_Pointer_swigregister(listitkBoxSpatialObject2_Pointer)

class listitkBoxSpatialObject3_Pointer(object):
    r"""Proxy of C++ std::list< itkBoxSpatialObject3_Pointer > class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    iterator = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer_iterator)
    def __iter__(self):
        return self.iterator()
    __nonzero__ = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer___nonzero__)
    __bool__ = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer___bool__)
    __len__ = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer___len__)
    __getslice__ = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer___getslice__)
    __setslice__ = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer___setslice__)
    __delslice__ = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer___delslice__)
    __delitem__ = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer___delitem__)
    __getitem__ = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer___getitem__)
    __setitem__ = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer___setitem__)
    pop = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer_pop)
    append = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer_append)
    empty = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer_empty)
    size = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer_size)
    swap = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer_swap)
    begin = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer_begin)
    end = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer_end)
    rbegin = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer_rbegin)
    rend = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer_rend)
    clear = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer_clear)
    get_allocator = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer_get_allocator)
    pop_back = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer_pop_back)
    erase = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer_erase)

    def __init__(self, *args):
        r"""
        __init__(listitkBoxSpatialObject3_Pointer self) -> listitkBoxSpatialObject3_Pointer
        __init__(listitkBoxSpatialObject3_Pointer self, listitkBoxSpatialObject3_Pointer other) -> listitkBoxSpatialObject3_Pointer
        __init__(listitkBoxSpatialObject3_Pointer self, std::list< itkBoxSpatialObject3_Pointer >::size_type size) -> listitkBoxSpatialObject3_Pointer
        __init__(listitkBoxSpatialObject3_Pointer self, std::list< itkBoxSpatialObject3_Pointer >::size_type size, std::list< itkBoxSpatialObject3_Pointer >::value_type const & value) -> listitkBoxSpatialObject3_Pointer
        """
        _itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer_swiginit(self, _itkBoxSpatialObjectPython.new_listitkBoxSpatialObject3_Pointer(*args))
    push_back = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer_push_back)
    front = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer_front)
    back = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer_back)
    assign = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer_assign)
    resize = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer_resize)
    insert = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer_insert)
    pop_front = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer_pop_front)
    push_front = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer_push_front)
    reverse = _swig_new_instance_method(_itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer_reverse)
    __swig_destroy__ = _itkBoxSpatialObjectPython.delete_listitkBoxSpatialObject3_Pointer

# Register listitkBoxSpatialObject3_Pointer in _itkBoxSpatialObjectPython:
_itkBoxSpatialObjectPython.listitkBoxSpatialObject3_Pointer_swigregister(listitkBoxSpatialObject3_Pointer)

class itkBoxSpatialObject2(itkSpatialObjectBasePython.itkSpatialObject2):
    r"""Proxy of C++ itkBoxSpatialObject2 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBoxSpatialObjectPython.itkBoxSpatialObject2___New_orig__)
    Clone = _swig_new_instance_method(_itkBoxSpatialObjectPython.itkBoxSpatialObject2_Clone)
    SetSizeInObjectSpace = _swig_new_instance_method(_itkBoxSpatialObjectPython.itkBoxSpatialObject2_SetSizeInObjectSpace)
    GetSizeInObjectSpace = _swig_new_instance_method(_itkBoxSpatialObjectPython.itkBoxSpatialObject2_GetSizeInObjectSpace)
    SetPositionInObjectSpace = _swig_new_instance_method(_itkBoxSpatialObjectPython.itkBoxSpatialObject2_SetPositionInObjectSpace)
    GetPositionInObjectSpace = _swig_new_instance_method(_itkBoxSpatialObjectPython.itkBoxSpatialObject2_GetPositionInObjectSpace)
    __swig_destroy__ = _itkBoxSpatialObjectPython.delete_itkBoxSpatialObject2
    cast = _swig_new_static_method(_itkBoxSpatialObjectPython.itkBoxSpatialObject2_cast)

    def New(*args, **kargs):
        """New() -> itkBoxSpatialObject2

        Create a new object of the class itkBoxSpatialObject2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBoxSpatialObject2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBoxSpatialObject2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBoxSpatialObject2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBoxSpatialObject2 in _itkBoxSpatialObjectPython:
_itkBoxSpatialObjectPython.itkBoxSpatialObject2_swigregister(itkBoxSpatialObject2)
itkBoxSpatialObject2___New_orig__ = _itkBoxSpatialObjectPython.itkBoxSpatialObject2___New_orig__
itkBoxSpatialObject2_cast = _itkBoxSpatialObjectPython.itkBoxSpatialObject2_cast

class itkBoxSpatialObject3(itkSpatialObjectBasePython.itkSpatialObject3):
    r"""Proxy of C++ itkBoxSpatialObject3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBoxSpatialObjectPython.itkBoxSpatialObject3___New_orig__)
    Clone = _swig_new_instance_method(_itkBoxSpatialObjectPython.itkBoxSpatialObject3_Clone)
    SetSizeInObjectSpace = _swig_new_instance_method(_itkBoxSpatialObjectPython.itkBoxSpatialObject3_SetSizeInObjectSpace)
    GetSizeInObjectSpace = _swig_new_instance_method(_itkBoxSpatialObjectPython.itkBoxSpatialObject3_GetSizeInObjectSpace)
    SetPositionInObjectSpace = _swig_new_instance_method(_itkBoxSpatialObjectPython.itkBoxSpatialObject3_SetPositionInObjectSpace)
    GetPositionInObjectSpace = _swig_new_instance_method(_itkBoxSpatialObjectPython.itkBoxSpatialObject3_GetPositionInObjectSpace)
    __swig_destroy__ = _itkBoxSpatialObjectPython.delete_itkBoxSpatialObject3
    cast = _swig_new_static_method(_itkBoxSpatialObjectPython.itkBoxSpatialObject3_cast)

    def New(*args, **kargs):
        """New() -> itkBoxSpatialObject3

        Create a new object of the class itkBoxSpatialObject3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBoxSpatialObject3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBoxSpatialObject3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBoxSpatialObject3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBoxSpatialObject3 in _itkBoxSpatialObjectPython:
_itkBoxSpatialObjectPython.itkBoxSpatialObject3_swigregister(itkBoxSpatialObject3)
itkBoxSpatialObject3___New_orig__ = _itkBoxSpatialObjectPython.itkBoxSpatialObject3___New_orig__
itkBoxSpatialObject3_cast = _itkBoxSpatialObjectPython.itkBoxSpatialObject3_cast



