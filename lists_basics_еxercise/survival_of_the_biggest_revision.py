numbers = input().split(' ')
copy_numbers = list(map(int, numbers))
count_of_nums = int(input())

for i in range(count_of_nums):
    min_number = min(copy_numbers)
    copy_numbers.remove(min_number)
    numbers.remove(str(min_number))

print(', '.join(numbers))
