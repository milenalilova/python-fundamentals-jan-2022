budget = float(input())
flower_price_per_kg = float(input())
loaf_count = 0
coloured_eggs = 0

eggs_price_per_pack = flower_price_per_kg * 0.75
milk_price_per_litre = flower_price_per_kg * 1.25
loaf_recipe_price = eggs_price_per_pack + flower_price_per_kg + milk_price_per_litre * 0.25

while budget > loaf_recipe_price:
    budget = budget - loaf_recipe_price
    loaf_count += 1
    coloured_eggs += 3
    if loaf_count % 3 == 0:
        coloured_eggs -= loaf_count - 2

print(f"You made {loaf_count} loaves of Easter bread! Now you have {coloured_eggs} eggs and {budget:.2f}BGN left.")
