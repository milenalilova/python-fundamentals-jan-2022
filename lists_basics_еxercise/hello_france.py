items = input().split("|")
budget = int(input())
condition = False
sum_new_prices = 0  # or make a list sum_new_prices = []
profit = 0
new_item_price_list = []

for current_item in items:
    item_info = current_item.split('->')
    item_type = item_info[0]
    item_price = float(item_info[1])
    condition = False

    if item_type == 'Clothes':
        if item_price <= 50:
            condition = True
    elif item_type == 'Shoes':
        if item_price <= 35:
            condition = True
    elif item_type == 'Accessories':
        if item_price <= 20.5:
            condition = True

    if condition:
        if budget >= item_price:
            budget -= item_price
            new_item_price = item_price + item_price * 0.4
            sum_new_prices += new_item_price
            profit += item_price * 0.4
            # print(f'{new_item_price:.2f}', end=' ')
            new_item_price_list.append(f'{new_item_price:.2f}')

print(' '.join(new_item_price_list))
print(f'Profit: {profit:.2f}')

if sum_new_prices + budget >= 150:    # or sum(sum_new_prices)
    print("Hello, France!")
else:
    print("Not enough money.")
