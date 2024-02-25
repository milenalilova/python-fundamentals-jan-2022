info = input().split(' ')
bakery_stock = {}
for i in range(0, len(info), 2):
    key = info[i]
    value = info[i + 1]
    bakery_stock[key] = int(value)

print(bakery_stock)
