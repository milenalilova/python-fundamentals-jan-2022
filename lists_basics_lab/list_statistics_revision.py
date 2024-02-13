n = int(input())
negatives_list = []
positives_list = []

for i in range(n):
    number = int(input())
    if number >= 0:
        positives_list.append(number)
    else:
        negatives_list.append(number)

positives_count = len(positives_list)
negatives_sum = sum(negatives_list)

print(positives_list)
print(negatives_list)

print(f"Count of positives: {positives_count}")
print(f"Sum of negatives: {negatives_sum}")
