# range

print("--- 一个参数 ---")
print(list(range(5)))

print("--- 两个参数 ---")
a = range(0, 10)
print(a)
print(list(a))

b = range(2, 4)
print(list(b))

print("--- 步长 ---")
print(list(range(0, 10, 2)))
print(list(range(1, 10, 3)))

print("--- 含头不含尾 ---")
print(list(range(3, 8)))

print("--- range 不是列表 ---")
print(a)
print(type(a))

nums = range(2, 11, 3)
print(nums.start)
print(nums.stop)
print(nums.step)

print("--- 倒着数 ---")
print(list(range(10, 0, -1)))
print(list(range(10, -1, -2)))

print("--- 空的 range ---")
print(list(range(10, 0)))
print(list(range(5, 5)))

print("--- 长度、下标、成员 ---")
nums = range(0, 10)
print(len(nums))
print(nums[0])
print(nums[3])
print(nums[-1])
print(5 in range(0, 10))
print(10 in range(0, 10))

print("--- 和 for 一起用 ---")
for i in range(3):
    print(i)

names = ["tom", "jerry", "spike"]
for i in range(len(names)):
    print(i, names[i])
