journal_items = input().split(', ')

command = input()

while command != "Craft!":
    data = command.split(' - ')
    action = data[0]
    item = data[1]

    if action == "Collect":
        if item not in journal_items:
            journal_items.append(item)

    elif action == "Drop":
        if item in journal_items:
            journal_items.remove(item)

    elif action == "Combine Items":
        old_item = item.split(':')[0]
        new_item = item.split(':')[1]
        if old_item in journal_items:
            index = journal_items.index(old_item)
            journal_items.insert(index + 1, new_item)

    elif action == "Renew":
        if item in journal_items:
            journal_items.remove(item)
            journal_items.append(item)

    command = input()

print(', '.join(journal_items))
