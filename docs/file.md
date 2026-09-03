# 文件处理

读文件、写文件是日常编程里最常用的能力之一。

Python 3.12 推荐用 `with open(...) as f`。它会在用完后自动关闭文件，不容易忘记 `close()`。

## 读文件

假设 `test.txt` 内容是：

```
hello world
i am a boy
i am very happy
```

```
with open("test.txt", encoding="utf-8") as f:
    data = f.read()

print(data)
```

`encoding="utf-8"` 建议写上，中文文件在 Windows 上更不容易乱码。

`open` 的第一个参数是文件名，可以是相对路径或绝对路径。第二个常见参数是模式：

* `r`：读（默认）
* `w`：写，文件不存在就创建，存在就覆盖
* `a`：追加
* `r+`：读写，文件必须存在

## read 和 readlines

```
with open("test.txt", encoding="utf-8") as f:
    content = f.read()
```

`read()` 一次读完全部内容。再读一次就是空的。

按行读：

```
with open("test.txt", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines:
    print(line)
```

`lines` 是列表，每个元素是一行。

也可以直接循环文件对象：

```
with open("test.txt", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

## 写文件

```
with open("a.txt", "w", encoding="utf-8") as f:
    f.write("hello")
```

`"w"` 会覆盖旧文件。不想覆盖、只在末尾加内容，用 `"a"`。

## 路径

处理路径时，3.12 也可以用 `pathlib`：

```
from pathlib import Path

p = Path("test.txt")
print(p.exists())
print(p.read_text(encoding="utf-8"))
```

入门先把 `open` 写熟。`Path` 在后面做金融数据读写时会更方便。
