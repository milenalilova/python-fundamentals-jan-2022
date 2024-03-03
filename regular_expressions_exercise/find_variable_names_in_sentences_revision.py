import re

text = input()

pattern = r"\b_{1}[a-zA-Z0-9]+\b"

matches = re.findall(pattern, text)

word_list = []

for word in matches:
    word_list.append(word[1:])

print(','.join(word_list))
