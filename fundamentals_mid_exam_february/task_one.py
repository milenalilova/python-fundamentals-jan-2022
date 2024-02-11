import math

number_biscuits = int(input())
num_workers = int(input())
competition_biscuits = int(input())
biscuits_count = 0
daily_biscuits_count = number_biscuits * num_workers

for day in range(1, 31):
    if day % 3 == 0:
        biscuits_count += math.floor(daily_biscuits_count * 0.75)
    else:
        biscuits_count += daily_biscuits_count

print(f'You have produced {biscuits_count} biscuits for the past month.')

diff = abs(biscuits_count - competition_biscuits)
percentage = diff / competition_biscuits * 100

if biscuits_count > competition_biscuits:
    print(f'You produce {percentage:.2f} percent more biscuits.')
else:
    print(f'You produce {percentage:.2f} percent less biscuits.')
