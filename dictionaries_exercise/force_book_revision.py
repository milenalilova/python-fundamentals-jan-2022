force_dict = {}


def join_force_side(force_user, force_side):
    if force_side not in force_dict:
        force_dict[force_side] = []
    if force_user not in [user for users in force_dict.values() for user in users]:
        force_dict[force_side].append(force_user)


def switch_force_side(force_user, force_side):
    for side, users in force_dict.items():
        if force_user in users:
            users.remove(force_user)
            break
    if force_side not in force_dict:
        force_dict[force_side] = []
    force_dict[force_side].append(force_user)
    print(f"{force_user} joins the {force_side} side!")


while True:
    command = input()
    if command == "Lumpawaroo":
        break

    if " | " in command:
        force_side, force_user = command.split(" | ")
        join_force_side(force_user, force_side)
    elif " -> " in command:
        force_user, force_side = command.split(" -> ")
        switch_force_side(force_user, force_side)

for force_side, force_users in force_dict.items():
    if force_users:
        print(f"Side: {force_side}, Members: {len(force_users)}")
        for user in force_users:
            print(f"! {user}")

#  Variant 2

# command = input()
# force_dict = {}
#
# while command != "Lumpawaroo":
#     if '|' in command:
#         info = command.split(' | ')
#         force_side = info[0]
#         force_user = info[1]
#
#         if force_side not in force_dict:
#             force_dict[force_side] = []
#
#         user_in_sides = False
#         for user in force_dict.values():
#             if force_user in user:
#                 user_in_sides = True
#                 break
#         if not user_in_sides:
#             force_dict[force_side] += [force_user]
#
#     elif ' -> ' in command:
#         info = command.split(' -> ')
#         force_user = info[0]
#         force_side = info[1]
#
#         for side, user in force_dict.items():
#             if force_user in user:
#                 user.remove(force_user)
#
#         if force_side not in force_dict:
#             force_dict[force_side] = [force_user]
#         else:
#             force_dict[force_side].append(force_user)
#
#         print(f"{force_user} joins the {force_side} side!")
#
#     command = input()
#
# for k, v in force_dict.items():
#     if len(v) > 0:
#         result = f"Side: {k}, Members: {len(v)}"
#         print(result)
#     for el in v:
#         print(f"! {el}")
