import os
import sys
import time

print(time.time())
print(sys.version)
print(os.getcwd())
time.sleep(1)
print(time.time())

from sys import version

print(version)

import cpython

print(cpython.website)
cpython.help()
