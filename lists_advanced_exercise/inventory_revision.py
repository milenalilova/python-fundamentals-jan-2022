collection = input().split(', ')

command = input()

while command != "Craft!":
    info = command.split(' - ')
    action = info[0]

    if action == "Collect":
        item = info[1]
        if item not in collection:
            collection.append(item)

    elif action == "Drop":
        item = info[1]
        if item in collection:
            collection.remove(item)

    elif action == "Combine Items":
        items = info[1]
        old_item = items.split(':')[0]
        new_item = items.split(':')[1]
        if old_item in collection:
            index = collection.index(old_item)
            index += 1
            collection.insert(index, new_item)

    elif action == "Renew":
        item = info[1]
        if item in collection:
            collection.remove(item)
            collection.append(item)

    command = input()

print(', '.join(collection))
