import re

regex = r"www\.[a-zA-Z0-9\-]+(\.[a-z]+)+"

while True:
    text = input()

    if not text:
        break

    matches = re.finditer(regex, text)
    for link in matches:
        print(link.group())
