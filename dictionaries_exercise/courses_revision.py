command = input()
course_dict = {}

while command != "end":
    info = command.split(' : ')
    course_name = info[0]
    student_name = info[1]

    if course_name not in course_dict.keys():
        course_dict[course_name] = []
    course_dict[course_name].append(student_name)

    command = input()

for course in course_dict.keys():
    print(f"{course}: {len(course_dict[course])}")
    for student in course_dict[course]:
        print(f"-- {student}")
