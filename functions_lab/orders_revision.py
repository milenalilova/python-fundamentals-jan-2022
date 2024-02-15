def order_cost(product, quantity):
    price = 0

    if product == "coffee":
        price = 1.50

    elif product == "coke":
        price = 1.4

    elif product == "water":
        price = 1

    elif product == "snacks":
        price = 2

    total_cost = quantity * price
    return f"{total_cost:.2f}"


current_product = input()
current_quantity = int(input())

print(order_cost(current_product, current_quantity))
