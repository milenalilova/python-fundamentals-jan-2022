def factorial(num):
    return 1 if num == 0 or num == 1 else num * factorial(num - 1)


num_a = int(input())
num_b = int(input())
result = factorial(num_a) / factorial(num_b)
print(f"{result:.2f}")



# def factorial_division(a, b):
#     factorial_a = 1
#     factorial_b = 1
#
#     for i in range(1, a + 1):
#         factorial_a *= i
#
#     for j in range(1, b + 1):
#         factorial_b *= j
#
#     result = f'{factorial_a / factorial_b:.2f}'
#     return result
#
#
# current_a = int(input())
# current_b = int(input())
# print(factorial_division(current_a, current_b))
