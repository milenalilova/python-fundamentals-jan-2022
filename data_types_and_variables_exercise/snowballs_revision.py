n = int(input())

highest_value = 0
highest_weight = 0
highest_speed = 0
highest_quality = 0

for snowball in range(n):
    weight = int(input())
    speed = int(input())
    quality = int(input())

    value = (weight / speed) ** quality

    if value > highest_value:
        highest_value = value
        highest_weight = weight
        highest_speed = speed
        highest_quality = quality

print(f"{highest_weight} : {highest_speed} = {int(highest_value)} ({highest_quality})")
