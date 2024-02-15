def round_nums(nums_list: list):
    rounded_list = []
    for num in nums_list:
        rounded_list.append(round(float(num)))
    return rounded_list


current_nums = input().split(' ')
print(round_nums(current_nums))


# nums_list = input().split(' ')
# rounded_list = []

# for num in nums_list:
#     rounded_list.append(round(float(num)))

# print(rounded_list)


