loot = [int(num) for num in input().split(", ")]
beggars = int(input())
count = 0
beggars_list = [0] * beggars

for coin in loot:
    beggars_list[count] += coin
    count += 1
    if count >= beggars:
        count = 0

print(beggars_list)
