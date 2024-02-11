# command = input()
# coffee_cups_counter = 0
#
# while command != 'END':
#     if command == 'END':
#         break
#     elif command == 'coding':
#         coffee_cups_counter += 1
#     elif command == 'CODING':
#         coffee_cups_counter += 2
#     elif command == 'dog' or command == "cat":
#         coffee_cups_counter += 1
#     elif command == 'DOG' or command == 'CAT':
#         coffee_cups_counter += 2
#     elif command == 'movie':
#         coffee_cups_counter += 1
#     elif command == 'MOVIE':
#         coffee_cups_counter += 2
#     else:
#         pass
#     command = input()
#
# if coffee_cups_counter > 5:
#     print('You need extra sleep')
# else:
#     print(coffee_cups_counter)


command = input()
coffee_cups_counter = 0

lower_command = ['coding', 'dog', 'cat', 'movie']
upper_command = ['CODING', 'DOG', 'CAT', 'MOVIE']

while command != 'END':
    if command == 'END':
        break
    elif command in lower_command:
        coffee_cups_counter += 1
    elif command in upper_command:
        coffee_cups_counter += 2
    else:
        pass
    command = input()

if coffee_cups_counter > 5:
    print('You need extra sleep')
else:
    print(coffee_cups_counter)
