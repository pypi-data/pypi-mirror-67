# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkSpatialObjectPropertyPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkSpatialObjectPropertyPython', [dirname(__file__)])
        except ImportError:
            import _itkSpatialObjectPropertyPython
            return _itkSpatialObjectPropertyPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkSpatialObjectPropertyPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkSpatialObjectPropertyPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkSpatialObjectPropertyPython
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


import itkRGBAPixelPython
import itkFixedArrayPython
import pyBasePython
import ITKCommonBasePython
class itkSpatialObjectProperty(object):
    """


    This class contains the objects properties such as colors, opacity,
    etc... it's templated over the representation to use for each color
    component.

    C++ includes: itkSpatialObjectProperty.h 
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    __swig_destroy__ = _itkSpatialObjectPropertyPython.delete_itkSpatialObjectProperty

    def Clear(self) -> "void":
        """Clear(itkSpatialObjectProperty self)"""
        return _itkSpatialObjectPropertyPython.itkSpatialObjectProperty_Clear(self)


    def GetColor(self, *args) -> "itkRGBAPixelD const &":
        """
        GetColor(itkSpatialObjectProperty self) -> itkRGBAPixelD
        GetColor(itkSpatialObjectProperty self) -> itkRGBAPixelD
        """
        return _itkSpatialObjectPropertyPython.itkSpatialObjectProperty_GetColor(self, *args)


    def SetColor(self, *args) -> "void":
        """
        SetColor(itkSpatialObjectProperty self, itkRGBAPixelD color)
        SetColor(itkSpatialObjectProperty self, double r, double g, double b)
        """
        return _itkSpatialObjectPropertyPython.itkSpatialObjectProperty_SetColor(self, *args)


    def SetRed(self, r: 'double') -> "void":
        """SetRed(itkSpatialObjectProperty self, double r)"""
        return _itkSpatialObjectPropertyPython.itkSpatialObjectProperty_SetRed(self, r)


    def GetRed(self) -> "double":
        """GetRed(itkSpatialObjectProperty self) -> double"""
        return _itkSpatialObjectPropertyPython.itkSpatialObjectProperty_GetRed(self)


    def SetGreen(self, g: 'double') -> "void":
        """SetGreen(itkSpatialObjectProperty self, double g)"""
        return _itkSpatialObjectPropertyPython.itkSpatialObjectProperty_SetGreen(self, g)


    def GetGreen(self) -> "double":
        """GetGreen(itkSpatialObjectProperty self) -> double"""
        return _itkSpatialObjectPropertyPython.itkSpatialObjectProperty_GetGreen(self)


    def SetBlue(self, b: 'double') -> "void":
        """SetBlue(itkSpatialObjectProperty self, double b)"""
        return _itkSpatialObjectPropertyPython.itkSpatialObjectProperty_SetBlue(self, b)


    def GetBlue(self) -> "double":
        """GetBlue(itkSpatialObjectProperty self) -> double"""
        return _itkSpatialObjectPropertyPython.itkSpatialObjectProperty_GetBlue(self)


    def SetAlpha(self, a: 'double') -> "void":
        """SetAlpha(itkSpatialObjectProperty self, double a)"""
        return _itkSpatialObjectPropertyPython.itkSpatialObjectProperty_SetAlpha(self, a)


    def GetAlpha(self) -> "double":
        """GetAlpha(itkSpatialObjectProperty self) -> double"""
        return _itkSpatialObjectPropertyPython.itkSpatialObjectProperty_GetAlpha(self)


    def SetName(self, name: 'std::string const &') -> "void":
        """SetName(itkSpatialObjectProperty self, std::string const & name)"""
        return _itkSpatialObjectPropertyPython.itkSpatialObjectProperty_SetName(self, name)


    def GetName(self, *args) -> "std::string const &":
        """
        GetName(itkSpatialObjectProperty self) -> std::string
        GetName(itkSpatialObjectProperty self) -> std::string const &
        """
        return _itkSpatialObjectPropertyPython.itkSpatialObjectProperty_GetName(self, *args)


    def SetTagScalarValue(self, tag: 'std::string const &', value: 'double') -> "void":
        """SetTagScalarValue(itkSpatialObjectProperty self, std::string const & tag, double value)"""
        return _itkSpatialObjectPropertyPython.itkSpatialObjectProperty_SetTagScalarValue(self, tag, value)


    def SetTagStringValue(self, tag: 'std::string const &', value: 'std::string const &') -> "void":
        """SetTagStringValue(itkSpatialObjectProperty self, std::string const & tag, std::string const & value)"""
        return _itkSpatialObjectPropertyPython.itkSpatialObjectProperty_SetTagStringValue(self, tag, value)


    def GetTagScalarValue(self, tag: 'std::string const &', value: 'double &') -> "bool":
        """GetTagScalarValue(itkSpatialObjectProperty self, std::string const & tag, double & value) -> bool"""
        return _itkSpatialObjectPropertyPython.itkSpatialObjectProperty_GetTagScalarValue(self, tag, value)


    def GetTagStringValue(self, tag: 'std::string const &', value: 'std::string &') -> "bool":
        """GetTagStringValue(itkSpatialObjectProperty self, std::string const & tag, std::string & value) -> bool"""
        return _itkSpatialObjectPropertyPython.itkSpatialObjectProperty_GetTagStringValue(self, tag, value)


    def GetTagScalarDictionary(self, *args) -> "std::map< std::string,double,std::less< std::string >,std::allocator< std::pair< std::string const,double > > > const &":
        """
        GetTagScalarDictionary(itkSpatialObjectProperty self) -> std::map< std::string,double,std::less< std::string >,std::allocator< std::pair< std::string const,double > > >
        GetTagScalarDictionary(itkSpatialObjectProperty self) -> std::map< std::string,double,std::less< std::string >,std::allocator< std::pair< std::string const,double > > > const &
        """
        return _itkSpatialObjectPropertyPython.itkSpatialObjectProperty_GetTagScalarDictionary(self, *args)


    def GetTagStringDictionary(self, *args) -> "std::map< std::string,std::string,std::less< std::string >,std::allocator< std::pair< std::string const,std::string > > > const &":
        """
        GetTagStringDictionary(itkSpatialObjectProperty self) -> std::map< std::string,std::string,std::less< std::string >,std::allocator< std::pair< std::string const,std::string > > >
        GetTagStringDictionary(itkSpatialObjectProperty self) -> std::map< std::string,std::string,std::less< std::string >,std::allocator< std::pair< std::string const,std::string > > > const &
        """
        return _itkSpatialObjectPropertyPython.itkSpatialObjectProperty_GetTagStringDictionary(self, *args)


    def SetTagScalarDictionary(self, dict: 'std::map< std::string,double,std::less< std::string >,std::allocator< std::pair< std::string const,double > > > const &') -> "void":
        """SetTagScalarDictionary(itkSpatialObjectProperty self, std::map< std::string,double,std::less< std::string >,std::allocator< std::pair< std::string const,double > > > const & dict)"""
        return _itkSpatialObjectPropertyPython.itkSpatialObjectProperty_SetTagScalarDictionary(self, dict)


    def SetTagStringDictionary(self, dict: 'std::map< std::string,std::string,std::less< std::string >,std::allocator< std::pair< std::string const,std::string > > > const &') -> "void":
        """SetTagStringDictionary(itkSpatialObjectProperty self, std::map< std::string,std::string,std::less< std::string >,std::allocator< std::pair< std::string const,std::string > > > const & dict)"""
        return _itkSpatialObjectPropertyPython.itkSpatialObjectProperty_SetTagStringDictionary(self, dict)


    def Print(self, os: 'ostream') -> "void":
        """Print(itkSpatialObjectProperty self, ostream os)"""
        return _itkSpatialObjectPropertyPython.itkSpatialObjectProperty_Print(self, os)


    def __init__(self, *args):
        """
        __init__(itkSpatialObjectProperty self) -> itkSpatialObjectProperty
        __init__(itkSpatialObjectProperty self, itkSpatialObjectProperty arg0) -> itkSpatialObjectProperty



        This class contains the objects properties such as colors, opacity,
        etc... it's templated over the representation to use for each color
        component.

        C++ includes: itkSpatialObjectProperty.h 
        """
        _itkSpatialObjectPropertyPython.itkSpatialObjectProperty_swiginit(self, _itkSpatialObjectPropertyPython.new_itkSpatialObjectProperty(*args))
itkSpatialObjectProperty.Clear = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectProperty_Clear, None, itkSpatialObjectProperty)
itkSpatialObjectProperty.GetColor = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectProperty_GetColor, None, itkSpatialObjectProperty)
itkSpatialObjectProperty.SetColor = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectProperty_SetColor, None, itkSpatialObjectProperty)
itkSpatialObjectProperty.SetRed = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectProperty_SetRed, None, itkSpatialObjectProperty)
itkSpatialObjectProperty.GetRed = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectProperty_GetRed, None, itkSpatialObjectProperty)
itkSpatialObjectProperty.SetGreen = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectProperty_SetGreen, None, itkSpatialObjectProperty)
itkSpatialObjectProperty.GetGreen = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectProperty_GetGreen, None, itkSpatialObjectProperty)
itkSpatialObjectProperty.SetBlue = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectProperty_SetBlue, None, itkSpatialObjectProperty)
itkSpatialObjectProperty.GetBlue = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectProperty_GetBlue, None, itkSpatialObjectProperty)
itkSpatialObjectProperty.SetAlpha = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectProperty_SetAlpha, None, itkSpatialObjectProperty)
itkSpatialObjectProperty.GetAlpha = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectProperty_GetAlpha, None, itkSpatialObjectProperty)
itkSpatialObjectProperty.SetName = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectProperty_SetName, None, itkSpatialObjectProperty)
itkSpatialObjectProperty.GetName = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectProperty_GetName, None, itkSpatialObjectProperty)
itkSpatialObjectProperty.SetTagScalarValue = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectProperty_SetTagScalarValue, None, itkSpatialObjectProperty)
itkSpatialObjectProperty.SetTagStringValue = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectProperty_SetTagStringValue, None, itkSpatialObjectProperty)
itkSpatialObjectProperty.GetTagScalarValue = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectProperty_GetTagScalarValue, None, itkSpatialObjectProperty)
itkSpatialObjectProperty.GetTagStringValue = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectProperty_GetTagStringValue, None, itkSpatialObjectProperty)
itkSpatialObjectProperty.GetTagScalarDictionary = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectProperty_GetTagScalarDictionary, None, itkSpatialObjectProperty)
itkSpatialObjectProperty.GetTagStringDictionary = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectProperty_GetTagStringDictionary, None, itkSpatialObjectProperty)
itkSpatialObjectProperty.SetTagScalarDictionary = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectProperty_SetTagScalarDictionary, None, itkSpatialObjectProperty)
itkSpatialObjectProperty.SetTagStringDictionary = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectProperty_SetTagStringDictionary, None, itkSpatialObjectProperty)
itkSpatialObjectProperty.Print = new_instancemethod(_itkSpatialObjectPropertyPython.itkSpatialObjectProperty_Print, None, itkSpatialObjectProperty)
itkSpatialObjectProperty_swigregister = _itkSpatialObjectPropertyPython.itkSpatialObjectProperty_swigregister
itkSpatialObjectProperty_swigregister(itkSpatialObjectProperty)



