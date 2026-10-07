# 随机数

`random` 是 Python 自带模块，装好 Python 就能用。模拟行情、抽样、做蒙特卡洛时会经常用到它。

```
import random
```

## 基础：整数和小数

```
a = random.randint(1, 10)
print(a)
```

`randint(1, 10)` 会在 1 到 10 里随机一个整数，**包含** 1 和 10。

```
print(random.random())
```

`random()` 随机一个 `0` 到 `1` 之间的小数，包含 0，不包含 1。

想要一个指定范围的小数，用 `uniform`：

```
print(random.uniform(0.5, 1.5))
```

`uniform(0.5, 1.5)` 随机一个 0.5 到 1.5 之间的小数。价格、收益率这类连续量常用它来模拟。

## 从序列里选

`choice` 从列表里随机选一个元素：

```
print(random.choice(["a", 1, 43, 544]))
```

`choices` 可以一次选多个，返回一个列表：

```
print(random.choices(["a", "b", "c"], k=3))
```

`k=3` 表示选 3 次，可能重复。例如：

```
['c', 'a', 'c']
```

`sample` 也一样选多个，但**不重复**，适合做抽样：

```
print(random.sample(range(1, 101), 5))
```

这是从 1 到 100 里不重复地抽 5 个数。做调查、抽检验样本时会用到。

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

注意 `shuffle` 没有返回值，它是原地修改。想要新列表而不是改原列表，用 `sample`：

```
l = [1, 2, 3, 4]
new = random.sample(l, len(l))
print(l)    # 原列表没变
print(new)  # 顺序打乱的新列表
```

## seed：让结果可复现

`seed` 固定随机数生成的起点。同一个 seed 之后，再生成的序列就一样了：

```
random.seed(7)
print(random.random())
print(random.random())
```

```
0.32383276483316237
0.1509...
```

再设一次同样的 seed，会得到同样的一串：

```
random.seed(7)
print(random.random())
print(random.random())
```

```
0.32383276483316237
0.1509...
```

对做实验、复现结果、调试很关键：想"每次结果都一样"时，在程序开头写一个固定的 `seed`。做蒙特卡洛模拟要随机性时，就**不要**设 seed，或用不同的值。

## 金融场景：模拟行情波动

随机数最典型的金融用法是模拟价格波动。下面模拟一只股票 5 个交易日的涨跌，每天按一个随机百分比波动：

```
import random

random.seed(1)
price = 10.0
for day in range(1, 6):
    change = random.uniform(-0.05, 0.05)  # 每天 -5% 到 +5%
    price = price * (1 + change)
    print(f"第{day}天: {price:.2f}")
```

```
第1天: 9.63
第2天: 9.97
第3天: 10.23
第4天: 9.98
第5天: 9.98
```

（不同 Python 版本下 `uniform` 的随机序列略有差异，你运行的结果可能和这里不完全一样，但都落在 ±5% 的波动范围内。）

把循环多跑几千次，就变成了最简单的蒙特卡洛模拟，可以估计某条路径下期末价格的范围。第二部分做量化入门时会用到。

## 小结

* `randint(a, b)`：a 到 b 之间的整数，包含两端
* `random()`：0 到 1 之间的小数
* `uniform(a, b)`：a 到 b 之间的小数
* `choice` 选一个，`choices` 可选多个（可重复），`sample` 选多个（不重复）
* `shuffle` 原地打乱列表；想要新列表用 `sample`
* `seed(n)` 固定随机起点，让结果可复现
* 模拟价格波动用 `uniform` + 循环，多次模拟就是蒙特卡洛

用 `python examples/rand_demo.py` 运行本节的例子。下一节学习 [正则](re.md)。
