treasure_chest = input().split('|')

command = input()

while command != "Yohoho!":
    info = command.split(' ')
    action = info[0]

    if action == "Loot":
        for i in range(1, len(info)):
            if info[i] not in treasure_chest:
                treasure_chest.insert(0, info[i])

    elif action == "Drop":
        index = int(info[1])
        if 0 <= index < len(treasure_chest):
            loot = treasure_chest.pop(index)
            treasure_chest.append(loot)

    elif action == "Steal":
        count = int(info[1])
        stolen_items = []
        if count >= len(treasure_chest):
            stolen_items = treasure_chest.copy()
            treasure_chest.clear()
        else:
            stolen_items = treasure_chest[-count:]
            treasure_chest = treasure_chest[0:-count]

        print(', '.join(stolen_items))

    command = input()

if not treasure_chest:
    print("Failed treasure hunt.")
else:
    average_gain = sum([len(el) for el in treasure_chest]) / len(treasure_chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")

