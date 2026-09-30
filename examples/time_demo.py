# 时间

import time

print("--- 时间戳和延时 ---")
start = time.time()
print(start)
time.sleep(1)
print(time.time())
spent = time.time() - start
print(round(spent, 1))

print("--- 可读字符串 ---")
print(time.ctime(0))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(0)))
print(time.strftime("%Y-%m-%d %H:%M:%S"))

print("--- 拆开年月日 ---")
local = time.localtime(0)
utc = time.gmtime(0)
print(local.tm_year, local.tm_mon, local.tm_mday, local.tm_hour)
print(utc.tm_hour)
print(time.mktime(local))

print("--- 从字符串读回 ---")
text = "2026-01-01 08:00:00"
parsed = time.strptime(text, "%Y-%m-%d %H:%M:%S")
print(parsed.tm_year, parsed.tm_mon, parsed.tm_mday)
print(time.strftime("%Y-%m-%d %H:%M:%S", parsed))

print("--- datetime ---")
from datetime import datetime, timedelta

day = datetime(2026, 1, 1, 8, 0, 0)
tomorrow = day + timedelta(days=1)
print(day.strftime("%Y-%m-%d"))
print(tomorrow.strftime("%Y-%m-%d %H:%M:%S"))
