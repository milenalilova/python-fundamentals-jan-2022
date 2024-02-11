# command = input()
# students_dict = {}
# language_dict = {}
#
# while True:
#
#     if command == "exam finished":
#         break
#
#     command = command.split("-")
#
#     if "banned" in command:
#         name = command[0]
#
#         students_dict.pop(name)
#
#     else:
#         name = command[0]
#         language = command[1]
#         points = int(command[2])
#
#         if name not in students_dict:
#             students_dict[name] = points
#             if language not in language_dict:
#                 language_dict[language] = [points]
#             else:
#                 language_dict[language].append(points)
#
#         elif name in students_dict and points > students_dict[name]:
#             students_dict[name] = points
#             language_dict[language].append(points)
#
#         elif name in students_dict and points < students_dict[name]:
#             language_dict[language].append(points)
#
#     command = input()
#
# print("Results:")
# [print(f"{name} | {points}") for name, points in students_dict.items()]
# print("Submissions:")
# [print(f"{language} - {len(language_dict[language])}") for language, count in language_dict.items()]


# def ban(dict: dict, name):
#     for key in dict.keys():
#         if name == key[0]:
#             dict.pop(key)
#             return True
#     return False
#
#
# def print_results(dict: dict):
#     print('Results:')
#     [print(f"{key[0]} | {points}") for key, points in dict.items()]
#
#
# def print_submissions(dict: dict):
#     print('Submissions:')
#     [print(f"{lang} - {count}") for lang, count in dict.items()]
#
#
# if __name__ == '__main__':
#     students_data = {}
#     language_data = {}
#
#     while True:
#
#         line = input().split('-')
#         if line[0] == 'exam finished':
#             break
#         elif line[1] == 'banned':
#             if ban(students_data, line[0]):
#                 ban(students_data, line[0])
#         else:
#             username = line[0]
#             language = line[1]
#             points = int(line[2])
#
#             if (username, language) not in students_data:
#                 students_data[(username, language)] = points
#             else:
#                 if students_data[(username, language)] < points:
#                     students_data[(username, language)] = points
#
#             if language not in language_data:
#                 language_data[language] = 0
#             language_data[language] += 1
#
#     print_results(students_data)
#     print_submissions(language_data)
#


command = input()
counter = {}
dict = {}

while "exam" not in command:

    com = command.split("-")
    username = com[0]
    language = com[1]

    if "banned" == com[1]:
        del dict[username]

    elif "banned" != com[1]:
        points = int(com[2])

        if username not in dict:
            dict[username] = [language, points]
        else:
            if language in dict[username]:
                # username.split(", ")
                # print(username.split(", "))
                index = dict[username].index(language)
                if points > dict[username][index + 1]:
                    dict[username][index + 1] = points
            else:
                dict[username] += [language, points]

        if language not in counter:
            counter[language] = 1
        else:
            counter[language] += 1

    command = input()

print(f"Results:")
for d in dict:
    # d.split(", ")
    # print(d.split(", "))
    print(f"{d} | {dict[d][1]}")
print(f"Submissions:")
for c in counter:
    print(f"{c} - {counter[c]}")