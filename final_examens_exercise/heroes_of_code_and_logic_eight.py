number_heroes = int(input())
heroes_dict = {}

for num in range(number_heroes):
    data = input().split(' ')
    hero_name = data[0]
    hit_points = int(data[1])
    mana_points = int(data[2])

    heroes_dict[hero_name] = []
    heroes_dict[hero_name].append(hit_points)
    heroes_dict[hero_name].append(mana_points)

command = input()

while command != 'End':
    info = command.split(' - ')
    action = info[0]
    current_hero_name = info[1]

    if action == 'CastSpell':
        mana_needed = int(info[2])
        spell_name = info[3]
        if heroes_dict[current_hero_name][1] >= mana_needed:
            heroes_dict[current_hero_name][1] -= mana_needed
            print(f"{current_hero_name} has successfully cast {spell_name} and now has"
                  f" {heroes_dict[current_hero_name][1]} MP!")
        else:
            print(f"{current_hero_name} does not have enough MP to cast {spell_name}!")

    elif action == 'TakeDamage':
        damage = int(info[2])
        attacker = info[3]
        heroes_dict[current_hero_name][0] -= damage
        if heroes_dict[current_hero_name][0] > 0:
            print(f"{current_hero_name} was hit for {damage} HP by {attacker} and now has"
                  f" {heroes_dict[current_hero_name][0]} HP left!")
        else:
            print(f"{current_hero_name} has been killed by {attacker}!")
            del heroes_dict[current_hero_name]

    elif action == 'Recharge':
        amount = int(info[2])
        diff = 200 - heroes_dict[current_hero_name][1]
        if diff >= amount:
            heroes_dict[current_hero_name][1] += amount
            print(f"{current_hero_name} recharged for {amount} MP!")
        else:
            heroes_dict[current_hero_name][1] += diff
            print(f"{current_hero_name} recharged for {diff} MP!")

    elif action == 'Heal':
        amount = int(info[2])
        diff = 100 - heroes_dict[current_hero_name][0]
        if diff >= amount:
            heroes_dict[current_hero_name][0] += amount
            print(f"{current_hero_name} healed for {amount} HP!")
        else:
            heroes_dict[current_hero_name][0] += diff
            print(f"{current_hero_name} healed for {diff} HP!")

    command = input()

for hero in heroes_dict.keys():
    print(f"{hero}\n  HP: {heroes_dict[hero][0]}\n  MP: {heroes_dict[hero][1]}")
