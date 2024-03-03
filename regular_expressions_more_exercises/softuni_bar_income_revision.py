import re

line = input()
pattern = r"%(?P<name>[A-Z][a-z]+)%([^\|\$\%\.]*?)<(?P<product>\w+)>([^\|\$\%\.]*?)\|(?P<count>\d+)\|([^\|\$\%\.]*?)(?P<price>[1-9]+[0-9]*[\.0-9]+?)\$"
name_pattern = r"%([A-Z][a-z]+)%"
product_pattern = r"<(\w+)>"
count_pattern = r"\|(\d+)\|"
price_pattern = r"([1-9]+[0-9]*[\.0-9]+?\$)"

total_income = 0

while line != "end of shift":
    matches = re.finditer(pattern, line)

    total_price = 0

    for match in matches:
        name = match.group('name')
        product = match.group('product')
        count = int(match.group('count'))
        price = float(match.group('price'))

        total_price = count * price
        total_income += total_price

        print(f"{name}: {product} - {total_price:.2f}")

    line = input()

print(f"Total income: {total_income:.2f}")
