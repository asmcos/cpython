#coding:utf-8

""" 引入模块 """

import os
import sys
import time

print(time.time())

print(sys.version)

print(os.uname())

time.sleep(1)

print(time.time())


from sys import version

print (version)

from os import uname

print(uname())
