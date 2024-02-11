health = 100
bitcoins = 0
dungeons_rooms = input().split('|')
room_number = 0

for room in dungeons_rooms:
    info = room.split(' ')
    command = info[0]
    value = int(info[1])
    room_number += 1
    if command == "potion":
        health += value
        if health >= 100:
            diff = health - 100
            health = 100
            print(f'You healed for {value - diff} hp.')
            print(f'Current health: {health} hp.')
        else:
            print(f'You healed for {value} hp.')
            print(f'Current health: {health} hp.')
    elif command == "chest":
        bitcoins += value
        print(f'You found {value} bitcoins.')
    else:
        health -= value
        if health <= 0:
            print(f'You died! Killed by {command}.')
            print(f'Best room: {room_number}')
            break
        else:
            print(f'You slayed {command}.')

if room_number >= len(dungeons_rooms) and health > 0:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
