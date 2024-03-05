activation_key = input()

command = input().split('>>>')

while command[0] != 'Generate':
    instruction = command[0]

    if instruction == "Contains":
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif instruction == "Flip":
        type_lettres = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        substring = activation_key[start_index:end_index]

        if type_lettres == "Upper":
            substring = substring.upper()

        elif type_lettres == "Lower":
            substring = substring.lower()

        activation_key = activation_key[:start_index] + substring + activation_key[end_index:]
        print(activation_key)

    elif instruction == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        slice = activation_key[start_index:end_index]
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)

    command = input().split('>>>')

print(f"Your activation key is: {activation_key}")
