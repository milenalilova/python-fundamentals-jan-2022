number_lines = int(input())
register_dict = {}

for num in range(number_lines):
    command = input().split(' ')
    username = command[1]

    if command[0] == 'register':
        license_plate_number = command[2]
        if username not in register_dict:
            register_dict[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {register_dict[username]}")

    elif command[0] == 'unregister':
        if username not in register_dict:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del register_dict[username]

for key, value in register_dict.items():
    print(f"{key} => {value}")
