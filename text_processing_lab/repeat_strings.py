text = input().split()

new_text = ""

for word in text:
    new_word = word * len(word)
    new_text += new_word

print(new_text)
