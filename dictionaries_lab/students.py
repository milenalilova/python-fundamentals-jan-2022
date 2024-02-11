text = input()
courses = dict()

while ":" in text:
    data = text.split(":")  # (name, id, course) = text.split(":")   tuple, one line instead of the four
    name = data[0]
    id = data[1]
    course = data[2]

    if course not in courses.keys():
        courses[course] = dict()

    courses[course][id] = name

    text = input()

text = text.replace("_", " ")

if text in courses:
    for id in courses[text]:
        print(f"{courses[text][id]} - {id}")



# Or just:
# for id in courses[text]:
#     print(f"{courses[text][id]} - {id}")
