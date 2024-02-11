budget = float(input())
flower_price_kg = float(input())
coloured_eggs = 0
breads_made = 0

eggs_price_pack = flower_price_kg * 0.75
milk_price_ltr = flower_price_kg + flower_price_kg * 0.25
bread_price = eggs_price_pack + flower_price_kg + milk_price_ltr / 4

while budget > bread_price:
    breads_made += 1
    coloured_eggs += 3
    budget -= bread_price

    if breads_made % 3 == 0:
        coloured_eggs -= breads_made - 2

print(f"You made {breads_made} loaves of Easter bread! Now you have {coloured_eggs} eggs and {budget:.2f}BGN left.")
