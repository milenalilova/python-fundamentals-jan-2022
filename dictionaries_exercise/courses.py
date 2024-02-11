command = input()
courses_dict = {}

while command != 'end':
    data = command.split(" : ")
    course = data[0]
    students_name = data[1]

    if course not in courses_dict:
        courses_dict[course] = [students_name]
    else:
        courses_dict[course] += [students_name]

    command = input()

for key, value in courses_dict.items():
    print(f"{key}: {len(value)}")
    for i in range(len(value)):
        print(f"-- {value[i]}")
