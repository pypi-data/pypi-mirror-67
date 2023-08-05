# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkOrImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkOrImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkOrImageFilterPython
            return _itkOrImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkOrImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkOrImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkOrImageFilterPython
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
import itkInPlaceImageFilterBPython
import itkImageToImageFilterBPython
import itkImagePython
import itkImageRegionPython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkRGBAPixelPython
import itkFixedArrayPython
import stdcomplexPython
import itkRGBPixelPython
import itkMatrixPython
import vnl_matrix_fixedPython
import vnl_matrixPython
import vnl_vectorPython
import itkVectorPython
import vnl_vector_refPython
import itkCovariantVectorPython
import itkPointPython
import itkSymmetricSecondRankTensorPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterAPython
import itkSimpleDataObjectDecoratorPython
import itkArrayPython

def itkOrImageFilterISS3ISS3ISS3_New():
  return itkOrImageFilterISS3ISS3ISS3.New()


def itkOrImageFilterISS2ISS2ISS2_New():
  return itkOrImageFilterISS2ISS2ISS2.New()


def itkOrImageFilterIUS3IUS3IUS3_New():
  return itkOrImageFilterIUS3IUS3IUS3.New()


def itkOrImageFilterIUS2IUS2IUS2_New():
  return itkOrImageFilterIUS2IUS2IUS2.New()


def itkOrImageFilterIUC3IUC3IUC3_New():
  return itkOrImageFilterIUC3IUC3IUC3.New()


def itkOrImageFilterIUC2IUC2IUC2_New():
  return itkOrImageFilterIUC2IUC2IUC2.New()

class itkOrImageFilterISS2ISS2ISS2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterISS2ISS2ISS2):
    """


    Implements the OR bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise OR operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be

    Where "|" is the boolean OR operator in C++.

    \\sphinx
    \\sphinxexample{Filtering/ImageIntensity/BinaryORTwoImages,Binary OR
    Two Images} \\endsphinx

    C++ includes: itkOrImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkOrImageFilterISS2ISS2ISS2_Pointer":
        """__New_orig__() -> itkOrImageFilterISS2ISS2ISS2_Pointer"""
        return _itkOrImageFilterPython.itkOrImageFilterISS2ISS2ISS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkOrImageFilterISS2ISS2ISS2_Pointer":
        """Clone(itkOrImageFilterISS2ISS2ISS2 self) -> itkOrImageFilterISS2ISS2ISS2_Pointer"""
        return _itkOrImageFilterPython.itkOrImageFilterISS2ISS2ISS2_Clone(self)

    Input1Input2OutputBitwiseOperatorsCheck = _itkOrImageFilterPython.itkOrImageFilterISS2ISS2ISS2_Input1Input2OutputBitwiseOperatorsCheck
    __swig_destroy__ = _itkOrImageFilterPython.delete_itkOrImageFilterISS2ISS2ISS2

    def cast(obj: 'itkLightObject') -> "itkOrImageFilterISS2ISS2ISS2 *":
        """cast(itkLightObject obj) -> itkOrImageFilterISS2ISS2ISS2"""
        return _itkOrImageFilterPython.itkOrImageFilterISS2ISS2ISS2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkOrImageFilterISS2ISS2ISS2

        Create a new object of the class itkOrImageFilterISS2ISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkOrImageFilterISS2ISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkOrImageFilterISS2ISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkOrImageFilterISS2ISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkOrImageFilterISS2ISS2ISS2.Clone = new_instancemethod(_itkOrImageFilterPython.itkOrImageFilterISS2ISS2ISS2_Clone, None, itkOrImageFilterISS2ISS2ISS2)
itkOrImageFilterISS2ISS2ISS2_swigregister = _itkOrImageFilterPython.itkOrImageFilterISS2ISS2ISS2_swigregister
itkOrImageFilterISS2ISS2ISS2_swigregister(itkOrImageFilterISS2ISS2ISS2)

def itkOrImageFilterISS2ISS2ISS2___New_orig__() -> "itkOrImageFilterISS2ISS2ISS2_Pointer":
    """itkOrImageFilterISS2ISS2ISS2___New_orig__() -> itkOrImageFilterISS2ISS2ISS2_Pointer"""
    return _itkOrImageFilterPython.itkOrImageFilterISS2ISS2ISS2___New_orig__()

def itkOrImageFilterISS2ISS2ISS2_cast(obj: 'itkLightObject') -> "itkOrImageFilterISS2ISS2ISS2 *":
    """itkOrImageFilterISS2ISS2ISS2_cast(itkLightObject obj) -> itkOrImageFilterISS2ISS2ISS2"""
    return _itkOrImageFilterPython.itkOrImageFilterISS2ISS2ISS2_cast(obj)

class itkOrImageFilterISS3ISS3ISS3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterISS3ISS3ISS3):
    """


    Implements the OR bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise OR operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be

    Where "|" is the boolean OR operator in C++.

    \\sphinx
    \\sphinxexample{Filtering/ImageIntensity/BinaryORTwoImages,Binary OR
    Two Images} \\endsphinx

    C++ includes: itkOrImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkOrImageFilterISS3ISS3ISS3_Pointer":
        """__New_orig__() -> itkOrImageFilterISS3ISS3ISS3_Pointer"""
        return _itkOrImageFilterPython.itkOrImageFilterISS3ISS3ISS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkOrImageFilterISS3ISS3ISS3_Pointer":
        """Clone(itkOrImageFilterISS3ISS3ISS3 self) -> itkOrImageFilterISS3ISS3ISS3_Pointer"""
        return _itkOrImageFilterPython.itkOrImageFilterISS3ISS3ISS3_Clone(self)

    Input1Input2OutputBitwiseOperatorsCheck = _itkOrImageFilterPython.itkOrImageFilterISS3ISS3ISS3_Input1Input2OutputBitwiseOperatorsCheck
    __swig_destroy__ = _itkOrImageFilterPython.delete_itkOrImageFilterISS3ISS3ISS3

    def cast(obj: 'itkLightObject') -> "itkOrImageFilterISS3ISS3ISS3 *":
        """cast(itkLightObject obj) -> itkOrImageFilterISS3ISS3ISS3"""
        return _itkOrImageFilterPython.itkOrImageFilterISS3ISS3ISS3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkOrImageFilterISS3ISS3ISS3

        Create a new object of the class itkOrImageFilterISS3ISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkOrImageFilterISS3ISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkOrImageFilterISS3ISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkOrImageFilterISS3ISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkOrImageFilterISS3ISS3ISS3.Clone = new_instancemethod(_itkOrImageFilterPython.itkOrImageFilterISS3ISS3ISS3_Clone, None, itkOrImageFilterISS3ISS3ISS3)
itkOrImageFilterISS3ISS3ISS3_swigregister = _itkOrImageFilterPython.itkOrImageFilterISS3ISS3ISS3_swigregister
itkOrImageFilterISS3ISS3ISS3_swigregister(itkOrImageFilterISS3ISS3ISS3)

def itkOrImageFilterISS3ISS3ISS3___New_orig__() -> "itkOrImageFilterISS3ISS3ISS3_Pointer":
    """itkOrImageFilterISS3ISS3ISS3___New_orig__() -> itkOrImageFilterISS3ISS3ISS3_Pointer"""
    return _itkOrImageFilterPython.itkOrImageFilterISS3ISS3ISS3___New_orig__()

def itkOrImageFilterISS3ISS3ISS3_cast(obj: 'itkLightObject') -> "itkOrImageFilterISS3ISS3ISS3 *":
    """itkOrImageFilterISS3ISS3ISS3_cast(itkLightObject obj) -> itkOrImageFilterISS3ISS3ISS3"""
    return _itkOrImageFilterPython.itkOrImageFilterISS3ISS3ISS3_cast(obj)

class itkOrImageFilterIUC2IUC2IUC2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUC2IUC2IUC2):
    """


    Implements the OR bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise OR operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be

    Where "|" is the boolean OR operator in C++.

    \\sphinx
    \\sphinxexample{Filtering/ImageIntensity/BinaryORTwoImages,Binary OR
    Two Images} \\endsphinx

    C++ includes: itkOrImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkOrImageFilterIUC2IUC2IUC2_Pointer":
        """__New_orig__() -> itkOrImageFilterIUC2IUC2IUC2_Pointer"""
        return _itkOrImageFilterPython.itkOrImageFilterIUC2IUC2IUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkOrImageFilterIUC2IUC2IUC2_Pointer":
        """Clone(itkOrImageFilterIUC2IUC2IUC2 self) -> itkOrImageFilterIUC2IUC2IUC2_Pointer"""
        return _itkOrImageFilterPython.itkOrImageFilterIUC2IUC2IUC2_Clone(self)

    Input1Input2OutputBitwiseOperatorsCheck = _itkOrImageFilterPython.itkOrImageFilterIUC2IUC2IUC2_Input1Input2OutputBitwiseOperatorsCheck
    __swig_destroy__ = _itkOrImageFilterPython.delete_itkOrImageFilterIUC2IUC2IUC2

    def cast(obj: 'itkLightObject') -> "itkOrImageFilterIUC2IUC2IUC2 *":
        """cast(itkLightObject obj) -> itkOrImageFilterIUC2IUC2IUC2"""
        return _itkOrImageFilterPython.itkOrImageFilterIUC2IUC2IUC2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkOrImageFilterIUC2IUC2IUC2

        Create a new object of the class itkOrImageFilterIUC2IUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkOrImageFilterIUC2IUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkOrImageFilterIUC2IUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkOrImageFilterIUC2IUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkOrImageFilterIUC2IUC2IUC2.Clone = new_instancemethod(_itkOrImageFilterPython.itkOrImageFilterIUC2IUC2IUC2_Clone, None, itkOrImageFilterIUC2IUC2IUC2)
itkOrImageFilterIUC2IUC2IUC2_swigregister = _itkOrImageFilterPython.itkOrImageFilterIUC2IUC2IUC2_swigregister
itkOrImageFilterIUC2IUC2IUC2_swigregister(itkOrImageFilterIUC2IUC2IUC2)

def itkOrImageFilterIUC2IUC2IUC2___New_orig__() -> "itkOrImageFilterIUC2IUC2IUC2_Pointer":
    """itkOrImageFilterIUC2IUC2IUC2___New_orig__() -> itkOrImageFilterIUC2IUC2IUC2_Pointer"""
    return _itkOrImageFilterPython.itkOrImageFilterIUC2IUC2IUC2___New_orig__()

def itkOrImageFilterIUC2IUC2IUC2_cast(obj: 'itkLightObject') -> "itkOrImageFilterIUC2IUC2IUC2 *":
    """itkOrImageFilterIUC2IUC2IUC2_cast(itkLightObject obj) -> itkOrImageFilterIUC2IUC2IUC2"""
    return _itkOrImageFilterPython.itkOrImageFilterIUC2IUC2IUC2_cast(obj)

class itkOrImageFilterIUC3IUC3IUC3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUC3IUC3IUC3):
    """


    Implements the OR bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise OR operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be

    Where "|" is the boolean OR operator in C++.

    \\sphinx
    \\sphinxexample{Filtering/ImageIntensity/BinaryORTwoImages,Binary OR
    Two Images} \\endsphinx

    C++ includes: itkOrImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkOrImageFilterIUC3IUC3IUC3_Pointer":
        """__New_orig__() -> itkOrImageFilterIUC3IUC3IUC3_Pointer"""
        return _itkOrImageFilterPython.itkOrImageFilterIUC3IUC3IUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkOrImageFilterIUC3IUC3IUC3_Pointer":
        """Clone(itkOrImageFilterIUC3IUC3IUC3 self) -> itkOrImageFilterIUC3IUC3IUC3_Pointer"""
        return _itkOrImageFilterPython.itkOrImageFilterIUC3IUC3IUC3_Clone(self)

    Input1Input2OutputBitwiseOperatorsCheck = _itkOrImageFilterPython.itkOrImageFilterIUC3IUC3IUC3_Input1Input2OutputBitwiseOperatorsCheck
    __swig_destroy__ = _itkOrImageFilterPython.delete_itkOrImageFilterIUC3IUC3IUC3

    def cast(obj: 'itkLightObject') -> "itkOrImageFilterIUC3IUC3IUC3 *":
        """cast(itkLightObject obj) -> itkOrImageFilterIUC3IUC3IUC3"""
        return _itkOrImageFilterPython.itkOrImageFilterIUC3IUC3IUC3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkOrImageFilterIUC3IUC3IUC3

        Create a new object of the class itkOrImageFilterIUC3IUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkOrImageFilterIUC3IUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkOrImageFilterIUC3IUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkOrImageFilterIUC3IUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkOrImageFilterIUC3IUC3IUC3.Clone = new_instancemethod(_itkOrImageFilterPython.itkOrImageFilterIUC3IUC3IUC3_Clone, None, itkOrImageFilterIUC3IUC3IUC3)
itkOrImageFilterIUC3IUC3IUC3_swigregister = _itkOrImageFilterPython.itkOrImageFilterIUC3IUC3IUC3_swigregister
itkOrImageFilterIUC3IUC3IUC3_swigregister(itkOrImageFilterIUC3IUC3IUC3)

def itkOrImageFilterIUC3IUC3IUC3___New_orig__() -> "itkOrImageFilterIUC3IUC3IUC3_Pointer":
    """itkOrImageFilterIUC3IUC3IUC3___New_orig__() -> itkOrImageFilterIUC3IUC3IUC3_Pointer"""
    return _itkOrImageFilterPython.itkOrImageFilterIUC3IUC3IUC3___New_orig__()

def itkOrImageFilterIUC3IUC3IUC3_cast(obj: 'itkLightObject') -> "itkOrImageFilterIUC3IUC3IUC3 *":
    """itkOrImageFilterIUC3IUC3IUC3_cast(itkLightObject obj) -> itkOrImageFilterIUC3IUC3IUC3"""
    return _itkOrImageFilterPython.itkOrImageFilterIUC3IUC3IUC3_cast(obj)

class itkOrImageFilterIUS2IUS2IUS2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUS2IUS2IUS2):
    """


    Implements the OR bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise OR operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be

    Where "|" is the boolean OR operator in C++.

    \\sphinx
    \\sphinxexample{Filtering/ImageIntensity/BinaryORTwoImages,Binary OR
    Two Images} \\endsphinx

    C++ includes: itkOrImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkOrImageFilterIUS2IUS2IUS2_Pointer":
        """__New_orig__() -> itkOrImageFilterIUS2IUS2IUS2_Pointer"""
        return _itkOrImageFilterPython.itkOrImageFilterIUS2IUS2IUS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkOrImageFilterIUS2IUS2IUS2_Pointer":
        """Clone(itkOrImageFilterIUS2IUS2IUS2 self) -> itkOrImageFilterIUS2IUS2IUS2_Pointer"""
        return _itkOrImageFilterPython.itkOrImageFilterIUS2IUS2IUS2_Clone(self)

    Input1Input2OutputBitwiseOperatorsCheck = _itkOrImageFilterPython.itkOrImageFilterIUS2IUS2IUS2_Input1Input2OutputBitwiseOperatorsCheck
    __swig_destroy__ = _itkOrImageFilterPython.delete_itkOrImageFilterIUS2IUS2IUS2

    def cast(obj: 'itkLightObject') -> "itkOrImageFilterIUS2IUS2IUS2 *":
        """cast(itkLightObject obj) -> itkOrImageFilterIUS2IUS2IUS2"""
        return _itkOrImageFilterPython.itkOrImageFilterIUS2IUS2IUS2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkOrImageFilterIUS2IUS2IUS2

        Create a new object of the class itkOrImageFilterIUS2IUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkOrImageFilterIUS2IUS2IUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkOrImageFilterIUS2IUS2IUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkOrImageFilterIUS2IUS2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkOrImageFilterIUS2IUS2IUS2.Clone = new_instancemethod(_itkOrImageFilterPython.itkOrImageFilterIUS2IUS2IUS2_Clone, None, itkOrImageFilterIUS2IUS2IUS2)
itkOrImageFilterIUS2IUS2IUS2_swigregister = _itkOrImageFilterPython.itkOrImageFilterIUS2IUS2IUS2_swigregister
itkOrImageFilterIUS2IUS2IUS2_swigregister(itkOrImageFilterIUS2IUS2IUS2)

def itkOrImageFilterIUS2IUS2IUS2___New_orig__() -> "itkOrImageFilterIUS2IUS2IUS2_Pointer":
    """itkOrImageFilterIUS2IUS2IUS2___New_orig__() -> itkOrImageFilterIUS2IUS2IUS2_Pointer"""
    return _itkOrImageFilterPython.itkOrImageFilterIUS2IUS2IUS2___New_orig__()

def itkOrImageFilterIUS2IUS2IUS2_cast(obj: 'itkLightObject') -> "itkOrImageFilterIUS2IUS2IUS2 *":
    """itkOrImageFilterIUS2IUS2IUS2_cast(itkLightObject obj) -> itkOrImageFilterIUS2IUS2IUS2"""
    return _itkOrImageFilterPython.itkOrImageFilterIUS2IUS2IUS2_cast(obj)

class itkOrImageFilterIUS3IUS3IUS3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIUS3IUS3IUS3):
    """


    Implements the OR bitwise operator pixel-wise between two images.

    This class is templated over the types of the two input images and the
    type of the output image. Numeric conversions (castings) are done by
    the C++ defaults.

    Since the bitwise OR operation is only defined in C++ for integer
    types, the images passed to this filter must comply with the
    requirement of using integer pixel type.

    The total operation over one pixel will be

    Where "|" is the boolean OR operator in C++.

    \\sphinx
    \\sphinxexample{Filtering/ImageIntensity/BinaryORTwoImages,Binary OR
    Two Images} \\endsphinx

    C++ includes: itkOrImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkOrImageFilterIUS3IUS3IUS3_Pointer":
        """__New_orig__() -> itkOrImageFilterIUS3IUS3IUS3_Pointer"""
        return _itkOrImageFilterPython.itkOrImageFilterIUS3IUS3IUS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkOrImageFilterIUS3IUS3IUS3_Pointer":
        """Clone(itkOrImageFilterIUS3IUS3IUS3 self) -> itkOrImageFilterIUS3IUS3IUS3_Pointer"""
        return _itkOrImageFilterPython.itkOrImageFilterIUS3IUS3IUS3_Clone(self)

    Input1Input2OutputBitwiseOperatorsCheck = _itkOrImageFilterPython.itkOrImageFilterIUS3IUS3IUS3_Input1Input2OutputBitwiseOperatorsCheck
    __swig_destroy__ = _itkOrImageFilterPython.delete_itkOrImageFilterIUS3IUS3IUS3

    def cast(obj: 'itkLightObject') -> "itkOrImageFilterIUS3IUS3IUS3 *":
        """cast(itkLightObject obj) -> itkOrImageFilterIUS3IUS3IUS3"""
        return _itkOrImageFilterPython.itkOrImageFilterIUS3IUS3IUS3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkOrImageFilterIUS3IUS3IUS3

        Create a new object of the class itkOrImageFilterIUS3IUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkOrImageFilterIUS3IUS3IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkOrImageFilterIUS3IUS3IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkOrImageFilterIUS3IUS3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkOrImageFilterIUS3IUS3IUS3.Clone = new_instancemethod(_itkOrImageFilterPython.itkOrImageFilterIUS3IUS3IUS3_Clone, None, itkOrImageFilterIUS3IUS3IUS3)
itkOrImageFilterIUS3IUS3IUS3_swigregister = _itkOrImageFilterPython.itkOrImageFilterIUS3IUS3IUS3_swigregister
itkOrImageFilterIUS3IUS3IUS3_swigregister(itkOrImageFilterIUS3IUS3IUS3)

def itkOrImageFilterIUS3IUS3IUS3___New_orig__() -> "itkOrImageFilterIUS3IUS3IUS3_Pointer":
    """itkOrImageFilterIUS3IUS3IUS3___New_orig__() -> itkOrImageFilterIUS3IUS3IUS3_Pointer"""
    return _itkOrImageFilterPython.itkOrImageFilterIUS3IUS3IUS3___New_orig__()

def itkOrImageFilterIUS3IUS3IUS3_cast(obj: 'itkLightObject') -> "itkOrImageFilterIUS3IUS3IUS3 *":
    """itkOrImageFilterIUS3IUS3IUS3_cast(itkLightObject obj) -> itkOrImageFilterIUS3IUS3IUS3"""
    return _itkOrImageFilterPython.itkOrImageFilterIUS3IUS3IUS3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def or_image_filter(*args, **kwargs):
    """Procedural interface for OrImageFilter"""
    import itk
    instance = itk.OrImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def or_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.OrImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.OrImageFilter.values()[0]
    else:
        filter_object = itk.OrImageFilter

    or_image_filter.__doc__ = filter_object.__doc__
    or_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    or_image_filter.__doc__ += "Available Keyword Arguments:\n"
    or_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



