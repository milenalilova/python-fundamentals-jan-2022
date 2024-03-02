import re

text = input()
pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

regex = re.findall(pattern, text)
print(' '.join(regex))
