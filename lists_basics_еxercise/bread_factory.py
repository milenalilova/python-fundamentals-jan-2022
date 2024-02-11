events = input().split('|')
energy = 100
coins = 100
condition = False

for current_event in events:
    event_info = current_event.split('-')
    event = event_info[0]
    value = int(event_info[1])

    if event == "rest":
        energy += value
        if energy > 100:
            energy = 100
            value = 0
        print(f"You gained {value} energy.")
        print(f"Current energy: {energy}.")

    elif event == "order":
        if energy >= 30:
            energy -= 30
            coins += value
            print(f"You earned {value} coins.")
        else:
            energy += 50
            print(f"You had to rest!")

    else:
        if coins >= value:
            coins -= value
            print(f"You bought {event}.")
        else:
            condition = True
            print(f"Closed! Cannot afford {event}.")
            break

if not condition:
    print(f'Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
