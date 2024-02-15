def smallest_number(first_int, second_int, third_int):
    ints_list = [first_int, second_int, third_int]
    min_number = min(ints_list)
    return min_number


current_first = int(input())
current_second = int(input())
current_third = int(input())

print(smallest_number(current_first, current_second, current_third))
