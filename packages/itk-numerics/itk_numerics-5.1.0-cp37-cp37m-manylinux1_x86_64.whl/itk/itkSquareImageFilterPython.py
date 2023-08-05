# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkSquareImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkSquareImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkSquareImageFilterPython
            return _itkSquareImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkSquareImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkSquareImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkSquareImageFilterPython
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


import itkUnaryGeneratorImageFilterPython
import itkInPlaceImageFilterBPython
import itkImageToImageFilterBPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import stdcomplexPython
import pyBasePython
import itkIndexPython
import itkSizePython
import itkOffsetPython
import ITKCommonBasePython
import itkImagePython
import itkPointPython
import vnl_vector_refPython
import vnl_vectorPython
import vnl_matrixPython
import itkFixedArrayPython
import itkVectorPython
import itkMatrixPython
import itkCovariantVectorPython
import vnl_matrix_fixedPython
import itkRGBAPixelPython
import itkImageRegionPython
import itkRGBPixelPython
import itkSymmetricSecondRankTensorPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterAPython

def itkSquareImageFilterID3ID3_New():
  return itkSquareImageFilterID3ID3.New()


def itkSquareImageFilterID2ID2_New():
  return itkSquareImageFilterID2ID2.New()


def itkSquareImageFilterIF3IF3_New():
  return itkSquareImageFilterIF3IF3.New()


def itkSquareImageFilterIF2IF2_New():
  return itkSquareImageFilterIF2IF2.New()


def itkSquareImageFilterIUS3IUS3_New():
  return itkSquareImageFilterIUS3IUS3.New()


def itkSquareImageFilterIUS2IUS2_New():
  return itkSquareImageFilterIUS2IUS2.New()


def itkSquareImageFilterIUC3IUC3_New():
  return itkSquareImageFilterIUC3IUC3.New()


def itkSquareImageFilterIUC2IUC2_New():
  return itkSquareImageFilterIUC2IUC2.New()


def itkSquareImageFilterISS3ISS3_New():
  return itkSquareImageFilterISS3ISS3.New()


def itkSquareImageFilterISS2ISS2_New():
  return itkSquareImageFilterISS2ISS2.New()

class itkSquareImageFilterID2ID2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID2ID2):
    """


    Computes the square of the intensity values pixel-wise.

    C++ includes: itkSquareImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSquareImageFilterID2ID2_Pointer":
        """__New_orig__() -> itkSquareImageFilterID2ID2_Pointer"""
        return _itkSquareImageFilterPython.itkSquareImageFilterID2ID2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSquareImageFilterID2ID2_Pointer":
        """Clone(itkSquareImageFilterID2ID2 self) -> itkSquareImageFilterID2ID2_Pointer"""
        return _itkSquareImageFilterPython.itkSquareImageFilterID2ID2_Clone(self)

    InputHasNumericTraitsCheck = _itkSquareImageFilterPython.itkSquareImageFilterID2ID2_InputHasNumericTraitsCheck
    RealTypeMultiplyOperatorCheck = _itkSquareImageFilterPython.itkSquareImageFilterID2ID2_RealTypeMultiplyOperatorCheck
    __swig_destroy__ = _itkSquareImageFilterPython.delete_itkSquareImageFilterID2ID2

    def cast(obj: 'itkLightObject') -> "itkSquareImageFilterID2ID2 *":
        """cast(itkLightObject obj) -> itkSquareImageFilterID2ID2"""
        return _itkSquareImageFilterPython.itkSquareImageFilterID2ID2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkSquareImageFilterID2ID2

        Create a new object of the class itkSquareImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSquareImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSquareImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSquareImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSquareImageFilterID2ID2.Clone = new_instancemethod(_itkSquareImageFilterPython.itkSquareImageFilterID2ID2_Clone, None, itkSquareImageFilterID2ID2)
itkSquareImageFilterID2ID2_swigregister = _itkSquareImageFilterPython.itkSquareImageFilterID2ID2_swigregister
itkSquareImageFilterID2ID2_swigregister(itkSquareImageFilterID2ID2)

def itkSquareImageFilterID2ID2___New_orig__() -> "itkSquareImageFilterID2ID2_Pointer":
    """itkSquareImageFilterID2ID2___New_orig__() -> itkSquareImageFilterID2ID2_Pointer"""
    return _itkSquareImageFilterPython.itkSquareImageFilterID2ID2___New_orig__()

def itkSquareImageFilterID2ID2_cast(obj: 'itkLightObject') -> "itkSquareImageFilterID2ID2 *":
    """itkSquareImageFilterID2ID2_cast(itkLightObject obj) -> itkSquareImageFilterID2ID2"""
    return _itkSquareImageFilterPython.itkSquareImageFilterID2ID2_cast(obj)

class itkSquareImageFilterID3ID3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterID3ID3):
    """


    Computes the square of the intensity values pixel-wise.

    C++ includes: itkSquareImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSquareImageFilterID3ID3_Pointer":
        """__New_orig__() -> itkSquareImageFilterID3ID3_Pointer"""
        return _itkSquareImageFilterPython.itkSquareImageFilterID3ID3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSquareImageFilterID3ID3_Pointer":
        """Clone(itkSquareImageFilterID3ID3 self) -> itkSquareImageFilterID3ID3_Pointer"""
        return _itkSquareImageFilterPython.itkSquareImageFilterID3ID3_Clone(self)

    InputHasNumericTraitsCheck = _itkSquareImageFilterPython.itkSquareImageFilterID3ID3_InputHasNumericTraitsCheck
    RealTypeMultiplyOperatorCheck = _itkSquareImageFilterPython.itkSquareImageFilterID3ID3_RealTypeMultiplyOperatorCheck
    __swig_destroy__ = _itkSquareImageFilterPython.delete_itkSquareImageFilterID3ID3

    def cast(obj: 'itkLightObject') -> "itkSquareImageFilterID3ID3 *":
        """cast(itkLightObject obj) -> itkSquareImageFilterID3ID3"""
        return _itkSquareImageFilterPython.itkSquareImageFilterID3ID3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkSquareImageFilterID3ID3

        Create a new object of the class itkSquareImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSquareImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSquareImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSquareImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSquareImageFilterID3ID3.Clone = new_instancemethod(_itkSquareImageFilterPython.itkSquareImageFilterID3ID3_Clone, None, itkSquareImageFilterID3ID3)
itkSquareImageFilterID3ID3_swigregister = _itkSquareImageFilterPython.itkSquareImageFilterID3ID3_swigregister
itkSquareImageFilterID3ID3_swigregister(itkSquareImageFilterID3ID3)

def itkSquareImageFilterID3ID3___New_orig__() -> "itkSquareImageFilterID3ID3_Pointer":
    """itkSquareImageFilterID3ID3___New_orig__() -> itkSquareImageFilterID3ID3_Pointer"""
    return _itkSquareImageFilterPython.itkSquareImageFilterID3ID3___New_orig__()

def itkSquareImageFilterID3ID3_cast(obj: 'itkLightObject') -> "itkSquareImageFilterID3ID3 *":
    """itkSquareImageFilterID3ID3_cast(itkLightObject obj) -> itkSquareImageFilterID3ID3"""
    return _itkSquareImageFilterPython.itkSquareImageFilterID3ID3_cast(obj)

class itkSquareImageFilterIF2IF2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF2IF2):
    """


    Computes the square of the intensity values pixel-wise.

    C++ includes: itkSquareImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSquareImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkSquareImageFilterIF2IF2_Pointer"""
        return _itkSquareImageFilterPython.itkSquareImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSquareImageFilterIF2IF2_Pointer":
        """Clone(itkSquareImageFilterIF2IF2 self) -> itkSquareImageFilterIF2IF2_Pointer"""
        return _itkSquareImageFilterPython.itkSquareImageFilterIF2IF2_Clone(self)

    InputHasNumericTraitsCheck = _itkSquareImageFilterPython.itkSquareImageFilterIF2IF2_InputHasNumericTraitsCheck
    RealTypeMultiplyOperatorCheck = _itkSquareImageFilterPython.itkSquareImageFilterIF2IF2_RealTypeMultiplyOperatorCheck
    __swig_destroy__ = _itkSquareImageFilterPython.delete_itkSquareImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkSquareImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkSquareImageFilterIF2IF2"""
        return _itkSquareImageFilterPython.itkSquareImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkSquareImageFilterIF2IF2

        Create a new object of the class itkSquareImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSquareImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSquareImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSquareImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSquareImageFilterIF2IF2.Clone = new_instancemethod(_itkSquareImageFilterPython.itkSquareImageFilterIF2IF2_Clone, None, itkSquareImageFilterIF2IF2)
itkSquareImageFilterIF2IF2_swigregister = _itkSquareImageFilterPython.itkSquareImageFilterIF2IF2_swigregister
itkSquareImageFilterIF2IF2_swigregister(itkSquareImageFilterIF2IF2)

def itkSquareImageFilterIF2IF2___New_orig__() -> "itkSquareImageFilterIF2IF2_Pointer":
    """itkSquareImageFilterIF2IF2___New_orig__() -> itkSquareImageFilterIF2IF2_Pointer"""
    return _itkSquareImageFilterPython.itkSquareImageFilterIF2IF2___New_orig__()

def itkSquareImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkSquareImageFilterIF2IF2 *":
    """itkSquareImageFilterIF2IF2_cast(itkLightObject obj) -> itkSquareImageFilterIF2IF2"""
    return _itkSquareImageFilterPython.itkSquareImageFilterIF2IF2_cast(obj)

class itkSquareImageFilterIF3IF3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIF3IF3):
    """


    Computes the square of the intensity values pixel-wise.

    C++ includes: itkSquareImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSquareImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkSquareImageFilterIF3IF3_Pointer"""
        return _itkSquareImageFilterPython.itkSquareImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSquareImageFilterIF3IF3_Pointer":
        """Clone(itkSquareImageFilterIF3IF3 self) -> itkSquareImageFilterIF3IF3_Pointer"""
        return _itkSquareImageFilterPython.itkSquareImageFilterIF3IF3_Clone(self)

    InputHasNumericTraitsCheck = _itkSquareImageFilterPython.itkSquareImageFilterIF3IF3_InputHasNumericTraitsCheck
    RealTypeMultiplyOperatorCheck = _itkSquareImageFilterPython.itkSquareImageFilterIF3IF3_RealTypeMultiplyOperatorCheck
    __swig_destroy__ = _itkSquareImageFilterPython.delete_itkSquareImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkSquareImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkSquareImageFilterIF3IF3"""
        return _itkSquareImageFilterPython.itkSquareImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkSquareImageFilterIF3IF3

        Create a new object of the class itkSquareImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSquareImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSquareImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSquareImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSquareImageFilterIF3IF3.Clone = new_instancemethod(_itkSquareImageFilterPython.itkSquareImageFilterIF3IF3_Clone, None, itkSquareImageFilterIF3IF3)
itkSquareImageFilterIF3IF3_swigregister = _itkSquareImageFilterPython.itkSquareImageFilterIF3IF3_swigregister
itkSquareImageFilterIF3IF3_swigregister(itkSquareImageFilterIF3IF3)

def itkSquareImageFilterIF3IF3___New_orig__() -> "itkSquareImageFilterIF3IF3_Pointer":
    """itkSquareImageFilterIF3IF3___New_orig__() -> itkSquareImageFilterIF3IF3_Pointer"""
    return _itkSquareImageFilterPython.itkSquareImageFilterIF3IF3___New_orig__()

def itkSquareImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkSquareImageFilterIF3IF3 *":
    """itkSquareImageFilterIF3IF3_cast(itkLightObject obj) -> itkSquareImageFilterIF3IF3"""
    return _itkSquareImageFilterPython.itkSquareImageFilterIF3IF3_cast(obj)

class itkSquareImageFilterISS2ISS2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterISS2ISS2):
    """


    Computes the square of the intensity values pixel-wise.

    C++ includes: itkSquareImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSquareImageFilterISS2ISS2_Pointer":
        """__New_orig__() -> itkSquareImageFilterISS2ISS2_Pointer"""
        return _itkSquareImageFilterPython.itkSquareImageFilterISS2ISS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSquareImageFilterISS2ISS2_Pointer":
        """Clone(itkSquareImageFilterISS2ISS2 self) -> itkSquareImageFilterISS2ISS2_Pointer"""
        return _itkSquareImageFilterPython.itkSquareImageFilterISS2ISS2_Clone(self)

    InputHasNumericTraitsCheck = _itkSquareImageFilterPython.itkSquareImageFilterISS2ISS2_InputHasNumericTraitsCheck
    RealTypeMultiplyOperatorCheck = _itkSquareImageFilterPython.itkSquareImageFilterISS2ISS2_RealTypeMultiplyOperatorCheck
    __swig_destroy__ = _itkSquareImageFilterPython.delete_itkSquareImageFilterISS2ISS2

    def cast(obj: 'itkLightObject') -> "itkSquareImageFilterISS2ISS2 *":
        """cast(itkLightObject obj) -> itkSquareImageFilterISS2ISS2"""
        return _itkSquareImageFilterPython.itkSquareImageFilterISS2ISS2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkSquareImageFilterISS2ISS2

        Create a new object of the class itkSquareImageFilterISS2ISS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSquareImageFilterISS2ISS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSquareImageFilterISS2ISS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSquareImageFilterISS2ISS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSquareImageFilterISS2ISS2.Clone = new_instancemethod(_itkSquareImageFilterPython.itkSquareImageFilterISS2ISS2_Clone, None, itkSquareImageFilterISS2ISS2)
itkSquareImageFilterISS2ISS2_swigregister = _itkSquareImageFilterPython.itkSquareImageFilterISS2ISS2_swigregister
itkSquareImageFilterISS2ISS2_swigregister(itkSquareImageFilterISS2ISS2)

def itkSquareImageFilterISS2ISS2___New_orig__() -> "itkSquareImageFilterISS2ISS2_Pointer":
    """itkSquareImageFilterISS2ISS2___New_orig__() -> itkSquareImageFilterISS2ISS2_Pointer"""
    return _itkSquareImageFilterPython.itkSquareImageFilterISS2ISS2___New_orig__()

def itkSquareImageFilterISS2ISS2_cast(obj: 'itkLightObject') -> "itkSquareImageFilterISS2ISS2 *":
    """itkSquareImageFilterISS2ISS2_cast(itkLightObject obj) -> itkSquareImageFilterISS2ISS2"""
    return _itkSquareImageFilterPython.itkSquareImageFilterISS2ISS2_cast(obj)

class itkSquareImageFilterISS3ISS3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterISS3ISS3):
    """


    Computes the square of the intensity values pixel-wise.

    C++ includes: itkSquareImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSquareImageFilterISS3ISS3_Pointer":
        """__New_orig__() -> itkSquareImageFilterISS3ISS3_Pointer"""
        return _itkSquareImageFilterPython.itkSquareImageFilterISS3ISS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSquareImageFilterISS3ISS3_Pointer":
        """Clone(itkSquareImageFilterISS3ISS3 self) -> itkSquareImageFilterISS3ISS3_Pointer"""
        return _itkSquareImageFilterPython.itkSquareImageFilterISS3ISS3_Clone(self)

    InputHasNumericTraitsCheck = _itkSquareImageFilterPython.itkSquareImageFilterISS3ISS3_InputHasNumericTraitsCheck
    RealTypeMultiplyOperatorCheck = _itkSquareImageFilterPython.itkSquareImageFilterISS3ISS3_RealTypeMultiplyOperatorCheck
    __swig_destroy__ = _itkSquareImageFilterPython.delete_itkSquareImageFilterISS3ISS3

    def cast(obj: 'itkLightObject') -> "itkSquareImageFilterISS3ISS3 *":
        """cast(itkLightObject obj) -> itkSquareImageFilterISS3ISS3"""
        return _itkSquareImageFilterPython.itkSquareImageFilterISS3ISS3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkSquareImageFilterISS3ISS3

        Create a new object of the class itkSquareImageFilterISS3ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSquareImageFilterISS3ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSquareImageFilterISS3ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSquareImageFilterISS3ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSquareImageFilterISS3ISS3.Clone = new_instancemethod(_itkSquareImageFilterPython.itkSquareImageFilterISS3ISS3_Clone, None, itkSquareImageFilterISS3ISS3)
itkSquareImageFilterISS3ISS3_swigregister = _itkSquareImageFilterPython.itkSquareImageFilterISS3ISS3_swigregister
itkSquareImageFilterISS3ISS3_swigregister(itkSquareImageFilterISS3ISS3)

def itkSquareImageFilterISS3ISS3___New_orig__() -> "itkSquareImageFilterISS3ISS3_Pointer":
    """itkSquareImageFilterISS3ISS3___New_orig__() -> itkSquareImageFilterISS3ISS3_Pointer"""
    return _itkSquareImageFilterPython.itkSquareImageFilterISS3ISS3___New_orig__()

def itkSquareImageFilterISS3ISS3_cast(obj: 'itkLightObject') -> "itkSquareImageFilterISS3ISS3 *":
    """itkSquareImageFilterISS3ISS3_cast(itkLightObject obj) -> itkSquareImageFilterISS3ISS3"""
    return _itkSquareImageFilterPython.itkSquareImageFilterISS3ISS3_cast(obj)

class itkSquareImageFilterIUC2IUC2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUC2IUC2):
    """


    Computes the square of the intensity values pixel-wise.

    C++ includes: itkSquareImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSquareImageFilterIUC2IUC2_Pointer":
        """__New_orig__() -> itkSquareImageFilterIUC2IUC2_Pointer"""
        return _itkSquareImageFilterPython.itkSquareImageFilterIUC2IUC2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSquareImageFilterIUC2IUC2_Pointer":
        """Clone(itkSquareImageFilterIUC2IUC2 self) -> itkSquareImageFilterIUC2IUC2_Pointer"""
        return _itkSquareImageFilterPython.itkSquareImageFilterIUC2IUC2_Clone(self)

    InputHasNumericTraitsCheck = _itkSquareImageFilterPython.itkSquareImageFilterIUC2IUC2_InputHasNumericTraitsCheck
    RealTypeMultiplyOperatorCheck = _itkSquareImageFilterPython.itkSquareImageFilterIUC2IUC2_RealTypeMultiplyOperatorCheck
    __swig_destroy__ = _itkSquareImageFilterPython.delete_itkSquareImageFilterIUC2IUC2

    def cast(obj: 'itkLightObject') -> "itkSquareImageFilterIUC2IUC2 *":
        """cast(itkLightObject obj) -> itkSquareImageFilterIUC2IUC2"""
        return _itkSquareImageFilterPython.itkSquareImageFilterIUC2IUC2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkSquareImageFilterIUC2IUC2

        Create a new object of the class itkSquareImageFilterIUC2IUC2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSquareImageFilterIUC2IUC2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSquareImageFilterIUC2IUC2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSquareImageFilterIUC2IUC2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSquareImageFilterIUC2IUC2.Clone = new_instancemethod(_itkSquareImageFilterPython.itkSquareImageFilterIUC2IUC2_Clone, None, itkSquareImageFilterIUC2IUC2)
itkSquareImageFilterIUC2IUC2_swigregister = _itkSquareImageFilterPython.itkSquareImageFilterIUC2IUC2_swigregister
itkSquareImageFilterIUC2IUC2_swigregister(itkSquareImageFilterIUC2IUC2)

def itkSquareImageFilterIUC2IUC2___New_orig__() -> "itkSquareImageFilterIUC2IUC2_Pointer":
    """itkSquareImageFilterIUC2IUC2___New_orig__() -> itkSquareImageFilterIUC2IUC2_Pointer"""
    return _itkSquareImageFilterPython.itkSquareImageFilterIUC2IUC2___New_orig__()

def itkSquareImageFilterIUC2IUC2_cast(obj: 'itkLightObject') -> "itkSquareImageFilterIUC2IUC2 *":
    """itkSquareImageFilterIUC2IUC2_cast(itkLightObject obj) -> itkSquareImageFilterIUC2IUC2"""
    return _itkSquareImageFilterPython.itkSquareImageFilterIUC2IUC2_cast(obj)

class itkSquareImageFilterIUC3IUC3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUC3IUC3):
    """


    Computes the square of the intensity values pixel-wise.

    C++ includes: itkSquareImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSquareImageFilterIUC3IUC3_Pointer":
        """__New_orig__() -> itkSquareImageFilterIUC3IUC3_Pointer"""
        return _itkSquareImageFilterPython.itkSquareImageFilterIUC3IUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSquareImageFilterIUC3IUC3_Pointer":
        """Clone(itkSquareImageFilterIUC3IUC3 self) -> itkSquareImageFilterIUC3IUC3_Pointer"""
        return _itkSquareImageFilterPython.itkSquareImageFilterIUC3IUC3_Clone(self)

    InputHasNumericTraitsCheck = _itkSquareImageFilterPython.itkSquareImageFilterIUC3IUC3_InputHasNumericTraitsCheck
    RealTypeMultiplyOperatorCheck = _itkSquareImageFilterPython.itkSquareImageFilterIUC3IUC3_RealTypeMultiplyOperatorCheck
    __swig_destroy__ = _itkSquareImageFilterPython.delete_itkSquareImageFilterIUC3IUC3

    def cast(obj: 'itkLightObject') -> "itkSquareImageFilterIUC3IUC3 *":
        """cast(itkLightObject obj) -> itkSquareImageFilterIUC3IUC3"""
        return _itkSquareImageFilterPython.itkSquareImageFilterIUC3IUC3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkSquareImageFilterIUC3IUC3

        Create a new object of the class itkSquareImageFilterIUC3IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSquareImageFilterIUC3IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSquareImageFilterIUC3IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSquareImageFilterIUC3IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSquareImageFilterIUC3IUC3.Clone = new_instancemethod(_itkSquareImageFilterPython.itkSquareImageFilterIUC3IUC3_Clone, None, itkSquareImageFilterIUC3IUC3)
itkSquareImageFilterIUC3IUC3_swigregister = _itkSquareImageFilterPython.itkSquareImageFilterIUC3IUC3_swigregister
itkSquareImageFilterIUC3IUC3_swigregister(itkSquareImageFilterIUC3IUC3)

def itkSquareImageFilterIUC3IUC3___New_orig__() -> "itkSquareImageFilterIUC3IUC3_Pointer":
    """itkSquareImageFilterIUC3IUC3___New_orig__() -> itkSquareImageFilterIUC3IUC3_Pointer"""
    return _itkSquareImageFilterPython.itkSquareImageFilterIUC3IUC3___New_orig__()

def itkSquareImageFilterIUC3IUC3_cast(obj: 'itkLightObject') -> "itkSquareImageFilterIUC3IUC3 *":
    """itkSquareImageFilterIUC3IUC3_cast(itkLightObject obj) -> itkSquareImageFilterIUC3IUC3"""
    return _itkSquareImageFilterPython.itkSquareImageFilterIUC3IUC3_cast(obj)

class itkSquareImageFilterIUS2IUS2(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUS2IUS2):
    """


    Computes the square of the intensity values pixel-wise.

    C++ includes: itkSquareImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSquareImageFilterIUS2IUS2_Pointer":
        """__New_orig__() -> itkSquareImageFilterIUS2IUS2_Pointer"""
        return _itkSquareImageFilterPython.itkSquareImageFilterIUS2IUS2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSquareImageFilterIUS2IUS2_Pointer":
        """Clone(itkSquareImageFilterIUS2IUS2 self) -> itkSquareImageFilterIUS2IUS2_Pointer"""
        return _itkSquareImageFilterPython.itkSquareImageFilterIUS2IUS2_Clone(self)

    InputHasNumericTraitsCheck = _itkSquareImageFilterPython.itkSquareImageFilterIUS2IUS2_InputHasNumericTraitsCheck
    RealTypeMultiplyOperatorCheck = _itkSquareImageFilterPython.itkSquareImageFilterIUS2IUS2_RealTypeMultiplyOperatorCheck
    __swig_destroy__ = _itkSquareImageFilterPython.delete_itkSquareImageFilterIUS2IUS2

    def cast(obj: 'itkLightObject') -> "itkSquareImageFilterIUS2IUS2 *":
        """cast(itkLightObject obj) -> itkSquareImageFilterIUS2IUS2"""
        return _itkSquareImageFilterPython.itkSquareImageFilterIUS2IUS2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkSquareImageFilterIUS2IUS2

        Create a new object of the class itkSquareImageFilterIUS2IUS2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSquareImageFilterIUS2IUS2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSquareImageFilterIUS2IUS2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSquareImageFilterIUS2IUS2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSquareImageFilterIUS2IUS2.Clone = new_instancemethod(_itkSquareImageFilterPython.itkSquareImageFilterIUS2IUS2_Clone, None, itkSquareImageFilterIUS2IUS2)
itkSquareImageFilterIUS2IUS2_swigregister = _itkSquareImageFilterPython.itkSquareImageFilterIUS2IUS2_swigregister
itkSquareImageFilterIUS2IUS2_swigregister(itkSquareImageFilterIUS2IUS2)

def itkSquareImageFilterIUS2IUS2___New_orig__() -> "itkSquareImageFilterIUS2IUS2_Pointer":
    """itkSquareImageFilterIUS2IUS2___New_orig__() -> itkSquareImageFilterIUS2IUS2_Pointer"""
    return _itkSquareImageFilterPython.itkSquareImageFilterIUS2IUS2___New_orig__()

def itkSquareImageFilterIUS2IUS2_cast(obj: 'itkLightObject') -> "itkSquareImageFilterIUS2IUS2 *":
    """itkSquareImageFilterIUS2IUS2_cast(itkLightObject obj) -> itkSquareImageFilterIUS2IUS2"""
    return _itkSquareImageFilterPython.itkSquareImageFilterIUS2IUS2_cast(obj)

class itkSquareImageFilterIUS3IUS3(itkUnaryGeneratorImageFilterPython.itkUnaryGeneratorImageFilterIUS3IUS3):
    """


    Computes the square of the intensity values pixel-wise.

    C++ includes: itkSquareImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkSquareImageFilterIUS3IUS3_Pointer":
        """__New_orig__() -> itkSquareImageFilterIUS3IUS3_Pointer"""
        return _itkSquareImageFilterPython.itkSquareImageFilterIUS3IUS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkSquareImageFilterIUS3IUS3_Pointer":
        """Clone(itkSquareImageFilterIUS3IUS3 self) -> itkSquareImageFilterIUS3IUS3_Pointer"""
        return _itkSquareImageFilterPython.itkSquareImageFilterIUS3IUS3_Clone(self)

    InputHasNumericTraitsCheck = _itkSquareImageFilterPython.itkSquareImageFilterIUS3IUS3_InputHasNumericTraitsCheck
    RealTypeMultiplyOperatorCheck = _itkSquareImageFilterPython.itkSquareImageFilterIUS3IUS3_RealTypeMultiplyOperatorCheck
    __swig_destroy__ = _itkSquareImageFilterPython.delete_itkSquareImageFilterIUS3IUS3

    def cast(obj: 'itkLightObject') -> "itkSquareImageFilterIUS3IUS3 *":
        """cast(itkLightObject obj) -> itkSquareImageFilterIUS3IUS3"""
        return _itkSquareImageFilterPython.itkSquareImageFilterIUS3IUS3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkSquareImageFilterIUS3IUS3

        Create a new object of the class itkSquareImageFilterIUS3IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkSquareImageFilterIUS3IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkSquareImageFilterIUS3IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkSquareImageFilterIUS3IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkSquareImageFilterIUS3IUS3.Clone = new_instancemethod(_itkSquareImageFilterPython.itkSquareImageFilterIUS3IUS3_Clone, None, itkSquareImageFilterIUS3IUS3)
itkSquareImageFilterIUS3IUS3_swigregister = _itkSquareImageFilterPython.itkSquareImageFilterIUS3IUS3_swigregister
itkSquareImageFilterIUS3IUS3_swigregister(itkSquareImageFilterIUS3IUS3)

def itkSquareImageFilterIUS3IUS3___New_orig__() -> "itkSquareImageFilterIUS3IUS3_Pointer":
    """itkSquareImageFilterIUS3IUS3___New_orig__() -> itkSquareImageFilterIUS3IUS3_Pointer"""
    return _itkSquareImageFilterPython.itkSquareImageFilterIUS3IUS3___New_orig__()

def itkSquareImageFilterIUS3IUS3_cast(obj: 'itkLightObject') -> "itkSquareImageFilterIUS3IUS3 *":
    """itkSquareImageFilterIUS3IUS3_cast(itkLightObject obj) -> itkSquareImageFilterIUS3IUS3"""
    return _itkSquareImageFilterPython.itkSquareImageFilterIUS3IUS3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def square_image_filter(*args, **kwargs):
    """Procedural interface for SquareImageFilter"""
    import itk
    instance = itk.SquareImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def square_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.SquareImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.SquareImageFilter.values()[0]
    else:
        filter_object = itk.SquareImageFilter

    square_image_filter.__doc__ = filter_object.__doc__
    square_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    square_image_filter.__doc__ += "Available Keyword Arguments:\n"
    square_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



