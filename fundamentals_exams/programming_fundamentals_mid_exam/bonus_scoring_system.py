from math import ceil

students_count = int(input())
lectures_count = int(input())
bonus_points = int(input())
max_points = 0
max_lectures = 0

for student in range(students_count):
    students_attendance = int(input())
    total_bonus = students_attendance / lectures_count * (5 + bonus_points)
    if total_bonus > max_points:
        max_points = total_bonus
        max_lectures = students_attendance

print(f"Max Bonus: {ceil(max_points)}.")
print(f"The student has attended {max_lectures} lectures.")
