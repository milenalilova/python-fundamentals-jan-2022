import re

while True:
    text = input()

    if not text:
        break

    pattern = r"\d+"
    matches = re.findall(pattern, text)
    if len(matches) > 0:
        print(' '.join(matches), end=' ')
