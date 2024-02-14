fires = input().split('#')
water = int(input())
effort = 0
total_fire = 0
print("Cells:")

for current_fire in fires:
    info = current_fire.split(' = ')
    type_fire = info[0]
    value = int(info[1])

    if type_fire == "High":
        if 81 <= value <= 125:
            if water >= value:
                water -= value
                effort += value * 0.25
                total_fire += value
                print(f" - {value}")

    elif type_fire == "Medium":
        if 51 <= value <= 80:
            if water > value:
                water -= value
                effort += value * 0.25
                total_fire += value
                print(f" - {value}")

    elif type_fire == "Low":
        if 1 <= value <= 50:
            if water >= value:
                water -= value
                effort += value * 0.25
                total_fire += value
                print(f" - {value}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
