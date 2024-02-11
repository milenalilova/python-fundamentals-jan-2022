command = input()
force_book_dict = {}

while command != 'Lumpawaroo':
    if "|" in command:
        info = command.split(" | ")
        force_side = info[0]
        force_user = info[1]

        if force_side not in force_book_dict:
            force_book_dict[force_side] = []
            for key, value in force_book_dict.items():
                if force_user not in value:
                    force_book_dict[force_side] += [force_user]

    elif "->" in command:
        info = command.split(" -> ")
        force_user = info[0]
        force_side = info[1]

        for key in force_book_dict:
            if force_user in force_book_dict[key]:
                if len(force_book_dict[key]) > 1:
                    force_book_dict[key].pop(force_user)
                    print(f"{force_user} joins the {force_side} side!")
                    break
                else:
                    del force_book_dict[key]
                    print(f"{force_user} joins the {force_side} side!")
                    break
            else:
                force_book_dict[force_side] += [force_user]
                print(f"{force_user} joins the {force_side} side!")
                break

        if force_side not in force_book_dict:
            force_book_dict[force_side] = [force_user]
        else:
            force_book_dict[force_side].append(force_user)

command = input()

for key, value in force_book_dict.items():
    print(f"Side: {key}, Members: {len(value)}")
    for i in range(len(value)):
        print(f"! {value[i]}")
