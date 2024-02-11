# n = int(input())
#
# even = list()
# odd = list()
# negative = list()
# positive = list()
#
# for i in range(n):
#     number = int(input())
#
#     if number % 2 == 0:
#         even.append(number)
#     if number % 2 != 0:
#         odd.append(number)
#     if number < 0:
#         negative.append(number)
#     if number >= 0:
#         positive.append(number)
#
# command = input()
# if command == "even":
#     print(even)
# elif command == "odd":
#     print(odd)
# elif command == "negative":
#     print(negative)
# elif command == "positive":
#     print(positive)


# variant 2

n = int(input())

even = list()
odd = list()
negative = list()
positive = list()

for i in range(n):
    number = int(input())

    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
    if number < 0:
        negative.append(number)
    else:
        positive.append(number)

command = input()

print(eval(command))

# variant 3

# n = int(input())
#
# numbers_list = list()
#
# for i in range(n):
#     current_number = int(input())
#     numbers_list.append(current_number)
#
# filter_word = input()
# filtered_list = list()
#
# for current_number in numbers_list:
#     if filter_word == "even":
#         if current_number % 2 == 0:
#             filtered_list.append(current_number)
#     if filter_word == "odd":
#         if current_number % 2 != 0:
#             filtered_list.append(current_number)
#     if filter_word == "negative":
#         if current_number < 0:
#             filtered_list.append(current_number)
#     if filter_word == "positive":
#         if current_number >= 0:
#             filtered_list.append(current_number)
#
# print(filtered_list)
