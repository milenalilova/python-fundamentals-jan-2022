command = input()
inventory_dict = {}

while command != 'stop':
    resource = command
    quantity = int(input())
    if resource not in inventory_dict.keys():
        inventory_dict[resource] = 0
    inventory_dict[resource] += quantity

    command = input()

for k, v in inventory_dict.items():
    print(f"{k} -> {v}")
