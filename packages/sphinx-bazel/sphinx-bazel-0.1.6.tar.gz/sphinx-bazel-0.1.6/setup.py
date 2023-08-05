#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

requires = ['Sphinx<2;python_version<"3.5"',
            'Sphinx<3;python_version<"3.6"',
            'Sphinx;python_version>="3.6"',
            ]

setup(
    name='sphinx-bazel',
    # If you raise, think about versions in conf.py and sphinx_bazel.py!!!
    version='0.1.6',
    url='http://github.com/useblocks/sphinx-bazel',
    download_url='http://pypi.python.org/pypi/sphinx-bazel',
    license='Apache 2.0',
    author='team useblocks',
    author_email='info@useblocks.com',
    description='Sphinx bazel extension to include content from bazel files.',
    long_description=open(os.path.join(os.path.dirname(__file__), "README.rst")).read(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
