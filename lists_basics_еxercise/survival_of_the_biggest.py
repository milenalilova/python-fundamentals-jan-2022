nums = input().split(' ')
copy_nums = list(map(int, nums))
count = int(input())

for _ in range(count):
    concurrent_min_element = min(copy_nums)
    nums.remove(str(concurrent_min_element))
    copy_nums.remove(concurrent_min_element)

print(', '.join(nums))
