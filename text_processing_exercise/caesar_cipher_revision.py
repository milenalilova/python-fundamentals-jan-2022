line = input()
new_line = [chr(ord(ch) + 3) for ch in line]
print(''.join(new_line))


# line = input()
# new_line = ''
#
# for ch in line:
#     new_line += chr(ord(ch) + 3)
#
# print(new_line)
