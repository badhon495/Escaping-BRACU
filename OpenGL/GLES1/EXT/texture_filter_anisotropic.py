'''OpenGL extension EXT.texture_filter_anisotropic

This module customises the behaviour of the 
OpenGL.raw.GLES1.EXT.texture_filter_anisotropic to provide a more 
Python-friendly API

Overview (from the spec)
	
	Texture mapping using OpenGL's existing mipmap texture filtering
	modes assumes that the projection of the pixel filter footprint into
	texture space is a square (ie, isotropic).  In practice however, the
	footprint may be long and narrow (ie, anisotropic).  Consequently,
	mipmap filtering severely blurs images on surfaces angled obliquely
	away from the viewer.
	
	Several approaches exist for improving texture sampling by accounting
	for the anisotropic nature of the pixel filter footprint into texture
	space.  This extension provides a general mechanism for supporting
	anisotropic texturing filtering schemes without specifying a
	particular formulation of anisotropic filtering.
	
	The extension permits the OpenGL application to specify on
	a per-texture object basis the maximum degree of anisotropy to
	account for in texture filtering.
	
	Increasing a texture object's maximum degree of anisotropy may
	improve texture filtering but may also significantly reduce the
	implementation's texture filtering rate.  Implementations are free
	to clamp the specified degree of anisotropy to the implementation's
	maximum supported degree of anisotropy.
	
	A texture's maximum degree of anisotropy is specified independent
	from the texture's minification and magnification filter (as
	opposed to being supported as an entirely new filtering mode).
	Implementations are free to use the specified minification and
	magnification filter to select a particular anisotropic texture
	filtering scheme.  For example, a NEAREST filter with a maximum
	degree of anisotropy of two could be treated as a 2-tap filter that
	accounts for the direction of anisotropy.  Implementations are also
	permitted to ignore the minification or magnification filter and
	implement the highest quality of anisotropic filtering possible.
	
	Applications seeking the highest quality anisotropic filtering
	available are advised to request a LINEAR_MIPMAP_LINEAR minification
	filter, a LINEAR magnification filter, and a large maximum degree
	of anisotropy.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/texture_filter_anisotropic.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES1 import _types, _glgets
from OpenGL.raw.GLES1.EXT.texture_filter_anisotropic import *
from OpenGL.raw.GLES1.EXT.texture_filter_anisotropic import _EXTENSION_NAME

def glInitTextureFilterAnisotropicEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION