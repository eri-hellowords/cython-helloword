USE_CYTHON = True

from cx_Freeze import Executable
from cx_Freeze import setup as cx_setup

build_exe_options = {
    "packages": ["os","struct"],
    "excludes": ["tkinter","tornado","zope","twisted","xmlrpc","xml"],
    "include_files": [],
    'create_shared_zip': True,
    'append_script_to_exe':True,
}

import os
if os.name == 'posix':
    build_exe_options['include_files'].extend(

        ['/usr/lib/libssl.so.1.0.0','/usr/lib/libcrypto.so.1.0.0']
    )
    
executables = [Executable(
    "main.py",
    base=None,
    targetName='main.exe'
    )]
    
if USE_CYTHON:
    from distutils.extension import Extension
    from distutils.core import setup
    from Cython.Build import cythonize

    build_exe_options['excludes'].append('module') #Убираем из ZIP и подсунем .SO

    extensions = [
        Extension("module", [
            "module.py",
            "libmodule/__init__.py",
            "libmodule/moduleclass.py"
            ]),
    ]

    setup(
        ext_modules = cythonize(extensions)
    )

cx_setup(  name = "cythonhello",
        version = "0.1",
        description = "Main",
        options = {"build_exe": build_exe_options},
        executables = executables,
        )
