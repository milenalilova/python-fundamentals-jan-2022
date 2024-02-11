word = input()
command = input()
new_password = word
# new_word = ''

while command != 'Done':
    info = command.split(' ')
    action = info[0]

    if action == 'TakeOdd':
        current_password = new_password
        new_password = ''
        for i in range(len(current_password)):
            if i % 2 != 0:
                new_password += current_password[i]
        print(new_password)

    elif action == 'Cut':
        index = int(info[1])
        length = int(info[2])
        end_index = index + (length - 1)
        substring = new_password[index:(end_index + 1)]
        # substring = new_password[index:] + new_password[:end_index + 1]
        new_password = new_password.replace(substring, '', 1)
        print(new_password)

    elif action == 'Substitute':
        substring = info[1]
        substitute = info[2]
        if substring in new_password:
            new_password = new_password.replace(substring, substitute)
            print(new_password)
        else:
            print('Nothing to replace!')
    command = input()

print(f'Your password is: {new_password}')


# MAYBE IT WORKS

# password = input()
# command = input()
#
# new_password = password  # changed
#
# while True:
#     tokens = command.split()
#     if tokens[0] == "TakeOdd":
#         curr_password = new_password  # changed
#         new_password = ""  # changed
#         for char in range(len(curr_password)):  # changed
#             if char % 2 != 0:
#                 letter = curr_password[char]  # changed
#                 new_password += letter
#         print(new_password)
#     elif tokens[0] == "Cut":
#         index = int(tokens[1])
#         length = new_password[index:(index + int(tokens[2]))]
#         new_password = new_password.replace(length, "", 1)
#         print(new_password)
#     elif tokens[0] == "Substitute":
#         substring = tokens[1]
#         substitute = tokens[2]
#         if substring in new_password:
#             new_password = new_password.replace(substring, substitute)
#             print(new_password)
#         else:
#             print("Nothing to replace!")
#
#     command = input()
#
#     if command == "Done":
#         print(f"Your password is: {new_password}")
#         break

