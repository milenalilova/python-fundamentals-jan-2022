words = input().split(" ")
words = list(map(lambda w: w.lower(), words))
occurrences = dict()

for word in words:
    if word not in occurrences:
        occurrences[word] = 1
    else:
        occurrences[word] += 1

odd_words = list()

for word in occurrences.keys():
    if occurrences[word] % 2 != 0:
        odd_words.append(word)

print(" ".join(odd_words))




# words = input().split(" ")
# dictionary = {}
#
# for word in words:
#     word_lower = word.lower()
#     if word_lower not in dictionary:
#         dictionary[word_lower] = 0
#     dictionary[word_lower] += 1
#
# for (key, value) in dictionary.items():
#     if value % 2 != 0:
#         print(key, end=" ")
