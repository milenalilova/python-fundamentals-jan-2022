pirate_ship = [int(x) for x in input().split('>')]
war_ship = [int(x) for x in input().split('>')]
max_health = int(input())
is_stalemate = True

command = input()

while command != "Retire":
    info = command.split(' ')
    action = info[0]

    if action == "Fire":
        index = int(info[1])
        damage = int(info[2])
        if 0 <= index < len(war_ship):
            war_ship[index] -= damage
            if war_ship[index] <= 0:
                is_stalemate = False
                print(f"You won! The enemy ship has sunken.")
                break

    elif action == "Defend":
        start_index = int(info[1])
        end_index = int(info[2])
        damage = int(info[3])
        if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
            for idx in range(start_index, end_index + 1):
                pirate_ship[idx] -= damage
                if pirate_ship[idx] <= 0:
                    is_stalemate = False
                    print(f"You lost! The pirate ship has sunken.")
                    break

    elif action == "Repair":
        index = int(info[1])
        health = int(info[2])
        if 0 <= index < len(pirate_ship):
            pirate_ship[index] += health
            if pirate_ship[index] > max_health:
                pirate_ship[index] = max_health

    elif action == "Status":
        need_repair = [num for num in pirate_ship if num < max_health * 0.2]
        print(f"{len(need_repair)} sections need repair.")

    command = input()

if is_stalemate:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(war_ship)}")
