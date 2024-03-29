numbers = list(map(int, input().split(', ')))

positives = [str(num) for num in numbers if num >= 0]
negatives = [str(num) for num in numbers if num < 0]
evens = [str(num) for num in numbers if num % 2 == 0]
odds = [str(num) for num in numbers if num % 2 != 0]

print(f"Positive: {', '.join(positives)}")
print(f"Negative: {', '.join(negatives)}")
print(f"Even: {', '.join(evens)}")
print(f"Odd: {', '.join(odds)}")
