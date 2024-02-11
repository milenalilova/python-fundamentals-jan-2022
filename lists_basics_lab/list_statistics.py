n = int(input())

positives = []
negatives = []
positives_count = 0
negatives_sum = 0

for num in range(n):
    number = int(input())

    if number >= 0:
        positives.append(number)
        positives_count += 1
    else:
        negatives.append(number)
        negatives_sum += number
print(positives)
print(negatives)
print(f"Count of positives: {positives_count}")
print(f"Sum of negatives: {negatives_sum}")
