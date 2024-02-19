text = input()
text = text.lower()
words_list = ["sand", "water", "fish", "sun"]
word_found = 0

for word in words_list:
    if word in text:
        count = text.count(word)
        word_found += count

print(word_found)
