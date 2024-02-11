string = input()
capitals = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cap_indexes = []

for i in range(len(string)):
    if string[i] in capitals:
        # cap_indexes.append(string[i])
        cap_indexes.append(i)

print(cap_indexes)
