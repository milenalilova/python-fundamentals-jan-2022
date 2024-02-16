command = input()
to_do_notes = [0] * 10

while command != "End":
    notes_info = command.split('-')
    importance = int(
        notes_info[0]) - 1  # There are 10 notes. We don't have 0 note or index 10, and we can have note 10.
    note = notes_info[1]

    to_do_notes.pop(importance)
    to_do_notes.insert(importance, note)

    command = input()

result = [x for x in to_do_notes if x != 0]
print(result)
