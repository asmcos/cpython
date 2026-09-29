# 模块

print("--- 标准库 ---")
import os
import sys
import time

print(time.time())
print(sys.version)
print(os.getcwd())
time.sleep(1)
print(time.time())

print("--- from 和 as ---")
import sys as system
from sys import version
from sys import version as py_version

print(sys.version == system.version == version == py_version)

from time import time, sleep as pause

print(time() > 0)
pause(1)

print("--- 自己的模块 ---")
import cpython

print(cpython.website)
cpython.show_site()
print(cpython.__name__)

from cpython import website

print(website)

import cpython as site

print(site.website)

print("--- 搜索路径的第一项 ---")
print(sys.path[0])
