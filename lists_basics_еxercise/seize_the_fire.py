fire_cells = input().split('#')
water_amount = int(input())
effort = 0
total_fire = 0
condition = False

print("Cells:")

for current_fire in fire_cells:
    fire_info = current_fire.split(' = ')
    fire_level = fire_info[0]
    fire_value = int(fire_info[1])
    condition = False

    if fire_level == "High":
        if 81 <= fire_value <= 125:
            condition = True
    elif fire_level == "Medium":
        if 51 <= fire_value <= 80:
            condition = True
    elif fire_level == "Low":
        if 1 <= fire_value <= 50:
            condition = True

    if condition:
        if water_amount >= fire_value:
            water_amount -= fire_value
            effort += fire_value * 0.25
            total_fire += fire_value
            print(f' - {fire_value}')

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
