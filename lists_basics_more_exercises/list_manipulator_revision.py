import sys

line = list(map(int, input().split(' ')))

command = input()

while command != "end":
    data = command.split(' ')
    manipulation = data[0]

    if manipulation == "exchange":
        idx = int(data[1])
        if idx < 0 or idx >= len(line):
            print("Invalid index")
        else:
            first_sublist = line[:idx + 1]
            second_sublist = line[idx + 1:]
            second_sublist.extend(first_sublist)
            line = second_sublist

    elif manipulation == "max":
        word = data[1]

        max_num = -sys.maxsize
        max_idx = None

        if word == "even":
            for i in range(len(line) - 1, -1, -1):
                if line[i] % 2 == 0 and line[i] > max_num:
                    max_num = line[i]
                    max_idx = i

        elif word == "odd":
            for i in range(len(line) - 1, -1, -1):
                if line[i] % 2 != 0 and line[i] > max_num:
                    max_num = line[i]
                    max_idx = i

        if max_idx is not None:
            print(max_idx)
        else:
            print("No matches")

    elif manipulation == "min":
        word = data[1]

        min_num = sys.maxsize
        min_idx = None

        if word == "even":
            for i in range(len(line) - 1, -1, -1):
                if line[i] % 2 == 0 and line[i] < min_num:
                    min_num = line[i]
                    min_idx = i

        elif word == "odd":
            for i in range(len(line) - 1, -1, -1):
                if line[i] % 2 != 0 and line[i] < min_num:
                    min_num = line[i]
                    min_idx = i
        if min_idx is not None:
            print(min_idx)
        else:
            print("No matches")

    elif manipulation == "first":
        count = int(data[1])
        word = data[2]

        if count > len(line):
            print("Invalid count")
        else:
            even_list = [x for x in line if x % 2 == 0]
            odd_list = [x for x in line if x % 2 != 0]
            current_list = []

            if word == "even":
                if len(even_list) < count:
                    count = len(even_list)
                current_list = even_list[:count]
            elif word == "odd":
                if len(odd_list) < count:
                    count = len(odd_list)
                current_list = odd_list[:count]

            print(current_list)

    elif manipulation == "last":
        count = int(data[1])
        word = data[2]

        if count > len(line):
            print("Invalid count")

        else:
            even_list = [x for x in line if x % 2 == 0]
            odd_list = [x for x in line if x % 2 != 0]
            current_list = []

            if word == "even":
                if len(even_list) < count:
                    count = len(even_list)
                current_list = even_list[-count:]
            elif word == "odd":
                if len(odd_list) < count:
                    count = len(odd_list)
                current_list = odd_list[-count:]

            print(current_list)

    command = input()

print(line)
