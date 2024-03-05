message = input()

command = input().split(':|:')

while command[0] != 'Reveal':
    instruction = command[0]
    has_changed = True

    if instruction == "InsertSpace":
        index = int(command[1])
        message = message[:index] + ' ' + message[index:]

    elif instruction == "Reverse":
        substring = command[1]
        if substring in message:
            message = message.replace(substring, '')
            message += substring[::-1]
        else:
            has_changed = False
            print("error")

    elif instruction == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        while substring in message:
            message = message.replace(substring, replacement)

    if has_changed:
        print(message)

    command = input().split(':|:')

print(f"You have a new text message: {message}")
