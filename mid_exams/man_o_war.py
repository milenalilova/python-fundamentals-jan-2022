pirate_ship_status = list(map(int, input().split('>')))
warship_status = list(map(int, input().split('>')))
max_health = int(input())
command = input()
is_stalemate = True

while command != 'Retire':
    info = command.split(' ')
    current_command = info[0]
    if current_command == 'Fire':
        index = int(info[1])
        damage = int(info[2])
        if 0 <= index < len(warship_status):
            warship_status[index] -= damage
            if warship_status[index] <= 0:
                is_stalemate = False
                print('You won! The enemy ship has sunken.')
                break
    elif current_command == 'Defend':
        start_index = int(info[1])
        end_index = int(info[2])
        damage = int(info[3])
        if 0 <= start_index < len(pirate_ship_status) and 0 <= end_index < len(pirate_ship_status):
            for section in range(start_index, end_index + 1):
                pirate_ship_status[section] -= damage
                if pirate_ship_status[section] <= 0:
                    is_stalemate = False
                    print('You lost! The pirate ship has sunken.')
                    break
    elif current_command == 'Repair':
        index = int(info[1])
        heal = int(info[2])
        if 0 <= index < len(pirate_ship_status):
            diff = max_health - pirate_ship_status[index]
            if diff > heal:
                pirate_ship_status[index] += heal
            else:
                pirate_ship_status[index] = max_health
    elif current_command == 'Status':
        repair_count = 0
        repair_status = max_health * 0.2
        for sec in pirate_ship_status:
            if sec < repair_status:
                repair_count += 1
        print(f'{repair_count} sections need repair.')

    command = input()
if is_stalemate:
    pirate_ship_sum = 0
    for part in pirate_ship_status:
        pirate_ship_sum += part
    print(f'Pirate ship status: {pirate_ship_sum}')

    warship_sum = 0
    for part in warship_status:
        warship_sum += part
    print(f'Warship status: {warship_sum}')
