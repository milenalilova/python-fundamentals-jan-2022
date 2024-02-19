numbers = list(map(int, input().split(', ')))

new_numbers = [num for num in numbers if num != 0]
zeros_list = [num for num in numbers if num == 0]
new_numbers.extend(zeros_list)

print(new_numbers)


# Variant 2
# numbers = list(map(int, input().split(', ')))

# new_numbers = []
# zeros_list = []

# for num in numbers:
#     if num != 0:
#         new_numbers.append(num)
#     else:
#         zeros_list.append(num)
# new_numbers.extend(zeros_list)

# print(new_numbers)


# Variant 3
# numbers = list(map(int, input().split(', ')))

# new_numbers = [num for num in numbers if num != 0]
# zeros = len(numbers) - len(new_numbers)

# if zeros > 0:
#     zeros_list = [0] * zeros
#     new_numbers.extend(zeros_list)

# print(new_numbers)


# Variant 4
# numbers = list(map(int, input().split(', ')))

# new_numbers = [num for num in numbers if num != 0]
# zeros = len(numbers) - len(new_numbers)

# if zeros > 0:
#     for zero in range(zeros):
#         new_numbers.append(0)

# print(new_numbers)


# Variant 5
# numbers = list(map(int, input().split(', ')))
# for i in range(len(numbers)-1, -1, -1):
#     if numbers[i] == 0:
#         zero = numbers.pop(i)
#         numbers.append(zero)
# print(numbers)
