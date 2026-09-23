# 字典 dict

## 为什么需要字典

列表和元组用「位置」来找值：想知道第 3 个元素是谁，得写 `l[2]`。可位置这东西不好记，过两天就忘了下标 2 存的是什么。

可有些数据天然就是「一对一」的：

~~~
姓名 → 成绩
科目 → 分数
商品 → 价格
~~~

用列表装也不是不行，但要装两份、还得自己保证顺序对齐：

~~~
names = ["Jike", "Anna"]
scores = [90, 85]
print(names[1], scores[1])
~~~

~~~
Anna 85
~~~

数据一多，两份列表很容易对不上号，删一个还得两边都删。

这种「名字 → 值」的对应关系，Python 里用**字典**（dict）来装。名字叫做 **key**，值叫做 **value**。

## 建立字典和取值

用花括号 `{}` 建立。空字典写成 `d = {}`。

~~~
d = {}
d["a"] = 1
d["b"] = 3
print(d)
~~~

~~~
{'a': 1, 'b': 3}
~~~

也可以在建立时直接写好，冒号左边是 key，右边是 value：

~~~
score = {"Jike": 90, "Anna": 85}
print(score["Jike"])
~~~

~~~
90
~~~

取值和列表一样用方括号，但括号里放的是 **key 的名字**，不是下标。

## key 不存在会怎样

取一个没有的 key，会报 `KeyError`：

~~~
score = {"Jike": 90}
print(score["Tom"])
~~~

~~~
KeyError: 'Tom'
~~~

报错信息直译过来就是「找不到 Tom 这个 key」。不想报错，用 `get`：

~~~
score = {"Jike": 90}
print(score.get("Tom"))
print(score.get("Tom", 0))
~~~

~~~
None
0
~~~

`get` 找不到时返回 `None`；给了第二个参数，就返回这个默认值。后面处理数据时 `get` 比方括号安全得多。

## 遍历

最常用的是 `items()`，一次取出 key 和 value：

~~~
d = {}
d["a"] = 1
d["b"] = "hello"
d["name"] = "Jike"
d["age"] = 21

for k, v in d.items():
    print(k, v)
~~~

~~~
a 1
b hello
name Jike
age 21
~~~

只想拿 key，用 `keys()`：

~~~
for k in d.keys():
    print(k, d[k])
~~~

~~~
a 1
b hello
name Jike
age 21
~~~

只想要值，用 `values()`：

~~~
for v in d.values():
    print(v)
~~~

Python 3 里 `d.keys()` 不是列表，而是一个**视图**，会跟着字典变。所以它不能像列表那样按下标取，但直接拿来循环完全可以。真需要列表时，用 `list(d.keys())` 转一下。

## 追加、更新和删除

给一个已存在的 key 赋值，就是改它的值：

~~~
d = {"a": 1}
d["a"] = 100
print(d)
~~~

~~~
{'a': 100}
~~~

给一个不存在的 key 赋值，就是新增一项：

~~~
d = {"a": 1}
d["b"] = 2
print(d)
~~~

~~~
{'a': 1, 'b': 2}
~~~

`update` 可以把另一个字典整个合进来，相同的 key 会被后写入的值覆盖：

~~~
d = {"a": 1, "name": "Jike", "age": 21}
b = {"g": [1, 2, 3], "a": 2}
d.update(b)
print(d)
~~~

~~~
{'a': 2, 'name': 'Jike', 'age': 21, 'g': [1, 2, 3]}
~~~

注意 `"a"` 从 1 变成了 2。

`del` 按 key 删掉一整项：

~~~
d = {"a": 1, "b": "hello"}
del d["b"]
print(d)
~~~

~~~
{'a': 1}
~~~

还有一个 `pop`，删的同时把值返回：

~~~
d = {"a": 1, "b": 2}
v = d.pop("a")
print(v)
print(d)
~~~

~~~
1
{'b': 2}
~~~

## 判断 key 在不在

用 `in`，判断的是 key，不是 value：

~~~
score = {"Jike": 90}
print("Jike" in score)
print("Tom" in score)
~~~

~~~
True
False
~~~

写程序时常见的安全写法是先判断再取：

~~~
score = {"Jike": 90}
if "Tom" in score:
    print(score["Tom"])
else:
    print("没有 Tom 的成绩")
~~~

## key 有什么要求

key 必须是**不可变**的类型：字符串、数字、元组都行。列表不行。

~~~
d = {}
d[[1, 2]] = "x"
~~~

~~~
TypeError: unhashable type: 'list'
~~~

报错里 `unhashable` 的意思是「不能算出哈希值」，换成白话说就是「列表会变，不能拿它当名字」。上一节 [元组](tuple.md) 讲的不可变特性，在这里正好用得上。

value 则可以是任何类型，列表、字典、另一个字典都没问题：

~~~
d = {"g": [1, 2, 3], "info": {"age": 21}}
print(d)
~~~

## 顺序

Python 3.7 以后，字典默认按**插入顺序**排列，3.12 里也是这样。上面所有例子的输出顺序，就是当初写进去的顺序。

不过顺序不该被拿来当逻辑用。要靠顺序就说明该用列表；字典的价值在于「按名字找」，不在「按位置找」。

## 和列表怎么选

一句话：**按位置找用列表，按名字找用字典。**

~~~
# 一队人按顺序排队，用列表
queue = ["Jike", "Anna", "Tom"]

# 每个人对应一个成绩，用字典
score = {"Jike": 90, "Anna": 85, "Tom": 78}
~~~

## 小结

* 字典装「key → value」，key 是名字，value 是值
* `d["a"] = 1` 新增或修改；`del d["a"]` 删除；`d.pop("a")` 删除并返回
* 取值用 `d["a"]`，key 不存在会报 `KeyError`；不确定就用 `d.get("a", 默认值)`
* 遍历用 `d.items()` 一次拿 key 和 value，`keys()` / `values()` 只拿一边
* `in` 判断的是 key 存不存在
* key 必须不可变：字符串、数字、元组可以，列表不行
* Python 3.12 里字典按插入顺序排列
* 选择依据：按位置找用列表，按名字找用字典

用 `python examples/dict.py` 运行本节的例子。
