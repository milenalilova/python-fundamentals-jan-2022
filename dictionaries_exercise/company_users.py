command = input()
employee_dict = {}

while command != 'End':
    info = command.split(' -> ')
    company_name = info[0]
    student_id = info[1]

    if company_name not in employee_dict:
        employee_dict[company_name] = [student_id]
    else:
        if student_id not in employee_dict[company_name]:
            employee_dict[company_name] += [student_id]

    command = input()

for key, value in employee_dict.items():
    print(f"{key}")
    for i in range(len(value)):
        print(f"-- {value[i]}")
