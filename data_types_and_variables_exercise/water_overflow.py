lines = int(input())
litres_count = 0
capacity = 255

for lit in range(lines):
    litres = int(input())
    if litres > capacity:
        print("Insufficient capacity!")
        continue
    else:
        litres_count += litres
        capacity -= litres

print(litres_count)
