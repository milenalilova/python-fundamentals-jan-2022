number_of_cars = int(input())
cars_data = {}

for num in range(number_of_cars):
    data = input().split('|')
    car = data[0]
    mileage = int(data[1])
    fuel = int(data[2])

    cars_data[car] = []
    cars_data[car].append(mileage)
    cars_data[car].append(fuel)

command = input()

while command != 'Stop':
    info = command.split(' : ')
    action = info[0]
    current_car = info[1]

    if action == 'Drive':
        distance = int(info[2])
        needed_fuel = int(info[3])

        if cars_data[current_car][1] < needed_fuel:
            print(f'Not enough fuel to make that ride')
        else:
            cars_data[current_car][0] += distance
            cars_data[current_car][1] -= needed_fuel
            print(f"{current_car} driven for {distance} kilometers. {needed_fuel} liters of fuel consumed.")

        if cars_data[current_car][0] >= 100000:
            print(f"Time to sell the {current_car}!")
            del cars_data[current_car]

    elif action == 'Refuel':
        refill_fuel = int(info[2])
        diff = 75 - cars_data[current_car][1]
        if diff >= refill_fuel:
            cars_data[current_car][1] += refill_fuel
            print(f"{current_car} refueled with {refill_fuel} liters")
        else:
            cars_data[current_car][1] += diff
            print(f"{current_car} refueled with {diff} liters")

    elif action == 'Revert':
        kilometers = int(info[2])
        cars_data[current_car][0] -= kilometers
        if cars_data[current_car][0] < 10000:
            cars_data[current_car][0] = 10000
        else:
            print(f"{current_car} mileage decreased by {kilometers} kilometers")

    command = input()

for car_key in cars_data.keys():
    print(f"{car_key} -> Mileage: {cars_data[car_key][0]} kms, Fuel in the tank: {cars_data[car_key][1]} lt.")
