num_cars = int(input())
cars_dict = {}

for n in range(num_cars):
    car_info = input().split('|')
    car = car_info[0]
    mileage = int(car_info[1])
    fuel = int(car_info[2])
    cars_dict[car] = {'mileage': mileage, 'fuel': fuel}

command = input().split(' : ')

while command[0] != "Stop":
    instruction = command[0]
    car = command[1]

    if instruction == "Drive":
        distance = int(command[2])
        fuel = int(command[3])
        if cars_dict[car]['fuel'] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars_dict[car]['mileage'] += distance
            cars_dict[car]['fuel'] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars_dict[car]['mileage'] >= 100000:
                del cars_dict[car]
                print(f"Time to sell the {car}!")

    elif instruction == "Refuel":
        fuel = int(command[2])
        if cars_dict[car]['fuel'] + fuel > 75:
            fuel = 75 - cars_dict[car]['fuel']
        cars_dict[car]['fuel'] += fuel
        print(f"{car} refueled with {fuel} liters")

    elif instruction == "Revert":
        kilometers = int(command[2])
        cars_dict[car]['mileage'] -= kilometers
        if cars_dict[car]['mileage'] < 10000:
            cars_dict[car]['mileage'] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input().split(' : ')

for car, info in cars_dict.items():
    mileage = cars_dict[car]['mileage']
    fuel = cars_dict[car]['fuel']
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")
