chest_state = input().split('|')
command = input()

while command != 'Yohoho!':
    info = command.split(' ')
    action = info[0]
    if action == 'Loot':
        for item in range(1, len(info)):
            if info[item] not in chest_state:
                chest_state.insert(0, info[item])
    elif action == 'Drop':
        index = int(info[1])
        if 0 <= abs(index) < len(chest_state):             # also maybe if 0 <= index < len(chest_state)
            item = chest_state.pop(index)
            chest_state.append(item)
            # item = chest_state[index]                    # also works with the following 3 lines
            # chest_state.remove(chest_state[index])       # also works
            # chest_state.append(item)                     # also works
    elif action == 'Steal':
        count = int(info[1])
        if count >= len(chest_state):
            stolen_items = ', '.join(chest_state)
            chest_state.clear()
            print(stolen_items)
        else:
            stolen_items = ', '.join(chest_state[-count:])
            chest_state = chest_state[:-count]
            print(stolen_items)
    command = input()

if len(chest_state) <= 0:
    print('Failed treasure hunt.')
else:
    gain = 0
    for el in chest_state:
        gain += len(el)
    average_gain = gain / len(chest_state)
    print(f'Average treasure gain: {average_gain:.2f} pirate credits.')


# loots = input().split("|")
# command = input()
# new_list = []
# while command != "Yohoho!":
#     res = command.split(" ")
#     action = res[0]
#     if action == "Loot":
#         items = res[1:]
#         for item in items:
#             if item not in loots:
#                 loots.insert(0, item)
#     elif action == "Drop":
#         index = int(res[1])
#         if 0 <= abs(index) <= len(loots):
#             removing = loots.pop(index)
#             loots.append(removing)
#     elif action == "Steal":
#         number = int(res[1])
#         removed_items = loots[-number:]
#         print(", ".join(removed_items))
#         loots = loots[:-number]
#     command = input()
#
# if len(new_list) > 0:
#     new_list.reverse()
#     print(", ".join(new_list))
# count = 0
# for y in loots:
#     count += len(y)
#
# if len(loots) > 0:
#     print(f"Average treasure gain: {float(count / len(loots)):.2f} pirate credits.")
# else:
#     print(f"Failed treasure hunt.")
#
#
