import re

number_inputs = int(input())

pattern = r'(.+)>([\d]{3})\|([a-z]{3})\|([A-Z]{3})\|([^\>\<]+)<\1'

for line in range(number_inputs):
    text = input()

    matches = re.search(pattern, text)
    if not matches:
        print(f"Try another password!")
    else:
        password = matches.group(2) + matches.group(3) + matches.group(4) + matches.group(5)
        print(f"Password: {password}")


# Encrypting Password Problem