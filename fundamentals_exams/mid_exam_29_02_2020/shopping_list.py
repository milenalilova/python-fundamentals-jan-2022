shopping_list = [el for el in input().split('!')]

command = input()

while command != "Go Shopping!":
    info = command.split(' ')
    action = info[0]
    item = info[1]

    if action == "Urgent":
        if item not in shopping_list:
            shopping_list.insert(0, item)

    elif action == "Unnecessary":
        if item in shopping_list:
            shopping_list.remove(item)

    elif action == "Correct":
        new_item = info[2]
        if item in shopping_list:
            index = shopping_list.index(item)
            shopping_list.remove(item)
            shopping_list.insert(index, new_item)

    elif action == "Rearrange":
        if item in shopping_list:
            shopping_list.remove(item)
            shopping_list.append(item)

    command = input()

print(', '.join(shopping_list))
