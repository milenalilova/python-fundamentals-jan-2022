number_of_cities = int(input())
tour_profit = 0
counter = 0

while counter < number_of_cities:
    city_name = input()
    owner_income = float(input())
    owner_expenses = float(input())

    counter += 1
    if counter % 15 == 0:
        owner_income -= 0.1 * owner_income

    elif counter % 3 == 0:
        owner_expenses += 0.5 * owner_expenses

    elif counter % 5 == 0:
        owner_income -= 0.1 * owner_income

    city_profit = owner_income - owner_expenses
    tour_profit += city_profit

    print(f'In {city_name} Burger Bus earned {city_profit:.2f} leva.')

print(f'Burger Bus total profit: {tour_profit:.2f} leva.')
