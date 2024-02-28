from collections import defaultdict, OrderedDict


def calculate_average_stats(dragons):
    total_damage = sum(dragon['damage'] for dragon in dragons)
    total_health = sum(dragon['health'] for dragon in dragons)
    total_armor = sum(dragon['armor'] for dragon in dragons)
    count = len(dragons)

    avg_damage = total_damage / count
    avg_health = total_health / count
    avg_armor = total_armor / count

    return avg_damage, avg_health, avg_armor


n = int(input())
dragons_by_type = defaultdict(OrderedDict)

# Process input
for _ in range(n):
    dragon_data = input().split()
    dragon_type, dragon_name = dragon_data[0], dragon_data[1]
    damage = int(dragon_data[2]) if dragon_data[2] != "null" else 45
    health = int(dragon_data[3]) if dragon_data[3] != "null" else 250
    armor = int(dragon_data[4]) if dragon_data[4] != "null" else 10

    dragons = dragons_by_type[dragon_type]
    existing_dragon = dragons.get(dragon_name)
    if existing_dragon:
        existing_dragon['damage'] = damage
        existing_dragon['health'] = health
        existing_dragon['armor'] = armor
    else:
        dragons[dragon_name] = {'name': dragon_name, 'damage': damage, 'health': health, 'armor': armor}

# Print output
for dragon_type, dragons in dragons_by_type.items():
    avg_damage, avg_health, avg_armor = calculate_average_stats(dragons.values())
    print(f"{dragon_type}::({avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f})")
    for dragon in sorted(dragons.values(), key=lambda x: x['name']):
        print(f"-{dragon['name']} -> damage: {dragon['damage']}, health: {dragon['health']}, armor: {dragon['armor']}")
