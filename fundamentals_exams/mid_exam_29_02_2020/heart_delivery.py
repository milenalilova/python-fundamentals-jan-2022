houses_list = [int(num) for num in input().split('@')]

current_index = 0
valentines_day = 0

command = input()

while command != 'Love!':
    jump = command.split(' ')
    index = int(jump[1])
    current_index += index

    if current_index >= len(houses_list):
        current_index = 0
    if houses_list[current_index] == 0:
        print(f"Place {current_index} already had Valentine's day.")
    else:
        houses_list[current_index] -= 2
        if houses_list[current_index] == 0:
            valentines_day += 1
            print(f"Place {current_index} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {current_index}.")
if sum(houses_list) == 0:
    print("Mission was successful.")
else:
    houses_list = [x for x in houses_list if x != 0]
    print(f"Cupid has failed {len(houses_list)} places.")
