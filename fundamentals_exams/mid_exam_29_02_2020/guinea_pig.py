quantity_food_kg = float(input())
quantity_hay_kg = float(input())
quantity_cover_kg = float(input())
guineas_weight_kg = float(input())

quantity_food_gr = quantity_food_kg * 1000
quantity_hay_gr = quantity_hay_kg * 1000
quantity_cover_gr = quantity_cover_kg * 1000
guineas_weight_gr = guineas_weight_kg * 1000

for day in range(1, 31):
    quantity_food_gr -= 300
    if day % 2 == 0:
        quantity_hay_gr -= quantity_food_gr * 0.05
    if day % 3 == 0:
        quantity_cover_gr -= guineas_weight_gr / 3
    if quantity_food_gr <= 0 or quantity_hay_gr <= 0 or quantity_cover_gr <= 0:
        print("Merry must go to the pet store!")
        break
else:
    print(
        f"Everything is fine! Puppy is happy! Food: {quantity_food_gr/1000:.2f}, Hay: {quantity_hay_gr/1000:.2f}, Cover: {quantity_cover_gr/1000:.2f}.")
