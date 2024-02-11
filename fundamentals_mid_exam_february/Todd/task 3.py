line = input().split(', ')
num = int(input())

for i in range(num):
    data = input().split(', ')

    command = data[0]

    if command == 'Add':
        card_name = data[1]
        if card_name in line:
            print(f'Card is already in the deck')
        else:
            line.append(card_name)
            print(f'Card successfully added')

    elif command == 'Remove':
        card_name = data[1]
        if card_name in line:
            line.remove(card_name)
            print(f'Card successfully removed')
        else:
            print('Card not found')

    elif command == 'Remove At':
        index = int(data[1])
        if index < 0 or index > len(line):
            print('Index out of range')
        else:
            line.pop(index)
            print('Card successfully removed')

    elif command == 'Insert':
        index = int(data[1])
        card_name = data[2]
        if index < 0 or index > len(line):
            print('Index out of range')
        elif card_name in line:
            print('Card is already added')
        else:
            line.insert(index, card_name)
            print('Card is already added')

print(', '.join(line))


