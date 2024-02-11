from string import ascii_lowercase


def extract_func(text):
    current_num = [num for num in text if num.isdigit()]
    result = 0

    for i in range(len(text)):
        if text[i].isalpha():
            index = ascii_lowercase.index(text[i].lower()) + 1

            if i == 0:
                if text[i] == text[i].lower():
                    result = int(''.join(current_num)) * index
                else:
                    result = int(''.join(current_num)) / index
            else:
                if text[i] == text[i].lower():
                    result += index
                else:
                    result -= index

    return result


def letters_change_numbers(data):
    result = 0

    for num in data:
        result += extract_func(num)

    print(f'{result:.2f}')


data = input().split()
letters_change_numbers(data)


# from string import ascii_lowercase
#
# word = input().split()
# result = 0
# total_sum = 0
#
# for text in word:
#     current_num = [num for num in text if num.isdigit()]
#
#     for i in range(len(text)):
#         if text[i].isalpha():
#             index = ascii_lowercase.index(text[i].lower()) + 1
#             if i == 0:
#                 if text[i] == text[i].lower():
#                     result = int(''.join(current_num)) * index
#                 else:
#                     result = int(''.join(current_num)) / index
#             else:
#                 if text[i] == text[i].lower():
#                     result += index
#                 else:
#                     result -= index
#
#     total_sum += result
#
# print(f"{total_sum:.2f}")


# from string import ascii_lowercase
#
# word = input().split()
# result = 0
# total_sum = 0
#
# for text in word:
#     current_num = [num for num in text if num.isdigit()]
#
#     index_one = ascii_lowercase.index(text[0].lower()) + 1
#     index_two = ascii_lowercase.index(text[-1].lower()) + 1
#
#     if text[0] == text[0].lower():
#         result = int(''.join(current_num)) * index_one
#     else:
#         result = int(''.join(current_num)) / index_one
#     if text[-1] == text[-1].lower():
#         result += index_two
#     else:
#         result -= index_two
#
#     total_sum += result
#
# print(f"{total_sum:.2f}")
