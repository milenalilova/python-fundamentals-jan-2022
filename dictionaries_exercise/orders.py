command = input()
products_dict = {}

while command != 'buy':
    data = command.split(' ')
    name = data[0]
    price = float(data[1])
    quantity = int(data[2])

    if name not in products_dict:
        products_dict[name] = [price, quantity]
    else:
        products_dict[name] = [price, (quantity + products_dict[name][1])]

    command = input()

for product in products_dict:
    total_price = products_dict[product][0] * products_dict[product][1]
    print(f"{product} -> {total_price:.2f}")
