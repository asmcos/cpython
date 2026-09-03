# 随机数

`random` 是 Python 自带模块，装好 Python 就能用。

```
import random

a = random.randint(1, 10)
print(a)
```

`randint(1, 10)` 会在 1 到 10 里随机一个整数，包含 1 和 10。

```
print(random.random())
```

`random()` 随机一个 `0` 到 `1` 之间的小数。

## 从列表里选一个

```
print(random.choice(["a", 1, 43, 544]))
```

## 打乱列表

```
l = ["432", "hello", 1, "a"]
random.shuffle(l)
print(l)
```

`shuffle` 会直接改原来的列表。每次运行顺序可能不同，例如：

```
[1, '432', 'hello', 'a']
```

后面做抽样、模拟行情波动时还会用到随机数。这一节先会这三个函数即可。
