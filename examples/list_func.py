nums = [3, 1, 2]
print(nums)

nums.append(4)
print(nums)

nums.insert(0, 100)
print(nums)

last = nums.pop()
print(last, nums)

first = nums.pop(0)
print(first, nums)

nums.remove(2)
print(nums)

print(nums.index(1))
print(nums.count(1))

nums.extend([7, 8])
print(nums)

nums.reverse()
print(nums)

nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

copy_nums = nums.copy()
copy_nums.append(999)
print(nums)
print(copy_nums)

nums.clear()
print(nums)
