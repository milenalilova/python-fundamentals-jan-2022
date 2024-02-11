# input_list = input().split(' ')
# rounded_list = list()
#
# for num in input_list:
#     round_num = round(float(num))
#     rounded_list.append(round_num)
#
# print(rounded_list)


def convert_list(base_list):
    final_list = list()
    for n in base_list:
        final_n = round(float(n))
        final_list.append(final_n)
    return final_list


input_list = input().split(' ')
print(convert_list(input_list))


# def convert_list(base_list, num_digits=0):      # rounding to the num_digits after the decimal
#     final_list = list()
#     for n in base_list:
#         final_n = round(float(n), num_digits)
#         final_list.append(final_n)
#     return final_list
#
#
# input_list = input().split(' ')
# current_round = int(input())
# print(convert_list(input_list, current_round))
