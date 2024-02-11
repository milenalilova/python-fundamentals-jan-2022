numbers = list(map(int, input().split(' ')))
average = sum(numbers) / len(numbers)
greater = list()
final_list = list()
no_greater = False

for num in numbers:
    if num > average:
        greater.append(num)
        greater.sort()
        greater.reverse()
        final_list = greater[0:5]

if not greater:   # OR if len(greater)==0
    print('No')
else:
    print(' '.join(map(str, final_list)))   # OR print(*final_list[:5])

