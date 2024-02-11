# notes = input()
# to_do_list = [""] * 11  # OR to_do_list = ["" for i in range(11)] notes are maximum 10, so we can have position 10
#
# while notes != 'End':
#     info = notes.split('-')
#     importance = int(info[0])
#     note = info[1]
#     to_do_list.pop(importance)
#     to_do_list.insert(importance, note)
#
#     notes = input()
#
# result = [element for element in to_do_list if element != ""]
#
# print(result)


notes = input()
to_do_list = [""] * 11  # OR to_do_list = ["" for i in range(11)] notes are maximum 10, so we can have position 10

while notes != 'End':
    info = notes.split('-')
    importance = int(info[0])
    note = info[1]
    to_do_list[importance] = note
    notes = input()

result = [element for element in to_do_list if element != ""]

print(result)
