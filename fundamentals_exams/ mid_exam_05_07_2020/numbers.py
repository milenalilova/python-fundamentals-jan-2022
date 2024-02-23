sequence = [int(num) for num in input().split(' ')]
average_value = sum(sequence) / len(sequence)

above_average_nums = [num for num in sequence if num > average_value]
above_average_nums = sorted(above_average_nums)
above_average_nums.reverse()

if not above_average_nums:
    print("No")
elif len(above_average_nums) <= 5:
    print(' '.join(map(str, above_average_nums)))
elif len(above_average_nums) > 5:
    above_average_nums = above_average_nums[:5]
    print(' '.join(map(str, above_average_nums)))
