import re

print(re.findall("l", "hello , world"))
print(re.findall("o.", "good morning"))
print(re.findall(r"\d\d", "qq:12345,phone:323"))
print(re.findall(r"\w\w", "qq:12345,phone:323"))
print(re.findall(r":\d*", "qq:12345"))
print(re.findall(r":\d+", "qq:12345"))
print(re.findall(r":\d?", "qq:12345"))
