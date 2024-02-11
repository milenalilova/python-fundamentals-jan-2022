command = input()
store = dict()

while command != "statistics":
    info = command.split(': ')
    product = info[0]
    quantity = int(info[1])
                                                                # OR
    if product in store.keys():                    #     if product not in store.keys():
        store[product] += quantity                 #         store[product] = quantity
    else:                                          #     else:
        store[product] = quantity                  #         store[product] += quantity

    command = input()

count = len(store.keys())
total = sum(store.values())

print(f'Products in stock:')
for product in store:
    print(f'- {product}: {store[product]}')

print(f'Total Products: {count}')
print(f'Total Quantity: {total}')
