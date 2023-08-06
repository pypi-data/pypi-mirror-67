#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='lapras',
    version='0.0.2',
    packages = find_packages(),
    # Project uses , so ensure
    install_requires=[],
    description='scorecard',
    # long_description=open("README.rst").read(),
    url='https://github.com/yhangang',
    author='Badtom',
    author_email='yhangang@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # include any *.msg files found in the 'test' package, too:
        'test': ['*.msg'],
    },

    keywords=['scorecard'],
    entry_points={

    },
)