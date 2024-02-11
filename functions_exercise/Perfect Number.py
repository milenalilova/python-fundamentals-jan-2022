# number = int(input())
# div_sum = 0
# is_perfect = False
#
# for num in range(1, number + 1):
#     result = number % num
#     if result == 0:
#         div_sum += num
#     perfect_num = div_sum / 2
#     if perfect_num == number:
#         is_perfect = True
#
# if is_perfect:
#     print('We have a perfect number!')
# else:
#     print("It's not so perfect.")


def perfect_number(number):
    id_perfect = False
    perfect_sum = 0

    for num in range(1, number + 1):
        result = number % num
        if result == 0:
            perfect_sum += num
    if perfect_sum / 2 == number:
        print('We have a perfect number!')
    else:
        print("It's not so perfect.")


current_number = int(input())
perfect_number(current_number)
