targets = [int(num) for num in input().split(' ')]
targets_shot = 0

command = input()

while command != "End":
    index = int(command)
    if 0 <= index < len(targets):
        current_value = targets[index]
        targets[index] = -1
        targets_shot += 1
        for target in range(len(targets)):
            if targets[target] != -1:
                if targets[target] > current_value:
                    targets[target] -= current_value
                else:
                    targets[target] += current_value

    command = input()

print(f"Shot targets: {targets_shot} -> {' '.join(map(str, targets))}")
