targets = [int(num) for num in input().split(' ')]

command = input()

while command != "End":
    data = command.split(' ')
    action = data[0]
    index = int(data[1])

    if action == "Shoot":
        power = int(data[2])
        if 0 <= index < len(targets):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)

    elif action == "Add":
        value = int(data[2])
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif action == "Strike":
        radius = int(data[2])
        start_index = index - radius
        end_index = index + radius

        if start_index < 0 or end_index >= len(targets):
            print("Strike missed!")
        else:
            targets = targets[0:start_index] + targets[end_index + 1:]

    command = input()

print('|'.join(map(str, targets)))
