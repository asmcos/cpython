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

show("类型判断 isinstance")
print(isinstance(12, int))
print(isinstance("12", int))
print(isinstance(3.14, float))


def fmt(v):
    if isinstance(v, (int, float)):
        return round(v, 2)
    return v


print(fmt(3.14159))
print(fmt("abc"))

show("map / filter")
prices = ["10.5", "11.2", "10.8"]
nums = list(map(float, prices))
print(nums)

nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

show("排序和判断")
print(sorted([3, 1, 2]))
print(sorted(["banana", "apple"], key=len))
print(all([True, True, False]))
print(any([False, True, False]))

show("金融场景：批处理价格")
prices = ["10.5", "9.8", "11.2", "10.8", "9.5"]
nums = list(map(float, prices))
above = list(filter(lambda x: x > 10, nums))
print(nums)
print(above)
print(sum(above))
