lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
repairs_cost = 0
shield_count = 0

for fight in range(1, lost_fights_count + 1):
    if fight % 2 == 0:
        repairs_cost += helmet_price
    if fight % 3 == 0:
        repairs_cost += sword_price
    if fight % 6 == 0:
        repairs_cost += shield_price
        shield_count += 1
        if shield_count % 2 == 0:
            repairs_cost += armor_price

print(f"Gladiator expenses: {repairs_cost:.2f} aureus")
