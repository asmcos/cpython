# 切片

s = "abcdefghijkl"

print("--- 取出一段 ---")
print(s[1])
print(s[5])
print(s[1:5])

print("--- 步长 ---")
print(s[0:5:1])
print(s[0:5:2])
print(s[0:5:3])
print(s[::2])
print(s[1::2])

print("--- 省略 ---")
print(s[:5])
print(s[5:])
print(s[:])

print("--- 负数下标 ---")
print(s[-3:])
print(s[:-3])
print(s[-5:-1])

print("--- 反序 ---")
print(s[5:0:-1])
print(s[::-1])
print(repr(s[5:0]))

print("--- 越界 ---")
s1 = "hello"
print(f"s1的长度{len(s1)}")
print(s1[4])
print(s1[0:4])
print(s1[0:10])
print(s1[-100:2])
print(repr(s1[100:200]))

print("--- 列表和元组 ---")
nums = [0, 1, 2, 3, 4]
print(nums[1:4])
print(nums[::2])

t = (0, 1, 2, 3, 4)
print(t[1:4])

print("--- 切片是新列表 ---")
a = [1, 2, 3, 4]
b = a[1:3]
b[0] = 100
print(b)
print(a)

print("--- 给切片赋值 ---")
nums = [0, 1, 2, 3, 4]
nums[1:3] = [8, 9]
print(nums)

nums = [0, 1, 2, 3, 4]
nums[1:4] = []
print(nums)

print("--- slice 函数 ---")
part = slice(1, 5)
print(s[part])
nums = [0, 8, 9, 3, 4]
print(nums[part])
print(part.start, part.stop, part.step)

print("--- 只复制了外层 ---")
a = [[1], [2], [3]]
b = a[:2]
b[0][0] = 9
print(a)
