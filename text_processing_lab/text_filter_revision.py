banned_words = input().split(', ')
text = input()

for word in banned_words:
    if word in text:
        stars = len(word)
        text = text.replace(word, '*' * stars)

print(text)
