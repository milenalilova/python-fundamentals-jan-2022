message = input()
command = input()

while command != 'Decode':
    info = command.split('|')
    instruction = info[0]

    if instruction == 'Move':
        num_letters = int(info[1])
        part_one = message[:num_letters]
        part_two = message[num_letters:]
        message = part_two + part_one

    elif instruction == 'Insert':
        index = int(info[1])
        value = info[2]
        part_one = message[:index]
        part_two = message[index:]
        message = part_one + value + part_two

    elif instruction == 'ChangeAll':
        substring = info[1]
        replacement = info[2]
        for letter in range(len(message)):
            if message[letter] == substring:
                message = message.replace(substring, replacement)

    command = input()

print(f'The decrypted message is: {message}')
