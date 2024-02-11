substrings = input().split(', ')
strings = input()
result = [el for el in substrings if el in strings]

print(result)



# substrings = input().split(', ')
# strings = input()
# new_list = []
#
# for sub_word in substrings:
#     if sub_word in strings:
#         new_list.append(sub_word)
#
# print(new_list)
