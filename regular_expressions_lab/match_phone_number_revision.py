import re

numbers = input()
pattern = r'\+359 2 [0-9]{3} [0-9]{4}|\+359-2-[0-9]{3}-[0-9]{4}\b'

matches = re.findall(pattern, numbers)
print(', '.join(matches))
