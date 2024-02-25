words = input().split(' ')
words_dict = {}

for word in words:
    if word.lower() not in words_dict.keys():
        words_dict[word.lower()] = 1
    else:
        words_dict[word.lower()] += 1

words_dict = [word for word in words_dict.keys() if words_dict[word] % 2 != 0]

print(' '.join(words_dict))

