days_count = int(input())
daily_plunder = int(input())
goal = float(input())
loot = 0

for day in range(1, days_count + 1):
    loot += daily_plunder
    if day % 3 == 0:
        loot += daily_plunder * 0.5
    if day % 5 == 0:
        loot -= loot * 0.3
percentage_collected = (loot * 100) / goal

if loot < goal:
    print(f'Collected only {percentage_collected:.2f}% of the plunder.')
else:
    print(f'Ahoy! {loot:.2f} plunder gained.')
