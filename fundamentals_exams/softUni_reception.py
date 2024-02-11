empl_one = int(input())
empl_two = int(input())
empl_three = int(input())
student_count = int(input())
hours_count = 0
break_hour = 0

students_per_hour = empl_one + empl_two + empl_three

while student_count > 0:
    if students_per_hour < student_count:
        student_count -= students_per_hour
        hours_count += 1
        if hours_count % 3 == 0:
            break_hour += 1
    else:
        student_count -= student_count
        hours_count += 1
total_time = hours_count + break_hour

print(f'Time needed: {total_time}h.')
