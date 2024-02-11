import re

text = input()

number = ''
cool_threshold = 1

pattern = r'([:*])\1[A-Z][a-z]{2,}\1\1'
emojis_list = []

for ch in text:
    if ch.isdigit():
        number += ch

for d in number:
    cool_threshold = int(d) * cool_threshold

emojis = re.finditer(pattern, text)
for emoji in emojis:
    emojis_list.append(emoji.group())

print(f'Cool threshold: {cool_threshold}')
print(f'{len(emojis_list)} emojis found in the text. The cool ones are:')

sum_char = 0
for el in emojis_list:
    for ch in el:
        if ch.isalpha():
            sum_char += ord(ch)
    if sum_char > cool_threshold:
        print(el)
    sum_char = 0
