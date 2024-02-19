sequence = list(map(int, input().split(' ')))

sum_values = 0

while sequence:
    index = int(input())

    current_value = 0

    if index < 0:
        current_value = sequence[0]
        last_element = sequence[-1]
        sequence.remove(sequence[0])
        sequence.append(last_element)

    elif index >= len(sequence):
        current_value = sequence[-1]
        first_element = sequence[0]
        sequence.pop(-1)
        sequence.append(first_element)

    else:
        current_value = sequence[index]
        sequence.pop(index)

    sum_values += current_value
    sequence = [el + current_value if el <= current_value else el - current_value for el in sequence]

print(sum_values)
