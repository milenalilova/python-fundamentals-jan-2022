products_dict = {}

command = input()

while command != "buy":
    data = command.split(' ')
    product_name = data[0]
    product_price = float(data[1])
    product_qty = int(data[2])

    if product_name not in products_dict.keys():
        products_dict[product_name] = [product_price, product_qty]
    else:
        products_dict[product_name] = [product_price, (product_qty + products_dict[product_name][1])]

    command = input()

for product in products_dict:
    total_price = products_dict[product][0] * products_dict[product][1]
    print(f"{product} -> {total_price:.2f}")
