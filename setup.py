# -*- coding: utf-8

from distutils.core import setup
import py2exe

setup(
    options = {'py2exe': {'bundle_files':1}},
    zipfile = None,
    console = [{'script':'pdfminer/tools/pdf2txt.py'}]
)
