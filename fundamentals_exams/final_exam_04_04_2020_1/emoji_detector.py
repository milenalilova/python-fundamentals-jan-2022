import re

text = input()
coolness_threshold = 1

for ch in text:
    if ch.isdigit():
        coolness_threshold *= int(ch)
print(f"Cool threshold: {coolness_threshold}")

pattern = r"(::([A-Z][a-z]{2,})::|(\*\*([A-Z][a-z]{2,})\*\*))"

matches = re.finditer(pattern, text)
emojis_dict = {}

for match in matches:
    emoji = match.group()
    emojis_dict[emoji] = 0  # to check if emoji in dict

print(f"{len(emojis_dict)} emojis found in the text. The cool ones are:")

for emoji in emojis_dict.keys():
    emoji_coolness = 0
    for ch in emoji:
        if ch.isalpha():
            emoji_coolness += ord(ch)
    if emoji_coolness >= coolness_threshold:
        print(emoji)
