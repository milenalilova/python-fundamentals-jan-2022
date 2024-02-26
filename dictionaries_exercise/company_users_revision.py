command = input()
companies_dict = {}

while command != "End":
    info = command.split(' -> ')
    company_name = info[0]
    employee_id = info[1]

    if company_name not in companies_dict.keys():
        companies_dict[company_name] = []
    if employee_id not in companies_dict[company_name]:
        companies_dict[company_name] += [employee_id]

    command = input()

for k in companies_dict.keys():
    print(f"{k}")
    for v in companies_dict[k]:
        print(f"-- {v}")
