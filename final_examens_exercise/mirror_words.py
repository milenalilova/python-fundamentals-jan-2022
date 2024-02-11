import re

text = input()

pattern = r'([@#])[a-zA-Z]{3,}\1\1[a-zA-Z]{3,}\1'

matches = re.finditer(pattern, text)

matches_dict = {}
mirror_words = {}
for match in matches:
    info = re.split('[@,#]', match.group())
    word_one = info[1]
    word_two = info[3]
    matches_dict[word_one] = word_two
    if word_one == word_two[::-1]:
        mirror_words[word_one] = word_two
    # print(word_two[::-1])

if len(matches_dict) == 0:
    print(f'No word pairs found!')
else:
    print(f"{len(matches_dict)} word pairs found!")
if len(mirror_words) == 0:
    print(f"No mirror words!")
else:
    print(f"The mirror words are:")
    print(', '.join('{} <=> {}'.format(k, v) for k, v in mirror_words.items()))

    # Or we use a string == "" to add all k, v in mirror_words
