# time

时间模块入门阶段常用下面几个函数。

```
import time

print(time.time())
time.sleep(1)
print(time.ctime())
```

* `time.time()`：Unix 时间戳，整数部分是秒
* `time.sleep(n)`：停 n 秒
* `time.ctime()`：当前时间的可读字符串

示例输出（数字会随你运行的时刻变化）：

```
1735600000.123456
Thu Jan  1 12:00:01 2026
```

如果要按自己的格式输出年、月、日，可以用 `time.strftime`：

```
print(time.strftime("%Y-%m-%d %H:%M:%S"))
```

金融数据后面会大量用到「日期」和「时间序列」，这一节先把秒、延时、当前时间这三件事记熟。
