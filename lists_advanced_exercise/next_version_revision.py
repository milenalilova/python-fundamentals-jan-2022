version = list(map(int, input().split('.')))
next_version = []

if version[2] == 9:
    version[2] = 0
    if version[1] == 9:
        version[1] = 0
        version[0] += 1
    else:
        version[1] += 1
else:
    version[2] += 1

next_version.append(version[0])
next_version.append(version[1])
next_version.append(version[2])

print('.'.join(str(x) for x in next_version))
