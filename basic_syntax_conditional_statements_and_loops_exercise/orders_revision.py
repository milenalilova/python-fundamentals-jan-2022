n = int(input())
total_price = 0

for i in range(n):
    price = float(input())
    days = int(input())
    capsules_needed = int(input())

    if not 0.01 <= price <= 100:
        continue
    if not 1 <= days <= 31:
        continue
    if not 1 <= capsules_needed <= 2000:
        continue

    coffee_price = days * capsules_needed * price
    total_price += coffee_price

    print(f"The price for the coffee is: ${coffee_price:.2f}")

print(f"Total: ${total_price:.2f}")
