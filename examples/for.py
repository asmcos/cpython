# for 循环

print("--- 遍历列表 ---")
names = ["tom", "jerry", "spike"]
for name in names:
    print(name)

print("--- 缩进 ---")
l1 = ["a", "b", "c"]
for i in l1:
    print(i)
print("结束")

print("--- 字符串 ---")
for ch in "hi":
    print(ch)

print("--- 按下标 ---")
l2 = ["2", "a", 1, "d"]
for i in range(0, 4):
    print(l2[i])

print("--- 直接遍历 ---")
for item in l2:
    print(item)

print("--- enumerate ---")
for i, item in enumerate(l2):
    print(i, item)

print(type(enumerate(l2)))
print(list(enumerate(["a", "b"])))

print("--- enumerate 字符串、元组、range、字典 ---")
for i, ch in enumerate("hi"):
    print(i, ch)

for i, n in enumerate((10, 20)):
    print(i, n)

for i, n in enumerate(range(3, 6)):
    print(i, n)

score = {"Jike": 90, "Anna": 85}
for i, name in enumerate(score):
    print(i, name, score[name])

print("--- enumerate 从 1 编号 ---")
for i, item in enumerate(l2, start=1):
    print(i, item)

print("--- 累加 ---")
total = 0
for n in [10, 20, 30]:
    total = total + n
print(total)

print("--- 嵌套 ---")
for i in range(1, 3):
    for j in range(1, 3):
        print(i, j)

print("--- break ---")
for n in [1, 2, 3, 4, 5]:
    if n == 3:
        break
    print(n)

print("--- continue ---")
for n in [1, 2, 3, 4, 5]:
    if n == 3:
        continue
    print(n)

print("--- for else：没有 break ---")
for n in [1, 3, 5]:
    if n % 2 == 0:
        print("找到偶数", n)
        break
else:
    print("全是奇数")

print("--- for else：被 break ---")
for n in [1, 4, 5]:
    if n % 2 == 0:
        print("找到偶数", n)
        break
else:
    print("全是奇数")

print("--- while ---")
n = 3
while n > 0:
    print(n)
    n = n - 1
print("停")

print("--- 循环变量还在 ---")
for i in range(3):
    print(i)
print("最后", i)

print("--- 遍历时删除会跳过 ---")
nums = [2, 4, 6]
for n in nums:
    nums.remove(n)
print(nums)
