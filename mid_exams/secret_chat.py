message = input()
command = input()

while command != 'Reveal':
    info = command.split(':|:')
    instruction = info[0]

    if instruction == 'InsertSpace':
        index = int(info[1])
        message = message[:index] + ' ' + message[index:]
        print(message)

    elif instruction == 'Reverse':
        substring = info[1]
        if substring in message:
            message = message.replace(substring, '', 1)
            substring = substring[::-1]
            message = message + substring
            print(message)
        else:
            print('error')

    elif instruction == 'ChangeAll':
        substring = info[1]
        replacement = info[2]
        message = message.replace(substring, replacement)
        print(message)

    # print(message)
    command = input()

print(f'You have a new text message: {message}')
