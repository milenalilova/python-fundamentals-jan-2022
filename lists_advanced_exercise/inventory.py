def inventory(data):

    while True:
        command = input().split(' - ')
        if command[0] == 'Craft!':
            print(', '.join(data))
            break
        elif command[0] == 'Collect':
            item = command[1]
            if item not in data:
                data.append(item)
            else:
                continue
        elif command[0] == 'Drop':
            item = command[1]
            if item in data:
                data.remove(item)
        elif command[0] == 'Combine Items':
            items = command[1].split(':')
            old_item = items[0]
            new_item = items[1]
            if old_item in data:
                new_index = data.index(old_item)
                data.insert((new_index + 1), new_item)
            else:
                continue
        elif command[0] == 'Renew':
            item = command[1]
            if item in data:
                data.remove(item)
                data.append(item)
            else:
                continue


current_data = input().split(', ')
inventory(current_data)


# There is a shorter way with functions (see video for tas Inventory)