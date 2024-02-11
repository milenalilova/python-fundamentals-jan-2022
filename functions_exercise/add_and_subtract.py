def sum_numbers(a, b):
    return a + b


def subtract(sums, c):
    return sums - c


a, b, c = int(input()), int(input()), int(input())
result = subtract(sum_numbers(a, b), c)
print(result)
