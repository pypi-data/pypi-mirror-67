# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _itkTransformFileWriterPython.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_itkTransformFileWriterPython', [dirname(__file__)])
        except ImportError:
            import _itkTransformFileWriterPython
            return _itkTransformFileWriterPython
        if fp is not None:
            try:
                _mod = imp.load_module('_itkTransformFileWriterPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _itkTransformFileWriterPython = swig_import_helper()
    del swig_import_helper
else:
    import _itkTransformFileWriterPython
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


import itkTransformBasePython
import itkArray2DPython
import vnl_matrixPython
import stdcomplexPython
import pyBasePython
import vnl_vectorPython
import itkDiffusionTensor3DPython
import itkSymmetricSecondRankTensorPython
import itkMatrixPython
import itkCovariantVectorPython
import itkVectorPython
import vnl_vector_refPython
import itkFixedArrayPython
import itkPointPython
import vnl_matrix_fixedPython
import itkArrayPython
import itkOptimizerParametersPython
import ITKCommonBasePython
import itkVariableLengthVectorPython
import itkTransformIOBaseTemplatePython

def itkTransformFileWriterTemplateD_New():
  return itkTransformFileWriterTemplateD.New()


def itkTransformFileWriterTemplateF_New():
  return itkTransformFileWriterTemplateF.New()

class itkTransformFileWriterTemplateD(ITKCommonBasePython.itkLightProcessObject):
    """Proxy of C++ itkTransformFileWriterTemplateD class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkTransformFileWriterTemplateD_Pointer":
        """__New_orig__() -> itkTransformFileWriterTemplateD_Pointer"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateD___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkTransformFileWriterTemplateD_Pointer":
        """Clone(itkTransformFileWriterTemplateD self) -> itkTransformFileWriterTemplateD_Pointer"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateD_Clone(self)


    def SetFileName(self, *args) -> "void":
        """
        SetFileName(itkTransformFileWriterTemplateD self, char const * _arg)
        SetFileName(itkTransformFileWriterTemplateD self, std::string const & _arg)
        """
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateD_SetFileName(self, *args)


    def GetFileName(self) -> "char const *":
        """GetFileName(itkTransformFileWriterTemplateD self) -> char const *"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateD_GetFileName(self)


    def SetAppendOff(self) -> "void":
        """SetAppendOff(itkTransformFileWriterTemplateD self)"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateD_SetAppendOff(self)


    def SetAppendOn(self) -> "void":
        """SetAppendOn(itkTransformFileWriterTemplateD self)"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateD_SetAppendOn(self)


    def SetAppendMode(self, mode: 'bool') -> "void":
        """SetAppendMode(itkTransformFileWriterTemplateD self, bool mode)"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateD_SetAppendMode(self, mode)


    def GetAppendMode(self) -> "bool":
        """GetAppendMode(itkTransformFileWriterTemplateD self) -> bool"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateD_GetAppendMode(self)


    def SetUseCompression(self, _arg: 'bool const') -> "void":
        """SetUseCompression(itkTransformFileWriterTemplateD self, bool const _arg)"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateD_SetUseCompression(self, _arg)


    def GetUseCompression(self) -> "bool":
        """GetUseCompression(itkTransformFileWriterTemplateD self) -> bool"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateD_GetUseCompression(self)


    def UseCompressionOn(self) -> "void":
        """UseCompressionOn(itkTransformFileWriterTemplateD self)"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateD_UseCompressionOn(self)


    def UseCompressionOff(self) -> "void":
        """UseCompressionOff(itkTransformFileWriterTemplateD self)"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateD_UseCompressionOff(self)


    def SetInput(self, transform: 'itkObject') -> "void":
        """SetInput(itkTransformFileWriterTemplateD self, itkObject transform)"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateD_SetInput(self, transform)


    def GetInput(self) -> "itkTransformBaseTemplateD const *":
        """GetInput(itkTransformFileWriterTemplateD self) -> itkTransformBaseTemplateD"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateD_GetInput(self)


    def AddTransform(self, transform: 'itkObject') -> "void":
        """AddTransform(itkTransformFileWriterTemplateD self, itkObject transform)"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateD_AddTransform(self, transform)


    def Update(self) -> "void":
        """Update(itkTransformFileWriterTemplateD self)"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateD_Update(self)


    def SetTransformIO(self, _arg: 'itkTransformIOBaseTemplateD') -> "void":
        """SetTransformIO(itkTransformFileWriterTemplateD self, itkTransformIOBaseTemplateD _arg)"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateD_SetTransformIO(self, _arg)


    def GetTransformIO(self) -> "itkTransformIOBaseTemplateD const *":
        """GetTransformIO(itkTransformFileWriterTemplateD self) -> itkTransformIOBaseTemplateD"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateD_GetTransformIO(self)

    __swig_destroy__ = _itkTransformFileWriterPython.delete_itkTransformFileWriterTemplateD

    def cast(obj: 'itkLightObject') -> "itkTransformFileWriterTemplateD *":
        """cast(itkLightObject obj) -> itkTransformFileWriterTemplateD"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateD_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkTransformFileWriterTemplateD

        Create a new object of the class itkTransformFileWriterTemplateD and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTransformFileWriterTemplateD.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTransformFileWriterTemplateD.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTransformFileWriterTemplateD.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkTransformFileWriterTemplateD.Clone = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateD_Clone, None, itkTransformFileWriterTemplateD)
itkTransformFileWriterTemplateD.SetFileName = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateD_SetFileName, None, itkTransformFileWriterTemplateD)
itkTransformFileWriterTemplateD.GetFileName = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateD_GetFileName, None, itkTransformFileWriterTemplateD)
itkTransformFileWriterTemplateD.SetAppendOff = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateD_SetAppendOff, None, itkTransformFileWriterTemplateD)
itkTransformFileWriterTemplateD.SetAppendOn = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateD_SetAppendOn, None, itkTransformFileWriterTemplateD)
itkTransformFileWriterTemplateD.SetAppendMode = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateD_SetAppendMode, None, itkTransformFileWriterTemplateD)
itkTransformFileWriterTemplateD.GetAppendMode = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateD_GetAppendMode, None, itkTransformFileWriterTemplateD)
itkTransformFileWriterTemplateD.SetUseCompression = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateD_SetUseCompression, None, itkTransformFileWriterTemplateD)
itkTransformFileWriterTemplateD.GetUseCompression = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateD_GetUseCompression, None, itkTransformFileWriterTemplateD)
itkTransformFileWriterTemplateD.UseCompressionOn = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateD_UseCompressionOn, None, itkTransformFileWriterTemplateD)
itkTransformFileWriterTemplateD.UseCompressionOff = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateD_UseCompressionOff, None, itkTransformFileWriterTemplateD)
itkTransformFileWriterTemplateD.SetInput = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateD_SetInput, None, itkTransformFileWriterTemplateD)
itkTransformFileWriterTemplateD.GetInput = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateD_GetInput, None, itkTransformFileWriterTemplateD)
itkTransformFileWriterTemplateD.AddTransform = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateD_AddTransform, None, itkTransformFileWriterTemplateD)
itkTransformFileWriterTemplateD.Update = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateD_Update, None, itkTransformFileWriterTemplateD)
itkTransformFileWriterTemplateD.SetTransformIO = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateD_SetTransformIO, None, itkTransformFileWriterTemplateD)
itkTransformFileWriterTemplateD.GetTransformIO = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateD_GetTransformIO, None, itkTransformFileWriterTemplateD)
itkTransformFileWriterTemplateD_swigregister = _itkTransformFileWriterPython.itkTransformFileWriterTemplateD_swigregister
itkTransformFileWriterTemplateD_swigregister(itkTransformFileWriterTemplateD)

def itkTransformFileWriterTemplateD___New_orig__() -> "itkTransformFileWriterTemplateD_Pointer":
    """itkTransformFileWriterTemplateD___New_orig__() -> itkTransformFileWriterTemplateD_Pointer"""
    return _itkTransformFileWriterPython.itkTransformFileWriterTemplateD___New_orig__()

def itkTransformFileWriterTemplateD_cast(obj: 'itkLightObject') -> "itkTransformFileWriterTemplateD *":
    """itkTransformFileWriterTemplateD_cast(itkLightObject obj) -> itkTransformFileWriterTemplateD"""
    return _itkTransformFileWriterPython.itkTransformFileWriterTemplateD_cast(obj)

class itkTransformFileWriterTemplateF(ITKCommonBasePython.itkLightProcessObject):
    """Proxy of C++ itkTransformFileWriterTemplateF class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __New_orig__() -> "itkTransformFileWriterTemplateF_Pointer":
        """__New_orig__() -> itkTransformFileWriterTemplateF_Pointer"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateF___New_orig__()

    __New_orig__ = staticmethod(__New_orig__)

    def Clone(self) -> "itkTransformFileWriterTemplateF_Pointer":
        """Clone(itkTransformFileWriterTemplateF self) -> itkTransformFileWriterTemplateF_Pointer"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateF_Clone(self)


    def SetFileName(self, *args) -> "void":
        """
        SetFileName(itkTransformFileWriterTemplateF self, char const * _arg)
        SetFileName(itkTransformFileWriterTemplateF self, std::string const & _arg)
        """
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateF_SetFileName(self, *args)


    def GetFileName(self) -> "char const *":
        """GetFileName(itkTransformFileWriterTemplateF self) -> char const *"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateF_GetFileName(self)


    def SetAppendOff(self) -> "void":
        """SetAppendOff(itkTransformFileWriterTemplateF self)"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateF_SetAppendOff(self)


    def SetAppendOn(self) -> "void":
        """SetAppendOn(itkTransformFileWriterTemplateF self)"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateF_SetAppendOn(self)


    def SetAppendMode(self, mode: 'bool') -> "void":
        """SetAppendMode(itkTransformFileWriterTemplateF self, bool mode)"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateF_SetAppendMode(self, mode)


    def GetAppendMode(self) -> "bool":
        """GetAppendMode(itkTransformFileWriterTemplateF self) -> bool"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateF_GetAppendMode(self)


    def SetUseCompression(self, _arg: 'bool const') -> "void":
        """SetUseCompression(itkTransformFileWriterTemplateF self, bool const _arg)"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateF_SetUseCompression(self, _arg)


    def GetUseCompression(self) -> "bool":
        """GetUseCompression(itkTransformFileWriterTemplateF self) -> bool"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateF_GetUseCompression(self)


    def UseCompressionOn(self) -> "void":
        """UseCompressionOn(itkTransformFileWriterTemplateF self)"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateF_UseCompressionOn(self)


    def UseCompressionOff(self) -> "void":
        """UseCompressionOff(itkTransformFileWriterTemplateF self)"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateF_UseCompressionOff(self)


    def SetInput(self, transform: 'itkObject') -> "void":
        """SetInput(itkTransformFileWriterTemplateF self, itkObject transform)"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateF_SetInput(self, transform)


    def GetInput(self) -> "itkTransformBaseTemplateF const *":
        """GetInput(itkTransformFileWriterTemplateF self) -> itkTransformBaseTemplateF"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateF_GetInput(self)


    def AddTransform(self, transform: 'itkObject') -> "void":
        """AddTransform(itkTransformFileWriterTemplateF self, itkObject transform)"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateF_AddTransform(self, transform)


    def Update(self) -> "void":
        """Update(itkTransformFileWriterTemplateF self)"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateF_Update(self)


    def SetTransformIO(self, _arg: 'itkTransformIOBaseTemplateF') -> "void":
        """SetTransformIO(itkTransformFileWriterTemplateF self, itkTransformIOBaseTemplateF _arg)"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateF_SetTransformIO(self, _arg)


    def GetTransformIO(self) -> "itkTransformIOBaseTemplateF const *":
        """GetTransformIO(itkTransformFileWriterTemplateF self) -> itkTransformIOBaseTemplateF"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateF_GetTransformIO(self)

    __swig_destroy__ = _itkTransformFileWriterPython.delete_itkTransformFileWriterTemplateF

    def cast(obj: 'itkLightObject') -> "itkTransformFileWriterTemplateF *":
        """cast(itkLightObject obj) -> itkTransformFileWriterTemplateF"""
        return _itkTransformFileWriterPython.itkTransformFileWriterTemplateF_cast(obj)

    cast = staticmethod(cast)

    def New(*args, **kargs):
        """New() -> itkTransformFileWriterTemplateF

        Create a new object of the class itkTransformFileWriterTemplateF and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkTransformFileWriterTemplateF.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkTransformFileWriterTemplateF.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkTransformFileWriterTemplateF.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)

itkTransformFileWriterTemplateF.Clone = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateF_Clone, None, itkTransformFileWriterTemplateF)
itkTransformFileWriterTemplateF.SetFileName = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateF_SetFileName, None, itkTransformFileWriterTemplateF)
itkTransformFileWriterTemplateF.GetFileName = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateF_GetFileName, None, itkTransformFileWriterTemplateF)
itkTransformFileWriterTemplateF.SetAppendOff = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateF_SetAppendOff, None, itkTransformFileWriterTemplateF)
itkTransformFileWriterTemplateF.SetAppendOn = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateF_SetAppendOn, None, itkTransformFileWriterTemplateF)
itkTransformFileWriterTemplateF.SetAppendMode = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateF_SetAppendMode, None, itkTransformFileWriterTemplateF)
itkTransformFileWriterTemplateF.GetAppendMode = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateF_GetAppendMode, None, itkTransformFileWriterTemplateF)
itkTransformFileWriterTemplateF.SetUseCompression = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateF_SetUseCompression, None, itkTransformFileWriterTemplateF)
itkTransformFileWriterTemplateF.GetUseCompression = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateF_GetUseCompression, None, itkTransformFileWriterTemplateF)
itkTransformFileWriterTemplateF.UseCompressionOn = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateF_UseCompressionOn, None, itkTransformFileWriterTemplateF)
itkTransformFileWriterTemplateF.UseCompressionOff = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateF_UseCompressionOff, None, itkTransformFileWriterTemplateF)
itkTransformFileWriterTemplateF.SetInput = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateF_SetInput, None, itkTransformFileWriterTemplateF)
itkTransformFileWriterTemplateF.GetInput = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateF_GetInput, None, itkTransformFileWriterTemplateF)
itkTransformFileWriterTemplateF.AddTransform = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateF_AddTransform, None, itkTransformFileWriterTemplateF)
itkTransformFileWriterTemplateF.Update = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateF_Update, None, itkTransformFileWriterTemplateF)
itkTransformFileWriterTemplateF.SetTransformIO = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateF_SetTransformIO, None, itkTransformFileWriterTemplateF)
itkTransformFileWriterTemplateF.GetTransformIO = new_instancemethod(_itkTransformFileWriterPython.itkTransformFileWriterTemplateF_GetTransformIO, None, itkTransformFileWriterTemplateF)
itkTransformFileWriterTemplateF_swigregister = _itkTransformFileWriterPython.itkTransformFileWriterTemplateF_swigregister
itkTransformFileWriterTemplateF_swigregister(itkTransformFileWriterTemplateF)

def itkTransformFileWriterTemplateF___New_orig__() -> "itkTransformFileWriterTemplateF_Pointer":
    """itkTransformFileWriterTemplateF___New_orig__() -> itkTransformFileWriterTemplateF_Pointer"""
    return _itkTransformFileWriterPython.itkTransformFileWriterTemplateF___New_orig__()

def itkTransformFileWriterTemplateF_cast(obj: 'itkLightObject') -> "itkTransformFileWriterTemplateF *":
    """itkTransformFileWriterTemplateF_cast(itkLightObject obj) -> itkTransformFileWriterTemplateF"""
    return _itkTransformFileWriterPython.itkTransformFileWriterTemplateF_cast(obj)



