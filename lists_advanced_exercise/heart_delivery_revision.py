integers_line = list(map(int, input().split('@')))

command = input()
current_index = 0

while command != "Love!":
    info = command.split(' ')
    jump_length = int(info[1])
    current_index += jump_length

    if current_index >= len(integers_line):
        current_index = 0
    if integers_line[current_index] == 0:
        print(f"Place {current_index} already had Valentine's day.")
    else:
        integers_line[current_index] -= 2
        if integers_line[current_index] == 0:
            print(f"Place {current_index} has Valentine's day.")

    command = input()

integers_line = [num for num in integers_line if num != 0]

print(f"Cupid's last position was {current_index}.")

if not integers_line:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(integers_line)} places.")
