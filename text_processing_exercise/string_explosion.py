text = input()
new_text = list()
strength = 0

for ch in text:
    if ch.isdigit():
        strength += int(ch)
        strength -= 1
        continue
    else:
        if strength < 1:
            new_text.append(ch)
        else:
            if ch == ">":
                new_text.append(ch)
            else:
                strength -= 1
                continue
print("".join(new_text))


# enter = input()
#
# new_list = ""
# explosion = 0
# lenght = 0
#
# while lenght < len(enter):
#     for i in range(len(enter)):
#         if not enter[i] == ">" and explosion > 0:
#             explosion -= 1
#         elif enter[i] == ">":
#             explosion += int(enter[i + 1])
#             new_list += enter[i]
#         else:
#             new_list += enter[i]
#         lenght += 1
# print(new_list)
