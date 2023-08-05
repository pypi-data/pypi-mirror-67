# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkAndImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkAndImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkAndImageFilterPython
            return _itkAndImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkAndImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkAndImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkAndImageFilterPython
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


import ITKCommonBasePython
import pyBasePython
import itkBinaryGeneratorImageFilterPython
import itkRGBAPixelPython
import itkFixedArrayPython
import itkInPlaceImageFilterBPython
import itkImageToImageFilterBPython
import itkImagePython
import itkVectorPython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython
import vnl_vector_refPython
import itkSizePython
import itkOffsetPython
import itkRGBPixelPython
import itkCovariantVectorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkPointPython
import itkSymmetricSecondRankTensorPython
import itkImageRegionPython
import itkIndexPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterAPython
import itkSimpleDataObjectDecoratorPython
import itkArrayPython

def itkAndImageFilterISS3ISS3ISS3_New():
  return itkAndImageFilterISS3ISS3ISS3.New()


def itkAndImageFilterISS2ISS2ISS2_New():
  return itkAndImageFilterISS2ISS2ISS2.New()


def itkAndImageFilterIUS3IUS3IUS3_New():
  return itkAndImageFilterIUS3IUS3IUS3.New()


def itkAndImageFilterIUS2IUS2IUS2_New():
  return itkAndImageFilterIUS2IUS2IUS2.New()


def itkAndImageFilterIUC3IUC3IUC3_New():
  return itkAndImageFilterIUC3IUC3IUC3.New()


def itkAndImageFilterIUC2IUC2IUC2_New():
  return itkAndImageFilterIUC2IUC2IUC2.New()

class itkAndImageFilterISS2ISS2ISS2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterISS2ISS2ISS2):
    """


    Implements the AND bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise AND operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be Where "&" is the bitwise
    AND operator in C++.

    C++ includes: itkAndImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAndImageFilterISS2ISS2ISS2_Pointer":
        """__New_orig__() -> itkAndImageFilterISS2ISS2ISS2_Pointer"""
        return _itkAndImageFilterPython.itkAndImageFilterISS2ISS2ISS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAndImageFilterISS2ISS2ISS2_Pointer":
        """Clone(itkAndImageFilterISS2ISS2ISS2 self) -> itkAndImageFilterISS2ISS2ISS2_Pointer"""
        return _itkAndImageFilterPython.itkAndImageFilterISS2ISS2ISS2_Clone(self)

    Input1Input2OutputBitwiseOperatorsCheck = _itkAndImageFilterPython.itkAndImageFilterISS2ISS2ISS2_Input1Input2OutputBitwiseOperatorsCheck
    __swig_destroy__ = _itkAndImageFilterPython.delete_itkAndImageFilterISS2ISS2ISS2

    def cast(obj: 'itkLightObject') -> "itkAndImageFilterISS2ISS2ISS2 *":
        """cast(itkLightObject obj) -> itkAndImageFilterISS2ISS2ISS2"""
        return _itkAndImageFilterPython.itkAndImageFilterISS2ISS2ISS2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkAndImageFilterISS2ISS2ISS2

        Create a new object of the class itkAndImageFilterISS2ISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAndImageFilterISS2ISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAndImageFilterISS2ISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAndImageFilterISS2ISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAndImageFilterISS2ISS2ISS2.Clone = new_instancemethod(_itkAndImageFilterPython.itkAndImageFilterISS2ISS2ISS2_Clone, None, itkAndImageFilterISS2ISS2ISS2)
itkAndImageFilterISS2ISS2ISS2_swigregister = _itkAndImageFilterPython.itkAndImageFilterISS2ISS2ISS2_swigregister
itkAndImageFilterISS2ISS2ISS2_swigregister(itkAndImageFilterISS2ISS2ISS2)

def itkAndImageFilterISS2ISS2ISS2___New_orig__() -> "itkAndImageFilterISS2ISS2ISS2_Pointer":
    """itkAndImageFilterISS2ISS2ISS2___New_orig__() -> itkAndImageFilterISS2ISS2ISS2_Pointer"""
    return _itkAndImageFilterPython.itkAndImageFilterISS2ISS2ISS2___New_orig__()

def itkAndImageFilterISS2ISS2ISS2_cast(obj: 'itkLightObject') -> "itkAndImageFilterISS2ISS2ISS2 *":
    """itkAndImageFilterISS2ISS2ISS2_cast(itkLightObject obj) -> itkAndImageFilterISS2ISS2ISS2"""
    return _itkAndImageFilterPython.itkAndImageFilterISS2ISS2ISS2_cast(obj)

class itkAndImageFilterISS3ISS3ISS3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterISS3ISS3ISS3):
    """


    Implements the AND bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise AND operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be Where "&" is the bitwise
    AND operator in C++.

    C++ includes: itkAndImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAndImageFilterISS3ISS3ISS3_Pointer":
        """__New_orig__() -> itkAndImageFilterISS3ISS3ISS3_Pointer"""
        return _itkAndImageFilterPython.itkAndImageFilterISS3ISS3ISS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAndImageFilterISS3ISS3ISS3_Pointer":
        """Clone(itkAndImageFilterISS3ISS3ISS3 self) -> itkAndImageFilterISS3ISS3ISS3_Pointer"""
        return _itkAndImageFilterPython.itkAndImageFilterISS3ISS3ISS3_Clone(self)

    Input1Input2OutputBitwiseOperatorsCheck = _itkAndImageFilterPython.itkAndImageFilterISS3ISS3ISS3_Input1Input2OutputBitwiseOperatorsCheck
    __swig_destroy__ = _itkAndImageFilterPython.delete_itkAndImageFilterISS3ISS3ISS3

    def cast(obj: 'itkLightObject') -> "itkAndImageFilterISS3ISS3ISS3 *":
        """cast(itkLightObject obj) -> itkAndImageFilterISS3ISS3ISS3"""
        return _itkAndImageFilterPython.itkAndImageFilterISS3ISS3ISS3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkAndImageFilterISS3ISS3ISS3

        Create a new object of the class itkAndImageFilterISS3ISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAndImageFilterISS3ISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAndImageFilterISS3ISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAndImageFilterISS3ISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAndImageFilterISS3ISS3ISS3.Clone = new_instancemethod(_itkAndImageFilterPython.itkAndImageFilterISS3ISS3ISS3_Clone, None, itkAndImageFilterISS3ISS3ISS3)
itkAndImageFilterISS3ISS3ISS3_swigregister = _itkAndImageFilterPython.itkAndImageFilterISS3ISS3ISS3_swigregister
itkAndImageFilterISS3ISS3ISS3_swigregister(itkAndImageFilterISS3ISS3ISS3)

def itkAndImageFilterISS3ISS3ISS3___New_orig__() -> "itkAndImageFilterISS3ISS3ISS3_Pointer":
    """itkAndImageFilterISS3ISS3ISS3___New_orig__() -> itkAndImageFilterISS3ISS3ISS3_Pointer"""
    return _itkAndImageFilterPython.itkAndImageFilterISS3ISS3ISS3___New_orig__()

def itkAndImageFilterISS3ISS3ISS3_cast(obj: 'itkLightObject') -> "itkAndImageFilterISS3ISS3ISS3 *":
    """itkAndImageFilterISS3ISS3ISS3_cast(itkLightObject obj) -> itkAndImageFilterISS3ISS3ISS3"""
    return _itkAndImageFilterPython.itkAndImageFilterISS3ISS3ISS3_cast(obj)

class itkAndImageFilterIUC2IUC2IUC2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUC2IUC2IUC2):
    """


    Implements the AND bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise AND operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be Where "&" is the bitwise
    AND operator in C++.

    C++ includes: itkAndImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAndImageFilterIUC2IUC2IUC2_Pointer":
        """__New_orig__() -> itkAndImageFilterIUC2IUC2IUC2_Pointer"""
        return _itkAndImageFilterPython.itkAndImageFilterIUC2IUC2IUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAndImageFilterIUC2IUC2IUC2_Pointer":
        """Clone(itkAndImageFilterIUC2IUC2IUC2 self) -> itkAndImageFilterIUC2IUC2IUC2_Pointer"""
        return _itkAndImageFilterPython.itkAndImageFilterIUC2IUC2IUC2_Clone(self)

    Input1Input2OutputBitwiseOperatorsCheck = _itkAndImageFilterPython.itkAndImageFilterIUC2IUC2IUC2_Input1Input2OutputBitwiseOperatorsCheck
    __swig_destroy__ = _itkAndImageFilterPython.delete_itkAndImageFilterIUC2IUC2IUC2

    def cast(obj: 'itkLightObject') -> "itkAndImageFilterIUC2IUC2IUC2 *":
        """cast(itkLightObject obj) -> itkAndImageFilterIUC2IUC2IUC2"""
        return _itkAndImageFilterPython.itkAndImageFilterIUC2IUC2IUC2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkAndImageFilterIUC2IUC2IUC2

        Create a new object of the class itkAndImageFilterIUC2IUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAndImageFilterIUC2IUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAndImageFilterIUC2IUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAndImageFilterIUC2IUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAndImageFilterIUC2IUC2IUC2.Clone = new_instancemethod(_itkAndImageFilterPython.itkAndImageFilterIUC2IUC2IUC2_Clone, None, itkAndImageFilterIUC2IUC2IUC2)
itkAndImageFilterIUC2IUC2IUC2_swigregister = _itkAndImageFilterPython.itkAndImageFilterIUC2IUC2IUC2_swigregister
itkAndImageFilterIUC2IUC2IUC2_swigregister(itkAndImageFilterIUC2IUC2IUC2)

def itkAndImageFilterIUC2IUC2IUC2___New_orig__() -> "itkAndImageFilterIUC2IUC2IUC2_Pointer":
    """itkAndImageFilterIUC2IUC2IUC2___New_orig__() -> itkAndImageFilterIUC2IUC2IUC2_Pointer"""
    return _itkAndImageFilterPython.itkAndImageFilterIUC2IUC2IUC2___New_orig__()

def itkAndImageFilterIUC2IUC2IUC2_cast(obj: 'itkLightObject') -> "itkAndImageFilterIUC2IUC2IUC2 *":
    """itkAndImageFilterIUC2IUC2IUC2_cast(itkLightObject obj) -> itkAndImageFilterIUC2IUC2IUC2"""
    return _itkAndImageFilterPython.itkAndImageFilterIUC2IUC2IUC2_cast(obj)

class itkAndImageFilterIUC3IUC3IUC3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUC3IUC3IUC3):
    """


    Implements the AND bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise AND operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be Where "&" is the bitwise
    AND operator in C++.

    C++ includes: itkAndImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAndImageFilterIUC3IUC3IUC3_Pointer":
        """__New_orig__() -> itkAndImageFilterIUC3IUC3IUC3_Pointer"""
        return _itkAndImageFilterPython.itkAndImageFilterIUC3IUC3IUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAndImageFilterIUC3IUC3IUC3_Pointer":
        """Clone(itkAndImageFilterIUC3IUC3IUC3 self) -> itkAndImageFilterIUC3IUC3IUC3_Pointer"""
        return _itkAndImageFilterPython.itkAndImageFilterIUC3IUC3IUC3_Clone(self)

    Input1Input2OutputBitwiseOperatorsCheck = _itkAndImageFilterPython.itkAndImageFilterIUC3IUC3IUC3_Input1Input2OutputBitwiseOperatorsCheck
    __swig_destroy__ = _itkAndImageFilterPython.delete_itkAndImageFilterIUC3IUC3IUC3

    def cast(obj: 'itkLightObject') -> "itkAndImageFilterIUC3IUC3IUC3 *":
        """cast(itkLightObject obj) -> itkAndImageFilterIUC3IUC3IUC3"""
        return _itkAndImageFilterPython.itkAndImageFilterIUC3IUC3IUC3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkAndImageFilterIUC3IUC3IUC3

        Create a new object of the class itkAndImageFilterIUC3IUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAndImageFilterIUC3IUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAndImageFilterIUC3IUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAndImageFilterIUC3IUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAndImageFilterIUC3IUC3IUC3.Clone = new_instancemethod(_itkAndImageFilterPython.itkAndImageFilterIUC3IUC3IUC3_Clone, None, itkAndImageFilterIUC3IUC3IUC3)
itkAndImageFilterIUC3IUC3IUC3_swigregister = _itkAndImageFilterPython.itkAndImageFilterIUC3IUC3IUC3_swigregister
itkAndImageFilterIUC3IUC3IUC3_swigregister(itkAndImageFilterIUC3IUC3IUC3)

def itkAndImageFilterIUC3IUC3IUC3___New_orig__() -> "itkAndImageFilterIUC3IUC3IUC3_Pointer":
    """itkAndImageFilterIUC3IUC3IUC3___New_orig__() -> itkAndImageFilterIUC3IUC3IUC3_Pointer"""
    return _itkAndImageFilterPython.itkAndImageFilterIUC3IUC3IUC3___New_orig__()

def itkAndImageFilterIUC3IUC3IUC3_cast(obj: 'itkLightObject') -> "itkAndImageFilterIUC3IUC3IUC3 *":
    """itkAndImageFilterIUC3IUC3IUC3_cast(itkLightObject obj) -> itkAndImageFilterIUC3IUC3IUC3"""
    return _itkAndImageFilterPython.itkAndImageFilterIUC3IUC3IUC3_cast(obj)

class itkAndImageFilterIUS2IUS2IUS2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUS2IUS2IUS2):
    """


    Implements the AND bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise AND operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be Where "&" is the bitwise
    AND operator in C++.

    C++ includes: itkAndImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAndImageFilterIUS2IUS2IUS2_Pointer":
        """__New_orig__() -> itkAndImageFilterIUS2IUS2IUS2_Pointer"""
        return _itkAndImageFilterPython.itkAndImageFilterIUS2IUS2IUS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAndImageFilterIUS2IUS2IUS2_Pointer":
        """Clone(itkAndImageFilterIUS2IUS2IUS2 self) -> itkAndImageFilterIUS2IUS2IUS2_Pointer"""
        return _itkAndImageFilterPython.itkAndImageFilterIUS2IUS2IUS2_Clone(self)

    Input1Input2OutputBitwiseOperatorsCheck = _itkAndImageFilterPython.itkAndImageFilterIUS2IUS2IUS2_Input1Input2OutputBitwiseOperatorsCheck
    __swig_destroy__ = _itkAndImageFilterPython.delete_itkAndImageFilterIUS2IUS2IUS2

    def cast(obj: 'itkLightObject') -> "itkAndImageFilterIUS2IUS2IUS2 *":
        """cast(itkLightObject obj) -> itkAndImageFilterIUS2IUS2IUS2"""
        return _itkAndImageFilterPython.itkAndImageFilterIUS2IUS2IUS2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkAndImageFilterIUS2IUS2IUS2

        Create a new object of the class itkAndImageFilterIUS2IUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAndImageFilterIUS2IUS2IUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAndImageFilterIUS2IUS2IUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAndImageFilterIUS2IUS2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAndImageFilterIUS2IUS2IUS2.Clone = new_instancemethod(_itkAndImageFilterPython.itkAndImageFilterIUS2IUS2IUS2_Clone, None, itkAndImageFilterIUS2IUS2IUS2)
itkAndImageFilterIUS2IUS2IUS2_swigregister = _itkAndImageFilterPython.itkAndImageFilterIUS2IUS2IUS2_swigregister
itkAndImageFilterIUS2IUS2IUS2_swigregister(itkAndImageFilterIUS2IUS2IUS2)

def itkAndImageFilterIUS2IUS2IUS2___New_orig__() -> "itkAndImageFilterIUS2IUS2IUS2_Pointer":
    """itkAndImageFilterIUS2IUS2IUS2___New_orig__() -> itkAndImageFilterIUS2IUS2IUS2_Pointer"""
    return _itkAndImageFilterPython.itkAndImageFilterIUS2IUS2IUS2___New_orig__()

def itkAndImageFilterIUS2IUS2IUS2_cast(obj: 'itkLightObject') -> "itkAndImageFilterIUS2IUS2IUS2 *":
    """itkAndImageFilterIUS2IUS2IUS2_cast(itkLightObject obj) -> itkAndImageFilterIUS2IUS2IUS2"""
    return _itkAndImageFilterPython.itkAndImageFilterIUS2IUS2IUS2_cast(obj)

class itkAndImageFilterIUS3IUS3IUS3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUS3IUS3IUS3):
    """


    Implements the AND bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise AND operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be Where "&" is the bitwise
    AND operator in C++.

    C++ includes: itkAndImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkAndImageFilterIUS3IUS3IUS3_Pointer":
        """__New_orig__() -> itkAndImageFilterIUS3IUS3IUS3_Pointer"""
        return _itkAndImageFilterPython.itkAndImageFilterIUS3IUS3IUS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkAndImageFilterIUS3IUS3IUS3_Pointer":
        """Clone(itkAndImageFilterIUS3IUS3IUS3 self) -> itkAndImageFilterIUS3IUS3IUS3_Pointer"""
        return _itkAndImageFilterPython.itkAndImageFilterIUS3IUS3IUS3_Clone(self)

    Input1Input2OutputBitwiseOperatorsCheck = _itkAndImageFilterPython.itkAndImageFilterIUS3IUS3IUS3_Input1Input2OutputBitwiseOperatorsCheck
    __swig_destroy__ = _itkAndImageFilterPython.delete_itkAndImageFilterIUS3IUS3IUS3

    def cast(obj: 'itkLightObject') -> "itkAndImageFilterIUS3IUS3IUS3 *":
        """cast(itkLightObject obj) -> itkAndImageFilterIUS3IUS3IUS3"""
        return _itkAndImageFilterPython.itkAndImageFilterIUS3IUS3IUS3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkAndImageFilterIUS3IUS3IUS3

        Create a new object of the class itkAndImageFilterIUS3IUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkAndImageFilterIUS3IUS3IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkAndImageFilterIUS3IUS3IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkAndImageFilterIUS3IUS3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkAndImageFilterIUS3IUS3IUS3.Clone = new_instancemethod(_itkAndImageFilterPython.itkAndImageFilterIUS3IUS3IUS3_Clone, None, itkAndImageFilterIUS3IUS3IUS3)
itkAndImageFilterIUS3IUS3IUS3_swigregister = _itkAndImageFilterPython.itkAndImageFilterIUS3IUS3IUS3_swigregister
itkAndImageFilterIUS3IUS3IUS3_swigregister(itkAndImageFilterIUS3IUS3IUS3)

def itkAndImageFilterIUS3IUS3IUS3___New_orig__() -> "itkAndImageFilterIUS3IUS3IUS3_Pointer":
    """itkAndImageFilterIUS3IUS3IUS3___New_orig__() -> itkAndImageFilterIUS3IUS3IUS3_Pointer"""
    return _itkAndImageFilterPython.itkAndImageFilterIUS3IUS3IUS3___New_orig__()

def itkAndImageFilterIUS3IUS3IUS3_cast(obj: 'itkLightObject') -> "itkAndImageFilterIUS3IUS3IUS3 *":
    """itkAndImageFilterIUS3IUS3IUS3_cast(itkLightObject obj) -> itkAndImageFilterIUS3IUS3IUS3"""
    return _itkAndImageFilterPython.itkAndImageFilterIUS3IUS3IUS3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def and_image_filter(*args, **kwargs):
    """Procedural interface for AndImageFilter"""
    import itk
    instance = itk.AndImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def and_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.AndImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.AndImageFilter.values()[0]
    else:
        filter_object = itk.AndImageFilter

    and_image_filter.__doc__ = filter_object.__doc__
    and_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    and_image_filter.__doc__ += "Available Keyword Arguments:\n"
    and_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



