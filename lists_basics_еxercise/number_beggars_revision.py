amounts = [int(num) for num in input().split(', ')]
beggars_count = int(input())
beggars_list = [0] * beggars_count
count = 0

for coin in amounts:
    beggars_list[count] += coin
    count += 1
    if count >= beggars_count:
        count = 0

print(beggars_list)
