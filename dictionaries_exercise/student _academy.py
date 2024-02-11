number = int(input())
grades_dict = {}

for num in range(number):
    name = input()
    grade = float(input())

    if name not in grades_dict:
        grades_dict[name] = [grade]
    else:
        grades_dict[name] += [grade]

for key in grades_dict.keys():
    average_grades = sum(grades_dict[key]) / len(grades_dict[key])
    grades_dict[key] = average_grades

for key in list(grades_dict.keys()):
    if grades_dict[key] < 4.50:
        del grades_dict[key]

for key, value in grades_dict.items():
    print(f"{key} -> {value:.2f}")
