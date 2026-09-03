# 错误和异常

有些代码不一定能执行成功。例如把不是数字的字符串转成整数：

```
print(int("567"))
print(int("56fdsa7"))
```

第一行得到 `567`。第二行会报错：

```
ValueError: invalid literal for int() with base 10: '56fdsa7'
```

程序如果不管这个错误，就会在这里停掉。

## try / except

把可能出错的语句放进 `try`，出错时执行 `except`：

```
try:
    print(int("56fdsa7"))
except ValueError:
    print("这不是一个整数")
```

结果是：

```
这不是一个整数
```

程序不会退出。`try` 里如果没有出错，`except` 不会执行。

入门阶段建议写上具体的异常类型，例如 `ValueError`、`FileNotFoundError`。不要养成空的 `except:` 什么都吞掉的习惯。

## 再看一个文件例子

```
try:
    with open("no_such_file.txt", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("文件不存在")
```

金融数据经常从文件或网络来，缺文件、格式不对都是常态。先学会接住错误，再继续算。
