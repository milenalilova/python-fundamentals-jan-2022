info = input()
phonebook_dict = {}

while '-' in info:
    info = info.split('-')
    name = info[0]
    phone_number = info[1]
    phonebook_dict[name] = phone_number

    info = input()

n = int(info)
for i in range(n):
    current_name = input()
    if current_name in phonebook_dict.keys():
        print(f"{current_name} -> {phonebook_dict[current_name]}")
    else:
        print(f"Contact {current_name} does not exist.")
