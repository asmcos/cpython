# if 判断

print("--- 条件成立 ---")
a = 5
if a > 1:
    print(a)

print("--- 缩进 ---")
a = 5
if a > 1:
    b = a
    print(b)

c = b
print(c)

print("--- 比较 ---")
print(1 == 1)
print(1 != 2)
print(5 > 1)

score = 75
print(60 <= score < 90)
print("3" == 3)

print("--- and or not ---")
age = 20
print(age >= 18 and age < 60)
print(age < 18 or age >= 60)
print(not age >= 18)

age = 20
score = 80
if age >= 18 and score >= 60:
    print("可以报名")
else:
    print("不能报名")

age = 16
score = 80
if age >= 18 and score >= 60:
    print("可以报名")
else:
    print("不能报名")

day = "周六"
if day == "周六" or day == "周日":
    print("休息")
else:
    print("上课")

day = "周一"
if day == "周六" or day == "周日":
    print("休息")
else:
    print("上课")

logged_in = False
if not logged_in:
    print("请先登录")

print("--- in ---")
if "a" in ["a", "b"]:
    print("在里面")

print("--- elif ---")
score = 75
if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("不及格")

print("--- elif 顺序 ---")
score = 95
if score >= 60:
    print("及格")
elif score >= 90:
    print("优秀")
else:
    print("不及格")

print("--- 空值当作假 ---")
name = ""
if name:
    print(name)
else:
    print("名字是空的")

name = "Jike"
if name:
    print(name)

print("--- 和 for 配合 ---")
scores = [58, 76, 90, 61]
passed = 0
for score in scores:
    if score >= 60:
        passed = passed + 1
print(passed)

print("--- while 里的 if ---")
n = 1
while n <= 4:
    if n % 2 == 0:
        print(n, "偶数")
    else:
        print(n, "奇数")
    n = n + 1

print("--- while 条件里的 and ---")
n = 0
while n < 5 and n != 3:
    print(n)
    n = n + 1

print("--- 条件表达式 ---")
score = 75
text = "及格" if score >= 60 else "不及格"
print(text)

print("--- match ---")
op = "+"
match op:
    case "+":
        print(1 + 2)
    case "-":
        print(1 - 2)
    case _:
        print("未知运算")
