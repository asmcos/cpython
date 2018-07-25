# time

时间库，我是用的最多的是下面的几个用法

```
import time
In [3]: time.time()
Out[3]: 1532510243.135594

In [4]: time.sleep(1)

In [5]: time.ctime()
Out[5]: 'Wed Jul 25 17:17:34 2018'

In [6]: time.sleep(1)

In [7]: time.ctime()
Out[7]: 'Wed Jul 25 17:17:42 2018'
```

time() 获取unix 时间戳，这是小数点前面的是 秒：1532510243秒。

sleep(n) 延时n秒

ctime()  年月日
