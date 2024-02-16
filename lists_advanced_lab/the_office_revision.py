employees_happiness = list(map(int, input().split(' ')))
factor = int(input())

multiplied_happiness = list(map(lambda x: x * factor, employees_happiness))
average_happiness = sum(multiplied_happiness) / len(multiplied_happiness)
happy_employees = [x for x in multiplied_happiness if x >= average_happiness]

happy_count = len(happy_employees)
total_count = len(multiplied_happiness)

if happy_count >= total_count / 2:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")
