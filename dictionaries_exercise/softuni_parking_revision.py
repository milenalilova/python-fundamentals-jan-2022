n = int(input())
parked_cars_dict = {}

for i in range(n):
    command = input().split(' ')
    action = command[0]
    username = command[1]

    if action == "register":
        license_plate_number = command[2]
        if username not in parked_cars_dict.keys():
            parked_cars_dict[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")

    elif action == "unregister":
        if username not in parked_cars_dict.keys():
            print(f"ERROR: user {username} not found")
        else:
            del parked_cars_dict[username]
            print(f"{username} unregistered successfully")

for k, v in parked_cars_dict.items():
    print(f"{k} => {v}")
