numbers = input().split(' ')
abs_numbers = []

for num in numbers:
    abs_numbers.append(abs(float(num)))

print(abs_numbers)


# Variant 2

# def absolute_values(string):
#     abs_values = []
#     for num in string:
#         abs_values.append(abs(float(num)))
#     return abs_values


# current_string = input().split(' ')
# print(absolute_values(current_string))
