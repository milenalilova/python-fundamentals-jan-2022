contest_dict = {}
individuals_dict = {}

info = input()

while info != "no more time":
    info = info.split(' -> ')
    username = info[0]
    contest = info[1]
    points = int(info[2])

    if contest not in contest_dict:
        contest_dict[contest] = {username: points}
        if username not in individuals_dict.keys():
            individuals_dict[username] = 0
        individuals_dict[username] += points
    else:
        if username not in contest_dict[contest]:
            contest_dict[contest][username] = points
            if username not in individuals_dict.keys():
                individuals_dict[username] = 0
            individuals_dict[username] += points

        else:
            if points > contest_dict[contest][username]:
                diff = points - contest_dict[contest][username]
                contest_dict[contest][username] = points
                individuals_dict[username] += diff

    info = input()

# Print contest participants
for contest, participants in contest_dict.items():
    print(f"{contest}: {len(participants)} participants")
    sorted_participants = sorted(participants.items(), key=lambda x: (-x[1], x[0]))
    for idx, (username, points) in enumerate(sorted_participants, start=1):
        print(f"{idx}. {username} <::> {points}")

# Print individual standings
print("Individual standings:")
sorted_standings = sorted(individuals_dict.items(), key=lambda x: (-x[1], x[0]))
for idx, (username, total_points) in enumerate(sorted_standings, start=1):
    print(f"{idx}. {username} -> {total_points}")


