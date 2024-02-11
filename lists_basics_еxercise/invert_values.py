nums = input().split(' ')
opposites = []

for num in nums:
    opposites.append(-int(num))

print(opposites)


# nums = [-num if num > 0 else abs(num) for num in list(map(int, input().split(' ')))
#
# print(nums)
