# sequence = input().split(' ')
# new_seq = []
#
# for i in sequence:
#     if int(i) % 2 == 0:
#         new_seq.append(int(i))
#
# print(new_seq)


# def even_numbers(sequence):
#     new_seq = []
#
#     for i in sequence:
#         if int(i) % 2 == 0:
#             new_seq.append(int(i))
#
#     print(new_seq)
#
#
# current_sequence = input().split(' ')
# even_numbers(current_sequence)


#  OR lambda

# result = list(filter(lambda x: x % 2 == 0, list(map(int, input().split(' ')))))
# print(list(result))

# OR filter()

def even_numbers(number):
    if number % 2 == 0:
        return True
    return False


result = filter(even_numbers, list(map(int, input().split(' '))))
print(list(result))
