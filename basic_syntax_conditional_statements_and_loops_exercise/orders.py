number_of_orders = int(input())
total_price = 0

for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())
    price_for_coffee = capsules_count * days * price_per_capsule
    total_price += price_for_coffee
    print(f"The price for the coffee is: ${price_for_coffee:.2f}")

print(f"Total: ${total_price:.2f}")
