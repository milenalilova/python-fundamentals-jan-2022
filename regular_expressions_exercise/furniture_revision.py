import re

pattern = r'>>([a-zA-Z]+)<<(\d+|\d+\.\d+)!(\d+)'
products_list = []
total_money = 0

info = input()
while info != "Purchase":
    matches = re.finditer(pattern, info)

    for match in matches:
        print(match[1])
        print(match[2])
        print(match[3])
        products_list.append(match[1])
        total_money += float(match[2]) * float(match[3])

    info = input()

print("Bought furniture:")
if total_money > 0:
    for product in products_list:
        print(product)
print(f"Total money spend: {total_money:.2f}")
