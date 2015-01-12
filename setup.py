#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from builtins import *
from setuptools import setup

setup(name="clang",
      version="3.4.dev192547",
      description="libclang python bindings",
      long_description=open("README.txt").read(),
      url="https://github.com/trolldbois/python-clang",
      download_url="https://github.com/trolldbois/python-clang/releases",
      license="License :: OSI Approved :: University of Illinois/NCSA Open Source License",
      classifiers=[
          "Intended Audience :: Developers",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Programming Language :: Python",
          "Development Status :: 5 - Production/Stable",
          "Topic :: Software Development :: Compilers"
      ],
      keywords=["llvm", "clang", "libclang"],
      author="Loic Jaquemet",  # meeeh... not.
      author_email="loic.jaquemet+python@gmail.com",
      zip_safe=False,
      install_requires=['future>=0.14.3'],
      packages=["clang"],
      # use pip requirements.txt instead
      # install_requires = ["libclang"],
      # build_tests_requires = ["libclang"],

      # if use nose.collector, many plugins not is avaliable
      # see: http://nose.readthedocs.org/en/latest/setuptools_integration.html
      test_suite="nose.collector",
      tests_require=['nose']
)


