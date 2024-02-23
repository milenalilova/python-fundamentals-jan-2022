dungeons_rooms = input().split('|')
health = 100
bitcoins = 0
rooms_count = 0

for room in dungeons_rooms:
    command = room.split()[0]
    number = int(room.split()[1])
    rooms_count += 1

    if command == "potion":
        if health + number > 100:
            number = 100 - health
            health = 100
        else:
            health += number
        print(f"You healed for {number} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {rooms_count}")
            break

else:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
