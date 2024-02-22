command = input()
total_price = 0

while command != 'special' and command != 'regular':
    price = float(command)
    if price < 0:
        print('Invalid price!')
    else:
        total_price += price

    command = input()

if total_price == 0:
    print('Invalid order!')
else:
    tax = total_price * 0.2
    net_price = total_price + tax

    if command == "special":
        net_price -= net_price * 0.1

    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {tax:.2f}$")
    print("-----------")
    print(f"Total price: {net_price:.2f}$")
