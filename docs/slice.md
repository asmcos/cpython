# 切片

字符串、列表、元组都能切片。写法是 `对象[起点:终点:步长]`。包含起点，不包含终点。

```
s = "abcdefghijkl"

print(s[1])
print(s[5])
print(s[1:5])
```

`s[1:5]` 取下标 1 到 4。

## 结果

```
b
f
bcde
```

## 第三个参数是步长

```
print(s[0:5:1])
print(s[0:5:2])
print(s[0:5:3])
```

## 结果

```
abcde
ace
ad
```

步长为 1 时和原来一样。步长为 2 表示隔一个取一个。`s[0:5:3]` 的结果是 `ad`。

## 省略写法

```
print(s[:5])
print(s[0:])
print(s[:])
```

起点不写表示从 0 开始，终点不写表示到末尾。

```
abcde
abcdefghijkl
abcdefghijkl
```

## 长度和下标

```
s1 = "hello"
print(f"s1的长度{len(s1)}")
print(s1[4])
print(s1[0:4])
print(s1[0:10])
```

`len(s1)` 是 5，最后一个下标是 4。`s1[0:4]` 不包含最后的 `o`。终点写得比长度大，也只取到末尾。

```
s1的长度5
o
hell
hello
```

## 反序切片

```
print(s[5:0:-1])
print(s[::-1])
```

`s[5:0:-1]` 是 `fedcb`，不包含 `s[0]`。`s[::-1]` 是整个字符串倒过来：`lkjihgfedcba`。
