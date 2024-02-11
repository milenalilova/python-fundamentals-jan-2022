numbers_list = list(map(int, input().split(', ')))

positive = list(str(num) for num in numbers_list if num >= 0)
negative = list(str(num) for num in numbers_list if num < 0)
even = list(str(num) for num in numbers_list if num % 2 == 0)
odd = list(str(num) for num in numbers_list if num % 2 != 0)

print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")
