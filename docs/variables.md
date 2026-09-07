# 变量

变量就是给一个值起名字，后面用这个名字来使用它。

```
a = 1
price = 3.14
name = "jeapedu"
```

`a`、`price`、`name` 是名字，等号右边是值。`type()` 可以查看类型：

```
print(type(a))
print(type(price))
print(type(name))
```

```
<class 'int'>
<class 'float'>
<class 'str'>
```

这一节先把数字讲清楚：`int` 是整数，`float` 是小数。字符串下一节再展开。

## int 整数

整数就是没有小数点的数：`0`、`21`、`-7`。Python 3 的整数没有位数上限，多大都可以。

```
n = 21
print(n)
print(1_000_000)
```

`1_000_000` 和 `1000000` 一样，下划线只是方便读，不算进数值。

常用运算：

| 运算 | 写法 | 例子 | 结果 |
| --- | --- | --- | --- |
| 加 | `+` | `7 + 3` | `10` |
| 减 | `-` | `7 - 3` | `4` |
| 乘 | `*` | `7 * 3` | `21` |
| 除 | `/` | `7 / 3` | `2.333...`（`float`） |
| 整除 | `//` | `7 // 3` | `2` |
| 取余 | `%` | `7 % 3` | `1` |
| 乘方 | `**` | `2 ** 10` | `1024` |

注意：Python 3 里 `7 / 3` 的结果是小数 `2.333...`，类型变成 `float`。只要整数商，用 `//`。

```
print(7 / 3)
print(7 // 3)
print(type(7 / 3), type(7 // 3))
```

```
2.3333333333333335
2
<class 'float'> <class 'int'>
```

`abs(-5)` 取绝对值，结果是 `5`。

## float 小数

带小数点的就是浮点数：`3.14`、`0.5`、`-2.0`。也可以写科学计数法：`1.2e3` 是 `1200.0`。

```
x = 3.14
y = 1.2e3
print(x, y)
print(type(x))
```

```
3.14 1200.0
<class 'float'>
```

整数和小数一起算，结果一般是 `float`：

```
print(2 + 0.5)
print(type(2 + 0.5))
```

```
2.5
<class 'float'>
```

`float` 用二进制近似十进制小数，所以有些看起来该是整数的算式，会多出一点点误差。经典例子：

```
print(0.1 + 0.2)
```

```
0.30000000000000004
```

入门阶段记住：屏幕上打印出来的位数，不等于「算得完全精确」。需要几位小数时，用下面的方法自己指定。

## 小数点后面留几位

常用两种做法。一种是**改数值**：`round`。一种是**只改显示**：f-string 或 `format`。

### round：四舍五入到指定位数

`round(数值, 小数位数)`。第二个参数是小数点后面留几位。

```
pi = 3.1415926
print(round(pi, 2))
print(round(pi, 4))
print(round(2.5))
```

```
3.14
3.1416
2
```

只写一个参数时，`round(2.5)` 得到整数。Python 对 `.5` 采用「银行家舍入」（偏向偶数），所以 `round(2.5)` 是 `2`，`round(3.5)` 是 `4`。作业里需要「普通四舍五入」时，先知道有这个差别。

`round` 的结果拿来继续算：

```
amount = round(10.129, 2)
print(amount, type(amount))
```

```
10.13 <class 'float'>
```

### 只用来打印：f-string 和 format

不想改数值，只想打印时看到两位小数：

```
price = 10.1
print(f"{price:.2f}")
print(format(price, ".2f"))
print("{:.2f}".format(price))
```

```
10.10
10.10
10.10
```

`.2f` 表示：按小数（fixed point）显示，小数点后面 2 位。改成 `.3f` 就是 3 位。`f"..."` 是 Python 3.12 里最常用的写法。

注意：`print(f"{price:.2f}")` 打印出来是字符串样子的 `10.10`，`price` 本身还是 `10.1`。

```
price = 10.1
print(f"{price:.2f}")
print(price)
```

```
10.10
10.1
```

金融里打印金额常用两位小数：`f"{money:.2f}"`。先 `round` 再显示，数字和打印会一致一些。

## int 和 float 互相转换

转换用 `int()`、`float()`。经典教材都会单独练这组函数。

### 整数 ↔ 小数

```
print(float(3))
print(int(3.9))
print(int(-3.9))
```

```
3.0
3
-3
```

`float(3)` 得到 `3.0`，类型变成 `float`。`int(3.9)` **不是四舍五入**，而是直接去掉小数部分（向 0 截断）。要四舍五入成整数，用 `round(3.9)`，结果是 `4`。

```
print(int(3.9))
print(round(3.9))
```

```
3
4
```

### 字符串 ↔ 数字

`input()` 读进来的永远是字符串。要拿来做加减，必须先转成数字。

```
s = "21"
print(int(s) + 1)
print(float("3.14"))
print(str(3.14))
```

```
22
3.14
3.14
```

字符串里是小数时，不能直接 `int("3.14")`，会报 `ValueError`。先转 `float`，再转 `int`：

```
print(int(float("3.14")))
```

```
3
```

不是数字的字符串也不能转：

```
int("21元")
```

会报 `ValueError`。后面 [错误和异常](error_except.md) 再讲怎么接住这种错误。

### 小结

| 写法 | 含义 |
| --- | --- |
| `int(3.9)` | 去掉小数，得到 `3` |
| `round(3.9)` | 四舍五入到整数，得到 `4` |
| `float(3)` | 变成 `3.0` |
| `int("21")` | 数字字符串 → 整数 |
| `float("3.14")` | 数字字符串 → 小数 |
| `int(float("3.14"))` | 带小数点的字符串 → 先 float 再 int |
| `str(3.14)` | 数字 → 字符串 |
| `round(x, 2)` | 数值留 2 位小数 |
| `f"{x:.2f}"` | 打印时显示 2 位小数 |

## 综合例子

```
a = 1
b = 2
s1 = "abc"

print(a, b, s1)

s2 = str(a)
print(s2)

s3 = "435"
c = int(s3)
print(c + a)

price = 10.129
print(float(c))
print(int(price))
print(round(price, 2))
print(f"{price:.2f}")
print(type(a), type(price), type(s1))
```

## 执行结果

```
1 2 abc
1
436
435.0
10
10.13
10.13
<class 'int'> <class 'float'> <class 'str'>
```

用 `python examples/variables.py` 可以自己跑一遍。下一节学习 [字符串](string.md)。
