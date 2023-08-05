# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkMagnitudeAndPhaseToComplexImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkMagnitudeAndPhaseToComplexImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkMagnitudeAndPhaseToComplexImageFilterPython
            return _itkMagnitudeAndPhaseToComplexImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkMagnitudeAndPhaseToComplexImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkMagnitudeAndPhaseToComplexImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkMagnitudeAndPhaseToComplexImageFilterPython
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
import itkRGBAPixelPython
import itkFixedArrayPython
import pyBasePython
import itkInPlaceImageFilterBPython
import itkImageToImageFilterBPython
import itkVectorImagePython
import itkIndexPython
import itkOffsetPython
import itkSizePython
import stdcomplexPython
import ITKCommonBasePython
import itkVariableLengthVectorPython
import itkImagePython
import itkPointPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import itkVectorPython
import itkRGBPixelPython
import itkImageRegionPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkImageToImageFilterCommonPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterAPython
import itkSimpleDataObjectDecoratorPython
import itkArrayPython

def itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3_New():
  return itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3.New()


def itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3_New():
  return itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3.New()


def itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2_New():
  return itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2.New()


def itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2_New():
  return itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2.New()

class itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterID2ID2ICF2):
    """


    Implements pixel-wise conversion of magnitude and phase data into
    complex voxels.

    This filter is parameterized over the types of the two input images
    and the type of the output image.

    The filter expect all images to have the same dimension (e.g. all 2D,
    or all 3D, or all ND)

    C++ includes: itkMagnitudeAndPhaseToComplexImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2_Pointer":
        """__New_orig__() -> itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2_Pointer"""
        return _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2_Pointer":
        """Clone(itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2 self) -> itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2_Pointer"""
        return _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2_Clone(self)

    Input1ConvertibleToDoubleCheck = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2_Input1ConvertibleToDoubleCheck
    Input2ConvertibleToDoubleCheck = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2_Input2ConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkMagnitudeAndPhaseToComplexImageFilterPython.delete_itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2

    def cast(obj: 'itkLightObject') -> "itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2 *":
        """cast(itkLightObject obj) -> itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2"""
        return _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2

        Create a new object of the class itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2.Clone = new_instancemethod(_itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2_Clone, None, itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2)
itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2_swigregister = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2_swigregister
itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2_swigregister(itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2)

def itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2___New_orig__() -> "itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2_Pointer":
    """itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2___New_orig__() -> itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2_Pointer"""
    return _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2___New_orig__()

def itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2_cast(obj: 'itkLightObject') -> "itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2 *":
    """itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2_cast(itkLightObject obj) -> itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2"""
    return _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID2ID2ICF2_cast(obj)

class itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterID3ID3ICF3):
    """


    Implements pixel-wise conversion of magnitude and phase data into
    complex voxels.

    This filter is parameterized over the types of the two input images
    and the type of the output image.

    The filter expect all images to have the same dimension (e.g. all 2D,
    or all 3D, or all ND)

    C++ includes: itkMagnitudeAndPhaseToComplexImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3_Pointer":
        """__New_orig__() -> itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3_Pointer"""
        return _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3_Pointer":
        """Clone(itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3 self) -> itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3_Pointer"""
        return _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3_Clone(self)

    Input1ConvertibleToDoubleCheck = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3_Input1ConvertibleToDoubleCheck
    Input2ConvertibleToDoubleCheck = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3_Input2ConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkMagnitudeAndPhaseToComplexImageFilterPython.delete_itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3

    def cast(obj: 'itkLightObject') -> "itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3 *":
        """cast(itkLightObject obj) -> itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3"""
        return _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3

        Create a new object of the class itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3.Clone = new_instancemethod(_itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3_Clone, None, itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3)
itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3_swigregister = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3_swigregister
itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3_swigregister(itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3)

def itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3___New_orig__() -> "itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3_Pointer":
    """itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3___New_orig__() -> itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3_Pointer"""
    return _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3___New_orig__()

def itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3_cast(obj: 'itkLightObject') -> "itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3 *":
    """itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3_cast(itkLightObject obj) -> itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3"""
    return _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterID3ID3ICF3_cast(obj)

class itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIF2IF2ICF2):
    """


    Implements pixel-wise conversion of magnitude and phase data into
    complex voxels.

    This filter is parameterized over the types of the two input images
    and the type of the output image.

    The filter expect all images to have the same dimension (e.g. all 2D,
    or all 3D, or all ND)

    C++ includes: itkMagnitudeAndPhaseToComplexImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2_Pointer":
        """__New_orig__() -> itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2_Pointer"""
        return _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2_Pointer":
        """Clone(itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2 self) -> itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2_Pointer"""
        return _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2_Clone(self)

    Input1ConvertibleToDoubleCheck = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2_Input1ConvertibleToDoubleCheck
    Input2ConvertibleToDoubleCheck = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2_Input2ConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkMagnitudeAndPhaseToComplexImageFilterPython.delete_itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2

    def cast(obj: 'itkLightObject') -> "itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2 *":
        """cast(itkLightObject obj) -> itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2"""
        return _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2

        Create a new object of the class itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2.Clone = new_instancemethod(_itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2_Clone, None, itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2)
itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2_swigregister = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2_swigregister
itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2_swigregister(itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2)

def itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2___New_orig__() -> "itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2_Pointer":
    """itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2___New_orig__() -> itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2_Pointer"""
    return _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2___New_orig__()

def itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2_cast(obj: 'itkLightObject') -> "itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2 *":
    """itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2_cast(itkLightObject obj) -> itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2"""
    return _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF2IF2ICF2_cast(obj)

class itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3(itkBinaryGeneratorImageFilterPython.itkBinaryGeneratorImageFilterIF3IF3ICF3):
    """


    Implements pixel-wise conversion of magnitude and phase data into
    complex voxels.

    This filter is parameterized over the types of the two input images
    and the type of the output image.

    The filter expect all images to have the same dimension (e.g. all 2D,
    or all 3D, or all ND)

    C++ includes: itkMagnitudeAndPhaseToComplexImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3_Pointer":
        """__New_orig__() -> itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3_Pointer"""
        return _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3_Pointer":
        """Clone(itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3 self) -> itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3_Pointer"""
        return _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3_Clone(self)

    Input1ConvertibleToDoubleCheck = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3_Input1ConvertibleToDoubleCheck
    Input2ConvertibleToDoubleCheck = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3_Input2ConvertibleToDoubleCheck
    DoubleConvertibleToOutputCheck = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3_DoubleConvertibleToOutputCheck
    __swig_destroy__ = _itkMagnitudeAndPhaseToComplexImageFilterPython.delete_itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3

    def cast(obj: 'itkLightObject') -> "itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3 *":
        """cast(itkLightObject obj) -> itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3"""
        return _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3

        Create a new object of the class itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3.Clone = new_instancemethod(_itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3_Clone, None, itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3)
itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3_swigregister = _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3_swigregister
itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3_swigregister(itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3)

def itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3___New_orig__() -> "itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3_Pointer":
    """itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3___New_orig__() -> itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3_Pointer"""
    return _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3___New_orig__()

def itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3_cast(obj: 'itkLightObject') -> "itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3 *":
    """itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3_cast(itkLightObject obj) -> itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3"""
    return _itkMagnitudeAndPhaseToComplexImageFilterPython.itkMagnitudeAndPhaseToComplexImageFilterIF3IF3ICF3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def magnitude_and_phase_to_complex_image_filter(*args, **kwargs):
    """Procedural interface for MagnitudeAndPhaseToComplexImageFilter"""
    import itk
    instance = itk.MagnitudeAndPhaseToComplexImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def magnitude_and_phase_to_complex_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.MagnitudeAndPhaseToComplexImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.MagnitudeAndPhaseToComplexImageFilter.values()[0]
    else:
        filter_object = itk.MagnitudeAndPhaseToComplexImageFilter

    magnitude_and_phase_to_complex_image_filter.__doc__ = filter_object.__doc__
    magnitude_and_phase_to_complex_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    magnitude_and_phase_to_complex_image_filter.__doc__ += "Available Keyword Arguments:\n"
    magnitude_and_phase_to_complex_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



