# number_students = int(input())
# number_lectures = int(input())
# additional_bonus = int(input())
# total_bonus = 0
# bonuses = []
# student_attendances_list = []
# max_bonus = 0
# max_attendance = 0
#
# for student in range(number_students):
#     student_attendances = int(input())
#     student_attendances_list.append(student_attendances)
#     total_bonus = round(student_attendances / number_lectures * (5 + additional_bonus))
#     bonuses.append(total_bonus)
#     max_bonus = max(bonuses)
#     max_attendance = max(student_attendances_list)
#
# print(f'Max Bonus: {max_bonus}.')
# print(f'The student has attended {max_attendance} lectures.')


number_students = int(input())
number_lectures = int(input())
additional_bonus = int(input())
total_bonus = 0
student_attendances_list = []
max_attendance = 0

for student in range(number_students):
    student_attendances = int(input())
    student_attendances_list.append(student_attendances)
    max_attendance = max(student_attendances_list)
    total_bonus = round(max_attendance / number_lectures * (5 + additional_bonus))

print(f'Max Bonus: {total_bonus}.')
print(f'The student has attended {max_attendance} lectures.')
