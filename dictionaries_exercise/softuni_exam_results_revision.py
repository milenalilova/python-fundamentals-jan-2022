exam_stats = {}
language_stats = {}

command = input()

while command != "exam finished":
    info = command.split('-')

    if len(info) > 2:
        username = info[0]
        language = info[1]
        points = int(info[2])

        if username not in exam_stats:
            exam_stats[username] = {}
            exam_stats[username][language] = points
        else:
            if language not in exam_stats[username].keys():
                exam_stats[username][language] = points
            else:
                if points > exam_stats[username][language]:
                    exam_stats[username][language] = points

        if language not in language_stats.keys():
            language_stats[language] = 1
        else:
            language_stats[language] += 1

    else:
        username = info[0]
        del exam_stats[username]

    command = input()

print("Results:")
for user in exam_stats.keys():
    for lang in exam_stats[user].values():
        print(f"{user} | {lang}")

print("Submissions:")
for lang, subs in language_stats.items():
    print(f"{lang} - {subs}")
