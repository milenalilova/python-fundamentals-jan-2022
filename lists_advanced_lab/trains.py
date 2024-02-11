train_length = int(input())
command = input()
wagons = [0 for i in range(train_length)]   # OR wagons = [0] * train_length

while command != 'End':
    current_command = command.split(' ')
    info = current_command[0]
    if info == 'add':
        people = int(current_command[1])
        wagons[-1] += people
    elif info == 'insert':
        index = int(current_command[1])
        people = int(current_command[2])
        wagons[index] += people
    elif info == 'leave':
        index = int(current_command[1])
        people = int(current_command[2])
        wagons[index] -= people

    command = input()

print(wagons)
