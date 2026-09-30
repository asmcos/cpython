# 时间

时间用标准库里的 `time` 模块。文件不要保存成 `time.py`，否则 `import time` 会找到你自己的文件。本节例子放在 `examples/time_demo.py`。

入门先分清三件事：时间戳、让程序停一下、把时间印成能读的字符串。后面的金融数据会大量用到日期，加减天数用本节末尾的 `datetime` 更直接。

## 时间戳和延时

`time.time()` 返回从 1970-01-01 00:00:00（协调世界时，UTC）到现在的秒数，带小数。这叫 Unix 时间戳。整数部分是秒，小数是不足 1 秒的部分。

~~~
import time

print(time.time())
time.sleep(1)
print(time.time())
~~~

两次打印都是一串会变动的数字。`time.sleep(1)` 让程序停 1 秒，所以第二个数大约比第一个大 1。停的这段时间里，后面的代码不会执行。

拿两次时间戳相减，就是中间花了多少秒：

~~~
start = time.time()
time.sleep(1)
spent = time.time() - start
print(round(spent, 1))
~~~

~~~
1.0
~~~

`round(spent, 1)` 保留一位小数。系统有时会稍微超过 1 秒，看到 `1.0` 或 `1.1` 都正常。

## 印成能读的字符串

时间戳不适合直接给人看。`time.ctime()` 把它转成英文的星期、月、日和时间：

~~~
print(time.ctime(0))
~~~

在中国（东八区）这是：

~~~
Thu Jan  1 08:00:00 1970
~~~

时间戳 `0` 在 UTC 是 1970 年 1 月 1 日 0 点。东八区比 UTC 早 8 小时，所以本地时间是早上 8 点。不写参数时，`time.ctime()` 用的是现在。电脑不在东八区时，`0` 对应的钟点会不同。

要自己规定格式，用 `time.strftime`。格式串里以 `%` 开头的记号会被换成数字，其余字符原样留下：

~~~
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(0)))
~~~

~~~
1970-01-01 08:00:00
~~~

常用记号：

| 记号 | 含义 | 例子 |
| --- | --- | --- |
| `%Y` | 四位年份 | `1970` |
| `%m` | 月份，两位 | `01` |
| `%d` | 日期，两位 | `01` |
| `%H` | 小时，00 到 23 | `08` |
| `%M` | 分钟 | `00` |
| `%S` | 秒 | `00` |

`%m` 是月份，`%M` 是分钟，大小写不同。不传第二个参数时，`strftime` 用当前本地时间：

~~~
print(time.strftime("%Y-%m-%d %H:%M:%S"))
~~~

打印出来是运行这一刻的年、月、日和时分秒。

## 拆开年月日

`time.localtime()` 把时间戳拆成本地时间的各个字段，得到一个 `struct_time`。`time.gmtime()` 拆的是 UTC，不加上时区偏移。

~~~
local = time.localtime(0)
utc = time.gmtime(0)
print(local.tm_year, local.tm_mon, local.tm_mday, local.tm_hour)
print(utc.tm_hour)
~~~

~~~
1970 1 1 8
0
~~~

同一瞬间，本地是 8 点，UTC 是 0 点。字段里 `tm_year`、`tm_mon`、`tm_mday` 是年月日，`tm_hour`、`tm_min`、`tm_sec` 是时分秒。月份从 1 开始，不是从 0。

反过来，把这种结构变回时间戳用 `time.mktime()`。它按本地时区理解：

~~~
stamp = time.mktime(local)
print(stamp)
~~~

~~~
0.0
~~~

## 从字符串读回时间

日志和表格里的时间常常是字符串。`time.strptime` 按你给的格式把它拆开，格式必须和字符串对得上。

~~~
text = "2026-01-01 08:00:00"
parsed = time.strptime(text, "%Y-%m-%d %H:%M:%S")
print(parsed.tm_year, parsed.tm_mon, parsed.tm_mday)
print(time.strftime("%Y-%m-%d %H:%M:%S", parsed))
~~~

~~~
2026 1 1
2026-01-01 08:00:00
~~~

格式不一致就报错。字符串用了斜杠，格式却写成横杠：

~~~
time.strptime("2026/01/01", "%Y-%m-%d")
~~~

~~~
ValueError: time data '2026/01/01' does not match format '%Y-%m-%d'
~~~

斜杠就要写成 `"%Y/%m/%d"`。

## 日期加减用 datetime

`time` 适合拿时间戳、延时和格式化。要计算“明天”“三天前”，用标准库 `datetime` 更直接。它也不是新语法，是另一个模块。

~~~
from datetime import datetime, timedelta

day = datetime(2026, 1, 1, 8, 0, 0)
tomorrow = day + timedelta(days=1)
print(day.strftime("%Y-%m-%d"))
print(tomorrow.strftime("%Y-%m-%d %H:%M:%S"))
~~~

~~~
2026-01-01
2026-01-02 08:00:00
~~~

`datetime(年, 月, 日, 时, 分, 秒)` 造一个不带时区的本地日期时间。`timedelta(days=1)` 表示 1 天，加到日期上就得到下一天，时间仍是 08:00:00。当前时刻用 `datetime.now()`。

金融数据里的“交易日”还要跳过周末和节假日，那是后面数据处理的内容。这里先会做自然日的加减。

## 常见坑

**文件名叫 `time.py`。** `import time` 会导入你自己的文件，`time.time` 就不存在了。练习保存为 `time_demo.py`。

**`sleep` 会卡住整个程序。** `time.sleep(60)` 这一分钟里，后面的打印和计算都不会发生。

**本地时间和 UTC 差 8 小时。** 时间戳本身不含时区。`localtime`、`ctime`、`mktime` 按电脑的本地时区换算；`gmtime` 按 UTC。同一串秒数，两种函数打印出来的钟点不同。

**`%m` 和 `%M` 看反。** 小写 m 是月，大写 M 是分。格式和字符串对不上时，`strptime` 报 `ValueError`。

## 小结

* `time.time()` 是从 1970-01-01 00:00:00 UTC 起的秒数
* `time.sleep(n)` 让程序停 n 秒
* `ctime`、`strftime` 把时间印成字符串；`strptime` 把字符串拆回来
* 东八区要把 UTC 加上 8 小时才是本地钟点
* 加减天数用 `datetime` 和 `timedelta`

下一节学习 [文件处理](file.md)。用 `python examples/time_demo.py` 运行本节的例子。
