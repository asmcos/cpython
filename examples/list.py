# 列表基础

names = ["tom", "jerry", "spike"]
print(names)

l1 = [1, 2, 3, 4]
print(l1[0])
print(l1[3])
print(l1[-1])
print(l1[-2])

l2 = ["abc", "1", "hello", 1]
print(l2[0])
print(l2[-1])

print("--- 修改元素 ---")

nums = [1, 2, 3]
nums[0] = 100
print(nums)

print("--- 切片 ---")

l = [1, 2, 3, 4, 5]
print(l[1:3])
print(l[:2])
print(l[2:])
print(l[:])

print("--- 长度和遍历 ---")

l = ["tom", "jerry", "spike"]
print(len(l))

for name in l:
    print(name)

for i, name in enumerate(l):
    print(i, name)

print("--- 判断存在 ---")

print("tom" in l)
print("bob" in l)

print("--- 排序 ---")

nums = [3, 1, 2]
print(sorted(nums))
print(nums)

nums.sort()
print(nums)
print(sorted(nums, reverse=True))

print("--- 列表推导式 ---")

squares = [x * x for x in range(5)]
print(squares)

odds = [x for x in range(10) if x % 2 == 1]
print(odds)

print("--- 合并和重复 ---")

print([1, 2] + [3, 4])
print([0] * 3)

print("--- 常见坑 ---")

a = [1, 2, 3]
part = a[:2]
part[0] = 100
print(part)
print(a)

a = [1, 2, 3]
b = a
b.append(4)
print(a)