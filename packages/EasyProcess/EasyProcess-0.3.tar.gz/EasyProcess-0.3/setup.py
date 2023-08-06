import os

from setuptools import setup

NAME = "easyprocess"
PYPI_NAME = "EasyProcess"
URL = "https://github.com/ponty/easyprocess"
DESCRIPTION = "Easy to use Python subprocess interface."
LONG_DESCRIPTION = """Easy to use Python subprocess interface.

home: https://github.com/ponty/easyprocess"""
PACKAGES = [
    NAME,
    NAME + ".examples",
]

# get __version__
__version__ = None
exec(open(os.path.join(NAME, "about.py")).read())
VERSION = __version__

# extra = {}
# if sys.version_info >= (3,):
#     extra['use_2to3'] = True

classifiers = [
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    "License :: OSI Approved :: BSD License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
]


setup(
    name=PYPI_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=classifiers,
    keywords="subprocess interface",
    author="ponty",
    # author_email='',
    url=URL,
    license="BSD",
    packages=PACKAGES,
    # **extra
)
