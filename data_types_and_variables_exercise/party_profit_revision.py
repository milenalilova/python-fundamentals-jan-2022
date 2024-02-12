from math import floor

group_size = int(input())
days = int(input())

coins_earned = 0

for day in range(1, days + 1):
    coins_earned += 50

    if day % 10 == 0:
        group_size -= 2
    if day % 3 == 0 and day % 5 == 0:
        group_size += 5
        coins_earned -= group_size * 2

    coins_earned -= group_size * 2

    if day % 3 == 0:
        coins_earned -= group_size * 3
    if day % 5 == 0:
        coins_earned += group_size * 20

coins_per_person = floor(coins_earned / group_size)

print(f"{group_size} companions received {coins_per_person} coins each.")
