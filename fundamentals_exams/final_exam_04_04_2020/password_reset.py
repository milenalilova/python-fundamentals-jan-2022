password = input()
new_password = password

command = input().split(' ')

while command[0] != "Done":
    instruction = command[0]

    if instruction == "TakeOdd":
        current_password = new_password
        new_password = ''
        for i in range(len(current_password)):
            if i % 2 != 0:
                new_password += current_password[i]
        print(new_password)

    elif instruction == "Cut":
        index = int(command[1])
        length = int(command[2])
        new_password = new_password[0:index] + new_password[index + length:]
        print(new_password)

    elif instruction == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in new_password:
            while substring in new_password:
                new_password = new_password.replace(substring, substitute)
            print(new_password)
        else:
            print("Nothing to replace!")

    command = input().split(' ')

print(f"Your password is: {new_password}")
