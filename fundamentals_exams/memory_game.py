elements_list = input().split()
command = input()
moves = 0

while command != 'end':
    index_one = int(command.split()[0])
    index_two = int(command.split()[1])
    moves += 1
    if index_one == index_two or index_one < 0 or index_two < 0 or \
            index_one >= len(elements_list) or index_two >= len(elements_list):
        print('Invalid input! Adding additional elements to the board')
        elements_list.insert(int(len(elements_list) / 2), f'-{str(moves)}a')
        elements_list.insert(int(len(elements_list) / 2), f'-{str(moves)}a')
    elif elements_list[index_one] == elements_list[index_two]:
        print(f'Congrats! You have found matching elements - {elements_list[index_one]}!')
        element = elements_list.pop(index_one)
        elements_list.remove(element)
    elif elements_list[index_one] != elements_list[index_two]:
        print('Try again!')
    if not elements_list:
        print(f'You have won in {moves} turns!')
        break

    command = input()

if command == 'end':
    print('Sorry you lose :(')
    print(' '.join(elements_list))
