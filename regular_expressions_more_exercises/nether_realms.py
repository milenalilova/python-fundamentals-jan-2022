import re

text = input()
health = 0
damage = 0
demons_data_dict = {}

pattern = r'[^\d\+\-\*\/\.]'
num_pattern = r'-?[0-9]+\.?[0-9]?'

name = re.split('[,, ]', text)
current_name = [el for el in name if el != '']
current_name = sorted(current_name)

for el in current_name:
    if el not in demons_data_dict:
        demons_data_dict[el] = {}

for item in current_name:
    matches = re.findall(pattern, item)

    for match in matches:
        health += ord(match)
    demons_data_dict[item]['health'] = health
    health = 0

for item in current_name:
    result = re.findall(num_pattern, item)
    for num in result:
        damage += float(num)

    for char in item:
        if char == '*':
            damage = damage * 2
        elif char == '/':
            damage = damage / 2
    demons_data_dict[item]['damage'] = f'{damage:.2f}'
    damage = 0

for key, value in demons_data_dict.items():
    print(f"{key} - {demons_data_dict[key]['health']} health, {demons_data_dict[key]['damage']} damage")
