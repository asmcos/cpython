# 正则

初学正则，不要一次记太多规则。先会「在一段文字里找某种样子的内容」。处理公告、交易流水、不规则文本时，正则非常有用。

```
import re
```

## 找所有匹配：findall

`findall` 找出所有匹配的子串，返回一个列表。

```
res = re.findall("cat", "The cat and the dog sat on the mat")
print(res)
```

```
['cat', 'cat']
```

这是在 `"The cat and the dog sat on the mat"` 里找出所有的 `cat`。

## 常用匹配符号

`cat` 和 `car` 前面两个字母一样，只有最后不同。想一次找出它们，可以用 `.` 表示"任意一个字符"：

```
print(re.findall("ca.", "cat and car"))
```

```
['cat', 'car']
```

`ca.` 先匹配固定的 `ca`，再用 `.` 匹配最后一个字符，所以 `cat`、`car` 都能对上。

`.` 还可以用在单词中间，例如 `o.` 表示 `o` 后面跟任意一个字符：

```
print(re.findall("o.", "good morning"))
```

```
['oo', 'or']
```

常用符号：

* `.` 匹配任意一个字符
* `\d` 匹配一个数字
* `\w` 匹配字母、数字或下划线（也匹配中文）

```
print(re.findall(r"\d\d", "qq:12345,phone:323"))
print(re.findall(r"\w\w", "qq:12345,phone:323"))
```

```
['12', '34', '32']
['qq', '12', '34', 'ph', 'on', '32']
```

建议写成原始字符串 `r"..."`，避免反斜杠被 Python 先吃掉。

`12345` 里最后的 `5` 后面没有数字了，所以按两位数字匹配时剩不下它。

## 个数：* + ?

* `*`：0 个或多个
* `+`：1 个或多个
* `?`：0 个或 1 个

```
print(re.findall(r":\d*", "qq:12345"))
print(re.findall(r":\d*", "qq:"))
```

```
[':12345']
[':']
```

`*` 允许数字一个都没有，所以单独的 `:` 也能匹配上。

```
print(re.findall(r":\d+", "qq:12345"))
print(re.findall(r":\d+", "qq:"))
```

```
[':12345']
[]
```

`+` 至少要有 1 个数字。

```
print(re.findall(r":\d?", "qq:12345"))
print(re.findall(r":\d?", "qq:"))
```

```
[':1']
[':']
```

`?` 最多再跟 1 个数字。

## 找第一个匹配：search

`findall` 找全部，`search` 只找第一个，返回一个匹配对象（match object），不是字符串。用 `.group()` 取到匹配到的内容：

```
m = re.search(r"\d+", "价格是 58 元")
print(m)
print(m.group())
```

```
<re.Match object; span=(3, 5), match='58'>
58
```

匹配不到时 `search` 返回 `None`：

```
m = re.search(r"\d+", "没有数字")
print(m)
```

```
None
```

所以用 `search` 前，先判断是不是 `None`：

```
m = re.search(r"\d+", "价格是 58 元")
if m:
    print("找到:", m.group())
else:
    print("没找到数字")
```

## 替换：sub

`sub(模式, 替换成什么, 文本)` 把匹配到的内容替换掉，返回新字符串：

```
print(re.sub(r"\d+", "XX", "订单 123 价格 45"))
```

```
订单 XX 价格 XX
```

清理文本里的多余内容（比如把股票代码里的空格去掉）：

```
print(re.sub(r"\s", "", "SH 600600"))
```

```
SH600600
```

`\s` 匹配空白（空格、换行、Tab）。

## 切分：split

`split(模式, 文本)` 按匹配到的位置切开，返回列表：

```
print(re.split(r"[,;]", "10,20;30,40"))
```

```
['10', '20', '30', '40']
```

`,` 或 `;` 都可以作为分隔点。普通的 `"10,20".split(",")` 只能按一种分隔符切，`re.split` 可以按一组模式切。

## 分组：括号

用 `()` 把要单独取出来的部分圈起来。`findall` 遇到括号时，只返回括号里的内容：

```
print(re.findall(r"(\d+)元", "苹果5元，梨3元"))
```

```
['5', '3']
```

整个模式是 `\d+元`，但只把 `\d+` 那部分取出来，所以结果里没有"元"字。用 `search` + 多个分组，可以同时取出几个字段：

```
m = re.search(r"(\d+)年(\d+)月", "成立于2020年6月")
print(m.group(1))   # 第一个括号
print(m.group(2))   # 第二个括号
```

```
2020
6
```

## 金融场景：从交易流水里提取信息

假设一段记录里有成交金额和数量，用分组一次性取出来：

```
line = "买入 600600 数量2000 价格39.95"
m = re.search(r"数量(\d+)\s+价格([\d.]+)", line)
if m:
    qty = int(m.group(1))
    price = float(m.group(2))
    print(f"数量 {qty}，价格 {price}，金额 {qty * price:.2f}")
```

```
数量 2000，价格 39.95，金额 79900.00
```

`[\d.]+` 表示数字或小数点出现 1 次以上，用来匹配 `39.95` 这种带小数的价格。`\s+` 表示一个或多个空白。

## 小结

* `findall` 找全部，返回列表；`search` 找第一个，返回 match 对象（用 `.group()` 取值）
* `.` 任意字符，`\d` 数字，`\w` 数字或字母，`\s` 空白
* `*` 0 或多个，`+` 1 或多个，`?` 0 或 1 个
* `sub` 替换，`split` 切分
* `()` 分组：`findall` 只取括号内容，`search` 用 `m.group(n)` 取第 n 个括号
* 原始字符串 `r"..."` 避免反斜杠被转义
* 用 `search` 前先判断返回是不是 `None`

用 `python examples/re_demo.py` 运行本节的例子。下一节学习 [常用内置函数](built_in_func.md)。
