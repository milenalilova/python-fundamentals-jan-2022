quantity = int(input())
days = int(input())
money_spent = 0
points = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        money_spent += quantity * 2
        points += 5
    if day % 3 == 0:
        money_spent += quantity * 5 + quantity * 3
        points += 13
    if day % 5 == 0:
        money_spent += quantity * 15
        points += 17
    if day % 3 == 0 and day % 5 == 0:
        points += 30
    if day % 10 == 0:
        points -= 20
        money_spent += 5 + 3 + 15
        if day == days:
            points -= 30

print(f"Total cost: {money_spent}")
print(f"Total spirit: {points}")
