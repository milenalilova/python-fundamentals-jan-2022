def moving_target(data):
    while True:
        command = input().split(' ')
        if command[0] == 'End':
            break
        elif command[0] == 'Shoot':
            index = int(command[1])
            power = int(command[2])
            if -1 < index < len(data):
                data[index] -= power
                if data[index] <= 0:
                    data.remove(data[index])     # Or data.pop(index)
        elif command[0] == 'Add':
            index = int(command[1])
            value = int(command[2])
            if -1 < index < len(data):
                data.insert(index, value)
            else:
                print("Invalid placement!")
        elif command[0] == 'Strike':
            index = int(command[1])
            radius = int(command[2])
            if -1 < index < len(data):
                if -1 < index - radius and index + radius < len(data):
                    data.remove(data[index + radius])
                    data.remove(data[index])
                    data.remove(data[index - radius])
                    # data = data[:index - radius] + data[index + radius + 1:]    It works better and easier to write
                else:
                    print('Strike missed!')
    data = list(map(str, data))
    print('|'.join(data))


targets = list(map(int, input().split(' ')))
moving_target(targets)

# There is a shorter way with functions (see video for task Inventory, list_advanced_exercise)
