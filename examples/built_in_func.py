# 常用内置函数：不需要 import 就能用


def show(name):
    print("-" * 12, name, "-" * 12)


show("查看和转换")
print(type(1))
print(len("hello"))
print(int("12"))
print(float("3.14"))
print(str(10))
print(bool(0), bool(1))

show("数字")
print(abs(-5))
print(round(3.14159, 2))
print(max(1, 9, 3))
print(min(1, 9, 3))
print(sum([1, 2, 3]))

show("遍历相关")
print(list(range(3)))
print(list(enumerate(["a", "b"])))
print(list(zip([1, 2], ["a", "b"])))

show("排序和判断")
print(sorted([3, 1, 2]))
print(sorted(["banana", "apple"], key=len))
print(all([True, True, False]))
print(any([False, True, False]))
