num_heroes = int(input())
heroes_dict = {}

for n in range(num_heroes):
    hero_info = input().split()
    hero_name = hero_info[0]
    hit_points = int(hero_info[1])
    mana_points = int(hero_info[2])
    heroes_dict[hero_name] = {'hit_points': hit_points, 'mana_points': mana_points}

command = input().split(' - ')

while command[0] != "End":
    action = command[0]
    hero_name = command[1]

    if action == "CastSpell":
        mana_points_needed = int(command[2])
        spell_name = command[3]
        if heroes_dict[hero_name]['mana_points'] >= mana_points_needed:
            heroes_dict[hero_name]['mana_points'] -= mana_points_needed
            mana_points_left = heroes_dict[hero_name]['mana_points']
            print(f"{hero_name} has successfully cast {spell_name} and now has {mana_points_left} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif action == "TakeDamage":
        damage = int(command[2])
        attacker = command[3]
        heroes_dict[hero_name]['hit_points'] -= damage
        hit_points_left = heroes_dict[hero_name]['hit_points']
        if hit_points_left > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {hit_points_left} HP left!")
        else:
            del heroes_dict[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")

    elif action == "Recharge":
        amount = int(command[2])
        if heroes_dict[hero_name]['mana_points'] + amount > 200:
            amount = 200 - heroes_dict[hero_name]['mana_points']
        heroes_dict[hero_name]['mana_points'] += amount
        print(f"{hero_name} recharged for {amount} MP!")

    elif action == "Heal":
        amount = int(command[2])
        if heroes_dict[hero_name]['hit_points'] + amount > 100:
            amount = 100 - heroes_dict[hero_name]['hit_points']
        heroes_dict[hero_name]['hit_points'] += amount
        print(f"{hero_name} healed for {amount} HP!")

    command = input().split(' - ')

for hero, info in heroes_dict.items():
    hit_points = heroes_dict[hero]['hit_points']
    mana_points = heroes_dict[hero]['mana_points']
    print(f"{hero}\n  HP: {hit_points}\n  MP: {mana_points}")
