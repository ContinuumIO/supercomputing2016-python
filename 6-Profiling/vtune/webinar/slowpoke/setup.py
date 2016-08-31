from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension('core', sources=["core.pyx"],
                             extra_compile_args=['/Z7'],
                             extra_link_args=['/DEBUG']),
                  ],
)