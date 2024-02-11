# command = input()
# users_results_dict = {}
# course_submissions_dict = {}
#
# while command != "exam finished":
#
#     if "banned" in command:
#         banned_info = command.split("-")
#         name = banned_info[0]
#         del users_results_dict[name]
#
#     else:
#         info = command.split("-")
#         username = info[0]
#         language = info[1]
#         points = int(info[2])
#
#         if username not in users_results_dict:
#             users_results_dict[username] = [language, points]
#         else:
#             if language not in users_results_dict[username]:
#                 users_results_dict[username] = [language, points]
#             else:
#                 index = users_results_dict[username].index(language)
#                 if points > users_results_dict[username][index + 1]:
#                     users_results_dict[username][index + 1] = points
#
#         if language not in course_submissions_dict:
#             course_submissions_dict[language] = 1
#         else:
#             course_submissions_dict[language] += 1
#
#     command = input()
#
# print("Results:")
# for key, value in users_results_dict.items():
#     print(f"{key} | {value[1]}")
# print("Submissions:")
# for key, value in course_submissions_dict.items():
#     print(f"{key} - {value}")


command = input()
users_results_dict = {}
course_submissions_dict = {}

while command != "exam finished":

    if "banned" in command:
        banned_info = command.split("-")
        name = banned_info[0]
        if name in users_results_dict.keys():
            del users_results_dict[name]

    else:
        info = command.split("-")
        username = info[0]
        language = info[1]
        points = int(info[2])

        if username not in users_results_dict:
            users_results_dict[username] = {}
            users_results_dict[username][language] = points
        else:
            if language not in users_results_dict[username]:
                users_results_dict[username][language] = {}
                users_results_dict[username][language] = points
            else:
                if points > users_results_dict[username][language]:
                    users_results_dict[username][language] = points

        if language not in course_submissions_dict:
            course_submissions_dict[language] = 1
        else:
            course_submissions_dict[language] += 1

    command = input()

print("Results:")
for key in users_results_dict:
    for lang in users_results_dict[key].values():
        print(f"{key} | {lang}")
print("Submissions:")
for key, value in course_submissions_dict.items():
    print(f"{key} - {value}")
