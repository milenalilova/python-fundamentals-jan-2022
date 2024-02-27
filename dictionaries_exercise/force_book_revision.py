command = input()
force_dict = {}

while command != "Lumpawaroo":
    if '|' in command:
        info = command.split(' | ')
        force_side = info[0]
        force_user = info[1]

        if force_side not in force_dict:
            force_dict[force_side] = []

        user_in_sides = False
        for user in force_dict.values():
            if force_user in user:
                user_in_sides = True
                break
        if not user_in_sides:
            force_dict[force_side] += [force_user]

    elif ' -> ' in command:
        info = command.split(' -> ')
        force_user = info[0]
        force_side = info[1]

        for side, user in force_dict.items():
            if force_user in user:
                user.remove(force_user)

        if force_side not in force_dict:
            force_dict[force_side] = [force_user]
        else:
            force_dict[force_side].append(force_user)

        print(f"{force_user} joins the {force_side} side!")

    command = input()

for k, v in force_dict.items():
    if len(v) > 0:
        result = f"Side: {k}, Members: {len(v)}"
        print(result)
    for el in v:
        print(f"! {el}")
