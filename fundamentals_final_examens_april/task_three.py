capacity = int(input())

username_dict = {}

command = input()

while command != "Statistics":
    info = command.split("=")
    action = info[0]

    if action == "Add":
        username = info[1]
        sent = int(info[2])
        received = int(info[3])
        if username not in username_dict:
            username_dict[username] = []
            username_dict[username].append(sent)
            username_dict[username].append(received)

    elif action == "Message":
        sender = info[1]
        receiver = info[2]

        if sender in username_dict and receiver in username_dict:
            username_dict[sender][0] += 1
            username_dict[receiver][1] += 1
            sum_sender = username_dict[sender][0] + username_dict[sender][1]
            sum_receiver = username_dict[receiver][0] + username_dict[receiver][1]

            if sum_sender >= capacity:
                print(f"{sender} reached the capacity!")
                del username_dict[sender]

            if sum_receiver >= capacity:
                print(f"{receiver} reached the capacity!")
                del username_dict[receiver]

    elif action == "Empty":
        username = info[1]
        if username in username_dict:
            del username_dict[username]
        if username == "All":
            username_dict.clear()

    command = input()

print(f"Users count: {len(username_dict)}")
if len(username_dict) > 0:
    # print(f"Users count: {len(username_dict)}")
    for key, value in username_dict.items():
        number_messages = username_dict[key][0] + username_dict[key][1]
        print(f"{key} - {number_messages}")


# Messages Manager Problem