sequence = input().split(' ')
moves = 0
command = input()

while command != 'end':

    indexes = command.split(' ')
    first_index = int(indexes[0])
    second_index = int(indexes[1])
    mid_index = len(sequence) // 2
    moves += 1

    if first_index == second_index \
            or first_index < 0 or first_index >= len(sequence) \
            or second_index < 0 or second_index >= len(sequence):
        insert_element = f"-{moves}a"
        sequence.insert(mid_index, insert_element)
        sequence.insert(mid_index, insert_element)
        print("Invalid input! Adding additional elements to the board")

    elif sequence[first_index] != sequence[second_index]:
        print("Try again!")

    elif sequence[first_index] == sequence[second_index]:
        element = sequence[first_index]
        sequence.remove(element)
        sequence.remove(element)
        print(f"Congrats! You have found matching elements - {element}!")

    if not sequence:
        print(f"You have won in {moves} turns!")
        break

    command = input()

if sequence:
    print("Sorry you lose :(")
    print(' '.join(sequence))



