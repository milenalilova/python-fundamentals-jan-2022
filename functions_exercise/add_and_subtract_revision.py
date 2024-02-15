def sum_numbers(a, b):
    return a + b


def subtract(result, c):
    return result - c


a = int(input())
b = int(input())
c = int(input())

result = subtract(sum_numbers(a, b), c)
print(result)
