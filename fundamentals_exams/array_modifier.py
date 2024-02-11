initial = list(map(int, input().split(' ')))
command = input().split(' ')

while command[0] != 'end':
    if command[0] == 'swap':
        initial[int(command[1])], initial[int(command[2])] = initial[int(command[2])], initial[int(command[1])]
    elif command[0] == 'multiply':
        result = int(initial[int(command[1])]) * int(initial[int(command[2])])
        initial[int(command[1])] = result
    elif command[0] == 'decrease':
        initial = list(map(lambda x: x - 1, initial))  # or initial = [x-1 for x in initial]

    command = input().split(' ')

print(', '.join(map(str, initial)))
