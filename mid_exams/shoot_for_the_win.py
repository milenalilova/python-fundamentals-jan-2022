targets = list(map(int, input().split(' ')))
shot_targets = 0

while True:
    command = input()
    if command == 'End':
        break
    index = int(command)
    if -1 < index < len(targets):
        if targets[index] > -1:
            value = targets[index]
            targets[index] = -1
            shot_targets += 1
            for target in range(len(targets)):
                if targets[target] > -1:
                    if targets[target] > value:
                        targets[target] -= value
                    else:
                        targets[target] += value
targets = list(map(str, targets))
print(f"Shot targets: {shot_targets} -> {' '.join(targets)} ")
