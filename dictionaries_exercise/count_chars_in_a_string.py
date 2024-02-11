# line = input()
# characters = dict()
#
# for ch in line:
#     if ch in characters:
#         characters[ch] += 1
#     else:
#         characters[ch] = 1
#
# for key, value in characters.items():
#     if key != ' ':
#         print(f"{key} -> {value}")


from collections import Counter

word = input()
result = Counter(word)

for key, value in result.items():
    if key != ' ':
        print(f"{key} -> {value}")
