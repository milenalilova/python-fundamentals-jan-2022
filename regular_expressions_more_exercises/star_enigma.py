import re

n = int(input())
special_letters = 'starSTAR'
letters_count = 0
pattern = r'@([a-zA-Z]+)[^\@\-\!\:\>]*:(\d+)[^\@\-\!\:\>]*!([A|D])![^\@\-\!\:\>]*->(\d+)'

attacked_planets = []
destroyed_planets = []

for line in range(n):
    text = input()
    new_text = ''

    for char in text:
        if char in special_letters:
            letters_count += 1

    for char in text:
        new_char = chr(ord(char) - letters_count)
        new_text += new_char

    letters_count = 0

    matches = re.finditer(pattern, new_text)
    if matches:
        for match in matches:
            planet = match.group(1)
            population = match.group(2)
            attack_type = match.group(3)
            soldier_count = match.group(4)

            if attack_type == 'A':
                attacked_planets.append(planet)
            elif attack_type == 'D':
                destroyed_planets.append(planet)

print(f"Attacked planets: {len(attacked_planets)}")
if len(attacked_planets) > 0:
    for item in sorted(attacked_planets):
        print(f"-> {item}")

print(f"Destroyed planets: {len(destroyed_planets)}")
if len(destroyed_planets) > 0:
    for el in sorted(destroyed_planets):
        print(f"-> {el}")


