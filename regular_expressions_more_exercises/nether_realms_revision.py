import re

demon_names = input().split(',')
demon_names = [name.strip() for name in demon_names]
health_pat = r"([^0-9\+\-\*\/\.])"
base_damage_path = r"([\+\-]?([0-9]+)(\.[0-9]+)?)"

for name in sorted(demon_names):
    health = 0
    base_damage = 0
    alternators = [ch for ch in name if ch == '*' or ch == '/']

    health_match = re.findall(health_pat, name)
    for ch in health_match:
        health += ord(ch)

    damage_match = re.finditer(base_damage_path, name)
    for match in damage_match:
        base_damage += float(match.group())
    for alt in alternators:
        if alt == '*':
            base_damage *= 2
        elif alt == '/':
            base_damage /= 2

    print(f"{name} - {health} health, {base_damage:.2f} damage")
