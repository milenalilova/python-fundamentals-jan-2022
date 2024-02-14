energy = 100
coins = 100
events_list = input().split('|')
had_to_close = False

for event in events_list:
    event_info = event.split('-')
    event_name = event_info[0]
    number = int(event_info[1])

    if event_name == "rest":
        if energy + number > 100:
            diff = 100 - energy
            energy = 100
            print(f"You gained {diff} energy.")
        else:
            energy += number
            print(f"You gained {number} energy.")
        print(f"Current energy: {energy}.")

    elif event_name == "order":
        if energy >= 30:
            energy -= 30
            coins += number
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:
        if coins >= number:
            coins -= number
            print(f"You bought {event_name}.")
        else:
            had_to_close = True
            print(f"Closed! Cannot afford {event_name}.")
            break

if not had_to_close:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
