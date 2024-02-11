# def sort_numbers(numbers_list):
#     sort_nums = []
#
#     for num in numbers_list:
#         sort_nums.append(int(num))
#         sort_nums.sort()
#     return sort_nums
#
#
# current_numbers = input().split(' ')
# print(sort_numbers(current_numbers))


# OR use sorted()

result = sorted(list(map(int, input().split(' '))))
print(result)


# OR

def sort_func(nums):
    return sorted(nums)


numbers = sorted(list(map(int, input().split(' '))))
print(sort_func(numbers))
