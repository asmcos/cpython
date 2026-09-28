# for 循环

`for` 用来把同一段代码重复执行。列表、字符串、字典、[range](range.md) 都可以交给它逐个处理。

Python 用缩进表示代码块，相当于其他语言的 `{}`。`for` 那一行以冒号结尾，下面缩进的几行才是循环体。

## 为什么需要循环

三个名字要各打印一次，可以写成三行：

~~~
print("tom")
print("jerry")
print("spike")
~~~

名字变成三十个，就要复制三十行。人会抄错，以后改格式还得改三十处。

循环只写一遍“拿到一个，就打印一个”，数据放在列表里，个数变了也不用改循环本身：

~~~
names = ["tom", "jerry", "spike"]
for name in names:
    print(name)
~~~

~~~
tom
jerry
spike
~~~

`for name in names` 的意思是：按顺序从 `names` 里取出每一个值，临时叫 `name`，然后执行缩进的代码。取完就停。

## 缩进决定循环体

~~~
l1 = ["a", "b", "c"]
for i in l1:
    print(i)
print("结束")
~~~

~~~
a
b
c
结束
~~~

`print(i)` 缩进了，所以打印三次。`print("结束")` 和 `for` 对齐，循环结束后只执行一次。

同一层要缩进同样多，推荐每层 4 个空格。少缩进、多缩进，或者空格和 Tab 混用，都会报 `IndentationError`。

循环体不能空着。暂时什么都不做，写 `pass`：

~~~
for i in l1:
    pass
~~~

## 字符串也会被逐个取出

`for` 不限于列表。字符串会按字符走：

~~~
for ch in "hi":
    print(ch)
~~~

~~~
h
i
~~~

元组和列表一样，按元素走。字典的遍历上一节 [字典](dict.md) 已经写过，最常用的是 `for k, v in d.items()`。

## 固定次数

次数事先知道，就配合 [range](range.md)。下面把列表按下标再走一遍：

~~~
l2 = ["2", "a", 1, "d"]
for i in range(0, 4):
    print(l2[i])
~~~

~~~
2
a
1
d
~~~

`range(0, 4)` 给出 0、1、2、3，正好是 `l2` 的合法下标。列表长度会变时，不要把 `4` 写死，用 `range(len(l2))`。

只是为了拿到元素时，直接遍历更短，也不用担心下标越界：

~~~
for item in l2:
    print(item)
~~~

~~~
2
a
1
d
~~~

## 下标和值一起拿：enumerate

既要位置又要元素，用 `enumerate`。它是内置函数，不是一种新语法。括号和 `print(...)`、`len(...)` 一样，表示在调用函数。

`for i, item in ...` 里的逗号才是语法：函数每次交出两个东西，这里把它们拆开，前一个叫 `i`，后一个叫 `item`。

~~~
for i, item in enumerate(l2):
    print(i, item)
~~~

~~~
0 2
1 a
2 1
3 d
~~~

直接打印函数的返回值，看到的不是列表，而是一个 enumerate 对象。要一次看完全部结果，用 `list()` 包一层。每一项是一个元组，里面是下标和元素：

~~~
print(type(enumerate(l2)))
print(list(enumerate(["a", "b"])))
~~~

~~~
<class 'enumerate'>
[(0, 'a'), (1, 'b')]
~~~

学习时用 `list()` 看结果即可。正式写循环时直接 `for i, item in enumerate(...)`，不必先转成列表。

### 括号里能放什么

第一个参数要能被 `for` 逐个取出。列表、字符串、元组、`range`、字典都可以。单独一个数字不行。

字符串按字符编号：

~~~
for i, ch in enumerate("hi"):
    print(i, ch)
~~~

~~~
0 h
1 i
~~~

元组、`range` 也一样，编号从 0 开始，跟元素自己的值无关：

~~~
for i, n in enumerate((10, 20)):
    print(i, n)

for i, n in enumerate(range(3, 6)):
    print(i, n)
~~~

~~~
0 10
1 20
0 3
1 4
2 5
~~~

`range(3, 6)` 产出的是 3、4、5。`enumerate` 另起一套编号 0、1、2，所以第一行是 `0 3`，不是 `3 3`。

字典放进去时，取出来的是 key，不是 value。编号表示这是第几个 key：

~~~
score = {"Jike": 90, "Anna": 85}
for i, name in enumerate(score):
    print(i, name, score[name])
~~~

~~~
0 Jike 90
1 Anna 85
~~~

要 key 和 value 一起走，仍用上一节的 `for name, value in score.items()`。`enumerate` 并不取代它。

整数没有“下一个元素”，传进去会报错：

~~~
print(enumerate(5))
~~~

~~~
TypeError: 'int' object is not iterable
~~~

集合虽然也能放进 `enumerate`，但集合没有固定的位置顺序，编出来的号不能当成列表下标用。

第二个参数 `start` 可以不写，用来指定编号从几开始，必须是整数。它只改变打印出来的编号，不改变列表里的真实下标。

~~~
for i, item in enumerate(l2, start=1):
    print(i, item)
~~~

~~~
1 2
2 a
3 1
4 d
~~~

## 在循环里累加

循环外面先准备一个变量，循环里面不断更新它。求三个数的和：

~~~
total = 0
for n in [10, 20, 30]:
    total = total + n
print(total)
~~~

~~~
60
~~~

`total` 必须写在循环外面。写在里面的话，每转一圈都会重新变成 0，前面加上的数就丢了。

`total = total + n` 也可以写成 `total += n`，两个写法一样。

## 循环里面再套循环

外层每走一步，内层都要完整走一遍。

~~~
for i in range(1, 3):
    for j in range(1, 3):
        print(i, j)
~~~

~~~
1 1
1 2
2 1
2 2
~~~

`i` 先取 1，这时 `j` 取 1 再取 2。然后 `i` 变成 2，`j` 再取 1 和 2。内层缩进比外层多一层。

## break 和 continue

有时不必走完。`break` 立刻结束整个循环，`continue` 跳过这一圈剩下的代码，直接进入下一圈。

这里用到了 `if`：条件成立才执行它下面的语句。`if` 的规则下一节再细讲。

~~~
for n in [1, 2, 3, 4, 5]:
    if n == 3:
        break
    print(n)
~~~

~~~
1
2
~~~

遇到 3 就停，4 和 5 不会再打印。

~~~
for n in [1, 2, 3, 4, 5]:
    if n == 3:
        continue
    print(n)
~~~

~~~
1
2
4
5
~~~

3 被跳过了，循环还在，所以 4 和 5 仍会打印。

## for 也可以带 else

`else` 写在整个 `for` 后面，和循环对齐。它在循环没有被 `break` 打断时执行。

~~~
for n in [1, 3, 5]:
    if n % 2 == 0:
        print("找到偶数", n)
        break
else:
    print("全是奇数")
~~~

~~~
全是奇数
~~~

三个数里没有偶数，`break` 没执行，所以走到 `else`。

~~~
for n in [1, 4, 5]:
    if n % 2 == 0:
        print("找到偶数", n)
        break
else:
    print("全是奇数")
~~~

~~~
找到偶数 4
~~~

4 触发了 `break`，`else` 就不执行。这个 `else` 表示“没被打断”，不是“循环一次都没跑”。

## while：条件成立就继续

`for` 适合“这一串东西，逐个处理”或者“次数已经知道”。还不知道要转几圈、只知道停下来的条件时，用 `while`。

~~~
n = 3
while n > 0:
    print(n)
    n = n - 1
print("停")
~~~

~~~
3
2
1
停
~~~

每次先看 `n > 0` 还成不成立。成立就执行循环体。这里每圈都把 `n` 减 1，减到 0 时条件不再成立，循环结束，然后打印“停”。

如果忘记写 `n = n - 1`，`n` 一直是 3，条件永远成立，程序就停不下来。这种循环叫死循环。终端里可以按 `Ctrl + C` 把它打断。

## 常见坑

**循环变量在循环结束后还在。** 它保留的是最后一圈的值。

~~~
for i in range(3):
    print(i)
print("最后", i)
~~~

~~~
0
1
2
最后 2
~~~

空序列一次都没进循环体时，这个变量不会被赋值，后面使用它会报 `NameError`。

**遍历列表时不要同时删元素。** 删除会让后面的元素往前移，循环仍按原来的步伐走，于是跳过一个。

~~~
nums = [2, 4, 6]
for n in nums:
    nums.remove(n)
print(nums)
~~~

~~~
[4]
~~~

三个偶数本来都想删掉，结果留下了 4。要删除时，先另做一个新列表，或者遍历 `nums[:]` 这份副本。

## 小结

* 冒号加缩进就是循环体，和 `for` 对齐的代码只在循环结束后执行一次
* 遍历列表、字符串，直接 `for item in ...`
* `enumerate` 是内置函数。括号里放列表、字符串、元组、`range`、字典这类能被 `for` 取出的对象，用来同时拿到编号和元素
* 累加用的变量要放在循环外面
* `break` 结束整个循环，`continue` 跳过本圈
* `for` 的 `else` 在没有 `break` 时执行
* 次数未知、只知道停止条件时用 `while`，记得让条件有机会变成不成立

下一节学习 [if 判断](if.md)。用 `python examples/for.py` 运行本节的例子。
