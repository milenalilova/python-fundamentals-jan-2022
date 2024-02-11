import re

while True:
    text = input()

    if not text:
        break

    pattern = r'(www)(\.[a-zA-Z0-9-]+)(\.[a-z]+)(\.[a-z]+)*'

    links = re.finditer(pattern, text)

    links_list = []

    for link in links:
        links_list.append(link.group())
        print(''.join(links_list))
