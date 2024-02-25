data = input().split(' ')
searched_products = input().split(' ')
shop_stock = {}

for prod in range(0, len(data), 2):
    product = data[prod]
    quantity = data[prod + 1]
    shop_stock[product] = int(quantity)

for item in searched_products:
    if item in shop_stock.keys():
        print(f"We have {shop_stock[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
