def max_min_sum(number):
    max_num = max(number)
    min_num = min(number)
    sum_nums = sum(number)

    print(f"The minimum number is {min_num}")
    print(f"The maximum number is {max_num}")
    print(f"The sum number is: {sum_nums}")


sequence = list(map(int, input().split(' ')))
max_min_sum(sequence)
