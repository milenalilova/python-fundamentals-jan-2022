line = input().split('>>')
initial_tax = 0
tax_increase = 0
tax_decline = 0
total_taxes = 0

for i in range(len(line)):
    data = line[i]

    car_type = data.split(' ')[0]
    years_taxed = int(data.split(' ')[1])
    km_travelled = int(data.split(' ')[2])

    if car_type == 'family':
        initial_tax = 50
        tax_decline = 5
        tax_increase = 12
        taxes_to_pay = initial_tax - (years_taxed * 5) + (km_travelled // 3000 * 12)
        total_taxes += taxes_to_pay
        print(f"A {car_type} car will pay {taxes_to_pay:.2f} euros in taxes.")

    elif car_type == 'heavyDuty':
        initial_tax = 80
        tax_decline = 8
        tax_increase = 14
        taxes_to_pay = initial_tax - (years_taxed * tax_decline) + (km_travelled // 9000 * tax_increase)
        total_taxes += taxes_to_pay

        print(f"A {car_type} car will pay {taxes_to_pay:.2f} euros in taxes.")

    elif car_type == 'sports':
        initial_tax = 100
        tax_decline = 9
        tax_increase = 18
        taxes_to_pay = initial_tax - (years_taxed * tax_decline) + (km_travelled // 2000 * tax_increase)
        total_taxes += taxes_to_pay

        print(f"A {car_type} car will pay {taxes_to_pay:.2f} euros in taxes.")

    else:
        print('Invalid car type.')

print(f'The National Revenue Agency will collect {total_taxes:.2f} euros in taxes.')
