dwarf_dict = {}

command = input()

while command != "Once upon a time":
    dwarf_name, dwarf_hat_color, dwarf_physics = command.split(' <:> ')
    dwarf_physics = int(dwarf_physics)

    if dwarf_name not in dwarf_dict.keys():
        dwarf_dict[dwarf_name] = {dwarf_hat_color: dwarf_physics}
    elif dwarf_name in dwarf_dict.keys():
        if dwarf_hat_color not in dwarf_dict[dwarf_name].keys():
            dwarf_dict[dwarf_name][dwarf_hat_color] = dwarf_physics
        else:
            if dwarf_physics > dwarf_dict[dwarf_name][dwarf_hat_color]:
                dwarf_dict[dwarf_name][dwarf_hat_color] = dwarf_physics

    command = input()

flattened_dwarfs = []
for name, data in dwarf_dict.items():
    for color, physics in data.items():
        count = sum(1 for _, d in dwarf_dict.items() if color in d)
        flattened_dwarfs.append((color, name, physics, count))

# Sort the list of dwarfs
sorted_dwarfs = sorted(flattened_dwarfs, key=lambda x: (-x[2], -x[3]))

# Print the dwarfs
for color, name, physics, _ in sorted_dwarfs:
    print(f"({color}) {name} <-> {physics}")
