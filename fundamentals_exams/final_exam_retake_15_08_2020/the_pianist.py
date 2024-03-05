n = int(input())
pieces_dict = {}

for i in range(n):
    line = input().split('|')
    piece = line[0]
    composer = line[1]
    key = line[2]
    pieces_dict[piece] = {composer: key}

command = input().split('|')

while command[0] != "Stop":
    instruction = command[0]
    piece = command[1]

    if instruction == "Add":
        composer = command[2]
        key = command[3]

        if piece in pieces_dict.keys():
            print(f"{piece} is already in the collection!")
        else:
            pieces_dict[piece] = {composer: key}
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif instruction == "Remove":
        if piece in pieces_dict.keys():
            print(f"Successfully removed {piece}!")
            del pieces_dict[piece]
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif instruction == "ChangeKey":
        new_key = command[2]
        if piece in pieces_dict.keys():
            for k, v in pieces_dict.items():
                if k == piece:
                    for k1, v1 in pieces_dict[k].items():
                        pieces_dict[k][k1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input().split('|')

for k, v in pieces_dict.items():
    for k1, v1 in pieces_dict[k].items():
        print(f"{k} -> Composer: {k1}, Key: {v1}")
