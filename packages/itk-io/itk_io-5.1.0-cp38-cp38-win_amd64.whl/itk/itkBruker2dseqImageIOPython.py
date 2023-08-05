# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkBruker2dseqImageIOPython
else:
    import _itkBruker2dseqImageIOPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkBruker2dseqImageIOPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkBruker2dseqImageIOPython.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import ITKCommonBasePython
import pyBasePython
import ITKIOImageBaseBasePython
import vnl_vectorPython
import stdcomplexPython
import vnl_matrixPython

def itkBruker2dseqImageIOFactory_New():
  return itkBruker2dseqImageIOFactory.New()


def itkBruker2dseqImageIO_New():
  return itkBruker2dseqImageIO.New()

class itkBruker2dseqImageIO(ITKIOImageBaseBasePython.itkImageIOBase):
    r"""Proxy of C++ itkBruker2dseqImageIO class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBruker2dseqImageIOPython.itkBruker2dseqImageIO___New_orig__)
    Clone = _swig_new_instance_method(_itkBruker2dseqImageIOPython.itkBruker2dseqImageIO_Clone)
    __swig_destroy__ = _itkBruker2dseqImageIOPython.delete_itkBruker2dseqImageIO
    cast = _swig_new_static_method(_itkBruker2dseqImageIOPython.itkBruker2dseqImageIO_cast)

    def New(*args, **kargs):
        """New() -> itkBruker2dseqImageIO

        Create a new object of the class itkBruker2dseqImageIO and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBruker2dseqImageIO.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBruker2dseqImageIO.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBruker2dseqImageIO.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBruker2dseqImageIO in _itkBruker2dseqImageIOPython:
_itkBruker2dseqImageIOPython.itkBruker2dseqImageIO_swigregister(itkBruker2dseqImageIO)
itkBruker2dseqImageIO___New_orig__ = _itkBruker2dseqImageIOPython.itkBruker2dseqImageIO___New_orig__
itkBruker2dseqImageIO_cast = _itkBruker2dseqImageIOPython.itkBruker2dseqImageIO_cast

class itkBruker2dseqImageIOFactory(ITKCommonBasePython.itkObjectFactoryBase):
    r"""Proxy of C++ itkBruker2dseqImageIOFactory class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkBruker2dseqImageIOPython.itkBruker2dseqImageIOFactory___New_orig__)
    RegisterOneFactory = _swig_new_static_method(_itkBruker2dseqImageIOPython.itkBruker2dseqImageIOFactory_RegisterOneFactory)
    __swig_destroy__ = _itkBruker2dseqImageIOPython.delete_itkBruker2dseqImageIOFactory
    cast = _swig_new_static_method(_itkBruker2dseqImageIOPython.itkBruker2dseqImageIOFactory_cast)

    def New(*args, **kargs):
        """New() -> itkBruker2dseqImageIOFactory

        Create a new object of the class itkBruker2dseqImageIOFactory and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkBruker2dseqImageIOFactory.New( reader, Threshold=10 )

        is (most of the time) equivalent to:

          obj = itkBruker2dseqImageIOFactory.New()
          obj.SetInput( 0, reader.GetOutput() )
          obj.SetThreshold( 10 )
        """
        obj = itkBruker2dseqImageIOFactory.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkBruker2dseqImageIOFactory in _itkBruker2dseqImageIOPython:
_itkBruker2dseqImageIOPython.itkBruker2dseqImageIOFactory_swigregister(itkBruker2dseqImageIOFactory)
itkBruker2dseqImageIOFactory___New_orig__ = _itkBruker2dseqImageIOPython.itkBruker2dseqImageIOFactory___New_orig__
itkBruker2dseqImageIOFactory_RegisterOneFactory = _itkBruker2dseqImageIOPython.itkBruker2dseqImageIOFactory_RegisterOneFactory
itkBruker2dseqImageIOFactory_cast = _itkBruker2dseqImageIOPython.itkBruker2dseqImageIOFactory_cast



