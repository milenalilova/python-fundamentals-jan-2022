number_of_cars = int(input())
car_data = dict()

for num in range(number_of_cars):
    data = input().split('|')
    car = data[0]
    mileage = int(data[1])
    fuel = int(data[2])

    # car_data = {car: {"mil": mileage, "fuel": fuel}}  It doesnt work! WHY???
    current_car_dict = {"mil": mileage, "fuel": fuel}
    car_data[car] = current_car_dict

command = input()

while command != "Stop":
    info = command.split(' : ')
    action = info[0]
    current_car = info[1]

    if action == "Drive":
        distance = int(info[2])
        current_fuel = int(info[3])

        if car_data[current_car]["fuel"] < current_fuel:
            print("Not enough fuel to make that ride")
        else:
            car_data[current_car]["mil"] += distance
            car_data[current_car]["fuel"] -= current_fuel
            print(f"{current_car} driven for {distance} kilometers. {current_fuel} liters of fuel consumed.")
        if car_data[current_car]["mil"] >= 100000:
            print(f"Time to sell the {current_car}!")
            del car_data[current_car]

    elif action == "Refuel":
        current_fuel = int(info[2])
        diff = 75 - car_data[current_car]["fuel"]
        if diff > current_fuel:
            car_data[current_car]["fuel"] += current_fuel
            print(f"{current_car} refueled with {current_fuel} liters")
        else:
            car_data[current_car]["fuel"] += diff
            print(f"{current_car} refueled with {diff} liters")

    elif action == "Revert":
        kilometers = int(info[2])
        car_data[current_car]["mil"] -= kilometers
        if car_data[current_car]["mil"] < 10000:
            car_data[current_car]["mil"] = 10000
        else:
            print(f"{current_car} mileage decreased by {kilometers} kilometers")

    command = input()

for car in car_data:
    print(f"{car} -> Mileage: {car_data[car]['mil']} kms, Fuel in the tank: {car_data[car]['fuel']} lt.")
