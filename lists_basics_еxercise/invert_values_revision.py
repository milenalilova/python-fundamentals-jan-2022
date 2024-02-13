line = input()
line_list = line.split(' ')
new_list = []

for i in range(len(line_list)):
    num = int(line_list[i])
    if num <= 0:
        new_list.append(abs(num))
    else:
        new_list.append(num * -1)

print(new_list)
