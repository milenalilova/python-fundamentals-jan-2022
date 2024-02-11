num_sequence = list(map(int, input().split(' ')))
command = input()

while command != 'Finish':
    info = command.split(' ')
    action = info[0]

    if action == 'Add':
        value = int(info[1])
        num_sequence.append(value)

    elif action == 'Remove':
        value = int(info[1])
        for i in range(len(num_sequence)):
            if num_sequence[i] == value:
                num_sequence.pop(i)
                break

        # if value in num_sequence:
        #     num_sequence.remove(value)

    elif action == 'Replace':
        value = int(info[1])
        replacement = int(info[2])

        for i in range(len(num_sequence)):
            if num_sequence[i] == value:
                num_sequence[i] = replacement
                break
        # if value in num_sequence:
        #     index = num_sequence.index(value)
        #     num_sequence.insert(index, replacement)
        #     num_sequence.remove(value)

    elif action == 'Collapse':
        value = int(info[1])
        for num in num_sequence:  # (use list comprehension or range(len(num_sequence)-1, -1, -1))
            if num < value:
                num_sequence.remove(num)

    command = input()

num_sequence = list(map(str, num_sequence))
print(' '.join(num_sequence))
