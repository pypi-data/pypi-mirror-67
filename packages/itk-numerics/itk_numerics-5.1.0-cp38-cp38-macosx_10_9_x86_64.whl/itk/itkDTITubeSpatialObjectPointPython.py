# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkDTITubeSpatialObjectPointPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkDTITubeSpatialObjectPointPython', [dirname(__file__)])
        except ImportError:
            import _itkDTITubeSpatialObjectPointPython
            return _itkDTITubeSpatialObjectPointPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkDTITubeSpatialObjectPointPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkDTITubeSpatialObjectPointPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkDTITubeSpatialObjectPointPython
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrixPython
import stdcomplexPython
import pyBasePython
import vnl_vectorPython
import itkCovariantVectorPython
import itkVectorPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkPointPython
import vnl_matrix_fixedPython
import itkTubeSpatialObjectPointPython
import ITKCommonBasePython
import itkSpatialObjectPointPython
import itkRGBAPixelPython
import itkSpatialObjectBasePython
import itkImageRegionPython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkBoundingBoxPython
import itkMapContainerPython
import itkVectorContainerPython
import itkContinuousIndexPython
import itkSpatialObjectPropertyPython
import itkAffineTransformPython
import itkTransformBasePython
import itkArray2DPython
import itkArrayPython
import itkOptimizerParametersPython
import itkVariableLengthVectorPython
import itkMatrixOffsetTransformBasePython
class vectoritkDTITubeSpatialObjectPoint3(object):
    """Proxy of C++ std::vector<(itkDTITubeSpatialObjectPoint3)> class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def iterator(self) -> "swig::SwigPyIterator *":
        """iterator(vectoritkDTITubeSpatialObjectPoint3 self) -> SwigPyIterator"""
        return _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_iterator(self)

    def __iter__(self):
        return self.iterator()

    def __nonzero__(self) -> "bool":
        """__nonzero__(vectoritkDTITubeSpatialObjectPoint3 self) -> bool"""
        return _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3___nonzero__(self)


    def __bool__(self) -> "bool":
        """__bool__(vectoritkDTITubeSpatialObjectPoint3 self) -> bool"""
        return _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3___bool__(self)


    def __len__(self) -> "std::vector< itkDTITubeSpatialObjectPoint3 >::size_type":
        """__len__(vectoritkDTITubeSpatialObjectPoint3 self) -> std::vector< itkDTITubeSpatialObjectPoint3 >::size_type"""
        return _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3___len__(self)


    def __getslice__(self, i: 'std::vector< itkDTITubeSpatialObjectPoint3 >::difference_type', j: 'std::vector< itkDTITubeSpatialObjectPoint3 >::difference_type') -> "std::vector< itkDTITubeSpatialObjectPoint3,std::allocator< itkDTITubeSpatialObjectPoint3 > > *":
        """__getslice__(vectoritkDTITubeSpatialObjectPoint3 self, std::vector< itkDTITubeSpatialObjectPoint3 >::difference_type i, std::vector< itkDTITubeSpatialObjectPoint3 >::difference_type j) -> vectoritkDTITubeSpatialObjectPoint3"""
        return _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3___getslice__(self, i, j)


    def __setslice__(self, *args) -> "void":
        """
        __setslice__(vectoritkDTITubeSpatialObjectPoint3 self, std::vector< itkDTITubeSpatialObjectPoint3 >::difference_type i, std::vector< itkDTITubeSpatialObjectPoint3 >::difference_type j)
        __setslice__(vectoritkDTITubeSpatialObjectPoint3 self, std::vector< itkDTITubeSpatialObjectPoint3 >::difference_type i, std::vector< itkDTITubeSpatialObjectPoint3 >::difference_type j, vectoritkDTITubeSpatialObjectPoint3 v)
        """
        return _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3___setslice__(self, *args)


    def __delslice__(self, i: 'std::vector< itkDTITubeSpatialObjectPoint3 >::difference_type', j: 'std::vector< itkDTITubeSpatialObjectPoint3 >::difference_type') -> "void":
        """__delslice__(vectoritkDTITubeSpatialObjectPoint3 self, std::vector< itkDTITubeSpatialObjectPoint3 >::difference_type i, std::vector< itkDTITubeSpatialObjectPoint3 >::difference_type j)"""
        return _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3___delslice__(self, i, j)


    def __delitem__(self, *args) -> "void":
        """
        __delitem__(vectoritkDTITubeSpatialObjectPoint3 self, std::vector< itkDTITubeSpatialObjectPoint3 >::difference_type i)
        __delitem__(vectoritkDTITubeSpatialObjectPoint3 self, PySliceObject * slice)
        """
        return _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3___delitem__(self, *args)


    def __getitem__(self, *args) -> "std::vector< itkDTITubeSpatialObjectPoint3 >::value_type const &":
        """
        __getitem__(vectoritkDTITubeSpatialObjectPoint3 self, PySliceObject * slice) -> vectoritkDTITubeSpatialObjectPoint3
        __getitem__(vectoritkDTITubeSpatialObjectPoint3 self, std::vector< itkDTITubeSpatialObjectPoint3 >::difference_type i) -> itkDTITubeSpatialObjectPoint3
        """
        return _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3___getitem__(self, *args)


    def __setitem__(self, *args) -> "void":
        """
        __setitem__(vectoritkDTITubeSpatialObjectPoint3 self, PySliceObject * slice, vectoritkDTITubeSpatialObjectPoint3 v)
        __setitem__(vectoritkDTITubeSpatialObjectPoint3 self, PySliceObject * slice)
        __setitem__(vectoritkDTITubeSpatialObjectPoint3 self, std::vector< itkDTITubeSpatialObjectPoint3 >::difference_type i, itkDTITubeSpatialObjectPoint3 x)
        """
        return _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3___setitem__(self, *args)


    def pop(self) -> "std::vector< itkDTITubeSpatialObjectPoint3 >::value_type":
        """pop(vectoritkDTITubeSpatialObjectPoint3 self) -> itkDTITubeSpatialObjectPoint3"""
        return _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_pop(self)


    def append(self, x: 'itkDTITubeSpatialObjectPoint3') -> "void":
        """append(vectoritkDTITubeSpatialObjectPoint3 self, itkDTITubeSpatialObjectPoint3 x)"""
        return _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_append(self, x)


    def empty(self) -> "bool":
        """empty(vectoritkDTITubeSpatialObjectPoint3 self) -> bool"""
        return _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_empty(self)


    def size(self) -> "std::vector< itkDTITubeSpatialObjectPoint3 >::size_type":
        """size(vectoritkDTITubeSpatialObjectPoint3 self) -> std::vector< itkDTITubeSpatialObjectPoint3 >::size_type"""
        return _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_size(self)


    def swap(self, v: 'vectoritkDTITubeSpatialObjectPoint3') -> "void":
        """swap(vectoritkDTITubeSpatialObjectPoint3 self, vectoritkDTITubeSpatialObjectPoint3 v)"""
        return _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_swap(self, v)


    def begin(self) -> "std::vector< itkDTITubeSpatialObjectPoint3 >::iterator":
        """begin(vectoritkDTITubeSpatialObjectPoint3 self) -> std::vector< itkDTITubeSpatialObjectPoint3 >::iterator"""
        return _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_begin(self)


    def end(self) -> "std::vector< itkDTITubeSpatialObjectPoint3 >::iterator":
        """end(vectoritkDTITubeSpatialObjectPoint3 self) -> std::vector< itkDTITubeSpatialObjectPoint3 >::iterator"""
        return _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_end(self)


    def rbegin(self) -> "std::vector< itkDTITubeSpatialObjectPoint3 >::reverse_iterator":
        """rbegin(vectoritkDTITubeSpatialObjectPoint3 self) -> std::vector< itkDTITubeSpatialObjectPoint3 >::reverse_iterator"""
        return _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_rbegin(self)


    def rend(self) -> "std::vector< itkDTITubeSpatialObjectPoint3 >::reverse_iterator":
        """rend(vectoritkDTITubeSpatialObjectPoint3 self) -> std::vector< itkDTITubeSpatialObjectPoint3 >::reverse_iterator"""
        return _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_rend(self)


    def clear(self) -> "void":
        """clear(vectoritkDTITubeSpatialObjectPoint3 self)"""
        return _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_clear(self)


    def get_allocator(self) -> "std::vector< itkDTITubeSpatialObjectPoint3 >::allocator_type":
        """get_allocator(vectoritkDTITubeSpatialObjectPoint3 self) -> std::vector< itkDTITubeSpatialObjectPoint3 >::allocator_type"""
        return _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_get_allocator(self)


    def pop_back(self) -> "void":
        """pop_back(vectoritkDTITubeSpatialObjectPoint3 self)"""
        return _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_pop_back(self)


    def erase(self, *args) -> "std::vector< itkDTITubeSpatialObjectPoint3 >::iterator":
        """
        erase(vectoritkDTITubeSpatialObjectPoint3 self, std::vector< itkDTITubeSpatialObjectPoint3 >::iterator pos) -> std::vector< itkDTITubeSpatialObjectPoint3 >::iterator
        erase(vectoritkDTITubeSpatialObjectPoint3 self, std::vector< itkDTITubeSpatialObjectPoint3 >::iterator first, std::vector< itkDTITubeSpatialObjectPoint3 >::iterator last) -> std::vector< itkDTITubeSpatialObjectPoint3 >::iterator
        """
        return _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_erase(self, *args)


    def __init__(self, *args):
        """
        __init__(std::vector<(itkDTITubeSpatialObjectPoint3)> self) -> vectoritkDTITubeSpatialObjectPoint3
        __init__(std::vector<(itkDTITubeSpatialObjectPoint3)> self, vectoritkDTITubeSpatialObjectPoint3 arg2) -> vectoritkDTITubeSpatialObjectPoint3
        __init__(std::vector<(itkDTITubeSpatialObjectPoint3)> self, std::vector< itkDTITubeSpatialObjectPoint3 >::size_type size) -> vectoritkDTITubeSpatialObjectPoint3
        __init__(std::vector<(itkDTITubeSpatialObjectPoint3)> self, std::vector< itkDTITubeSpatialObjectPoint3 >::size_type size, itkDTITubeSpatialObjectPoint3 value) -> vectoritkDTITubeSpatialObjectPoint3
        """
        _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_swiginit(self, _itkDTITubeSpatialObjectPointPython.new_vectoritkDTITubeSpatialObjectPoint3(*args))

    def push_back(self, x: 'itkDTITubeSpatialObjectPoint3') -> "void":
        """push_back(vectoritkDTITubeSpatialObjectPoint3 self, itkDTITubeSpatialObjectPoint3 x)"""
        return _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_push_back(self, x)


    def front(self) -> "std::vector< itkDTITubeSpatialObjectPoint3 >::value_type const &":
        """front(vectoritkDTITubeSpatialObjectPoint3 self) -> itkDTITubeSpatialObjectPoint3"""
        return _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_front(self)


    def back(self) -> "std::vector< itkDTITubeSpatialObjectPoint3 >::value_type const &":
        """back(vectoritkDTITubeSpatialObjectPoint3 self) -> itkDTITubeSpatialObjectPoint3"""
        return _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_back(self)


    def assign(self, n: 'std::vector< itkDTITubeSpatialObjectPoint3 >::size_type', x: 'itkDTITubeSpatialObjectPoint3') -> "void":
        """assign(vectoritkDTITubeSpatialObjectPoint3 self, std::vector< itkDTITubeSpatialObjectPoint3 >::size_type n, itkDTITubeSpatialObjectPoint3 x)"""
        return _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_assign(self, n, x)


    def resize(self, *args) -> "void":
        """
        resize(vectoritkDTITubeSpatialObjectPoint3 self, std::vector< itkDTITubeSpatialObjectPoint3 >::size_type new_size)
        resize(vectoritkDTITubeSpatialObjectPoint3 self, std::vector< itkDTITubeSpatialObjectPoint3 >::size_type new_size, itkDTITubeSpatialObjectPoint3 x)
        """
        return _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_resize(self, *args)


    def insert(self, *args) -> "void":
        """
        insert(vectoritkDTITubeSpatialObjectPoint3 self, std::vector< itkDTITubeSpatialObjectPoint3 >::iterator pos, itkDTITubeSpatialObjectPoint3 x) -> std::vector< itkDTITubeSpatialObjectPoint3 >::iterator
        insert(vectoritkDTITubeSpatialObjectPoint3 self, std::vector< itkDTITubeSpatialObjectPoint3 >::iterator pos, std::vector< itkDTITubeSpatialObjectPoint3 >::size_type n, itkDTITubeSpatialObjectPoint3 x)
        """
        return _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_insert(self, *args)


    def reserve(self, n: 'std::vector< itkDTITubeSpatialObjectPoint3 >::size_type') -> "void":
        """reserve(vectoritkDTITubeSpatialObjectPoint3 self, std::vector< itkDTITubeSpatialObjectPoint3 >::size_type n)"""
        return _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_reserve(self, n)


    def capacity(self) -> "std::vector< itkDTITubeSpatialObjectPoint3 >::size_type":
        """capacity(vectoritkDTITubeSpatialObjectPoint3 self) -> std::vector< itkDTITubeSpatialObjectPoint3 >::size_type"""
        return _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_capacity(self)

    __swig_destroy__ = _itkDTITubeSpatialObjectPointPython.delete_vectoritkDTITubeSpatialObjectPoint3
vectoritkDTITubeSpatialObjectPoint3.iterator = new_instancemethod(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_iterator, None, vectoritkDTITubeSpatialObjectPoint3)
vectoritkDTITubeSpatialObjectPoint3.__nonzero__ = new_instancemethod(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3___nonzero__, None, vectoritkDTITubeSpatialObjectPoint3)
vectoritkDTITubeSpatialObjectPoint3.__bool__ = new_instancemethod(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3___bool__, None, vectoritkDTITubeSpatialObjectPoint3)
vectoritkDTITubeSpatialObjectPoint3.__len__ = new_instancemethod(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3___len__, None, vectoritkDTITubeSpatialObjectPoint3)
vectoritkDTITubeSpatialObjectPoint3.__getslice__ = new_instancemethod(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3___getslice__, None, vectoritkDTITubeSpatialObjectPoint3)
vectoritkDTITubeSpatialObjectPoint3.__setslice__ = new_instancemethod(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3___setslice__, None, vectoritkDTITubeSpatialObjectPoint3)
vectoritkDTITubeSpatialObjectPoint3.__delslice__ = new_instancemethod(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3___delslice__, None, vectoritkDTITubeSpatialObjectPoint3)
vectoritkDTITubeSpatialObjectPoint3.__delitem__ = new_instancemethod(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3___delitem__, None, vectoritkDTITubeSpatialObjectPoint3)
vectoritkDTITubeSpatialObjectPoint3.__getitem__ = new_instancemethod(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3___getitem__, None, vectoritkDTITubeSpatialObjectPoint3)
vectoritkDTITubeSpatialObjectPoint3.__setitem__ = new_instancemethod(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3___setitem__, None, vectoritkDTITubeSpatialObjectPoint3)
vectoritkDTITubeSpatialObjectPoint3.pop = new_instancemethod(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_pop, None, vectoritkDTITubeSpatialObjectPoint3)
vectoritkDTITubeSpatialObjectPoint3.append = new_instancemethod(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_append, None, vectoritkDTITubeSpatialObjectPoint3)
vectoritkDTITubeSpatialObjectPoint3.empty = new_instancemethod(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_empty, None, vectoritkDTITubeSpatialObjectPoint3)
vectoritkDTITubeSpatialObjectPoint3.size = new_instancemethod(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_size, None, vectoritkDTITubeSpatialObjectPoint3)
vectoritkDTITubeSpatialObjectPoint3.swap = new_instancemethod(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_swap, None, vectoritkDTITubeSpatialObjectPoint3)
vectoritkDTITubeSpatialObjectPoint3.begin = new_instancemethod(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_begin, None, vectoritkDTITubeSpatialObjectPoint3)
vectoritkDTITubeSpatialObjectPoint3.end = new_instancemethod(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_end, None, vectoritkDTITubeSpatialObjectPoint3)
vectoritkDTITubeSpatialObjectPoint3.rbegin = new_instancemethod(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_rbegin, None, vectoritkDTITubeSpatialObjectPoint3)
vectoritkDTITubeSpatialObjectPoint3.rend = new_instancemethod(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_rend, None, vectoritkDTITubeSpatialObjectPoint3)
vectoritkDTITubeSpatialObjectPoint3.clear = new_instancemethod(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_clear, None, vectoritkDTITubeSpatialObjectPoint3)
vectoritkDTITubeSpatialObjectPoint3.get_allocator = new_instancemethod(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_get_allocator, None, vectoritkDTITubeSpatialObjectPoint3)
vectoritkDTITubeSpatialObjectPoint3.pop_back = new_instancemethod(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_pop_back, None, vectoritkDTITubeSpatialObjectPoint3)
vectoritkDTITubeSpatialObjectPoint3.erase = new_instancemethod(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_erase, None, vectoritkDTITubeSpatialObjectPoint3)
vectoritkDTITubeSpatialObjectPoint3.push_back = new_instancemethod(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_push_back, None, vectoritkDTITubeSpatialObjectPoint3)
vectoritkDTITubeSpatialObjectPoint3.front = new_instancemethod(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_front, None, vectoritkDTITubeSpatialObjectPoint3)
vectoritkDTITubeSpatialObjectPoint3.back = new_instancemethod(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_back, None, vectoritkDTITubeSpatialObjectPoint3)
vectoritkDTITubeSpatialObjectPoint3.assign = new_instancemethod(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_assign, None, vectoritkDTITubeSpatialObjectPoint3)
vectoritkDTITubeSpatialObjectPoint3.resize = new_instancemethod(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_resize, None, vectoritkDTITubeSpatialObjectPoint3)
vectoritkDTITubeSpatialObjectPoint3.insert = new_instancemethod(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_insert, None, vectoritkDTITubeSpatialObjectPoint3)
vectoritkDTITubeSpatialObjectPoint3.reserve = new_instancemethod(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_reserve, None, vectoritkDTITubeSpatialObjectPoint3)
vectoritkDTITubeSpatialObjectPoint3.capacity = new_instancemethod(_itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_capacity, None, vectoritkDTITubeSpatialObjectPoint3)
vectoritkDTITubeSpatialObjectPoint3_swigregister = _itkDTITubeSpatialObjectPointPython.vectoritkDTITubeSpatialObjectPoint3_swigregister
vectoritkDTITubeSpatialObjectPoint3_swigregister(vectoritkDTITubeSpatialObjectPoint3)

class itkDTITubeSpatialObjectPoint3(itkTubeSpatialObjectPointPython.itkTubeSpatialObjectPoint3):
    """


    Point used for a tube definition.

    This class contains all the functions necessary to define a point that
    can be used to build tubes.

    See:   DTITubeSpatialObject

    C++ includes: itkDTITubeSpatialObjectPoint.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkDTITubeSpatialObjectPointPython.delete_itkDTITubeSpatialObjectPoint3

    def SetTensorMatrix(self, *args) -> "void":
        """
        SetTensorMatrix(itkDTITubeSpatialObjectPoint3 self, itkDiffusionTensor3DD matrix)
        SetTensorMatrix(itkDTITubeSpatialObjectPoint3 self, itkDiffusionTensor3DF matrix)
        SetTensorMatrix(itkDTITubeSpatialObjectPoint3 self, float const * matrix)

        Set/Get the tensor
        matrix 
        """
        return _itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_SetTensorMatrix(self, *args)


    def GetTensorMatrix(self) -> "float const *":
        """GetTensorMatrix(itkDTITubeSpatialObjectPoint3 self) -> float const *"""
        return _itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_GetTensorMatrix(self)


    def AddField(self, *args) -> "void":
        """
        AddField(itkDTITubeSpatialObjectPoint3 self, char const * name, float value)
        AddField(itkDTITubeSpatialObjectPoint3 self, itkDTITubeSpatialObjectPointEnums::DTITubeSpatialObjectPointField name, float value)

        Add a field to the point
        list 
        """
        return _itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_AddField(self, *args)


    def SetField(self, *args) -> "void":
        """
        SetField(itkDTITubeSpatialObjectPoint3 self, itkDTITubeSpatialObjectPointEnums::DTITubeSpatialObjectPointField name, float value)
        SetField(itkDTITubeSpatialObjectPoint3 self, char const * name, float value)

        Set a field value 
        """
        return _itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_SetField(self, *args)


    def GetFields(self) -> "std::vector< std::pair< std::string,float >,std::allocator< std::pair< std::string,float > > > const &":
        """
        GetFields(itkDTITubeSpatialObjectPoint3 self) -> std::vector< std::pair< std::string,float >,std::allocator< std::pair< std::string,float > > > const &

        Return the list of extra
        fields 
        """
        return _itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_GetFields(self)


    def GetField(self, *args) -> "float":
        """
        GetField(itkDTITubeSpatialObjectPoint3 self, char const * name) -> float
        GetField(itkDTITubeSpatialObjectPoint3 self, itkDTITubeSpatialObjectPointEnums::DTITubeSpatialObjectPointField name) -> float

        Return the value of the
        specific fiedls 
        """
        return _itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_GetField(self, *args)


    def __init__(self, *args):
        """
        __init__(itkDTITubeSpatialObjectPoint3 self) -> itkDTITubeSpatialObjectPoint3
        __init__(itkDTITubeSpatialObjectPoint3 self, itkDTITubeSpatialObjectPoint3 arg0) -> itkDTITubeSpatialObjectPoint3



        Point used for a tube definition.

        This class contains all the functions necessary to define a point that
        can be used to build tubes.

        See:   DTITubeSpatialObject

        C++ includes: itkDTITubeSpatialObjectPoint.h 
        """
        _itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_swiginit(self, _itkDTITubeSpatialObjectPointPython.new_itkDTITubeSpatialObjectPoint3(*args))
itkDTITubeSpatialObjectPoint3.SetTensorMatrix = new_instancemethod(_itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_SetTensorMatrix, None, itkDTITubeSpatialObjectPoint3)
itkDTITubeSpatialObjectPoint3.GetTensorMatrix = new_instancemethod(_itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_GetTensorMatrix, None, itkDTITubeSpatialObjectPoint3)
itkDTITubeSpatialObjectPoint3.AddField = new_instancemethod(_itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_AddField, None, itkDTITubeSpatialObjectPoint3)
itkDTITubeSpatialObjectPoint3.SetField = new_instancemethod(_itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_SetField, None, itkDTITubeSpatialObjectPoint3)
itkDTITubeSpatialObjectPoint3.GetFields = new_instancemethod(_itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_GetFields, None, itkDTITubeSpatialObjectPoint3)
itkDTITubeSpatialObjectPoint3.GetField = new_instancemethod(_itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_GetField, None, itkDTITubeSpatialObjectPoint3)
itkDTITubeSpatialObjectPoint3_swigregister = _itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPoint3_swigregister
itkDTITubeSpatialObjectPoint3_swigregister(itkDTITubeSpatialObjectPoint3)

class itkDTITubeSpatialObjectPointEnums(object):
    """Proxy of C++ itkDTITubeSpatialObjectPointEnums class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    DTITubeSpatialObjectPointField_FA = _itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPointEnums_DTITubeSpatialObjectPointField_FA
    DTITubeSpatialObjectPointField_ADC = _itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPointEnums_DTITubeSpatialObjectPointField_ADC
    DTITubeSpatialObjectPointField_GA = _itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPointEnums_DTITubeSpatialObjectPointField_GA

    def __init__(self, *args):
        """
        __init__(itkDTITubeSpatialObjectPointEnums self) -> itkDTITubeSpatialObjectPointEnums
        __init__(itkDTITubeSpatialObjectPointEnums self, itkDTITubeSpatialObjectPointEnums arg0) -> itkDTITubeSpatialObjectPointEnums
        """
        _itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPointEnums_swiginit(self, _itkDTITubeSpatialObjectPointPython.new_itkDTITubeSpatialObjectPointEnums(*args))
    __swig_destroy__ = _itkDTITubeSpatialObjectPointPython.delete_itkDTITubeSpatialObjectPointEnums
itkDTITubeSpatialObjectPointEnums_swigregister = _itkDTITubeSpatialObjectPointPython.itkDTITubeSpatialObjectPointEnums_swigregister
itkDTITubeSpatialObjectPointEnums_swigregister(itkDTITubeSpatialObjectPointEnums)



