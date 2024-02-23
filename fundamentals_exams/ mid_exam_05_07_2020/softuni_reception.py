first_employee_capacity = int(input())
second_employee_capacity = int(input())
third_employee_capacity = int(input())
students_count = int(input())
hours_count = 0
rest_hours = 0
students_served = first_employee_capacity + second_employee_capacity + third_employee_capacity

while students_count > 0:

    if students_count > students_served:
        students_count -= students_served
        hours_count += 1
        if hours_count % 3 == 0:
            rest_hours += 1
    else:
        students_count -= students_count
        hours_count += 1

hours_count += rest_hours

print(f"Time needed: {hours_count}h.")
