activation_key = input()
command = input()

while command != 'Generate':
    info = command.split('>>>')
    operation = info[0]

    if operation == 'Contains':
        substring = info[1]
        if substring in activation_key:
            print(f'{activation_key} contains {substring}')
        else:
            print(f'Substring not found!')

    elif operation == 'Flip':
        action = info[1]
        start_index = int(info[2])
        end_index = int(info[3])

        if action == 'Upper':
            upper_string = activation_key[start_index:end_index].upper()
            activation_key = activation_key[:start_index] + upper_string + activation_key[end_index:]
            print(activation_key)

        elif action == 'Lower':
            lower_string = activation_key[start_index:end_index].lower()
            activation_key = activation_key[:start_index] + lower_string + activation_key[end_index:]
            print(activation_key)

    elif operation == 'Slice':
        start_index = int(info[1])
        end_index = int(info[2])
        activation_key = activation_key[:start_index] + '' + activation_key[end_index:]
        print(activation_key)

    command = input()

print(f'Your activation key is: {activation_key}')
