#coding:utf-8
s = "abcdefghijkl"

print(s[1])
print(s[5])
print(s[1:5])

""" 切片的第三个参数 """

print (s[0:5:1])
print (s[0:5:2])
print (s[0:5:3])


print ("特殊参数")
print (s[:5])
print (s[0:])
print (s[:])

s1="hello"
print ("s1的长度%d" % len(s1))
"""
len(s1) = 5
最后一个下标是 4 ，因为从0开始
"""
print (s1[4])

""" 这里是不包含最后一个 o 的 """
print (s1[0:4])

""" 切片可以支持 大于长度的值，但是结果 还是取总长度"""

print (s1[0:10])



""" 反序切片 """
print ("反序切片")
print (s[5:0:-1])
