import re

pattern = r'%([A-Z][a-z]+)%([^\|\$\%\.]*?)<(\w+)>([^\|\$\%\.]*?)\|(\d+)\|([^\|\$\%\.]*?)([1-9]+[0-9]*[\.[0-9]+)?\$'
name_pat = r'%([A-Z][a-z]+)%'
product_pat = r'<(\w+)>'
quantity_pat = r'\|(\d+)\|'
price_pat = r'([1-9]+[0-9]*[\.[0-9]+)?\$'

text = input()
orders = []
final_price = 0

while text != 'end of shift':
    matches = re.findall(pattern, text)

    if matches:
        name = re.findall(name_pat, text)
        product = re.findall(product_pat, text)
        quantity = re.findall(quantity_pat, text)
        price = re.findall(price_pat, text)

        total_price = int(quantity[0]) * float(price[0])
        final_price += total_price
        orders.append([name[0], product[0], total_price])

    text = input()

for order in orders:
    print(f"{order[0]}: {order[1]} - {order[2]:.2f}")

print(f"Total income: {final_price:.2f}")
