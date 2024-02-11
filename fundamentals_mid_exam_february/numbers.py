num_sequence = input()
command = input()
print(num_sequence)

while command != 'Finish':
    info = command.split(' ')
    action = info[0]

    if action == 'Add':
        value = info[1]
        num_sequence = num_sequence + ' ' + value

    elif action == 'Remove':
        value = info[1]
        for i in range(len(num_sequence)):
            if num_sequence[i] == value:
                num_sequence.remove(num_sequence[i])
                break

        # if value in num_sequence:
        #     num_sequence.remove(value)

    elif action == 'Replace':
        value = info[1]
        replacement = info[2]
        if value in num_sequence:
            num_sequence = num_sequence.replace(value, replacement, 1)

        # for i in range(len(num_sequence)):
        #     if num_sequence[i] == value:
        #         num_sequence[i] = replacement
        #         break
        # if value in num_sequence:
        #     index = num_sequence.index(value)
        #     num_sequence.insert(index, replacement)
        #     num_sequence.remove(value)

    elif action == 'Collapse':
        value = int(info[1])
        for i in range(len(num_sequence)):
            if int(num_sequence[i]) < value:
                num_sequence = num_sequence.replace(num_sequence[i], '')

    command = input()

# num_sequence = list(map(str, num_sequence))
print(num_sequence)
