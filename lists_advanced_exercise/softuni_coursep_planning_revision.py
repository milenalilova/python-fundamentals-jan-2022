schedule = input().split(', ')

command = input()

while command != "course start":
    data = command.split(':')
    action = data[0]
    lesson_title = data[1]

    if action == "Add":
        if lesson_title not in schedule:
            schedule.append(lesson_title)

    elif action == "Insert":
        index = int(data[2])
        if lesson_title not in schedule:
            schedule.insert(index, lesson_title)

    elif action == "Remove":
        if lesson_title in schedule:
            if f"{lesson_title}-Exercise" in schedule:
                schedule.remove(f"{lesson_title}-Exercise")
            schedule.remove(lesson_title)

    elif action == "Swap":
        new_lesson_title = data[2]
        if lesson_title in schedule and new_lesson_title in schedule:
            lesson_title_index = schedule.index(lesson_title)
            new_lesson_title_index = schedule.index(new_lesson_title)
            schedule[lesson_title_index], schedule[new_lesson_title_index] = \
                schedule[new_lesson_title_index], schedule[lesson_title_index]

            if f"{lesson_title}-Exercise" in schedule:
                exercise_index = schedule.index(f"{lesson_title}-Exercise")
                new_position_exercise = schedule.pop(exercise_index)
                schedule.insert(lesson_title_index + 1, new_position_exercise)
            if f"{new_lesson_title}-Exercise" in schedule:
                exercise_index = schedule.index(f"{new_lesson_title}-Exercise")
                new_position_exercise = schedule.pop(exercise_index)
                schedule.insert(lesson_title_index + 1, new_position_exercise)

    elif action == "Exercise":
        if lesson_title in schedule:
            if f"{lesson_title}-Exercise" not in schedule:
                lesson_title_index = schedule.index(lesson_title) + 1
                schedule.insert(lesson_title_index, f"{lesson_title}-Exercise")
        else:
            schedule.append(lesson_title)
            schedule.append(f"{lesson_title}-Exercise")

    command = input()

for n in range(len(schedule)):
    print(f"{n + 1}.{schedule[n]}")
