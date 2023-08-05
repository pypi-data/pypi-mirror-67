# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkCastSpatialObjectFilterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkCastSpatialObjectFilterPython', [dirname(__file__)])
        except ImportError:
            import _itkCastSpatialObjectFilterPython
            return _itkCastSpatialObjectFilterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkCastSpatialObjectFilterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkCastSpatialObjectFilterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkCastSpatialObjectFilterPython
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


import itkBoxSpatialObjectPython
import itkSpatialObjectBasePython
import itkCovariantVectorPython
import vnl_vector_refPython
import stdcomplexPython
import pyBasePython
import vnl_vectorPython
import vnl_matrixPython
import itkFixedArrayPython
import itkVectorPython
import itkAffineTransformPython
import itkMatrixPython
import itkPointPython
import vnl_matrix_fixedPython
import ITKCommonBasePython
import itkMatrixOffsetTransformBasePython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkVariableLengthVectorPython
import itkOptimizerParametersPython
import itkArrayPython
import itkTransformBasePython
import itkArray2DPython
import itkBoundingBoxPython
import itkMapContainerPython
import itkVectorContainerPython
import itkOffsetPython
import itkSizePython
import itkContinuousIndexPython
import itkIndexPython
import itkImageRegionPython
import itkSpatialObjectPropertyPython
import itkRGBAPixelPython
import itkLineSpatialObjectPython
import itkLineSpatialObjectPointPython
import itkSpatialObjectPointPython
import itkLandmarkSpatialObjectPython
import itkPointBasedSpatialObjectPython
import itkArrowSpatialObjectPython
import itkBlobSpatialObjectPython
import itkImageMaskSpatialObjectPython
import itkImageSpatialObjectPython
import itkImagePython
import itkRGBPixelPython
import itkInterpolateImageFunctionPython
import itkImageFunctionBasePython
import itkFunctionBasePython
import itkGroupSpatialObjectPython
import itkContourSpatialObjectPython
import itkContourSpatialObjectPointPython
import itkTubeSpatialObjectPython
import itkTubeSpatialObjectPointPython
import itkEllipseSpatialObjectPython
import itkGaussianSpatialObjectPython
import itkSurfaceSpatialObjectPython
import itkSurfaceSpatialObjectPointPython
import itkPolygonSpatialObjectPython

def itkCastSpatialObjectFilter3_New():
  return itkCastSpatialObjectFilter3.New()


def itkCastSpatialObjectFilter2_New():
  return itkCastSpatialObjectFilter2.New()

class itkCastSpatialObjectFilter2(ITKCommonBasePython.itkObject):
    """


    This filter casts one spatialobject to another, when the class
    hierarchy supports it (e.g., Tube to PointBased). Particularly useful
    in Python where casting objects without public contructors (e.g.,
    objects managed by smartpointers) is problematic.

    C++ includes: itkCastSpatialObjectFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkCastSpatialObjectFilter2_Pointer":
        """__New_orig__() -> itkCastSpatialObjectFilter2_Pointer"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkCastSpatialObjectFilter2_Pointer":
        """Clone(itkCastSpatialObjectFilter2 self) -> itkCastSpatialObjectFilter2_Pointer"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_Clone(self)


    def SetInput(self, _arg: 'itkSpatialObject2') -> "void":
        """SetInput(itkCastSpatialObjectFilter2 self, itkSpatialObject2 _arg)"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_SetInput(self, _arg)


    def GetInput(self) -> "itkSpatialObject2 const *":
        """GetInput(itkCastSpatialObjectFilter2 self) -> itkSpatialObject2"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetInput(self)


    def GetArrows(self) -> "std::list< itkArrowSpatialObject2_Pointer,std::allocator< itkArrowSpatialObject2_Pointer > > *":
        """GetArrows(itkCastSpatialObjectFilter2 self) -> std::list< itkArrowSpatialObject2_Pointer,std::allocator< itkArrowSpatialObject2_Pointer > > *"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetArrows(self)


    def GetBlobs(self) -> "std::list< itkBlobSpatialObject2_Pointer,std::allocator< itkBlobSpatialObject2_Pointer > > *":
        """GetBlobs(itkCastSpatialObjectFilter2 self) -> std::list< itkBlobSpatialObject2_Pointer,std::allocator< itkBlobSpatialObject2_Pointer > > *"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetBlobs(self)


    def GetBoxes(self) -> "std::list< itkBoxSpatialObject2_Pointer,std::allocator< itkBoxSpatialObject2_Pointer > > *":
        """GetBoxes(itkCastSpatialObjectFilter2 self) -> listitkBoxSpatialObject2_Pointer"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetBoxes(self)


    def GetContours(self) -> "std::list< itkContourSpatialObject2_Pointer,std::allocator< itkContourSpatialObject2_Pointer > > *":
        """GetContours(itkCastSpatialObjectFilter2 self) -> listitkContourSpatialObject2_Pointer"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetContours(self)


    def GetEllipses(self) -> "std::list< itkEllipseSpatialObject2_Pointer,std::allocator< itkEllipseSpatialObject2_Pointer > > *":
        """GetEllipses(itkCastSpatialObjectFilter2 self) -> listitkEllipseSpatialObject2_Pointer"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetEllipses(self)


    def GetGaussians(self) -> "std::list< itkGaussianSpatialObject2_Pointer,std::allocator< itkGaussianSpatialObject2_Pointer > > *":
        """GetGaussians(itkCastSpatialObjectFilter2 self) -> listitkGaussianSpatialObject2_Pointer"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetGaussians(self)


    def GetGroups(self) -> "std::list< itkGroupSpatialObject2_Pointer,std::allocator< itkGroupSpatialObject2_Pointer > > *":
        """GetGroups(itkCastSpatialObjectFilter2 self) -> listitkGroupSpatialObject2_Pointer"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetGroups(self)


    def GetImageMasks(self) -> "std::list< itkImageMaskSpatialObject2_Pointer,std::allocator< itkImageMaskSpatialObject2_Pointer > > *":
        """GetImageMasks(itkCastSpatialObjectFilter2 self) -> listitkImageMaskSpatialObject2_Pointer"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetImageMasks(self)


    def GetImages(self) -> "std::list< itkImageSpatialObject2UC_Pointer,std::allocator< itkImageSpatialObject2UC_Pointer > > *":
        """GetImages(itkCastSpatialObjectFilter2 self) -> listitkImageSpatialObject2UC_Pointer"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetImages(self)


    def GetLandmarks(self) -> "std::list< itkLandmarkSpatialObject2_Pointer,std::allocator< itkLandmarkSpatialObject2_Pointer > > *":
        """GetLandmarks(itkCastSpatialObjectFilter2 self) -> listitkLandmarkSpatialObject2_Pointer"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetLandmarks(self)


    def GetLines(self) -> "std::list< itkLineSpatialObject2_Pointer,std::allocator< itkLineSpatialObject2_Pointer > > *":
        """GetLines(itkCastSpatialObjectFilter2 self) -> listitkLineSpatialObject2_Pointer"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetLines(self)


    def GetPointBased(self) -> "std::list< itkPointBasedSpatialObject2_Pointer,std::allocator< itkPointBasedSpatialObject2_Pointer > > *":
        """GetPointBased(itkCastSpatialObjectFilter2 self) -> listitkPointBasedSpatialObject2_Pointer"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetPointBased(self)


    def GetPolygons(self) -> "std::list< itkPolygonSpatialObject2_Pointer,std::allocator< itkPolygonSpatialObject2_Pointer > > *":
        """GetPolygons(itkCastSpatialObjectFilter2 self) -> listitkPolygonSpatialObject2_Pointer"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetPolygons(self)


    def GetSpatialObjects(self) -> "std::list< itkSpatialObject2_Pointer,std::allocator< itkSpatialObject2_Pointer > > *":
        """GetSpatialObjects(itkCastSpatialObjectFilter2 self) -> listitkSpatialObject2_Pointer"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetSpatialObjects(self)


    def GetSurfaces(self) -> "std::list< itkSurfaceSpatialObject2_Pointer,std::allocator< itkSurfaceSpatialObject2_Pointer > > *":
        """GetSurfaces(itkCastSpatialObjectFilter2 self) -> listitkSurfaceSpatialObject2_Pointer"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetSurfaces(self)


    def GetTubes(self) -> "std::list< itkTubeSpatialObject2_Pointer,std::allocator< itkTubeSpatialObject2_Pointer > > *":
        """GetTubes(itkCastSpatialObjectFilter2 self) -> listitkTubeSpatialObject2_Pointer"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetTubes(self)

    __swig_destroy__ = _itkCastSpatialObjectFilterPython.delete_itkCastSpatialObjectFilter2

    def cast(obj: 'itkLightObject') -> "itkCastSpatialObjectFilter2 *":
        """cast(itkLightObject obj) -> itkCastSpatialObjectFilter2"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkCastSpatialObjectFilter2

        Create a new object of the class itkCastSpatialObjectFilter2 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCastSpatialObjectFilter2.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCastSpatialObjectFilter2.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCastSpatialObjectFilter2.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkCastSpatialObjectFilter2.Clone = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_Clone, None, itkCastSpatialObjectFilter2)
itkCastSpatialObjectFilter2.SetInput = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_SetInput, None, itkCastSpatialObjectFilter2)
itkCastSpatialObjectFilter2.GetInput = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetInput, None, itkCastSpatialObjectFilter2)
itkCastSpatialObjectFilter2.GetArrows = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetArrows, None, itkCastSpatialObjectFilter2)
itkCastSpatialObjectFilter2.GetBlobs = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetBlobs, None, itkCastSpatialObjectFilter2)
itkCastSpatialObjectFilter2.GetBoxes = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetBoxes, None, itkCastSpatialObjectFilter2)
itkCastSpatialObjectFilter2.GetContours = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetContours, None, itkCastSpatialObjectFilter2)
itkCastSpatialObjectFilter2.GetEllipses = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetEllipses, None, itkCastSpatialObjectFilter2)
itkCastSpatialObjectFilter2.GetGaussians = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetGaussians, None, itkCastSpatialObjectFilter2)
itkCastSpatialObjectFilter2.GetGroups = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetGroups, None, itkCastSpatialObjectFilter2)
itkCastSpatialObjectFilter2.GetImageMasks = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetImageMasks, None, itkCastSpatialObjectFilter2)
itkCastSpatialObjectFilter2.GetImages = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetImages, None, itkCastSpatialObjectFilter2)
itkCastSpatialObjectFilter2.GetLandmarks = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetLandmarks, None, itkCastSpatialObjectFilter2)
itkCastSpatialObjectFilter2.GetLines = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetLines, None, itkCastSpatialObjectFilter2)
itkCastSpatialObjectFilter2.GetPointBased = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetPointBased, None, itkCastSpatialObjectFilter2)
itkCastSpatialObjectFilter2.GetPolygons = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetPolygons, None, itkCastSpatialObjectFilter2)
itkCastSpatialObjectFilter2.GetSpatialObjects = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetSpatialObjects, None, itkCastSpatialObjectFilter2)
itkCastSpatialObjectFilter2.GetSurfaces = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetSurfaces, None, itkCastSpatialObjectFilter2)
itkCastSpatialObjectFilter2.GetTubes = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_GetTubes, None, itkCastSpatialObjectFilter2)
itkCastSpatialObjectFilter2_swigregister = _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_swigregister
itkCastSpatialObjectFilter2_swigregister(itkCastSpatialObjectFilter2)

def itkCastSpatialObjectFilter2___New_orig__() -> "itkCastSpatialObjectFilter2_Pointer":
    """itkCastSpatialObjectFilter2___New_orig__() -> itkCastSpatialObjectFilter2_Pointer"""
    return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2___New_orig__()

def itkCastSpatialObjectFilter2_cast(obj: 'itkLightObject') -> "itkCastSpatialObjectFilter2 *":
    """itkCastSpatialObjectFilter2_cast(itkLightObject obj) -> itkCastSpatialObjectFilter2"""
    return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter2_cast(obj)

class itkCastSpatialObjectFilter3(ITKCommonBasePython.itkObject):
    """


    This filter casts one spatialobject to another, when the class
    hierarchy supports it (e.g., Tube to PointBased). Particularly useful
    in Python where casting objects without public contructors (e.g.,
    objects managed by smartpointers) is problematic.

    C++ includes: itkCastSpatialObjectFilter.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkCastSpatialObjectFilter3_Pointer":
        """__New_orig__() -> itkCastSpatialObjectFilter3_Pointer"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkCastSpatialObjectFilter3_Pointer":
        """Clone(itkCastSpatialObjectFilter3 self) -> itkCastSpatialObjectFilter3_Pointer"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_Clone(self)


    def SetInput(self, _arg: 'itkSpatialObject3') -> "void":
        """SetInput(itkCastSpatialObjectFilter3 self, itkSpatialObject3 _arg)"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_SetInput(self, _arg)


    def GetInput(self) -> "itkSpatialObject3 const *":
        """GetInput(itkCastSpatialObjectFilter3 self) -> itkSpatialObject3"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetInput(self)


    def GetArrows(self) -> "std::list< itkArrowSpatialObject3_Pointer,std::allocator< itkArrowSpatialObject3_Pointer > > *":
        """GetArrows(itkCastSpatialObjectFilter3 self) -> std::list< itkArrowSpatialObject3_Pointer,std::allocator< itkArrowSpatialObject3_Pointer > > *"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetArrows(self)


    def GetBlobs(self) -> "std::list< itkBlobSpatialObject3_Pointer,std::allocator< itkBlobSpatialObject3_Pointer > > *":
        """GetBlobs(itkCastSpatialObjectFilter3 self) -> std::list< itkBlobSpatialObject3_Pointer,std::allocator< itkBlobSpatialObject3_Pointer > > *"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetBlobs(self)


    def GetBoxes(self) -> "std::list< itkBoxSpatialObject3_Pointer,std::allocator< itkBoxSpatialObject3_Pointer > > *":
        """GetBoxes(itkCastSpatialObjectFilter3 self) -> listitkBoxSpatialObject3_Pointer"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetBoxes(self)


    def GetContours(self) -> "std::list< itkContourSpatialObject3_Pointer,std::allocator< itkContourSpatialObject3_Pointer > > *":
        """GetContours(itkCastSpatialObjectFilter3 self) -> listitkContourSpatialObject3_Pointer"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetContours(self)


    def GetEllipses(self) -> "std::list< itkEllipseSpatialObject3_Pointer,std::allocator< itkEllipseSpatialObject3_Pointer > > *":
        """GetEllipses(itkCastSpatialObjectFilter3 self) -> listitkEllipseSpatialObject3_Pointer"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetEllipses(self)


    def GetGaussians(self) -> "std::list< itkGaussianSpatialObject3_Pointer,std::allocator< itkGaussianSpatialObject3_Pointer > > *":
        """GetGaussians(itkCastSpatialObjectFilter3 self) -> listitkGaussianSpatialObject3_Pointer"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetGaussians(self)


    def GetGroups(self) -> "std::list< itkGroupSpatialObject3_Pointer,std::allocator< itkGroupSpatialObject3_Pointer > > *":
        """GetGroups(itkCastSpatialObjectFilter3 self) -> listitkGroupSpatialObject3_Pointer"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetGroups(self)


    def GetImageMasks(self) -> "std::list< itkImageMaskSpatialObject3_Pointer,std::allocator< itkImageMaskSpatialObject3_Pointer > > *":
        """GetImageMasks(itkCastSpatialObjectFilter3 self) -> listitkImageMaskSpatialObject3_Pointer"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetImageMasks(self)


    def GetImages(self) -> "std::list< itkImageSpatialObject3UC_Pointer,std::allocator< itkImageSpatialObject3UC_Pointer > > *":
        """GetImages(itkCastSpatialObjectFilter3 self) -> listitkImageSpatialObject3UC_Pointer"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetImages(self)


    def GetLandmarks(self) -> "std::list< itkLandmarkSpatialObject3_Pointer,std::allocator< itkLandmarkSpatialObject3_Pointer > > *":
        """GetLandmarks(itkCastSpatialObjectFilter3 self) -> listitkLandmarkSpatialObject3_Pointer"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetLandmarks(self)


    def GetLines(self) -> "std::list< itkLineSpatialObject3_Pointer,std::allocator< itkLineSpatialObject3_Pointer > > *":
        """GetLines(itkCastSpatialObjectFilter3 self) -> listitkLineSpatialObject3_Pointer"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetLines(self)


    def GetPointBased(self) -> "std::list< itkPointBasedSpatialObject3_Pointer,std::allocator< itkPointBasedSpatialObject3_Pointer > > *":
        """GetPointBased(itkCastSpatialObjectFilter3 self) -> listitkPointBasedSpatialObject3_Pointer"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetPointBased(self)


    def GetPolygons(self) -> "std::list< itkPolygonSpatialObject3_Pointer,std::allocator< itkPolygonSpatialObject3_Pointer > > *":
        """GetPolygons(itkCastSpatialObjectFilter3 self) -> listitkPolygonSpatialObject3_Pointer"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetPolygons(self)


    def GetSpatialObjects(self) -> "std::list< itkSpatialObject3_Pointer,std::allocator< itkSpatialObject3_Pointer > > *":
        """GetSpatialObjects(itkCastSpatialObjectFilter3 self) -> listitkSpatialObject3_Pointer"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetSpatialObjects(self)


    def GetSurfaces(self) -> "std::list< itkSurfaceSpatialObject3_Pointer,std::allocator< itkSurfaceSpatialObject3_Pointer > > *":
        """GetSurfaces(itkCastSpatialObjectFilter3 self) -> listitkSurfaceSpatialObject3_Pointer"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetSurfaces(self)


    def GetTubes(self) -> "std::list< itkTubeSpatialObject3_Pointer,std::allocator< itkTubeSpatialObject3_Pointer > > *":
        """GetTubes(itkCastSpatialObjectFilter3 self) -> listitkTubeSpatialObject3_Pointer"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetTubes(self)

    __swig_destroy__ = _itkCastSpatialObjectFilterPython.delete_itkCastSpatialObjectFilter3

    def cast(obj: 'itkLightObject') -> "itkCastSpatialObjectFilter3 *":
        """cast(itkLightObject obj) -> itkCastSpatialObjectFilter3"""
        return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkCastSpatialObjectFilter3

        Create a new object of the class itkCastSpatialObjectFilter3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkCastSpatialObjectFilter3.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkCastSpatialObjectFilter3.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkCastSpatialObjectFilter3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkCastSpatialObjectFilter3.Clone = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_Clone, None, itkCastSpatialObjectFilter3)
itkCastSpatialObjectFilter3.SetInput = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_SetInput, None, itkCastSpatialObjectFilter3)
itkCastSpatialObjectFilter3.GetInput = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetInput, None, itkCastSpatialObjectFilter3)
itkCastSpatialObjectFilter3.GetArrows = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetArrows, None, itkCastSpatialObjectFilter3)
itkCastSpatialObjectFilter3.GetBlobs = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetBlobs, None, itkCastSpatialObjectFilter3)
itkCastSpatialObjectFilter3.GetBoxes = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetBoxes, None, itkCastSpatialObjectFilter3)
itkCastSpatialObjectFilter3.GetContours = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetContours, None, itkCastSpatialObjectFilter3)
itkCastSpatialObjectFilter3.GetEllipses = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetEllipses, None, itkCastSpatialObjectFilter3)
itkCastSpatialObjectFilter3.GetGaussians = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetGaussians, None, itkCastSpatialObjectFilter3)
itkCastSpatialObjectFilter3.GetGroups = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetGroups, None, itkCastSpatialObjectFilter3)
itkCastSpatialObjectFilter3.GetImageMasks = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetImageMasks, None, itkCastSpatialObjectFilter3)
itkCastSpatialObjectFilter3.GetImages = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetImages, None, itkCastSpatialObjectFilter3)
itkCastSpatialObjectFilter3.GetLandmarks = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetLandmarks, None, itkCastSpatialObjectFilter3)
itkCastSpatialObjectFilter3.GetLines = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetLines, None, itkCastSpatialObjectFilter3)
itkCastSpatialObjectFilter3.GetPointBased = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetPointBased, None, itkCastSpatialObjectFilter3)
itkCastSpatialObjectFilter3.GetPolygons = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetPolygons, None, itkCastSpatialObjectFilter3)
itkCastSpatialObjectFilter3.GetSpatialObjects = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetSpatialObjects, None, itkCastSpatialObjectFilter3)
itkCastSpatialObjectFilter3.GetSurfaces = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetSurfaces, None, itkCastSpatialObjectFilter3)
itkCastSpatialObjectFilter3.GetTubes = new_instancemethod(_itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_GetTubes, None, itkCastSpatialObjectFilter3)
itkCastSpatialObjectFilter3_swigregister = _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_swigregister
itkCastSpatialObjectFilter3_swigregister(itkCastSpatialObjectFilter3)

def itkCastSpatialObjectFilter3___New_orig__() -> "itkCastSpatialObjectFilter3_Pointer":
    """itkCastSpatialObjectFilter3___New_orig__() -> itkCastSpatialObjectFilter3_Pointer"""
    return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3___New_orig__()

def itkCastSpatialObjectFilter3_cast(obj: 'itkLightObject') -> "itkCastSpatialObjectFilter3 *":
    """itkCastSpatialObjectFilter3_cast(itkLightObject obj) -> itkCastSpatialObjectFilter3"""
    return _itkCastSpatialObjectFilterPython.itkCastSpatialObjectFilter3_cast(obj)



