num_pieces = int(input())
collection = []

for i in range(num_pieces):
    pieces = input().split('|')
    collection.append(pieces)

command = input()

while command != 'Stop':
    info = command.split('|')
    current_command = info[0]
    if current_command == 'Add':
        piece = info[1]
        composer = info[2]
        key = info[3]
        is_in_collection = False
        for item in collection:
            if piece in item:
                is_in_collection = True
        if is_in_collection:
            print(f'{piece} is already in the collection!')
        else:
            collection.append(info[1:])
            print(f'{piece} by {composer} in {key} added to the collection!')
    elif current_command == 'Remove':
        piece = info[1]
        is_in_collection = False
        for item in collection:
            if piece in item:
                collection.remove(item)
                is_in_collection = True
        if is_in_collection:
            print(f'Successfully removed {piece}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')
    elif current_command == 'ChangeKey':
        piece = info[1]
        new_key = info[2]
        is_in_collection = False
        for item in collection:
            if piece in item:
                item[2] = new_key
                is_in_collection = True
        if is_in_collection:
            print(f'Changed the key of {piece} to {new_key}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')

    command = input()

for el in collection:
    print(f'{el[0]} -> Composer: {el[1]}, Key: {el[2]}')
