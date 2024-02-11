shopping_list = input().split('!')

while True:
    command = input()
    if command == 'Go Shopping!':
        break
    action = command.split(' ')[0]
    if action == 'Urgent':
        item = command.split(' ')[1]
        if item not in shopping_list:
            shopping_list.insert(0, item)
    if action == 'Unnecessary':
        item = command.split(' ')[1]
        if item in shopping_list:
            shopping_list.remove(item)
    if action == 'Correct':
        item = command.split(' ')[1]
        new_item = command.split(' ')[2]
        if item in shopping_list:
            index_new_item = shopping_list.index(item)
            shopping_list.insert(index_new_item, new_item)
            shopping_list.remove(item)
    if action == 'Rearrange':
        item = command.split(' ')[1]
        if item in shopping_list:
            shopping_list.remove(item)
            shopping_list.append(item)

print(', '.join(shopping_list))
