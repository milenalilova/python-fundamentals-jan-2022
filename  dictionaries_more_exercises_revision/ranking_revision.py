contests_info_dict = {}

contests_info = input()

while contests_info != "end of contests":
    contest, password = contests_info.split(':')
    contests_info_dict[contest] = password

    contests_info = input()

submissions_dict = {}

submissions_info = input()

while submissions_info != "end of submissions":
    contest, password, username, points = submissions_info.split('=>')
    if contest in contests_info_dict.keys():
        if password in contests_info_dict[contest]:
            if username not in submissions_dict.keys():
                submissions_dict[username] = {}
                submissions_dict[username][contest] = int(points)
            else:
                if contest not in submissions_dict[username]:
                    submissions_dict[username][contest] = int(points)
                else:
                    if int(points) > submissions_dict[username][contest]:
                        submissions_dict[username][contest] = int(points)

    submissions_info = input()

best_score = 0
best_student = ''
for user, submissions in submissions_dict.items():
    total = 0
    for el in submissions.values():
        total += el
    if total > best_score:
        best_score = total
        best_student = user

print(f"Best candidate is {best_student} with total {best_score} points.")

sorted_submissions_dict = sorted(submissions_dict.keys())
print("Ranking:")

for user in sorted_submissions_dict:
    print(user)
    for contest, points in sorted(submissions_dict[user].items(), key=lambda x: x[1], reverse=True):
        print(f"#  {contest} -> {points}")
