#随机数

随机数是python自带的一个库（模块），一般安装好python就可以直接引用随机数模块了

# 引用

```
import random

a = random.randint(1,10)
```

a 是从1到10中任意一个数字，包含1和10。
也就是说可能会随机出1或者10来。

```
random.random()
```

会随机一个浮点数出来

# 随机选一个

```
random.choice(["a",1,43,544])
```

# 给列表乱序

```
l = ["432","hello",1,"a"]
random.shuffle(l)
print(l)
```

#结果

```
[1, '432', 'hello', 'a']
```
