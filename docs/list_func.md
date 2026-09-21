# 列表函数

上一节 [列表](list.md) 讲了怎么建立列表、按下标取值、切片和遍历。这一节讲列表的**常用方法**——也就是「往列表里加东西、删东西、改顺序」的办法。

方法的名字都写在列表变量后面，用小括号调用，例如 `l.append(1)`。列表本身是可变的，所以这些方法多数会**直接修改原列表**，不返回新列表。

## 先建一个空列表

新学一个方法时，习惯先建一个空列表，再一点点往里放，这样每一步都能看清结果。

~~~
l = []
print(l)
~~~

~~~
[]
~~~

## append：往末尾追加

`append` 把元素加到列表**最后面**。一次只能加一个，加什么类型都行。

~~~
l = []
l.append(1)
l.append("3243")
l.append("a")
l.append(["good", "morning"])
print(l)
~~~

~~~
[1, '3243', 'a', ['good', 'morning']]
~~~

上例最后一行把「另一个列表」也当作一个元素放了进去，所以结果里出现了嵌套的方括号。追加一个列表并不会把它的元素摊开。

## pop：删除并返回

`pop` 从末尾删掉一个元素，并把删掉的值**返回**出来。所以可以一边删、一边用。

~~~
l = [1, "3243", "a", ["good", "morning"]]

print(l.pop())
print(l)
~~~

~~~
['good', 'morning']
[1, '3243', 'a']
~~~

`pop()` 默认删最后一个。也可以指定下标，`l.pop(0)` 就是删除第一个。

~~~
l.pop(0)
print(l)
~~~

~~~
['3243', 'a']
~~~

## insert：在指定位置插入

`insert(下标, 值)` 把值插到指定位置，原来的元素依次往后挪。

~~~
l = [1, '3243', 'a']
l.insert(2, "insss")
print(l)
~~~

~~~
[1, '3243', 'insss', 'a']
~~~

`insert` 和 `append` 的区别：`append` 只能加在最后，`insert` 可以选位置。想加在最前面就写 `l.insert(0, 值)`。

## remove：按值删除

前面 `pop` 是按**下标**删。如果知道要删的值，用 `remove` 按**值**删。

~~~
nums = [1, 2, 3, 2]
nums.remove(2)
print(nums)
~~~

~~~
[1, 3, 2]
~~~

注意：列表里有两个 `2`，`remove` 只删**第一个**。如果值不存在，会报 `ValueError`。

## index 和 count：查找

`index` 找某个值第一次出现的下标，`count` 数某个值出现了几次。

~~~
nums = [10, 20, 30, 20]
print(nums.index(20))
print(nums.count(20))
~~~

~~~
1
2
~~~

## 排序：sort 和 sorted

`sort` 把原列表从小到大排好，**直接改原列表**。

~~~
nums = [3, 1, 2]
nums.sort()
print(nums)
~~~

~~~
[1, 2, 3]
~~~

如果不希望改动原来的列表，用 `sorted`，它**返回一个新列表**。

~~~
nums = [3, 1, 2]
print(sorted(nums))
print(nums)
~~~

~~~
[1, 2, 3]
[3, 1, 2]
~~~

两个函数都可以加 `reverse=True` 从大到小排。

~~~
print(sorted(nums, reverse=True))
~~~

~~~
[3, 2, 1]
~~~

`len(nums)` 看列表长度，`sum(nums)` 求和，也常和排序一起用。

## 小结

* `append` 往末尾加，`insert` 在指定位置加
* `pop` 按下标删并返回，`remove` 按值删
* `index` 找下标，`count` 数次数
* `sort` 改原列表，`sorted` 返回新列表
* 这些方法都直接改原列表（`sorted` 除外），改完记得看结果

完整例子见 `examples/list_func.py`。列表的建立、下标和切片见 [列表](list.md)。
