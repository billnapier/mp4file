#!/usr/bin/python
from distutils.core import setup
setup(
    name = "mp4file",
    version = "0.3",
    packages = ['mp4file'],

    # metadata for upload to PyPI
    author = "Bill Napier",
    author_email = "napier@pobox.com",
    description = "Library for rudimentary parsing of mp4 atoms, especially metadata atoms.",
    license = "PSF",
    keywords = "mp4 atom quicktime",
)
