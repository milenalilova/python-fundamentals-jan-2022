text = input()
command = input()

while command != "Done":
    info = command.split(' ')
    action = info[0]

    if action == "Change":
        char = info[1]
        replacement = info[2]
        text = text.replace(char, replacement)
        print(text)

    elif action == "Includes":
        substring = info[1]
        if substring in text:
            print(True)
        else:
            print(False)

    elif action == "End":
        subtext = info[1]
        index = len(subtext)
        if text[-index:] == subtext:
            print(True)
        else:
            print(False)

    elif action == "Uppercase":
        text = text.upper()
        print(text)

    elif action == "FindIndex":
        char = info[1]
        for i in range(len(text)):
            if text[i] == char:
                print(i)
                break

    elif action == "Cut":
        start_index = int(info[1])
        count = int(info[2])
        end_index = start_index + count
        text = text[start_index:end_index]
        print(text)

    command = input()


# String Game Problem