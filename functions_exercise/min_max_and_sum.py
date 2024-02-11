def min_max_sum(numbers):
    min_num = min(numbers)
    max_num = max(numbers)
    sum_nums = sum(numbers)

    print(f'The minimum number is {min_num}')
    print(f'The maximum number is {max_num}')
    print(f'The sum number is: {sum_nums}')


current_numbers = list(map(int, input().split(' ')))
min_max_sum(current_numbers)
