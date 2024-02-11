# command = input()
# sum_prices = 0
# discount = 0
#
# while command != "special" or command != "regular":
#     if command == 'special':
#         discount = (sum_prices + (sum_prices * 0.2)) * 0.1
#         break
#     elif command == 'regular':
#         discount = 0
#         break
#     if float(command) < 0:
#         print('Invalid price!')
#     else:
#         sum_prices += float(command)
#
#     command = input()
#
# taxes = sum_prices * 0.2
# total_price = sum_prices + taxes
# final_price = total_price - discount
#
# if final_price == 0:
#     print('Invalid order!')
# else:
#     print("Congratulations you've just bought a new computer!")
#     print(f"Price without taxes: {sum_prices:.2f}$")
#     print(f"Taxes: {taxes:.2f}$")
#     print("-----------")
#     print(f"Total price: {final_price:.2f}$")


line = input()
net_price = 0

while line != 'special' and line != 'regular':
    current_price = float(line)

    if current_price > 0:
        net_price += current_price
    else:
        print('Invalid price!')

    line = input()

if net_price <= 0:
    print('Invalid order!')
else:
    taxes = net_price * 0.2
    final_price = net_price + taxes

    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {net_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")

    if line == 'special':
        final_price = final_price * 0.9

    print(f"Total price: {final_price:.2f}$")
