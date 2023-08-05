#!/usr/bin/env python
# coding: utf-8

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-pangu-championchangpeng", # Replace with your own username
    version="0.0.1",
    author="championchangpeng",
    author_email="championchangpeng@gmail.com",
    description="ai adapter client for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/GokGok_group/python-pangu",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
