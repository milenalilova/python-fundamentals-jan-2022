import re

text = input()

pattern = r"([@#])([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1"

matches = re.finditer(pattern, text)
matches_counter = 0
matching_pairs = []

for match in matches:
    matches_counter += 1
    left_word = match.group(2)
    right_word = match.group(3)

    if left_word == right_word[::-1]:
        matching_pairs += [f"{left_word} <=> {right_word}"]

if matches_counter == 0:
    print("No word pairs found!")
else:
    print(f"{matches_counter} word pairs found!")

if matching_pairs:
    print("The mirror words are:")
    print(', '.join(matching_pairs))
else:
    print("No mirror words!")
