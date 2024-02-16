wagons_num = int(input())

train = [0] * wagons_num

command = input()

while command != "End":
    train_info = command.split(' ')
    action = train_info[0]

    if action == "add":
        people = int(train_info[1])
        train[-1] += people

    elif action == "insert":
        index = int(train_info[1])
        people = int(train_info[2])
        train[index] += people

    elif action == "leave":
        index = int(train_info[1])
        people = int(train_info[2])
        train[index] -= people

    command = input()

print(train)
