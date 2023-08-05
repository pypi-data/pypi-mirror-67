#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: mage
# Mail: mage@woodcol.com
# Created Time:  2018-1-23 19:17:34
#############################################


from setuptools import setup, find_packages
with open("README.md", "r" ,encoding = "utf-8") as fh:
    long_description = fh.read()

setup(
    name = "requests-cpp",
    version = "0.1.0",
    keywords = ("pip", "requests","cpr", "pybind11"),
    description = "Use c ++ multi-threaded http request library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license = "MIT Licence",

    url = "https://github.com/daimiaopeng/fast_requests",
    author = "daimiaopeng",
    author_email = "daimiaopeng@qq.com",

    package_data={
        '': ['*.pyd','*.dll'],
    },
    packages = find_packages(),
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)