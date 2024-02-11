command = input()
cities_dict = {}

while command != 'Sail':
    data = command.split('||')
    city = data[0]
    population = int(data[1])
    gold = int(data[2])
    if city not in cities_dict:
        cities_dict[city] = []
        cities_dict[city].append(population)
        cities_dict[city].append(gold)
    else:
        cities_dict[city][0] += population
        cities_dict[city][1] += gold

    command = input()

events = input()

while events != 'End':
    info = events.split('=>')
    action = info[0]
    current_city = info[1]

    if action == 'Plunder':
        people = int(info[2])
        current_gold = int(info[3])
        print(f'{current_city} plundered! {current_gold} gold stolen, {people} citizens killed.')
        cities_dict[current_city][0] -= people
        cities_dict[current_city][1] -= current_gold
        if cities_dict[current_city][0] <= 0 or cities_dict[current_city][1] <= 0:
            print(f"{current_city} has been wiped off the map!")
            del cities_dict[current_city]

    elif action == 'Prosper':
        current_city = info[1]
        current_gold = int(info[2])
        if current_gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities_dict[current_city][1] += current_gold
            print(f"{current_gold} gold added to the city treasury. {current_city} now has "
                  f"{cities_dict[current_city][1]} gold.")

    events = input()

if len(cities_dict) <= 0:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')
else:
    print(f"Ahoy, Captain! There are {len(cities_dict)} wealthy settlements to go to:")
    for el in cities_dict.keys():
        print(f"{el} -> Population: {cities_dict[el][0]} citizens, Gold: {cities_dict[el][1]} kg")
