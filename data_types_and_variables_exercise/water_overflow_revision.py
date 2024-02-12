n = int(input())

capacity = 255

for i in range(n):
    litres = int(input())
    if litres <= capacity:
        capacity -= litres
    else:
        print("Insufficient capacity!")
        continue

print(255 - capacity)
