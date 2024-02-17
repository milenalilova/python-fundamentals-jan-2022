def group_numbers(sequence):
    boundary = 10
    while sequence:
        group_list = [num for num in sequence if num <= boundary]
        print(f"Group of {boundary}'s: {group_list}")
        sequence = [el for el in sequence if el not in group_list]
        boundary += 10


current_sequence = list(map(int, input().split(', ')))
group_numbers(current_sequence)


# Variant 2

# numbers_sequence = list(map(int, input().split(', ')))

# boundary = 10

# while numbers_sequence:
#     group_list = [num for num in numbers_sequence if num <= boundary]
#     print(f"Group of {boundary}'s: {group_list}")
#     numbers_sequence = [el for el in numbers_sequence if el not in group_list]
#     boundary += 10



