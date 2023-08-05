#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 06:38:30 2020

@author: Sara Ben Shabbat
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="elasticsearch_sbs",
    version="2.0.0",
    author="Sara Ben Shabbat",
    author_email="sarabenshabbat@gmail.com",
    description="A package for ElasticSearch operations.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["elasticsearch_sbs"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)


