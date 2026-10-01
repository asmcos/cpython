# 文件处理：open / write / read / seek / close / with
# 脚本会自己创建 test.txt 等临时文件，跑完会删掉。

import os
from pathlib import Path


def clean_up(*names):
    for name in names:
        p = Path(name)
        if p.exists():
            p.unlink()


print("--- write: 写入 ---")
f = open("test.txt", "w", encoding="utf-8")
n = f.write("hello world\n")
print("write 返回字符数:", n)
f.write("i am a boy\n")
f.write("i am very happy\n")
print("指针位置 tell():", f.tell())
f.close()

print("--- read: 读取 ---")
f = open("test.txt", encoding="utf-8")
print("read(5):", repr(f.read(5)))
print("tell():", f.tell())
print("readline():", repr(f.readline()))
f.close()

print("--- seek: 移动指针 ---")
f = open("test.txt", encoding="utf-8")
f.seek(0)
print("seek(0) 后 read(5):", repr(f.read(5)))
f.seek(0, 2)
print("seek(0,2) 即文件末尾 tell():", f.tell())
f.close()

print("--- readlines / for 逐行 ---")
f = open("test.txt", encoding="utf-8")
lines = f.readlines()
print("readlines:", lines)
f.close()

f = open("test.txt", encoding="utf-8")
for line in f:
    print("line:", line.strip())
f.close()

print("--- 追加模式 'a' ---")
f = open("a.txt", "a", encoding="utf-8")
print("追加时 tell():", f.tell())
f.write("!")
f.close()
print("a.txt 内容:", repr(open("a.txt", encoding="utf-8").read()))

print("--- with ... as f ---")
with open("test.txt", encoding="utf-8") as f:
    data = f.read()
print("with 外 f.closed:", f.closed)
print("data 前几行:", data.splitlines()[:2])

print("--- pathlib ---")
p = Path("test.txt")
print("exists():", p.exists())
print("read_text 首行:", p.read_text(encoding="utf-8").splitlines()[0])

clean_up("test.txt", "a.txt", "lines.txt", "cn.txt", "b.txt")
print("--- 清理完成 ---")
