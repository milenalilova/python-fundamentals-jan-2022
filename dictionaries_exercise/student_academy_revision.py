n = int(input())
student_dict = {}

for i in range(n):
    student_name = input()
    student_note = float(input())

    if student_name not in student_dict.keys():
        student_dict[student_name] = []
    student_dict[student_name].append(student_note)

for k, v in student_dict.items():
    average = sum(v) / len(v)
    student_dict[k] = average

for k in list(student_dict.keys()):
    if student_dict[k] < 4.50:
        del student_dict[k]

for k, v in student_dict.items():
    print(f"{k} -> {student_dict[k]:.2f}")
