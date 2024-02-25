info = input()
courses_data = {}

while ':' in info:
    info = info.split(':')
    name = info[0]
    id = info[1]
    course = info[2]
    if course not in courses_data.keys():
        courses_data[course] = {}
    courses_data[course][name] = id

    info = input()

course_name = info.replace('_', ' ')

for el in courses_data.keys():
    if el == course_name:
        for name, id in courses_data[el].items():
            print(f"{name} - {id}")
