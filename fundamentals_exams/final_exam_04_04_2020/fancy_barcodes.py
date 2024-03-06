import re

pattern = r"@#+([A-Z][a-zA-Z0-9]{4,}[A-Z])@#+"

n = int(input())

products_list = []

for i in range(n):
    text = input()

    matches = re.match(pattern, text)

    if matches:
        product = matches.group(1)
        digits = ''
        for ch in product:
            if ch.isdigit():
                digits += ch
        if not digits:
            print("Product group: 00")
        else:
            print(f"Product group: {digits}")

    else:
        print("Invalid barcode")
