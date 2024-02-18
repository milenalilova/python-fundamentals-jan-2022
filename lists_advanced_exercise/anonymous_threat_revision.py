line = input().split(' ')

command = input()

while command != "3:1":
    data = command.split(' ')
    action = data[0]

    if action == "merge":
        start_index = int(data[1])
        end_index = int(data[2])
        new_string = ''

        if start_index < 0:
            start_index = 0
        if end_index > len(line) - 1:
            end_index = len(line) - 1

        for i in range(start_index, end_index + 1):
            new_string += line[i]
        line = line[0:start_index] + line[end_index + 1:]
        line.insert(start_index, new_string)

    elif action == "divide":
        index = int(data[1])
        partitions = int(data[2])

        new_subs = []
        current_sub = line[index]

        if len(current_sub) % partitions == 0:
            partitions_index = int(len(current_sub) / partitions)
            for i in range(0, len(current_sub), partitions_index):
                new_subs.append(current_sub[i:partitions_index + i])
            line.pop(index)
            current_index = index
            for el in new_subs:
                line.insert(current_index, el)
                current_index += 1

        else:
            partitions_index = len(current_sub) // partitions

            for i in range(0, len(current_sub), partitions_index):
                new_subs.append(current_sub[i:partitions_index + i])
            line.pop(index)
            last_sub = new_subs[-1]
            new_subs.pop(-1)
            new_subs[-1] += last_sub

            current_index = index
            for el in new_subs:
                line.insert(current_index, el)
                current_index += 1

    command = input()

print(' '.join(line))

# Should be optimised
