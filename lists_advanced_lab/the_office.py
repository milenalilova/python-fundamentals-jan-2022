employees = input().split(' ')
factor = int(input())  # No need to use. But: employees = list(map(lambda x: x*factor, employees))

employees = list(map(int, employees))
happy_list = list(filter(lambda emp: emp >= sum(employees) / len(employees), employees))

if len(happy_list) >= len(employees) / 2:
    print(f'Score: {len(happy_list)}/{len(employees)}. Employees are happy!')
else:
    print(f'Score: {len(happy_list)}/{len(employees)}. Employees are not happy!')
