# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkXorImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkXorImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkXorImageFilterPython
            return _itkXorImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkXorImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkXorImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkXorImageFilterPython
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


import itkBinaryGeneratorImageFilterPython
import itkInPlaceImageFilterBPython
import ITKCommonBasePython
import pyBasePython
import itkImageToImageFilterBPython
import itkImageSourcePython
import itkImagePython
import itkCovariantVectorPython
import itkVectorPython
import vnl_vectorPython
import vnl_matrixPython
import stdcomplexPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkRGBPixelPython
import itkPointPython
import itkOffsetPython
import itkSizePython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkIndexPython
import itkRGBAPixelPython
import itkSymmetricSecondRankTensorPython
import itkImageRegionPython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkSimpleDataObjectDecoratorPython
import itkArrayPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterAPython

def itkXorImageFilterISS3ISS3ISS3_New():
  return itkXorImageFilterISS3ISS3ISS3.New()


def itkXorImageFilterISS2ISS2ISS2_New():
  return itkXorImageFilterISS2ISS2ISS2.New()


def itkXorImageFilterIUS3IUS3IUS3_New():
  return itkXorImageFilterIUS3IUS3IUS3.New()


def itkXorImageFilterIUS2IUS2IUS2_New():
  return itkXorImageFilterIUS2IUS2IUS2.New()


def itkXorImageFilterIUC3IUC3IUC3_New():
  return itkXorImageFilterIUC3IUC3IUC3.New()


def itkXorImageFilterIUC2IUC2IUC2_New():
  return itkXorImageFilterIUC2IUC2IUC2.New()

class itkXorImageFilterISS2ISS2ISS2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterISS2ISS2ISS2):
    """


    Computes the XOR bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise XOR operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be

    Where "^" is the boolean XOR operator in C++.

    \\sphinx
    \\sphinxexample{Filtering/ImageIntensity/BinaryXORTwoImages,Binary
    XOR Two Images} \\endsphinx

    C++ includes: itkXorImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkXorImageFilterISS2ISS2ISS2_Pointer":
        """__New_orig__() -> itkXorImageFilterISS2ISS2ISS2_Pointer"""
        return _itkXorImageFilterPython.itkXorImageFilterISS2ISS2ISS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkXorImageFilterISS2ISS2ISS2_Pointer":
        """Clone(itkXorImageFilterISS2ISS2ISS2 self) -> itkXorImageFilterISS2ISS2ISS2_Pointer"""
        return _itkXorImageFilterPython.itkXorImageFilterISS2ISS2ISS2_Clone(self)

    Input1Input2OutputBitwiseOperatorsCheck = _itkXorImageFilterPython.itkXorImageFilterISS2ISS2ISS2_Input1Input2OutputBitwiseOperatorsCheck
    __swig_destroy__ = _itkXorImageFilterPython.delete_itkXorImageFilterISS2ISS2ISS2

    def cast(obj: 'itkLightObject') -> "itkXorImageFilterISS2ISS2ISS2 *":
        """cast(itkLightObject obj) -> itkXorImageFilterISS2ISS2ISS2"""
        return _itkXorImageFilterPython.itkXorImageFilterISS2ISS2ISS2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkXorImageFilterISS2ISS2ISS2

        Create a new object of the class itkXorImageFilterISS2ISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkXorImageFilterISS2ISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkXorImageFilterISS2ISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkXorImageFilterISS2ISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkXorImageFilterISS2ISS2ISS2.Clone = new_instancemethod(_itkXorImageFilterPython.itkXorImageFilterISS2ISS2ISS2_Clone, None, itkXorImageFilterISS2ISS2ISS2)
itkXorImageFilterISS2ISS2ISS2_swigregister = _itkXorImageFilterPython.itkXorImageFilterISS2ISS2ISS2_swigregister
itkXorImageFilterISS2ISS2ISS2_swigregister(itkXorImageFilterISS2ISS2ISS2)

def itkXorImageFilterISS2ISS2ISS2___New_orig__() -> "itkXorImageFilterISS2ISS2ISS2_Pointer":
    """itkXorImageFilterISS2ISS2ISS2___New_orig__() -> itkXorImageFilterISS2ISS2ISS2_Pointer"""
    return _itkXorImageFilterPython.itkXorImageFilterISS2ISS2ISS2___New_orig__()

def itkXorImageFilterISS2ISS2ISS2_cast(obj: 'itkLightObject') -> "itkXorImageFilterISS2ISS2ISS2 *":
    """itkXorImageFilterISS2ISS2ISS2_cast(itkLightObject obj) -> itkXorImageFilterISS2ISS2ISS2"""
    return _itkXorImageFilterPython.itkXorImageFilterISS2ISS2ISS2_cast(obj)

class itkXorImageFilterISS3ISS3ISS3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterISS3ISS3ISS3):
    """


    Computes the XOR bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise XOR operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be

    Where "^" is the boolean XOR operator in C++.

    \\sphinx
    \\sphinxexample{Filtering/ImageIntensity/BinaryXORTwoImages,Binary
    XOR Two Images} \\endsphinx

    C++ includes: itkXorImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkXorImageFilterISS3ISS3ISS3_Pointer":
        """__New_orig__() -> itkXorImageFilterISS3ISS3ISS3_Pointer"""
        return _itkXorImageFilterPython.itkXorImageFilterISS3ISS3ISS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkXorImageFilterISS3ISS3ISS3_Pointer":
        """Clone(itkXorImageFilterISS3ISS3ISS3 self) -> itkXorImageFilterISS3ISS3ISS3_Pointer"""
        return _itkXorImageFilterPython.itkXorImageFilterISS3ISS3ISS3_Clone(self)

    Input1Input2OutputBitwiseOperatorsCheck = _itkXorImageFilterPython.itkXorImageFilterISS3ISS3ISS3_Input1Input2OutputBitwiseOperatorsCheck
    __swig_destroy__ = _itkXorImageFilterPython.delete_itkXorImageFilterISS3ISS3ISS3

    def cast(obj: 'itkLightObject') -> "itkXorImageFilterISS3ISS3ISS3 *":
        """cast(itkLightObject obj) -> itkXorImageFilterISS3ISS3ISS3"""
        return _itkXorImageFilterPython.itkXorImageFilterISS3ISS3ISS3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkXorImageFilterISS3ISS3ISS3

        Create a new object of the class itkXorImageFilterISS3ISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkXorImageFilterISS3ISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkXorImageFilterISS3ISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkXorImageFilterISS3ISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkXorImageFilterISS3ISS3ISS3.Clone = new_instancemethod(_itkXorImageFilterPython.itkXorImageFilterISS3ISS3ISS3_Clone, None, itkXorImageFilterISS3ISS3ISS3)
itkXorImageFilterISS3ISS3ISS3_swigregister = _itkXorImageFilterPython.itkXorImageFilterISS3ISS3ISS3_swigregister
itkXorImageFilterISS3ISS3ISS3_swigregister(itkXorImageFilterISS3ISS3ISS3)

def itkXorImageFilterISS3ISS3ISS3___New_orig__() -> "itkXorImageFilterISS3ISS3ISS3_Pointer":
    """itkXorImageFilterISS3ISS3ISS3___New_orig__() -> itkXorImageFilterISS3ISS3ISS3_Pointer"""
    return _itkXorImageFilterPython.itkXorImageFilterISS3ISS3ISS3___New_orig__()

def itkXorImageFilterISS3ISS3ISS3_cast(obj: 'itkLightObject') -> "itkXorImageFilterISS3ISS3ISS3 *":
    """itkXorImageFilterISS3ISS3ISS3_cast(itkLightObject obj) -> itkXorImageFilterISS3ISS3ISS3"""
    return _itkXorImageFilterPython.itkXorImageFilterISS3ISS3ISS3_cast(obj)

class itkXorImageFilterIUC2IUC2IUC2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUC2IUC2IUC2):
    """


    Computes the XOR bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise XOR operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be

    Where "^" is the boolean XOR operator in C++.

    \\sphinx
    \\sphinxexample{Filtering/ImageIntensity/BinaryXORTwoImages,Binary
    XOR Two Images} \\endsphinx

    C++ includes: itkXorImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkXorImageFilterIUC2IUC2IUC2_Pointer":
        """__New_orig__() -> itkXorImageFilterIUC2IUC2IUC2_Pointer"""
        return _itkXorImageFilterPython.itkXorImageFilterIUC2IUC2IUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkXorImageFilterIUC2IUC2IUC2_Pointer":
        """Clone(itkXorImageFilterIUC2IUC2IUC2 self) -> itkXorImageFilterIUC2IUC2IUC2_Pointer"""
        return _itkXorImageFilterPython.itkXorImageFilterIUC2IUC2IUC2_Clone(self)

    Input1Input2OutputBitwiseOperatorsCheck = _itkXorImageFilterPython.itkXorImageFilterIUC2IUC2IUC2_Input1Input2OutputBitwiseOperatorsCheck
    __swig_destroy__ = _itkXorImageFilterPython.delete_itkXorImageFilterIUC2IUC2IUC2

    def cast(obj: 'itkLightObject') -> "itkXorImageFilterIUC2IUC2IUC2 *":
        """cast(itkLightObject obj) -> itkXorImageFilterIUC2IUC2IUC2"""
        return _itkXorImageFilterPython.itkXorImageFilterIUC2IUC2IUC2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkXorImageFilterIUC2IUC2IUC2

        Create a new object of the class itkXorImageFilterIUC2IUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkXorImageFilterIUC2IUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkXorImageFilterIUC2IUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkXorImageFilterIUC2IUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkXorImageFilterIUC2IUC2IUC2.Clone = new_instancemethod(_itkXorImageFilterPython.itkXorImageFilterIUC2IUC2IUC2_Clone, None, itkXorImageFilterIUC2IUC2IUC2)
itkXorImageFilterIUC2IUC2IUC2_swigregister = _itkXorImageFilterPython.itkXorImageFilterIUC2IUC2IUC2_swigregister
itkXorImageFilterIUC2IUC2IUC2_swigregister(itkXorImageFilterIUC2IUC2IUC2)

def itkXorImageFilterIUC2IUC2IUC2___New_orig__() -> "itkXorImageFilterIUC2IUC2IUC2_Pointer":
    """itkXorImageFilterIUC2IUC2IUC2___New_orig__() -> itkXorImageFilterIUC2IUC2IUC2_Pointer"""
    return _itkXorImageFilterPython.itkXorImageFilterIUC2IUC2IUC2___New_orig__()

def itkXorImageFilterIUC2IUC2IUC2_cast(obj: 'itkLightObject') -> "itkXorImageFilterIUC2IUC2IUC2 *":
    """itkXorImageFilterIUC2IUC2IUC2_cast(itkLightObject obj) -> itkXorImageFilterIUC2IUC2IUC2"""
    return _itkXorImageFilterPython.itkXorImageFilterIUC2IUC2IUC2_cast(obj)

class itkXorImageFilterIUC3IUC3IUC3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUC3IUC3IUC3):
    """


    Computes the XOR bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise XOR operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be

    Where "^" is the boolean XOR operator in C++.

    \\sphinx
    \\sphinxexample{Filtering/ImageIntensity/BinaryXORTwoImages,Binary
    XOR Two Images} \\endsphinx

    C++ includes: itkXorImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkXorImageFilterIUC3IUC3IUC3_Pointer":
        """__New_orig__() -> itkXorImageFilterIUC3IUC3IUC3_Pointer"""
        return _itkXorImageFilterPython.itkXorImageFilterIUC3IUC3IUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkXorImageFilterIUC3IUC3IUC3_Pointer":
        """Clone(itkXorImageFilterIUC3IUC3IUC3 self) -> itkXorImageFilterIUC3IUC3IUC3_Pointer"""
        return _itkXorImageFilterPython.itkXorImageFilterIUC3IUC3IUC3_Clone(self)

    Input1Input2OutputBitwiseOperatorsCheck = _itkXorImageFilterPython.itkXorImageFilterIUC3IUC3IUC3_Input1Input2OutputBitwiseOperatorsCheck
    __swig_destroy__ = _itkXorImageFilterPython.delete_itkXorImageFilterIUC3IUC3IUC3

    def cast(obj: 'itkLightObject') -> "itkXorImageFilterIUC3IUC3IUC3 *":
        """cast(itkLightObject obj) -> itkXorImageFilterIUC3IUC3IUC3"""
        return _itkXorImageFilterPython.itkXorImageFilterIUC3IUC3IUC3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkXorImageFilterIUC3IUC3IUC3

        Create a new object of the class itkXorImageFilterIUC3IUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkXorImageFilterIUC3IUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkXorImageFilterIUC3IUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkXorImageFilterIUC3IUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkXorImageFilterIUC3IUC3IUC3.Clone = new_instancemethod(_itkXorImageFilterPython.itkXorImageFilterIUC3IUC3IUC3_Clone, None, itkXorImageFilterIUC3IUC3IUC3)
itkXorImageFilterIUC3IUC3IUC3_swigregister = _itkXorImageFilterPython.itkXorImageFilterIUC3IUC3IUC3_swigregister
itkXorImageFilterIUC3IUC3IUC3_swigregister(itkXorImageFilterIUC3IUC3IUC3)

def itkXorImageFilterIUC3IUC3IUC3___New_orig__() -> "itkXorImageFilterIUC3IUC3IUC3_Pointer":
    """itkXorImageFilterIUC3IUC3IUC3___New_orig__() -> itkXorImageFilterIUC3IUC3IUC3_Pointer"""
    return _itkXorImageFilterPython.itkXorImageFilterIUC3IUC3IUC3___New_orig__()

def itkXorImageFilterIUC3IUC3IUC3_cast(obj: 'itkLightObject') -> "itkXorImageFilterIUC3IUC3IUC3 *":
    """itkXorImageFilterIUC3IUC3IUC3_cast(itkLightObject obj) -> itkXorImageFilterIUC3IUC3IUC3"""
    return _itkXorImageFilterPython.itkXorImageFilterIUC3IUC3IUC3_cast(obj)

class itkXorImageFilterIUS2IUS2IUS2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUS2IUS2IUS2):
    """


    Computes the XOR bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise XOR operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be

    Where "^" is the boolean XOR operator in C++.

    \\sphinx
    \\sphinxexample{Filtering/ImageIntensity/BinaryXORTwoImages,Binary
    XOR Two Images} \\endsphinx

    C++ includes: itkXorImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkXorImageFilterIUS2IUS2IUS2_Pointer":
        """__New_orig__() -> itkXorImageFilterIUS2IUS2IUS2_Pointer"""
        return _itkXorImageFilterPython.itkXorImageFilterIUS2IUS2IUS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkXorImageFilterIUS2IUS2IUS2_Pointer":
        """Clone(itkXorImageFilterIUS2IUS2IUS2 self) -> itkXorImageFilterIUS2IUS2IUS2_Pointer"""
        return _itkXorImageFilterPython.itkXorImageFilterIUS2IUS2IUS2_Clone(self)

    Input1Input2OutputBitwiseOperatorsCheck = _itkXorImageFilterPython.itkXorImageFilterIUS2IUS2IUS2_Input1Input2OutputBitwiseOperatorsCheck
    __swig_destroy__ = _itkXorImageFilterPython.delete_itkXorImageFilterIUS2IUS2IUS2

    def cast(obj: 'itkLightObject') -> "itkXorImageFilterIUS2IUS2IUS2 *":
        """cast(itkLightObject obj) -> itkXorImageFilterIUS2IUS2IUS2"""
        return _itkXorImageFilterPython.itkXorImageFilterIUS2IUS2IUS2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkXorImageFilterIUS2IUS2IUS2

        Create a new object of the class itkXorImageFilterIUS2IUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkXorImageFilterIUS2IUS2IUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkXorImageFilterIUS2IUS2IUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkXorImageFilterIUS2IUS2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkXorImageFilterIUS2IUS2IUS2.Clone = new_instancemethod(_itkXorImageFilterPython.itkXorImageFilterIUS2IUS2IUS2_Clone, None, itkXorImageFilterIUS2IUS2IUS2)
itkXorImageFilterIUS2IUS2IUS2_swigregister = _itkXorImageFilterPython.itkXorImageFilterIUS2IUS2IUS2_swigregister
itkXorImageFilterIUS2IUS2IUS2_swigregister(itkXorImageFilterIUS2IUS2IUS2)

def itkXorImageFilterIUS2IUS2IUS2___New_orig__() -> "itkXorImageFilterIUS2IUS2IUS2_Pointer":
    """itkXorImageFilterIUS2IUS2IUS2___New_orig__() -> itkXorImageFilterIUS2IUS2IUS2_Pointer"""
    return _itkXorImageFilterPython.itkXorImageFilterIUS2IUS2IUS2___New_orig__()

def itkXorImageFilterIUS2IUS2IUS2_cast(obj: 'itkLightObject') -> "itkXorImageFilterIUS2IUS2IUS2 *":
    """itkXorImageFilterIUS2IUS2IUS2_cast(itkLightObject obj) -> itkXorImageFilterIUS2IUS2IUS2"""
    return _itkXorImageFilterPython.itkXorImageFilterIUS2IUS2IUS2_cast(obj)

class itkXorImageFilterIUS3IUS3IUS3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUS3IUS3IUS3):
    """


    Computes the XOR bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise XOR operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be

    Where "^" is the boolean XOR operator in C++.

    \\sphinx
    \\sphinxexample{Filtering/ImageIntensity/BinaryXORTwoImages,Binary
    XOR Two Images} \\endsphinx

    C++ includes: itkXorImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkXorImageFilterIUS3IUS3IUS3_Pointer":
        """__New_orig__() -> itkXorImageFilterIUS3IUS3IUS3_Pointer"""
        return _itkXorImageFilterPython.itkXorImageFilterIUS3IUS3IUS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkXorImageFilterIUS3IUS3IUS3_Pointer":
        """Clone(itkXorImageFilterIUS3IUS3IUS3 self) -> itkXorImageFilterIUS3IUS3IUS3_Pointer"""
        return _itkXorImageFilterPython.itkXorImageFilterIUS3IUS3IUS3_Clone(self)

    Input1Input2OutputBitwiseOperatorsCheck = _itkXorImageFilterPython.itkXorImageFilterIUS3IUS3IUS3_Input1Input2OutputBitwiseOperatorsCheck
    __swig_destroy__ = _itkXorImageFilterPython.delete_itkXorImageFilterIUS3IUS3IUS3

    def cast(obj: 'itkLightObject') -> "itkXorImageFilterIUS3IUS3IUS3 *":
        """cast(itkLightObject obj) -> itkXorImageFilterIUS3IUS3IUS3"""
        return _itkXorImageFilterPython.itkXorImageFilterIUS3IUS3IUS3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkXorImageFilterIUS3IUS3IUS3

        Create a new object of the class itkXorImageFilterIUS3IUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkXorImageFilterIUS3IUS3IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkXorImageFilterIUS3IUS3IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkXorImageFilterIUS3IUS3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkXorImageFilterIUS3IUS3IUS3.Clone = new_instancemethod(_itkXorImageFilterPython.itkXorImageFilterIUS3IUS3IUS3_Clone, None, itkXorImageFilterIUS3IUS3IUS3)
itkXorImageFilterIUS3IUS3IUS3_swigregister = _itkXorImageFilterPython.itkXorImageFilterIUS3IUS3IUS3_swigregister
itkXorImageFilterIUS3IUS3IUS3_swigregister(itkXorImageFilterIUS3IUS3IUS3)

def itkXorImageFilterIUS3IUS3IUS3___New_orig__() -> "itkXorImageFilterIUS3IUS3IUS3_Pointer":
    """itkXorImageFilterIUS3IUS3IUS3___New_orig__() -> itkXorImageFilterIUS3IUS3IUS3_Pointer"""
    return _itkXorImageFilterPython.itkXorImageFilterIUS3IUS3IUS3___New_orig__()

def itkXorImageFilterIUS3IUS3IUS3_cast(obj: 'itkLightObject') -> "itkXorImageFilterIUS3IUS3IUS3 *":
    """itkXorImageFilterIUS3IUS3IUS3_cast(itkLightObject obj) -> itkXorImageFilterIUS3IUS3IUS3"""
    return _itkXorImageFilterPython.itkXorImageFilterIUS3IUS3IUS3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def xor_image_filter(*args, **kwargs):
    """Procedural interface for XorImageFilter"""
    import itk
    instance = itk.XorImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def xor_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.XorImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.XorImageFilter.values()[0]
    else:
        filter_object = itk.XorImageFilter

    xor_image_filter.__doc__ = filter_object.__doc__
    xor_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    xor_image_filter.__doc__ += "Available Keyword Arguments:\n"
    xor_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



