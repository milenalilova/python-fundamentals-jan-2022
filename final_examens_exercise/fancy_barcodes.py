import re

num = int(input())

pattern = r'@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+'

for line in range(num):

    text = input()

    barcode = re.findall(pattern, text)
    product_group = ''

    if not barcode:
        print('Invalid barcode')
    else:
        for ch in text:
            if ch.isdigit():
                product_group += ch
        if product_group == '':
            print('Product group: 00')
        else:
            print(f'Product group: {product_group}')
