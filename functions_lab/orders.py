def total_price(item, quantity, ):
    if item == 'coffee':
        return quantity * 1.5
    elif item == 'water':
        return quantity * 1
    elif item == 'coke':
        return quantity * 1.4
    elif item == 'snacks':
        return quantity * 2


current_item = input()
current_quantity = int(input())
final_price = total_price(current_item, current_quantity)

print(f'{final_price:.2f}')
