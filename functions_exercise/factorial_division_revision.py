# n = int(input())
# result = 1
# for i in range(1, n + 1):
#     result *= i
# print(result)


def factorial_division(a, b):
    factorial_a = 1
    factorial_b = 1

    for i in range(1, a + 1):
        factorial_a *= i

    for j in range(1, b + 1):
        factorial_b *= j

    result = f'{factorial_a / factorial_b:.2f}'
    return result


current_a = int(input())
current_b = int(input())
print(factorial_division(current_a, current_b))
