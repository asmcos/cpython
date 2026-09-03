s = "abcdefghijkl"

print(s[1])
print(s[5])
print(s[1:5])

print(s[0:5:1])
print(s[0:5:2])
print(s[0:5:3])

print("特殊参数")
print(s[:5])
print(s[0:])
print(s[:])

s1 = "hello"
print(f"s1的长度{len(s1)}")
print(s1[4])
print(s1[0:4])
print(s1[0:10])

print("反序切片")
print(s[5:0:-1])
print(s[::-1])
