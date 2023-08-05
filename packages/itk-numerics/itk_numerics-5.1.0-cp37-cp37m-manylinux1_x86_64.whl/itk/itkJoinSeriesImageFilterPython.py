# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkJoinSeriesImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkJoinSeriesImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkJoinSeriesImageFilterPython
            return _itkJoinSeriesImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkJoinSeriesImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkJoinSeriesImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkJoinSeriesImageFilterPython
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
import itkImageRegionPython
import itkIndexPython
import itkSizePython
import itkOffsetPython
import itkImageToImageFilterBPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import stdcomplexPython
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
import itkRGBPixelPython
import itkSymmetricSecondRankTensorPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython

def itkJoinSeriesImageFilterID2ID3_New():
  return itkJoinSeriesImageFilterID2ID3.New()


def itkJoinSeriesImageFilterIF2IF3_New():
  return itkJoinSeriesImageFilterIF2IF3.New()


def itkJoinSeriesImageFilterIUS2IUS3_New():
  return itkJoinSeriesImageFilterIUS2IUS3.New()


def itkJoinSeriesImageFilterIUC2IUC3_New():
  return itkJoinSeriesImageFilterIUC2IUC3.New()


def itkJoinSeriesImageFilterISS2ISS3_New():
  return itkJoinSeriesImageFilterISS2ISS3.New()

class itkJoinSeriesImageFilterID2ID3(itkImageToImageFilterBPython.itkImageToImageFilterID2ID3):
    """


    Join N-D images into an (N+1)-D image.

    This filter is templated over the input image type and the output
    image type. The pixel type of them must be the same and the input
    dimension must be less than the output dimension. When the input
    images are N-dimensional, they are joined in order and the size of the
    N+1'th dimension of the output is same as the number of the inputs.
    The spacing and the origin (where the first input is placed) for the
    N+1'th dimension is specified in this filter. The output image
    informations for the first N dimensions are taken from the first
    input. Note that all the inputs should have the same information.

    Hideaki Hiraki  Contributed in the users
    listhttp://public.kitware.com/pipermail/insight-
    users/2004-February/006542.html

    C++ includes: itkJoinSeriesImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkJoinSeriesImageFilterID2ID3_Pointer":
        """__New_orig__() -> itkJoinSeriesImageFilterID2ID3_Pointer"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterID2ID3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkJoinSeriesImageFilterID2ID3_Pointer":
        """Clone(itkJoinSeriesImageFilterID2ID3 self) -> itkJoinSeriesImageFilterID2ID3_Pointer"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterID2ID3_Clone(self)


    def SetSpacing(self, _arg: 'double const') -> "void":
        """
        SetSpacing(itkJoinSeriesImageFilterID2ID3 self, double const _arg)

        Set/Get spacing of the
        new dimension 
        """
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterID2ID3_SetSpacing(self, _arg)


    def GetSpacing(self) -> "double":
        """GetSpacing(itkJoinSeriesImageFilterID2ID3 self) -> double"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterID2ID3_GetSpacing(self)


    def SetOrigin(self, _arg: 'double const') -> "void":
        """
        SetOrigin(itkJoinSeriesImageFilterID2ID3 self, double const _arg)

        Set/Get origin of the new
        dimension 
        """
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterID2ID3_SetOrigin(self, _arg)


    def GetOrigin(self) -> "double":
        """GetOrigin(itkJoinSeriesImageFilterID2ID3 self) -> double"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterID2ID3_GetOrigin(self)

    InputConvertibleToOutputCheck = _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterID2ID3_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkJoinSeriesImageFilterPython.delete_itkJoinSeriesImageFilterID2ID3

    def cast(obj: 'itkLightObject') -> "itkJoinSeriesImageFilterID2ID3 *":
        """cast(itkLightObject obj) -> itkJoinSeriesImageFilterID2ID3"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterID2ID3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkJoinSeriesImageFilterID2ID3

        Create a new object of the class itkJoinSeriesImageFilterID2ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkJoinSeriesImageFilterID2ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkJoinSeriesImageFilterID2ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkJoinSeriesImageFilterID2ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkJoinSeriesImageFilterID2ID3.Clone = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterID2ID3_Clone, None, itkJoinSeriesImageFilterID2ID3)
itkJoinSeriesImageFilterID2ID3.SetSpacing = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterID2ID3_SetSpacing, None, itkJoinSeriesImageFilterID2ID3)
itkJoinSeriesImageFilterID2ID3.GetSpacing = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterID2ID3_GetSpacing, None, itkJoinSeriesImageFilterID2ID3)
itkJoinSeriesImageFilterID2ID3.SetOrigin = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterID2ID3_SetOrigin, None, itkJoinSeriesImageFilterID2ID3)
itkJoinSeriesImageFilterID2ID3.GetOrigin = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterID2ID3_GetOrigin, None, itkJoinSeriesImageFilterID2ID3)
itkJoinSeriesImageFilterID2ID3_swigregister = _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterID2ID3_swigregister
itkJoinSeriesImageFilterID2ID3_swigregister(itkJoinSeriesImageFilterID2ID3)

def itkJoinSeriesImageFilterID2ID3___New_orig__() -> "itkJoinSeriesImageFilterID2ID3_Pointer":
    """itkJoinSeriesImageFilterID2ID3___New_orig__() -> itkJoinSeriesImageFilterID2ID3_Pointer"""
    return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterID2ID3___New_orig__()

def itkJoinSeriesImageFilterID2ID3_cast(obj: 'itkLightObject') -> "itkJoinSeriesImageFilterID2ID3 *":
    """itkJoinSeriesImageFilterID2ID3_cast(itkLightObject obj) -> itkJoinSeriesImageFilterID2ID3"""
    return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterID2ID3_cast(obj)

class itkJoinSeriesImageFilterIF2IF3(itkImageToImageFilterBPython.itkImageToImageFilterIF2IF3):
    """


    Join N-D images into an (N+1)-D image.

    This filter is templated over the input image type and the output
    image type. The pixel type of them must be the same and the input
    dimension must be less than the output dimension. When the input
    images are N-dimensional, they are joined in order and the size of the
    N+1'th dimension of the output is same as the number of the inputs.
    The spacing and the origin (where the first input is placed) for the
    N+1'th dimension is specified in this filter. The output image
    informations for the first N dimensions are taken from the first
    input. Note that all the inputs should have the same information.

    Hideaki Hiraki  Contributed in the users
    listhttp://public.kitware.com/pipermail/insight-
    users/2004-February/006542.html

    C++ includes: itkJoinSeriesImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkJoinSeriesImageFilterIF2IF3_Pointer":
        """__New_orig__() -> itkJoinSeriesImageFilterIF2IF3_Pointer"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkJoinSeriesImageFilterIF2IF3_Pointer":
        """Clone(itkJoinSeriesImageFilterIF2IF3 self) -> itkJoinSeriesImageFilterIF2IF3_Pointer"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3_Clone(self)


    def SetSpacing(self, _arg: 'double const') -> "void":
        """
        SetSpacing(itkJoinSeriesImageFilterIF2IF3 self, double const _arg)

        Set/Get spacing of the
        new dimension 
        """
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3_SetSpacing(self, _arg)


    def GetSpacing(self) -> "double":
        """GetSpacing(itkJoinSeriesImageFilterIF2IF3 self) -> double"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3_GetSpacing(self)


    def SetOrigin(self, _arg: 'double const') -> "void":
        """
        SetOrigin(itkJoinSeriesImageFilterIF2IF3 self, double const _arg)

        Set/Get origin of the new
        dimension 
        """
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3_SetOrigin(self, _arg)


    def GetOrigin(self) -> "double":
        """GetOrigin(itkJoinSeriesImageFilterIF2IF3 self) -> double"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3_GetOrigin(self)

    InputConvertibleToOutputCheck = _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkJoinSeriesImageFilterPython.delete_itkJoinSeriesImageFilterIF2IF3

    def cast(obj: 'itkLightObject') -> "itkJoinSeriesImageFilterIF2IF3 *":
        """cast(itkLightObject obj) -> itkJoinSeriesImageFilterIF2IF3"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkJoinSeriesImageFilterIF2IF3

        Create a new object of the class itkJoinSeriesImageFilterIF2IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkJoinSeriesImageFilterIF2IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkJoinSeriesImageFilterIF2IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkJoinSeriesImageFilterIF2IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkJoinSeriesImageFilterIF2IF3.Clone = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3_Clone, None, itkJoinSeriesImageFilterIF2IF3)
itkJoinSeriesImageFilterIF2IF3.SetSpacing = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3_SetSpacing, None, itkJoinSeriesImageFilterIF2IF3)
itkJoinSeriesImageFilterIF2IF3.GetSpacing = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3_GetSpacing, None, itkJoinSeriesImageFilterIF2IF3)
itkJoinSeriesImageFilterIF2IF3.SetOrigin = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3_SetOrigin, None, itkJoinSeriesImageFilterIF2IF3)
itkJoinSeriesImageFilterIF2IF3.GetOrigin = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3_GetOrigin, None, itkJoinSeriesImageFilterIF2IF3)
itkJoinSeriesImageFilterIF2IF3_swigregister = _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3_swigregister
itkJoinSeriesImageFilterIF2IF3_swigregister(itkJoinSeriesImageFilterIF2IF3)

def itkJoinSeriesImageFilterIF2IF3___New_orig__() -> "itkJoinSeriesImageFilterIF2IF3_Pointer":
    """itkJoinSeriesImageFilterIF2IF3___New_orig__() -> itkJoinSeriesImageFilterIF2IF3_Pointer"""
    return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3___New_orig__()

def itkJoinSeriesImageFilterIF2IF3_cast(obj: 'itkLightObject') -> "itkJoinSeriesImageFilterIF2IF3 *":
    """itkJoinSeriesImageFilterIF2IF3_cast(itkLightObject obj) -> itkJoinSeriesImageFilterIF2IF3"""
    return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIF2IF3_cast(obj)

class itkJoinSeriesImageFilterISS2ISS3(itkImageToImageFilterBPython.itkImageToImageFilterISS2ISS3):
    """


    Join N-D images into an (N+1)-D image.

    This filter is templated over the input image type and the output
    image type. The pixel type of them must be the same and the input
    dimension must be less than the output dimension. When the input
    images are N-dimensional, they are joined in order and the size of the
    N+1'th dimension of the output is same as the number of the inputs.
    The spacing and the origin (where the first input is placed) for the
    N+1'th dimension is specified in this filter. The output image
    informations for the first N dimensions are taken from the first
    input. Note that all the inputs should have the same information.

    Hideaki Hiraki  Contributed in the users
    listhttp://public.kitware.com/pipermail/insight-
    users/2004-February/006542.html

    C++ includes: itkJoinSeriesImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkJoinSeriesImageFilterISS2ISS3_Pointer":
        """__New_orig__() -> itkJoinSeriesImageFilterISS2ISS3_Pointer"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkJoinSeriesImageFilterISS2ISS3_Pointer":
        """Clone(itkJoinSeriesImageFilterISS2ISS3 self) -> itkJoinSeriesImageFilterISS2ISS3_Pointer"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3_Clone(self)


    def SetSpacing(self, _arg: 'double const') -> "void":
        """
        SetSpacing(itkJoinSeriesImageFilterISS2ISS3 self, double const _arg)

        Set/Get spacing of the
        new dimension 
        """
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3_SetSpacing(self, _arg)


    def GetSpacing(self) -> "double":
        """GetSpacing(itkJoinSeriesImageFilterISS2ISS3 self) -> double"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3_GetSpacing(self)


    def SetOrigin(self, _arg: 'double const') -> "void":
        """
        SetOrigin(itkJoinSeriesImageFilterISS2ISS3 self, double const _arg)

        Set/Get origin of the new
        dimension 
        """
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3_SetOrigin(self, _arg)


    def GetOrigin(self) -> "double":
        """GetOrigin(itkJoinSeriesImageFilterISS2ISS3 self) -> double"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3_GetOrigin(self)

    InputConvertibleToOutputCheck = _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkJoinSeriesImageFilterPython.delete_itkJoinSeriesImageFilterISS2ISS3

    def cast(obj: 'itkLightObject') -> "itkJoinSeriesImageFilterISS2ISS3 *":
        """cast(itkLightObject obj) -> itkJoinSeriesImageFilterISS2ISS3"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkJoinSeriesImageFilterISS2ISS3

        Create a new object of the class itkJoinSeriesImageFilterISS2ISS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkJoinSeriesImageFilterISS2ISS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkJoinSeriesImageFilterISS2ISS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkJoinSeriesImageFilterISS2ISS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkJoinSeriesImageFilterISS2ISS3.Clone = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3_Clone, None, itkJoinSeriesImageFilterISS2ISS3)
itkJoinSeriesImageFilterISS2ISS3.SetSpacing = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3_SetSpacing, None, itkJoinSeriesImageFilterISS2ISS3)
itkJoinSeriesImageFilterISS2ISS3.GetSpacing = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3_GetSpacing, None, itkJoinSeriesImageFilterISS2ISS3)
itkJoinSeriesImageFilterISS2ISS3.SetOrigin = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3_SetOrigin, None, itkJoinSeriesImageFilterISS2ISS3)
itkJoinSeriesImageFilterISS2ISS3.GetOrigin = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3_GetOrigin, None, itkJoinSeriesImageFilterISS2ISS3)
itkJoinSeriesImageFilterISS2ISS3_swigregister = _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3_swigregister
itkJoinSeriesImageFilterISS2ISS3_swigregister(itkJoinSeriesImageFilterISS2ISS3)

def itkJoinSeriesImageFilterISS2ISS3___New_orig__() -> "itkJoinSeriesImageFilterISS2ISS3_Pointer":
    """itkJoinSeriesImageFilterISS2ISS3___New_orig__() -> itkJoinSeriesImageFilterISS2ISS3_Pointer"""
    return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3___New_orig__()

def itkJoinSeriesImageFilterISS2ISS3_cast(obj: 'itkLightObject') -> "itkJoinSeriesImageFilterISS2ISS3 *":
    """itkJoinSeriesImageFilterISS2ISS3_cast(itkLightObject obj) -> itkJoinSeriesImageFilterISS2ISS3"""
    return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterISS2ISS3_cast(obj)

class itkJoinSeriesImageFilterIUC2IUC3(itkImageToImageFilterBPython.itkImageToImageFilterIUC2IUC3):
    """


    Join N-D images into an (N+1)-D image.

    This filter is templated over the input image type and the output
    image type. The pixel type of them must be the same and the input
    dimension must be less than the output dimension. When the input
    images are N-dimensional, they are joined in order and the size of the
    N+1'th dimension of the output is same as the number of the inputs.
    The spacing and the origin (where the first input is placed) for the
    N+1'th dimension is specified in this filter. The output image
    informations for the first N dimensions are taken from the first
    input. Note that all the inputs should have the same information.

    Hideaki Hiraki  Contributed in the users
    listhttp://public.kitware.com/pipermail/insight-
    users/2004-February/006542.html

    C++ includes: itkJoinSeriesImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkJoinSeriesImageFilterIUC2IUC3_Pointer":
        """__New_orig__() -> itkJoinSeriesImageFilterIUC2IUC3_Pointer"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkJoinSeriesImageFilterIUC2IUC3_Pointer":
        """Clone(itkJoinSeriesImageFilterIUC2IUC3 self) -> itkJoinSeriesImageFilterIUC2IUC3_Pointer"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3_Clone(self)


    def SetSpacing(self, _arg: 'double const') -> "void":
        """
        SetSpacing(itkJoinSeriesImageFilterIUC2IUC3 self, double const _arg)

        Set/Get spacing of the
        new dimension 
        """
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3_SetSpacing(self, _arg)


    def GetSpacing(self) -> "double":
        """GetSpacing(itkJoinSeriesImageFilterIUC2IUC3 self) -> double"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3_GetSpacing(self)


    def SetOrigin(self, _arg: 'double const') -> "void":
        """
        SetOrigin(itkJoinSeriesImageFilterIUC2IUC3 self, double const _arg)

        Set/Get origin of the new
        dimension 
        """
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3_SetOrigin(self, _arg)


    def GetOrigin(self) -> "double":
        """GetOrigin(itkJoinSeriesImageFilterIUC2IUC3 self) -> double"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3_GetOrigin(self)

    InputConvertibleToOutputCheck = _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkJoinSeriesImageFilterPython.delete_itkJoinSeriesImageFilterIUC2IUC3

    def cast(obj: 'itkLightObject') -> "itkJoinSeriesImageFilterIUC2IUC3 *":
        """cast(itkLightObject obj) -> itkJoinSeriesImageFilterIUC2IUC3"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkJoinSeriesImageFilterIUC2IUC3

        Create a new object of the class itkJoinSeriesImageFilterIUC2IUC3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkJoinSeriesImageFilterIUC2IUC3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkJoinSeriesImageFilterIUC2IUC3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkJoinSeriesImageFilterIUC2IUC3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkJoinSeriesImageFilterIUC2IUC3.Clone = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3_Clone, None, itkJoinSeriesImageFilterIUC2IUC3)
itkJoinSeriesImageFilterIUC2IUC3.SetSpacing = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3_SetSpacing, None, itkJoinSeriesImageFilterIUC2IUC3)
itkJoinSeriesImageFilterIUC2IUC3.GetSpacing = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3_GetSpacing, None, itkJoinSeriesImageFilterIUC2IUC3)
itkJoinSeriesImageFilterIUC2IUC3.SetOrigin = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3_SetOrigin, None, itkJoinSeriesImageFilterIUC2IUC3)
itkJoinSeriesImageFilterIUC2IUC3.GetOrigin = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3_GetOrigin, None, itkJoinSeriesImageFilterIUC2IUC3)
itkJoinSeriesImageFilterIUC2IUC3_swigregister = _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3_swigregister
itkJoinSeriesImageFilterIUC2IUC3_swigregister(itkJoinSeriesImageFilterIUC2IUC3)

def itkJoinSeriesImageFilterIUC2IUC3___New_orig__() -> "itkJoinSeriesImageFilterIUC2IUC3_Pointer":
    """itkJoinSeriesImageFilterIUC2IUC3___New_orig__() -> itkJoinSeriesImageFilterIUC2IUC3_Pointer"""
    return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3___New_orig__()

def itkJoinSeriesImageFilterIUC2IUC3_cast(obj: 'itkLightObject') -> "itkJoinSeriesImageFilterIUC2IUC3 *":
    """itkJoinSeriesImageFilterIUC2IUC3_cast(itkLightObject obj) -> itkJoinSeriesImageFilterIUC2IUC3"""
    return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUC2IUC3_cast(obj)

class itkJoinSeriesImageFilterIUS2IUS3(itkImageToImageFilterBPython.itkImageToImageFilterIUS2IUS3):
    """


    Join N-D images into an (N+1)-D image.

    This filter is templated over the input image type and the output
    image type. The pixel type of them must be the same and the input
    dimension must be less than the output dimension. When the input
    images are N-dimensional, they are joined in order and the size of the
    N+1'th dimension of the output is same as the number of the inputs.
    The spacing and the origin (where the first input is placed) for the
    N+1'th dimension is specified in this filter. The output image
    informations for the first N dimensions are taken from the first
    input. Note that all the inputs should have the same information.

    Hideaki Hiraki  Contributed in the users
    listhttp://public.kitware.com/pipermail/insight-
    users/2004-February/006542.html

    C++ includes: itkJoinSeriesImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkJoinSeriesImageFilterIUS2IUS3_Pointer":
        """__New_orig__() -> itkJoinSeriesImageFilterIUS2IUS3_Pointer"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUS2IUS3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkJoinSeriesImageFilterIUS2IUS3_Pointer":
        """Clone(itkJoinSeriesImageFilterIUS2IUS3 self) -> itkJoinSeriesImageFilterIUS2IUS3_Pointer"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUS2IUS3_Clone(self)


    def SetSpacing(self, _arg: 'double const') -> "void":
        """
        SetSpacing(itkJoinSeriesImageFilterIUS2IUS3 self, double const _arg)

        Set/Get spacing of the
        new dimension 
        """
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUS2IUS3_SetSpacing(self, _arg)


    def GetSpacing(self) -> "double":
        """GetSpacing(itkJoinSeriesImageFilterIUS2IUS3 self) -> double"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUS2IUS3_GetSpacing(self)


    def SetOrigin(self, _arg: 'double const') -> "void":
        """
        SetOrigin(itkJoinSeriesImageFilterIUS2IUS3 self, double const _arg)

        Set/Get origin of the new
        dimension 
        """
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUS2IUS3_SetOrigin(self, _arg)


    def GetOrigin(self) -> "double":
        """GetOrigin(itkJoinSeriesImageFilterIUS2IUS3 self) -> double"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUS2IUS3_GetOrigin(self)

    InputConvertibleToOutputCheck = _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUS2IUS3_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkJoinSeriesImageFilterPython.delete_itkJoinSeriesImageFilterIUS2IUS3

    def cast(obj: 'itkLightObject') -> "itkJoinSeriesImageFilterIUS2IUS3 *":
        """cast(itkLightObject obj) -> itkJoinSeriesImageFilterIUS2IUS3"""
        return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUS2IUS3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkJoinSeriesImageFilterIUS2IUS3

        Create a new object of the class itkJoinSeriesImageFilterIUS2IUS3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkJoinSeriesImageFilterIUS2IUS3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkJoinSeriesImageFilterIUS2IUS3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkJoinSeriesImageFilterIUS2IUS3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkJoinSeriesImageFilterIUS2IUS3.Clone = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUS2IUS3_Clone, None, itkJoinSeriesImageFilterIUS2IUS3)
itkJoinSeriesImageFilterIUS2IUS3.SetSpacing = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUS2IUS3_SetSpacing, None, itkJoinSeriesImageFilterIUS2IUS3)
itkJoinSeriesImageFilterIUS2IUS3.GetSpacing = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUS2IUS3_GetSpacing, None, itkJoinSeriesImageFilterIUS2IUS3)
itkJoinSeriesImageFilterIUS2IUS3.SetOrigin = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUS2IUS3_SetOrigin, None, itkJoinSeriesImageFilterIUS2IUS3)
itkJoinSeriesImageFilterIUS2IUS3.GetOrigin = new_instancemethod(_itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUS2IUS3_GetOrigin, None, itkJoinSeriesImageFilterIUS2IUS3)
itkJoinSeriesImageFilterIUS2IUS3_swigregister = _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUS2IUS3_swigregister
itkJoinSeriesImageFilterIUS2IUS3_swigregister(itkJoinSeriesImageFilterIUS2IUS3)

def itkJoinSeriesImageFilterIUS2IUS3___New_orig__() -> "itkJoinSeriesImageFilterIUS2IUS3_Pointer":
    """itkJoinSeriesImageFilterIUS2IUS3___New_orig__() -> itkJoinSeriesImageFilterIUS2IUS3_Pointer"""
    return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUS2IUS3___New_orig__()

def itkJoinSeriesImageFilterIUS2IUS3_cast(obj: 'itkLightObject') -> "itkJoinSeriesImageFilterIUS2IUS3 *":
    """itkJoinSeriesImageFilterIUS2IUS3_cast(itkLightObject obj) -> itkJoinSeriesImageFilterIUS2IUS3"""
    return _itkJoinSeriesImageFilterPython.itkJoinSeriesImageFilterIUS2IUS3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def join_series_image_filter(*args, **kwargs):
    """Procedural interface for JoinSeriesImageFilter"""
    import itk
    instance = itk.JoinSeriesImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def join_series_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.JoinSeriesImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.JoinSeriesImageFilter.values()[0]
    else:
        filter_object = itk.JoinSeriesImageFilter

    join_series_image_filter.__doc__ = filter_object.__doc__
    join_series_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    join_series_image_filter.__doc__ += "Available Keyword Arguments:\n"
    join_series_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



