# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkMinMaxCurvatureFlowImageFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkMinMaxCurvatureFlowImageFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkMinMaxCurvatureFlowImageFilterPython
            return _itkMinMaxCurvatureFlowImageFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkMinMaxCurvatureFlowImageFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkMinMaxCurvatureFlowImageFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkMinMaxCurvatureFlowImageFilterPython
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
import itkCurvatureFlowImageFilterPython
import itkDenseFiniteDifferenceImageFilterPython
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
import itkFiniteDifferenceImageFilterPython
import itkInPlaceImageFilterAPython
import itkImageToImageFilterBPython
import itkImageSourcePython
import itkImageSourceCommonPython
import itkVectorImagePython
import itkVariableLengthVectorPython
import itkImageToImageFilterCommonPython
import itkImageToImageFilterAPython
import itkFiniteDifferenceFunctionPython

def itkMinMaxCurvatureFlowImageFilterID3ID3_New():
  return itkMinMaxCurvatureFlowImageFilterID3ID3.New()


def itkMinMaxCurvatureFlowImageFilterID2ID2_New():
  return itkMinMaxCurvatureFlowImageFilterID2ID2.New()


def itkMinMaxCurvatureFlowImageFilterIF3IF3_New():
  return itkMinMaxCurvatureFlowImageFilterIF3IF3.New()


def itkMinMaxCurvatureFlowImageFilterIF2IF2_New():
  return itkMinMaxCurvatureFlowImageFilterIF2IF2.New()

class itkMinMaxCurvatureFlowImageFilterID2ID2(itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID2ID2):
    """


    Denoise an image using min/max curvature flow.

    MinMaxCurvatureFlowImageFilter implements a curvature driven image
    denoising algorithm. Iso- brightness contours in the grayscale input
    image are viewed as a level set. The level set is then evolved using a
    curvature-based speed function:

    \\[ I_t = F_{\\mbox{minmax}} |\\nabla I| \\]

    where $ F_{\\mbox{minmax}} = \\max(\\kappa,0) $ if $
    \\mbox{Avg}_{\\mbox{stencil}}(x) $ is less than or equal to $
    T_{threshold} $ and $ \\min(\\kappa,0) $, otherwise. $ \\kappa $
    is the mean curvature of the iso-brightness contour at point $ x $.

    In min/max curvature flow, movement is turned on or off depending on
    the scale of the noise one wants to remove. Switching depends on the
    average image value of a region of radius $ R $ around each point. The
    choice of $ R $, the stencil radius, governs the scale of the noise to
    be removed.

    The threshold value $ T_{threshold} $ is the average intensity
    obtained in the direction perpendicular to the gradient at point $ x $
    at the extrema of the local neighborhood.

    This filter make use of the multi-threaded finite difference solver
    hierarchy. Updates are computed using a MinMaxCurvatureFlowFunction
    object. A zero flux Neumann boundary condition is used when computing
    derivatives near the data boundary.

    WARNING:  This filter assumes that the input and output types have the
    same dimensions. This filter also requires that the output image
    pixels are of a real type. This filter works for any dimensional
    images, however for dimensions greater than 3D, an expensive brute-
    force search is used to compute the local threshold.  Reference:
    "Level Set Methods and Fast Marching Methods", J.A. Sethian,
    Cambridge Press, Chapter 16, Second edition, 1999.

    See:  MinMaxCurvatureFlowFunction

    See:   CurvatureFlowImageFilter

    See:   BinaryMinMaxCurvatureFlowImageFilter  \\sphinx
    \\sphinxexample{Filtering/CurvatureFlow/SmoothImageUsing
    MinMaxCurvatureFlow,Smooth Image Using Min Max Curvature Flow} \\sph
    inxexample{Filtering/CurvatureFlow/SmoothRGBImageUsingMinMaxCurvatureF
    low,SmoothRGBImageUsingMinMaxCurvatureFlow} \\endsphinx

    C++ includes: itkMinMaxCurvatureFlowImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMinMaxCurvatureFlowImageFilterID2ID2_Pointer":
        """__New_orig__() -> itkMinMaxCurvatureFlowImageFilterID2ID2_Pointer"""
        return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMinMaxCurvatureFlowImageFilterID2ID2_Pointer":
        """Clone(itkMinMaxCurvatureFlowImageFilterID2ID2 self) -> itkMinMaxCurvatureFlowImageFilterID2ID2_Pointer"""
        return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2_Clone(self)


    def SetStencilRadius(self, _arg: 'unsigned long const') -> "void":
        """
        SetStencilRadius(itkMinMaxCurvatureFlowImageFilterID2ID2 self, unsigned long const _arg)

        Set/Get the
        stencil radius. 
        """
        return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2_SetStencilRadius(self, _arg)


    def GetStencilRadius(self) -> "unsigned long":
        """GetStencilRadius(itkMinMaxCurvatureFlowImageFilterID2ID2 self) -> unsigned long"""
        return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2_GetStencilRadius(self)

    UnsignedLongConvertibleToOutputCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2_UnsignedLongConvertibleToOutputCheck
    OutputLessThanComparableCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2_OutputLessThanComparableCheck
    LongConvertibleToOutputCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2_LongConvertibleToOutputCheck
    OutputDoubleComparableCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2_OutputDoubleComparableCheck
    OutputDoubleMultiplyAndAssignOperatorCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2_OutputDoubleMultiplyAndAssignOperatorCheck
    OutputGreaterThanUnsignedLongCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2_OutputGreaterThanUnsignedLongCheck
    UnsignedLongOutputAditiveOperatorsCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2_UnsignedLongOutputAditiveOperatorsCheck
    __swig_destroy__ = _itkMinMaxCurvatureFlowImageFilterPython.delete_itkMinMaxCurvatureFlowImageFilterID2ID2

    def cast(obj: 'itkLightObject') -> "itkMinMaxCurvatureFlowImageFilterID2ID2 *":
        """cast(itkLightObject obj) -> itkMinMaxCurvatureFlowImageFilterID2ID2"""
        return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkMinMaxCurvatureFlowImageFilterID2ID2

        Create a new object of the class itkMinMaxCurvatureFlowImageFilterID2ID2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMinMaxCurvatureFlowImageFilterID2ID2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMinMaxCurvatureFlowImageFilterID2ID2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMinMaxCurvatureFlowImageFilterID2ID2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMinMaxCurvatureFlowImageFilterID2ID2.Clone = new_instancemethod(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2_Clone, None, itkMinMaxCurvatureFlowImageFilterID2ID2)
itkMinMaxCurvatureFlowImageFilterID2ID2.SetStencilRadius = new_instancemethod(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2_SetStencilRadius, None, itkMinMaxCurvatureFlowImageFilterID2ID2)
itkMinMaxCurvatureFlowImageFilterID2ID2.GetStencilRadius = new_instancemethod(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2_GetStencilRadius, None, itkMinMaxCurvatureFlowImageFilterID2ID2)
itkMinMaxCurvatureFlowImageFilterID2ID2_swigregister = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2_swigregister
itkMinMaxCurvatureFlowImageFilterID2ID2_swigregister(itkMinMaxCurvatureFlowImageFilterID2ID2)

def itkMinMaxCurvatureFlowImageFilterID2ID2___New_orig__() -> "itkMinMaxCurvatureFlowImageFilterID2ID2_Pointer":
    """itkMinMaxCurvatureFlowImageFilterID2ID2___New_orig__() -> itkMinMaxCurvatureFlowImageFilterID2ID2_Pointer"""
    return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2___New_orig__()

def itkMinMaxCurvatureFlowImageFilterID2ID2_cast(obj: 'itkLightObject') -> "itkMinMaxCurvatureFlowImageFilterID2ID2 *":
    """itkMinMaxCurvatureFlowImageFilterID2ID2_cast(itkLightObject obj) -> itkMinMaxCurvatureFlowImageFilterID2ID2"""
    return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID2ID2_cast(obj)

class itkMinMaxCurvatureFlowImageFilterID3ID3(itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterID3ID3):
    """


    Denoise an image using min/max curvature flow.

    MinMaxCurvatureFlowImageFilter implements a curvature driven image
    denoising algorithm. Iso- brightness contours in the grayscale input
    image are viewed as a level set. The level set is then evolved using a
    curvature-based speed function:

    \\[ I_t = F_{\\mbox{minmax}} |\\nabla I| \\]

    where $ F_{\\mbox{minmax}} = \\max(\\kappa,0) $ if $
    \\mbox{Avg}_{\\mbox{stencil}}(x) $ is less than or equal to $
    T_{threshold} $ and $ \\min(\\kappa,0) $, otherwise. $ \\kappa $
    is the mean curvature of the iso-brightness contour at point $ x $.

    In min/max curvature flow, movement is turned on or off depending on
    the scale of the noise one wants to remove. Switching depends on the
    average image value of a region of radius $ R $ around each point. The
    choice of $ R $, the stencil radius, governs the scale of the noise to
    be removed.

    The threshold value $ T_{threshold} $ is the average intensity
    obtained in the direction perpendicular to the gradient at point $ x $
    at the extrema of the local neighborhood.

    This filter make use of the multi-threaded finite difference solver
    hierarchy. Updates are computed using a MinMaxCurvatureFlowFunction
    object. A zero flux Neumann boundary condition is used when computing
    derivatives near the data boundary.

    WARNING:  This filter assumes that the input and output types have the
    same dimensions. This filter also requires that the output image
    pixels are of a real type. This filter works for any dimensional
    images, however for dimensions greater than 3D, an expensive brute-
    force search is used to compute the local threshold.  Reference:
    "Level Set Methods and Fast Marching Methods", J.A. Sethian,
    Cambridge Press, Chapter 16, Second edition, 1999.

    See:  MinMaxCurvatureFlowFunction

    See:   CurvatureFlowImageFilter

    See:   BinaryMinMaxCurvatureFlowImageFilter  \\sphinx
    \\sphinxexample{Filtering/CurvatureFlow/SmoothImageUsing
    MinMaxCurvatureFlow,Smooth Image Using Min Max Curvature Flow} \\sph
    inxexample{Filtering/CurvatureFlow/SmoothRGBImageUsingMinMaxCurvatureF
    low,SmoothRGBImageUsingMinMaxCurvatureFlow} \\endsphinx

    C++ includes: itkMinMaxCurvatureFlowImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMinMaxCurvatureFlowImageFilterID3ID3_Pointer":
        """__New_orig__() -> itkMinMaxCurvatureFlowImageFilterID3ID3_Pointer"""
        return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMinMaxCurvatureFlowImageFilterID3ID3_Pointer":
        """Clone(itkMinMaxCurvatureFlowImageFilterID3ID3 self) -> itkMinMaxCurvatureFlowImageFilterID3ID3_Pointer"""
        return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3_Clone(self)


    def SetStencilRadius(self, _arg: 'unsigned long const') -> "void":
        """
        SetStencilRadius(itkMinMaxCurvatureFlowImageFilterID3ID3 self, unsigned long const _arg)

        Set/Get the
        stencil radius. 
        """
        return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3_SetStencilRadius(self, _arg)


    def GetStencilRadius(self) -> "unsigned long":
        """GetStencilRadius(itkMinMaxCurvatureFlowImageFilterID3ID3 self) -> unsigned long"""
        return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3_GetStencilRadius(self)

    UnsignedLongConvertibleToOutputCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3_UnsignedLongConvertibleToOutputCheck
    OutputLessThanComparableCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3_OutputLessThanComparableCheck
    LongConvertibleToOutputCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3_LongConvertibleToOutputCheck
    OutputDoubleComparableCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3_OutputDoubleComparableCheck
    OutputDoubleMultiplyAndAssignOperatorCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3_OutputDoubleMultiplyAndAssignOperatorCheck
    OutputGreaterThanUnsignedLongCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3_OutputGreaterThanUnsignedLongCheck
    UnsignedLongOutputAditiveOperatorsCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3_UnsignedLongOutputAditiveOperatorsCheck
    __swig_destroy__ = _itkMinMaxCurvatureFlowImageFilterPython.delete_itkMinMaxCurvatureFlowImageFilterID3ID3

    def cast(obj: 'itkLightObject') -> "itkMinMaxCurvatureFlowImageFilterID3ID3 *":
        """cast(itkLightObject obj) -> itkMinMaxCurvatureFlowImageFilterID3ID3"""
        return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkMinMaxCurvatureFlowImageFilterID3ID3

        Create a new object of the class itkMinMaxCurvatureFlowImageFilterID3ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMinMaxCurvatureFlowImageFilterID3ID3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMinMaxCurvatureFlowImageFilterID3ID3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMinMaxCurvatureFlowImageFilterID3ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMinMaxCurvatureFlowImageFilterID3ID3.Clone = new_instancemethod(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3_Clone, None, itkMinMaxCurvatureFlowImageFilterID3ID3)
itkMinMaxCurvatureFlowImageFilterID3ID3.SetStencilRadius = new_instancemethod(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3_SetStencilRadius, None, itkMinMaxCurvatureFlowImageFilterID3ID3)
itkMinMaxCurvatureFlowImageFilterID3ID3.GetStencilRadius = new_instancemethod(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3_GetStencilRadius, None, itkMinMaxCurvatureFlowImageFilterID3ID3)
itkMinMaxCurvatureFlowImageFilterID3ID3_swigregister = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3_swigregister
itkMinMaxCurvatureFlowImageFilterID3ID3_swigregister(itkMinMaxCurvatureFlowImageFilterID3ID3)

def itkMinMaxCurvatureFlowImageFilterID3ID3___New_orig__() -> "itkMinMaxCurvatureFlowImageFilterID3ID3_Pointer":
    """itkMinMaxCurvatureFlowImageFilterID3ID3___New_orig__() -> itkMinMaxCurvatureFlowImageFilterID3ID3_Pointer"""
    return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3___New_orig__()

def itkMinMaxCurvatureFlowImageFilterID3ID3_cast(obj: 'itkLightObject') -> "itkMinMaxCurvatureFlowImageFilterID3ID3 *":
    """itkMinMaxCurvatureFlowImageFilterID3ID3_cast(itkLightObject obj) -> itkMinMaxCurvatureFlowImageFilterID3ID3"""
    return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterID3ID3_cast(obj)

class itkMinMaxCurvatureFlowImageFilterIF2IF2(itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF2IF2):
    """


    Denoise an image using min/max curvature flow.

    MinMaxCurvatureFlowImageFilter implements a curvature driven image
    denoising algorithm. Iso- brightness contours in the grayscale input
    image are viewed as a level set. The level set is then evolved using a
    curvature-based speed function:

    \\[ I_t = F_{\\mbox{minmax}} |\\nabla I| \\]

    where $ F_{\\mbox{minmax}} = \\max(\\kappa,0) $ if $
    \\mbox{Avg}_{\\mbox{stencil}}(x) $ is less than or equal to $
    T_{threshold} $ and $ \\min(\\kappa,0) $, otherwise. $ \\kappa $
    is the mean curvature of the iso-brightness contour at point $ x $.

    In min/max curvature flow, movement is turned on or off depending on
    the scale of the noise one wants to remove. Switching depends on the
    average image value of a region of radius $ R $ around each point. The
    choice of $ R $, the stencil radius, governs the scale of the noise to
    be removed.

    The threshold value $ T_{threshold} $ is the average intensity
    obtained in the direction perpendicular to the gradient at point $ x $
    at the extrema of the local neighborhood.

    This filter make use of the multi-threaded finite difference solver
    hierarchy. Updates are computed using a MinMaxCurvatureFlowFunction
    object. A zero flux Neumann boundary condition is used when computing
    derivatives near the data boundary.

    WARNING:  This filter assumes that the input and output types have the
    same dimensions. This filter also requires that the output image
    pixels are of a real type. This filter works for any dimensional
    images, however for dimensions greater than 3D, an expensive brute-
    force search is used to compute the local threshold.  Reference:
    "Level Set Methods and Fast Marching Methods", J.A. Sethian,
    Cambridge Press, Chapter 16, Second edition, 1999.

    See:  MinMaxCurvatureFlowFunction

    See:   CurvatureFlowImageFilter

    See:   BinaryMinMaxCurvatureFlowImageFilter  \\sphinx
    \\sphinxexample{Filtering/CurvatureFlow/SmoothImageUsing
    MinMaxCurvatureFlow,Smooth Image Using Min Max Curvature Flow} \\sph
    inxexample{Filtering/CurvatureFlow/SmoothRGBImageUsingMinMaxCurvatureF
    low,SmoothRGBImageUsingMinMaxCurvatureFlow} \\endsphinx

    C++ includes: itkMinMaxCurvatureFlowImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMinMaxCurvatureFlowImageFilterIF2IF2_Pointer":
        """__New_orig__() -> itkMinMaxCurvatureFlowImageFilterIF2IF2_Pointer"""
        return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMinMaxCurvatureFlowImageFilterIF2IF2_Pointer":
        """Clone(itkMinMaxCurvatureFlowImageFilterIF2IF2 self) -> itkMinMaxCurvatureFlowImageFilterIF2IF2_Pointer"""
        return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_Clone(self)


    def SetStencilRadius(self, _arg: 'unsigned long const') -> "void":
        """
        SetStencilRadius(itkMinMaxCurvatureFlowImageFilterIF2IF2 self, unsigned long const _arg)

        Set/Get the
        stencil radius. 
        """
        return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_SetStencilRadius(self, _arg)


    def GetStencilRadius(self) -> "unsigned long":
        """GetStencilRadius(itkMinMaxCurvatureFlowImageFilterIF2IF2 self) -> unsigned long"""
        return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_GetStencilRadius(self)

    UnsignedLongConvertibleToOutputCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_UnsignedLongConvertibleToOutputCheck
    OutputLessThanComparableCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_OutputLessThanComparableCheck
    LongConvertibleToOutputCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_LongConvertibleToOutputCheck
    OutputDoubleComparableCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_OutputDoubleComparableCheck
    OutputDoubleMultiplyAndAssignOperatorCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_OutputDoubleMultiplyAndAssignOperatorCheck
    OutputGreaterThanUnsignedLongCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_OutputGreaterThanUnsignedLongCheck
    UnsignedLongOutputAditiveOperatorsCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_UnsignedLongOutputAditiveOperatorsCheck
    __swig_destroy__ = _itkMinMaxCurvatureFlowImageFilterPython.delete_itkMinMaxCurvatureFlowImageFilterIF2IF2

    def cast(obj: 'itkLightObject') -> "itkMinMaxCurvatureFlowImageFilterIF2IF2 *":
        """cast(itkLightObject obj) -> itkMinMaxCurvatureFlowImageFilterIF2IF2"""
        return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkMinMaxCurvatureFlowImageFilterIF2IF2

        Create a new object of the class itkMinMaxCurvatureFlowImageFilterIF2IF2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMinMaxCurvatureFlowImageFilterIF2IF2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMinMaxCurvatureFlowImageFilterIF2IF2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMinMaxCurvatureFlowImageFilterIF2IF2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMinMaxCurvatureFlowImageFilterIF2IF2.Clone = new_instancemethod(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_Clone, None, itkMinMaxCurvatureFlowImageFilterIF2IF2)
itkMinMaxCurvatureFlowImageFilterIF2IF2.SetStencilRadius = new_instancemethod(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_SetStencilRadius, None, itkMinMaxCurvatureFlowImageFilterIF2IF2)
itkMinMaxCurvatureFlowImageFilterIF2IF2.GetStencilRadius = new_instancemethod(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_GetStencilRadius, None, itkMinMaxCurvatureFlowImageFilterIF2IF2)
itkMinMaxCurvatureFlowImageFilterIF2IF2_swigregister = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_swigregister
itkMinMaxCurvatureFlowImageFilterIF2IF2_swigregister(itkMinMaxCurvatureFlowImageFilterIF2IF2)

def itkMinMaxCurvatureFlowImageFilterIF2IF2___New_orig__() -> "itkMinMaxCurvatureFlowImageFilterIF2IF2_Pointer":
    """itkMinMaxCurvatureFlowImageFilterIF2IF2___New_orig__() -> itkMinMaxCurvatureFlowImageFilterIF2IF2_Pointer"""
    return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2___New_orig__()

def itkMinMaxCurvatureFlowImageFilterIF2IF2_cast(obj: 'itkLightObject') -> "itkMinMaxCurvatureFlowImageFilterIF2IF2 *":
    """itkMinMaxCurvatureFlowImageFilterIF2IF2_cast(itkLightObject obj) -> itkMinMaxCurvatureFlowImageFilterIF2IF2"""
    return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF2IF2_cast(obj)

class itkMinMaxCurvatureFlowImageFilterIF3IF3(itkCurvatureFlowImageFilterPython.itkCurvatureFlowImageFilterIF3IF3):
    """


    Denoise an image using min/max curvature flow.

    MinMaxCurvatureFlowImageFilter implements a curvature driven image
    denoising algorithm. Iso- brightness contours in the grayscale input
    image are viewed as a level set. The level set is then evolved using a
    curvature-based speed function:

    \\[ I_t = F_{\\mbox{minmax}} |\\nabla I| \\]

    where $ F_{\\mbox{minmax}} = \\max(\\kappa,0) $ if $
    \\mbox{Avg}_{\\mbox{stencil}}(x) $ is less than or equal to $
    T_{threshold} $ and $ \\min(\\kappa,0) $, otherwise. $ \\kappa $
    is the mean curvature of the iso-brightness contour at point $ x $.

    In min/max curvature flow, movement is turned on or off depending on
    the scale of the noise one wants to remove. Switching depends on the
    average image value of a region of radius $ R $ around each point. The
    choice of $ R $, the stencil radius, governs the scale of the noise to
    be removed.

    The threshold value $ T_{threshold} $ is the average intensity
    obtained in the direction perpendicular to the gradient at point $ x $
    at the extrema of the local neighborhood.

    This filter make use of the multi-threaded finite difference solver
    hierarchy. Updates are computed using a MinMaxCurvatureFlowFunction
    object. A zero flux Neumann boundary condition is used when computing
    derivatives near the data boundary.

    WARNING:  This filter assumes that the input and output types have the
    same dimensions. This filter also requires that the output image
    pixels are of a real type. This filter works for any dimensional
    images, however for dimensions greater than 3D, an expensive brute-
    force search is used to compute the local threshold.  Reference:
    "Level Set Methods and Fast Marching Methods", J.A. Sethian,
    Cambridge Press, Chapter 16, Second edition, 1999.

    See:  MinMaxCurvatureFlowFunction

    See:   CurvatureFlowImageFilter

    See:   BinaryMinMaxCurvatureFlowImageFilter  \\sphinx
    \\sphinxexample{Filtering/CurvatureFlow/SmoothImageUsing
    MinMaxCurvatureFlow,Smooth Image Using Min Max Curvature Flow} \\sph
    inxexample{Filtering/CurvatureFlow/SmoothRGBImageUsingMinMaxCurvatureF
    low,SmoothRGBImageUsingMinMaxCurvatureFlow} \\endsphinx

    C++ includes: itkMinMaxCurvatureFlowImageFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkMinMaxCurvatureFlowImageFilterIF3IF3_Pointer":
        """__New_orig__() -> itkMinMaxCurvatureFlowImageFilterIF3IF3_Pointer"""
        return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkMinMaxCurvatureFlowImageFilterIF3IF3_Pointer":
        """Clone(itkMinMaxCurvatureFlowImageFilterIF3IF3 self) -> itkMinMaxCurvatureFlowImageFilterIF3IF3_Pointer"""
        return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_Clone(self)


    def SetStencilRadius(self, _arg: 'unsigned long const') -> "void":
        """
        SetStencilRadius(itkMinMaxCurvatureFlowImageFilterIF3IF3 self, unsigned long const _arg)

        Set/Get the
        stencil radius. 
        """
        return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_SetStencilRadius(self, _arg)


    def GetStencilRadius(self) -> "unsigned long":
        """GetStencilRadius(itkMinMaxCurvatureFlowImageFilterIF3IF3 self) -> unsigned long"""
        return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_GetStencilRadius(self)

    UnsignedLongConvertibleToOutputCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_UnsignedLongConvertibleToOutputCheck
    OutputLessThanComparableCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_OutputLessThanComparableCheck
    LongConvertibleToOutputCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_LongConvertibleToOutputCheck
    OutputDoubleComparableCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_OutputDoubleComparableCheck
    OutputDoubleMultiplyAndAssignOperatorCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_OutputDoubleMultiplyAndAssignOperatorCheck
    OutputGreaterThanUnsignedLongCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_OutputGreaterThanUnsignedLongCheck
    UnsignedLongOutputAditiveOperatorsCheck = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_UnsignedLongOutputAditiveOperatorsCheck
    __swig_destroy__ = _itkMinMaxCurvatureFlowImageFilterPython.delete_itkMinMaxCurvatureFlowImageFilterIF3IF3

    def cast(obj: 'itkLightObject') -> "itkMinMaxCurvatureFlowImageFilterIF3IF3 *":
        """cast(itkLightObject obj) -> itkMinMaxCurvatureFlowImageFilterIF3IF3"""
        return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkMinMaxCurvatureFlowImageFilterIF3IF3

        Create a new object of the class itkMinMaxCurvatureFlowImageFilterIF3IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkMinMaxCurvatureFlowImageFilterIF3IF3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkMinMaxCurvatureFlowImageFilterIF3IF3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkMinMaxCurvatureFlowImageFilterIF3IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkMinMaxCurvatureFlowImageFilterIF3IF3.Clone = new_instancemethod(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_Clone, None, itkMinMaxCurvatureFlowImageFilterIF3IF3)
itkMinMaxCurvatureFlowImageFilterIF3IF3.SetStencilRadius = new_instancemethod(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_SetStencilRadius, None, itkMinMaxCurvatureFlowImageFilterIF3IF3)
itkMinMaxCurvatureFlowImageFilterIF3IF3.GetStencilRadius = new_instancemethod(_itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_GetStencilRadius, None, itkMinMaxCurvatureFlowImageFilterIF3IF3)
itkMinMaxCurvatureFlowImageFilterIF3IF3_swigregister = _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_swigregister
itkMinMaxCurvatureFlowImageFilterIF3IF3_swigregister(itkMinMaxCurvatureFlowImageFilterIF3IF3)

def itkMinMaxCurvatureFlowImageFilterIF3IF3___New_orig__() -> "itkMinMaxCurvatureFlowImageFilterIF3IF3_Pointer":
    """itkMinMaxCurvatureFlowImageFilterIF3IF3___New_orig__() -> itkMinMaxCurvatureFlowImageFilterIF3IF3_Pointer"""
    return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3___New_orig__()

def itkMinMaxCurvatureFlowImageFilterIF3IF3_cast(obj: 'itkLightObject') -> "itkMinMaxCurvatureFlowImageFilterIF3IF3 *":
    """itkMinMaxCurvatureFlowImageFilterIF3IF3_cast(itkLightObject obj) -> itkMinMaxCurvatureFlowImageFilterIF3IF3"""
    return _itkMinMaxCurvatureFlowImageFilterPython.itkMinMaxCurvatureFlowImageFilterIF3IF3_cast(obj)


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def min_max_curvature_flow_image_filter(*args, **kwargs):
    """Procedural interface for MinMaxCurvatureFlowImageFilter"""
    import itk
    instance = itk.MinMaxCurvatureFlowImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def min_max_curvature_flow_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.MinMaxCurvatureFlowImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.MinMaxCurvatureFlowImageFilter.values()[0]
    else:
        filter_object = itk.MinMaxCurvatureFlowImageFilter

    min_max_curvature_flow_image_filter.__doc__ = filter_object.__doc__
    min_max_curvature_flow_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    min_max_curvature_flow_image_filter.__doc__ += "Available Keyword Arguments:\n"
    min_max_curvature_flow_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])



