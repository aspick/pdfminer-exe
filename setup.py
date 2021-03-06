# -*- coding: utf-8

import sys
sys.path.append("./pdfminer")

from distutils.core import setup
import py2exe

import os
import glob

def find_data_files(source,target,patterns):
    """Locates the specified data-files and returns the matches
   in a data_files compatible format.

   source is the root of the source data tree.
       Use '' or '.' for current directory.
     target is the root of the target data tree.
         Use '' or '.' for the distribution directory.
     patterns is a sequence of glob-patterns for the
         files you want to copy.
    """
    if glob.has_magic(source) or glob.has_magic(target):
        raise ValueError("Magic not allowed in src, target")
    ret = {}
    for pattern in patterns:
        pattern = os.path.join(source,pattern)
        for filename in glob.glob(pattern):
            if os.path.isfile(filename):
                targetpath = os.path.join(target,os.path.relpath(filename,source))
                path = os.path.dirname(targetpath)
                ret.setdefault(path,[]).append(filename)
    return sorted(ret.items())

setup(
    options = {'py2exe': {'bundle_files':1}},
    zipfile = None,
    console = [{'script':'pdfminer/tools/pdf2txt.py'}],
    data_files = find_data_files('pdfminer/pdfminer/cmap', 'cmap', [
        '*',
    ]),
)
