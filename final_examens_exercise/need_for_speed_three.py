number_of_cars = int(input())
car_data = dict()

for num in range(number_of_cars):
    data = input().split('|')
    car = data[0]
    mileage = int(data[1])
    fuel = int(data[2])
    car_data[car] = {}
    car_data[car][mileage] = fuel

command = input()

while command != 'Stop':
    info = command.split(' : ')
    action = info[0]
    current_car = info[1]

    if action == 'Drive':
        distance = int(info[2])
        current_fuel = int(info[3])
        for key in car_data[current_car]:
            if car_data[current_car][key] < current_fuel:
                print("Not enough fuel to make that ride")
            else:
                new_key = key + distance
                car_data[current_car][key] -= current_fuel
                car_data[current_car][new_key] = car_data[current_car][key]
                del car_data[current_car][key]
                print(f"{current_car} driven for {distance} kilometers. {current_fuel} liters of fuel consumed.")
                if new_key >= 100000:
                    print(f"Time to sell the {current_car}!")
                    del car_data[current_car]
            break

    elif action == 'Refuel':
        ref_fuel = int(info[2])
        for key in car_data[current_car]:
            if car_data[current_car][key] + ref_fuel > 75:
                diff = 75 - car_data[current_car][key]
                car_data[current_car][key] = 75
                print(f"{current_car} refueled with {diff} liters")
            else:
                car_data[current_car][key] += ref_fuel
                print(f"{current_car} refueled with {ref_fuel} liters")
            break

    elif action == 'Revert':
        kilometers = int(info[2])
        for key in car_data[current_car]:
            new_key = key - kilometers
            if new_key >= 10000:
                print(f"{current_car} mileage decreased by {kilometers} kilometers")
            else:
                new_key = 10000
            car_data[current_car][new_key] = car_data[current_car][key]
            del car_data[current_car][key]
            break

    command = input()

for k, v in car_data.items():
    for nested_key, nested_value in v.items():
        print(f"{k} -> Mileage: {nested_key} kms, Fuel in the tank: {nested_value} lt.")
