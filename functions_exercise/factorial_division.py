# def factorial(num):
#     f = 1
#     if num >= 1:
#         for i in range(1, num + 1):
#             f = f * i
#     return f
#
#
# num_a = int(input())
# num_b = int(input())
# result = factorial(num_a) / factorial(num_b)
# print(f'{result:.2f}')


def factorial(num):
    return 1 if num == 0 or num == 1 else num * factorial(num - 1)


num_a = int(input())
num_b = int(input())
result = factorial(num_a) / factorial(num_b)
print(f'{result:.2f}')
