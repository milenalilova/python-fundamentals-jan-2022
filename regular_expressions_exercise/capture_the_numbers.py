import re

while True:
    text = input()

    if not text:
        break

    result = re.findall(r'\d+', text)    # result is a list (findall returns a list)

    if len(result) > 0:
        print(' '.join(result), end=' ')
