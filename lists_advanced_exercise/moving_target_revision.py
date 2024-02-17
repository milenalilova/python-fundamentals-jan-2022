sequence = list(map(int, input().split(' ')))
command = input()

while command != "End":
    info = command.split(' ')
    action = info[0]
    index = int(info[1])

    if action == 'Shoot':
        power = int(info[2])
        if 0 <= index < len(sequence):
            sequence[index] -= power
            if sequence[index] <= 0:
                sequence.pop(index)

    elif action == 'Add':
        value = int(info[2])
        if 0 <= index < len(sequence):
            sequence.insert(index, value)
        else:
            print("Invalid placement!")

    elif action == 'Strike':
        radius = int(info[2])
        if 0 <= index < len(sequence):
            if index - radius < 0 or index + radius > len(sequence):
                print("Strike missed!")
            else:
                start_index = index - radius
                end_index = index + radius
                sequence = sequence[0:start_index] + sequence[end_index + 1::]

    command = input()

sequence = list(map(str, sequence))
print('|'.join(sequence))
