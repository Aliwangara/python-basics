# https://docs.python.org/3/py-modindex.html


# import platform
# we can shorten the name by giving the imported module a new name eg:
import platform as pl
from platform import python_version, system
# or
import string as st
import os

from Scrimba.dictionary import python

print(dir(pl))
print(pl.python_version()) # this gives the version
print(python_version()) # this gives the python version same as what we have done above
print(system()) # gives the system out python is running on/ the system we are using
print(dir(st))
print(dir(os))