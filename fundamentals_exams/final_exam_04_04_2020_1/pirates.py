cities = input().split('||')
cities_dict = {}

while cities[0] != "Sail":
    city = cities[0]
    population = int(cities[1])
    gold = int(cities[2])

    if city not in cities_dict.keys():
        cities_dict[city] = {'population': population, 'gold': gold}
    else:
        cities_dict[city]['population'] += population
        cities_dict[city]['gold'] += gold

    cities = input().split('||')

line = input().split('=>')

while line[0] != "End":
    event = line[0]
    town = line[1]

    if event == "Plunder":
        people = int(line[2])
        gold = int(line[3])
        cities_dict[town]['population'] -= people
        cities_dict[town]['gold'] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        if cities_dict[town]['population'] <= 0 or cities_dict[town]['gold'] <= 0:
            print(f"{town} has been wiped off the map!")
            del cities_dict[town]

    elif event == "Prosper":
        gold = int(line[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities_dict[town]['gold'] += gold
            total_gold = cities_dict[town]['gold']
            print(f"{gold} gold added to the city treasury. {town} now has {total_gold} gold.")

    line = input().split('=>')

if cities_dict:
    print(f"Ahoy, Captain! There are {len(cities_dict)} wealthy settlements to go to:")

    for town, info in cities_dict.items():
        population = cities_dict[town]['population']
        gold = cities_dict[town]['gold']
        print(f"{town} -> Population: {population} citizens, Gold: {gold} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
