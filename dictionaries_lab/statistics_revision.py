data = input().split(' ')
shop_stock = {}
total_products = 0

while data[0] != 'statistics':
    product = data[0]
    product = product[0:-1]
    quantity = int(data[1])

    if product not in shop_stock.keys():
        shop_stock[product] = 0
    shop_stock[product] += quantity

    total_products += quantity

    data = input().split(' ')

result = "Products in stock:\n"
for k, v in shop_stock.items():
    result += f"- {k}: {v}\n"

print(result.strip())
print(f"Total Products: {len(shop_stock)}")
print(f"Total Quantity: {total_products}")
