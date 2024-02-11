usernames = input().split(", ")
elements = ["_", "-"]

valid_usernames = [x for x in usernames if 3 <= len(x) <= 16]
users = [x for x in valid_usernames if x.isalnum() or "_" in x or "-" in x]


print('\n'.join(users))


# import string
#
#
# def valid_username(data):
#     flag = 0  # or condition = False
#     expected_elements = string.digits + string.ascii_letters + "_" + "-"
#     for name in data:
#         flag = 0
#         if 3 > len(name) or len(name) > 16:
#             flag = 1
#         elif len([x for x in name if x in expected_elements]) != len(name):
#             flag = 1
#         elif flag == 0:
#             print(name)


d = input().split(", ")
valid_username(d)
