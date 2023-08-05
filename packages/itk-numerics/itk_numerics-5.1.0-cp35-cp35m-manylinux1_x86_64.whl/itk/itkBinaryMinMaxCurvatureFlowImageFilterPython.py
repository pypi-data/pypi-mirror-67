# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkBinaryMinMaxCurvatureFlowImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkBinaryMinMaxCurvatureFlowImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkBinaryMinMaxCurvatureFlowImageFilterPython
            return _itkBinaryMinMaxCurvatureFlowImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkBinaryMinMaxCurvatureFlowImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkBinaryMinMaxCurvatureFlowImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkBinaryMinMaxCurvatureFlowImageFilterPython
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


import itkMinMaxCurvatureFlowImageFilterPython
import ITKCommonBasePython
import pyBasePython
import itkCurvatureFlowImageFilterPython
import itkDenseFiniteDifferenceImageFilterPython
import itkImagePython
import itkImageRegionPython
import itkSizePython
import itkIndexPython
import itkOffsetPython
import itkRGBPixelPython
import itkFixedArrayPython
import stdcomplexPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import vnl_vectorPython
import vnl_matrixPython
import itkPointPython
import vnl_vector_refPython
import itkVectorPython
import vnl_matrix_fixedPython
import itkCovariantVectorPython
import itkRGBAPixelPython
import itkFiniteDifferenceImageFilterPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterBPython
import itkImageSourcePython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageSourceCommonPython
import itkImageToImageFilterCommonPython
import itkImageToImageFilterAPython
import itkFiniteDifferenceFunctionPython

def itkBinaryMinMaxCurvatureFlowImageFilterID3ID3_New():
  return itkBinaryMinMaxCurvatureFlowImageFilterID3ID3.New()


def itkBinaryMinMaxCurvatureFlowImageFilterID2ID2_New():
  return itkBinaryMinMaxCurvatureFlowImageFilterID2ID2.New()


def itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_New():
  return itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3.New()


def itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_New():
  return itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2.New()

class itkBinaryMinMaxCurvatureFlowImageFilterID2ID2(itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2):
    """


    Denoise a binary image using min/max curvature flow.

    BinaryMinMaxCurvatureFlowImageFilter implements a curvature driven
    image denoising algorithm. This filter assumes that the image is
    essentially binary: consisting of two classes. Iso-brightness contours
    in the input image are viewed as a level set. The level set is then
    evolved using a curvature-based speed function:

    \\[ I_t = F_{\\mbox{minmax}} |\\nabla I| \\]

    where $ F_{\\mbox{minmax}} = \\min(\\kappa,0) $ if $
    \\mbox{Avg}_{\\mbox{stencil}}(x) $ is less than or equal to $
    T_{threshold} $ and $ \\max(\\kappa,0) $, otherwise. $ \\kappa $
    is the mean curvature of the iso-brightness contour at point $ x $.

    In min/max curvature flow, movement is turned on or off depending on
    the scale of the noise one wants to remove. Switching depends on the
    average image value of a region of radius $ R $ around each point. The
    choice of $ R $, the stencil radius, governs the scale of the noise to
    be removed.

    The threshold value $ T_{threshold} $ is a user specified value which
    discriminates between the two pixel classes.

    This filter make use of the multi-threaded finite difference solver
    hierarchy. Updates are computed using a
    BinaryMinMaxCurvatureFlowFunction object. A zero flux Neumann boundary
    condition is used when computing derivatives near the data boundary.

    WARNING:  This filter assumes that the input and output types have the
    same dimensions. This filter also requires that the output image
    pixels are of a real type. This filter works for any dimensional
    images.  Reference: "Level Set Methods and Fast Marching Methods",
    J.A. Sethian, Cambridge Press, Chapter 16, Second edition, 1999.

    See:  BinaryMinMaxCurvatureFlowFunction

    See:   CurvatureFlowImageFilter

    See:   MinMaxCurvatureFlowImageFilter

    C++ includes: itkBinaryMinMaxCurvatureFlowImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBinaryMinMaxCurvatureFlowImageFilterID2ID2_Pointer":
        """__New_orig__() -> itkBinaryMinMaxCurvatureFlowImageFilterID2ID2_Pointer"""
        return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterID2ID2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBinaryMinMaxCurvatureFlowImageFilterID2ID2_Pointer":
        """Clone(itkBinaryMinMaxCurvatureFlowImageFilterID2ID2 self) -> itkBinaryMinMaxCurvatureFlowImageFilterID2ID2_Pointer"""
        return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterID2ID2_Clone(self)


    def SetThreshold(self, _arg: 'double const') -> "void":
        """
        SetThreshold(itkBinaryMinMaxCurvatureFlowImageFilterID2ID2 self, double const _arg)

        Set/Get the threshold
        value. 
        """
        return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterID2ID2_SetThreshold(self, _arg)


    def GetThreshold(self) -> "double":
        """GetThreshold(itkBinaryMinMaxCurvatureFlowImageFilterID2ID2 self) -> double"""
        return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterID2ID2_GetThreshold(self)

    InputConvertibleToOutputCheck = _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterID2ID2_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkBinaryMinMaxCurvatureFlowImageFilterPython.delete_itkBinaryMinMaxCurvatureFlowImageFilterID2ID2

    def cast(obj: 'itkLightObject') -> "itkBinaryMinMaxCurvatureFlowImageFilterID2ID2 *":
        """cast(itkLightObject obj) -> itkBinaryMinMaxCurvatureFlowImageFilterID2ID2"""
        return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterID2ID2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkBinaryMinMaxCurvatureFlowImageFilterID2ID2

        Create a new object of the class itkBinaryMinMaxCurvatureFlowImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryMinMaxCurvatureFlowImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryMinMaxCurvatureFlowImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryMinMaxCurvatureFlowImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinaryMinMaxCurvatureFlowImageFilterID2ID2.Clone = new_instancemethod(_itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterID2ID2_Clone, None, itkBinaryMinMaxCurvatureFlowImageFilterID2ID2)
itkBinaryMinMaxCurvatureFlowImageFilterID2ID2.SetThreshold = new_instancemethod(_itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterID2ID2_SetThreshold, None, itkBinaryMinMaxCurvatureFlowImageFilterID2ID2)
itkBinaryMinMaxCurvatureFlowImageFilterID2ID2.GetThreshold = new_instancemethod(_itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterID2ID2_GetThreshold, None, itkBinaryMinMaxCurvatureFlowImageFilterID2ID2)
itkBinaryMinMaxCurvatureFlowImageFilterID2ID2_swigregister = _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterID2ID2_swigregister
itkBinaryMinMaxCurvatureFlowImageFilterID2ID2_swigregister(itkBinaryMinMaxCurvatureFlowImageFilterID2ID2)

def itkBinaryMinMaxCurvatureFlowImageFilterID2ID2___New_orig__() -> "itkBinaryMinMaxCurvatureFlowImageFilterID2ID2_Pointer":
    """itkBinaryMinMaxCurvatureFlowImageFilterID2ID2___New_orig__() -> itkBinaryMinMaxCurvatureFlowImageFilterID2ID2_Pointer"""
    return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterID2ID2___New_orig__()

def itkBinaryMinMaxCurvatureFlowImageFilterID2ID2_cast(obj: 'itkLightObject') -> "itkBinaryMinMaxCurvatureFlowImageFilterID2ID2 *":
    """itkBinaryMinMaxCurvatureFlowImageFilterID2ID2_cast(itkLightObject obj) -> itkBinaryMinMaxCurvatureFlowImageFilterID2ID2"""
    return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterID2ID2_cast(obj)

class itkBinaryMinMaxCurvatureFlowImageFilterID3ID3(itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3):
    """


    Denoise a binary image using min/max curvature flow.

    BinaryMinMaxCurvatureFlowImageFilter implements a curvature driven
    image denoising algorithm. This filter assumes that the image is
    essentially binary: consisting of two classes. Iso-brightness contours
    in the input image are viewed as a level set. The level set is then
    evolved using a curvature-based speed function:

    \\[ I_t = F_{\\mbox{minmax}} |\\nabla I| \\]

    where $ F_{\\mbox{minmax}} = \\min(\\kappa,0) $ if $
    \\mbox{Avg}_{\\mbox{stencil}}(x) $ is less than or equal to $
    T_{threshold} $ and $ \\max(\\kappa,0) $, otherwise. $ \\kappa $
    is the mean curvature of the iso-brightness contour at point $ x $.

    In min/max curvature flow, movement is turned on or off depending on
    the scale of the noise one wants to remove. Switching depends on the
    average image value of a region of radius $ R $ around each point. The
    choice of $ R $, the stencil radius, governs the scale of the noise to
    be removed.

    The threshold value $ T_{threshold} $ is a user specified value which
    discriminates between the two pixel classes.

    This filter make use of the multi-threaded finite difference solver
    hierarchy. Updates are computed using a
    BinaryMinMaxCurvatureFlowFunction object. A zero flux Neumann boundary
    condition is used when computing derivatives near the data boundary.

    WARNING:  This filter assumes that the input and output types have the
    same dimensions. This filter also requires that the output image
    pixels are of a real type. This filter works for any dimensional
    images.  Reference: "Level Set Methods and Fast Marching Methods",
    J.A. Sethian, Cambridge Press, Chapter 16, Second edition, 1999.

    See:  BinaryMinMaxCurvatureFlowFunction

    See:   CurvatureFlowImageFilter

    See:   MinMaxCurvatureFlowImageFilter

    C++ includes: itkBinaryMinMaxCurvatureFlowImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBinaryMinMaxCurvatureFlowImageFilterID3ID3_Pointer":
        """__New_orig__() -> itkBinaryMinMaxCurvatureFlowImageFilterID3ID3_Pointer"""
        return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterID3ID3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBinaryMinMaxCurvatureFlowImageFilterID3ID3_Pointer":
        """Clone(itkBinaryMinMaxCurvatureFlowImageFilterID3ID3 self) -> itkBinaryMinMaxCurvatureFlowImageFilterID3ID3_Pointer"""
        return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterID3ID3_Clone(self)


    def SetThreshold(self, _arg: 'double const') -> "void":
        """
        SetThreshold(itkBinaryMinMaxCurvatureFlowImageFilterID3ID3 self, double const _arg)

        Set/Get the threshold
        value. 
        """
        return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterID3ID3_SetThreshold(self, _arg)


    def GetThreshold(self) -> "double":
        """GetThreshold(itkBinaryMinMaxCurvatureFlowImageFilterID3ID3 self) -> double"""
        return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterID3ID3_GetThreshold(self)

    InputConvertibleToOutputCheck = _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterID3ID3_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkBinaryMinMaxCurvatureFlowImageFilterPython.delete_itkBinaryMinMaxCurvatureFlowImageFilterID3ID3

    def cast(obj: 'itkLightObject') -> "itkBinaryMinMaxCurvatureFlowImageFilterID3ID3 *":
        """cast(itkLightObject obj) -> itkBinaryMinMaxCurvatureFlowImageFilterID3ID3"""
        return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterID3ID3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkBinaryMinMaxCurvatureFlowImageFilterID3ID3

        Create a new object of the class itkBinaryMinMaxCurvatureFlowImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryMinMaxCurvatureFlowImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryMinMaxCurvatureFlowImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryMinMaxCurvatureFlowImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinaryMinMaxCurvatureFlowImageFilterID3ID3.Clone = new_instancemethod(_itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterID3ID3_Clone, None, itkBinaryMinMaxCurvatureFlowImageFilterID3ID3)
itkBinaryMinMaxCurvatureFlowImageFilterID3ID3.SetThreshold = new_instancemethod(_itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterID3ID3_SetThreshold, None, itkBinaryMinMaxCurvatureFlowImageFilterID3ID3)
itkBinaryMinMaxCurvatureFlowImageFilterID3ID3.GetThreshold = new_instancemethod(_itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterID3ID3_GetThreshold, None, itkBinaryMinMaxCurvatureFlowImageFilterID3ID3)
itkBinaryMinMaxCurvatureFlowImageFilterID3ID3_swigregister = _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterID3ID3_swigregister
itkBinaryMinMaxCurvatureFlowImageFilterID3ID3_swigregister(itkBinaryMinMaxCurvatureFlowImageFilterID3ID3)

def itkBinaryMinMaxCurvatureFlowImageFilterID3ID3___New_orig__() -> "itkBinaryMinMaxCurvatureFlowImageFilterID3ID3_Pointer":
    """itkBinaryMinMaxCurvatureFlowImageFilterID3ID3___New_orig__() -> itkBinaryMinMaxCurvatureFlowImageFilterID3ID3_Pointer"""
    return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterID3ID3___New_orig__()

def itkBinaryMinMaxCurvatureFlowImageFilterID3ID3_cast(obj: 'itkLightObject') -> "itkBinaryMinMaxCurvatureFlowImageFilterID3ID3 *":
    """itkBinaryMinMaxCurvatureFlowImageFilterID3ID3_cast(itkLightObject obj) -> itkBinaryMinMaxCurvatureFlowImageFilterID3ID3"""
    return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterID3ID3_cast(obj)

class itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2(itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2):
    """


    Denoise a binary image using min/max curvature flow.

    BinaryMinMaxCurvatureFlowImageFilter implements a curvature driven
    image denoising algorithm. This filter assumes that the image is
    essentially binary: consisting of two classes. Iso-brightness contours
    in the input image are viewed as a level set. The level set is then
    evolved using a curvature-based speed function:

    \\[ I_t = F_{\\mbox{minmax}} |\\nabla I| \\]

    where $ F_{\\mbox{minmax}} = \\min(\\kappa,0) $ if $
    \\mbox{Avg}_{\\mbox{stencil}}(x) $ is less than or equal to $
    T_{threshold} $ and $ \\max(\\kappa,0) $, otherwise. $ \\kappa $
    is the mean curvature of the iso-brightness contour at point $ x $.

    In min/max curvature flow, movement is turned on or off depending on
    the scale of the noise one wants to remove. Switching depends on the
    average image value of a region of radius $ R $ around each point. The
    choice of $ R $, the stencil radius, governs the scale of the noise to
    be removed.

    The threshold value $ T_{threshold} $ is a user specified value which
    discriminates between the two pixel classes.

    This filter make use of the multi-threaded finite difference solver
    hierarchy. Updates are computed using a
    BinaryMinMaxCurvatureFlowFunction object. A zero flux Neumann boundary
    condition is used when computing derivatives near the data boundary.

    WARNING:  This filter assumes that the input and output types have the
    same dimensions. This filter also requires that the output image
    pixels are of a real type. This filter works for any dimensional
    images.  Reference: "Level Set Methods and Fast Marching Methods",
    J.A. Sethian, Cambridge Press, Chapter 16, Second edition, 1999.

    See:  BinaryMinMaxCurvatureFlowFunction

    See:   CurvatureFlowImageFilter

    See:   MinMaxCurvatureFlowImageFilter

    C++ includes: itkBinaryMinMaxCurvatureFlowImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_Pointer"""
        return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_Pointer":
        """Clone(itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2 self) -> itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_Pointer"""
        return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_Clone(self)


    def SetThreshold(self, _arg: 'double const') -> "void":
        """
        SetThreshold(itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2 self, double const _arg)

        Set/Get the threshold
        value. 
        """
        return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_SetThreshold(self, _arg)


    def GetThreshold(self) -> "double":
        """GetThreshold(itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2 self) -> double"""
        return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_GetThreshold(self)

    InputConvertibleToOutputCheck = _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkBinaryMinMaxCurvatureFlowImageFilterPython.delete_itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2"""
        return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2

        Create a new object of the class itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2.Clone = new_instancemethod(_itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_Clone, None, itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2)
itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2.SetThreshold = new_instancemethod(_itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_SetThreshold, None, itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2)
itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2.GetThreshold = new_instancemethod(_itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_GetThreshold, None, itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2)
itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_swigregister = _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_swigregister
itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_swigregister(itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2)

def itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2___New_orig__() -> "itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_Pointer":
    """itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2___New_orig__() -> itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_Pointer"""
    return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2___New_orig__()

def itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2 *":
    """itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_cast(itkLightObject obj) -> itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2"""
    return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF2IF2_cast(obj)

class itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3(itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3):
    """


    Denoise a binary image using min/max curvature flow.

    BinaryMinMaxCurvatureFlowImageFilter implements a curvature driven
    image denoising algorithm. This filter assumes that the image is
    essentially binary: consisting of two classes. Iso-brightness contours
    in the input image are viewed as a level set. The level set is then
    evolved using a curvature-based speed function:

    \\[ I_t = F_{\\mbox{minmax}} |\\nabla I| \\]

    where $ F_{\\mbox{minmax}} = \\min(\\kappa,0) $ if $
    \\mbox{Avg}_{\\mbox{stencil}}(x) $ is less than or equal to $
    T_{threshold} $ and $ \\max(\\kappa,0) $, otherwise. $ \\kappa $
    is the mean curvature of the iso-brightness contour at point $ x $.

    In min/max curvature flow, movement is turned on or off depending on
    the scale of the noise one wants to remove. Switching depends on the
    average image value of a region of radius $ R $ around each point. The
    choice of $ R $, the stencil radius, governs the scale of the noise to
    be removed.

    The threshold value $ T_{threshold} $ is a user specified value which
    discriminates between the two pixel classes.

    This filter make use of the multi-threaded finite difference solver
    hierarchy. Updates are computed using a
    BinaryMinMaxCurvatureFlowFunction object. A zero flux Neumann boundary
    condition is used when computing derivatives near the data boundary.

    WARNING:  This filter assumes that the input and output types have the
    same dimensions. This filter also requires that the output image
    pixels are of a real type. This filter works for any dimensional
    images.  Reference: "Level Set Methods and Fast Marching Methods",
    J.A. Sethian, Cambridge Press, Chapter 16, Second edition, 1999.

    See:  BinaryMinMaxCurvatureFlowFunction

    See:   CurvatureFlowImageFilter

    See:   MinMaxCurvatureFlowImageFilter

    C++ includes: itkBinaryMinMaxCurvatureFlowImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_Pointer"""
        return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_Pointer":
        """Clone(itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3 self) -> itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_Pointer"""
        return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_Clone(self)


    def SetThreshold(self, _arg: 'double const') -> "void":
        """
        SetThreshold(itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3 self, double const _arg)

        Set/Get the threshold
        value. 
        """
        return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_SetThreshold(self, _arg)


    def GetThreshold(self) -> "double":
        """GetThreshold(itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3 self) -> double"""
        return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_GetThreshold(self)

    InputConvertibleToOutputCheck = _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_InputConvertibleToOutputCheck
    __swig_destroy__ = _itkBinaryMinMaxCurvatureFlowImageFilterPython.delete_itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3"""
        return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3

        Create a new object of the class itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3.Clone = new_instancemethod(_itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_Clone, None, itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3)
itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3.SetThreshold = new_instancemethod(_itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_SetThreshold, None, itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3)
itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3.GetThreshold = new_instancemethod(_itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_GetThreshold, None, itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3)
itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_swigregister = _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_swigregister
itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_swigregister(itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3)

def itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3___New_orig__() -> "itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_Pointer":
    """itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3___New_orig__() -> itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_Pointer"""
    return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3___New_orig__()

def itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3 *":
    """itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_cast(itkLightObject obj) -> itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3"""
    return _itkBinaryMinMaxCurvatureFlowImageFilterPython.itkBinaryMinMaxCurvatureFlowImageFilterIF3IF3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def binary_min_max_curvature_flow_image_filter(*args, **kwargs):
    """Procedural interface for BinaryMinMaxCurvatureFlowImageFilter"""
    import itk
    instance = itk.BinaryMinMaxCurvatureFlowImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def binary_min_max_curvature_flow_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.BinaryMinMaxCurvatureFlowImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.BinaryMinMaxCurvatureFlowImageFilter.values()[0]
    else:
        filter_object = itk.BinaryMinMaxCurvatureFlowImageFilter

    binary_min_max_curvature_flow_image_filter.__doc__ = filter_object.__doc__
    binary_min_max_curvature_flow_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    binary_min_max_curvature_flow_image_filter.__doc__ += "Available Keyword Arguments:\n"
    binary_min_max_curvature_flow_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



