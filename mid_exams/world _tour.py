stops_list = input()

command = input()

while command != 'Travel':

    info = command.split(':')
    action = info[0]

    if action == 'Add Stop':
        index = int(info[1])
        string = info[2]
        if 0 <= index < len(stops_list):
            stops_list = stops_list[0:index] + string + stops_list[index:]

    elif action == 'Remove Stop':
        start_index = int(info[1])
        end_index = int(info[2])
        if 0 <= start_index < len(stops_list) and 0 <= end_index < len(stops_list):
            stops_list = stops_list[:start_index] + stops_list[end_index+1:]

    elif action == 'Switch':
        old_string = info[1]
        new_string = info[2]
        if old_string in stops_list:
            stops_list = stops_list.replace(old_string, new_string)

    print(stops_list)
    command = input()

print(f'Ready for world tour! Planned stops: {stops_list}')
