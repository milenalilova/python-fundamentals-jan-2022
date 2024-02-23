int_list = [int(num) for num in input().split(' ')]
command = input()

while command != "end":
    data = command.split(' ')
    action = data[0]

    if action == "swap":
        first_index = int(data[1])
        second_index = int(data[2])
        int_list[first_index], int_list[second_index] = int_list[second_index], int_list[first_index]

    elif action == "multiply":
        first_index = int(data[1])
        second_index = int(data[2])
        result = int_list[first_index] * int_list[second_index]
        int_list[first_index] = result

    elif action == "decrease":
        int_list = [num - 1 for num in int_list]

    command = input()

int_list = [str(num) for num in int_list]
print(', '.join(int_list))
