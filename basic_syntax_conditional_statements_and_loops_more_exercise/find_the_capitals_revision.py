text = input()

capitals_indices = []

for ch in range(len(text)):
    if text[ch].isupper():
        capitals_indices.append(ch)

print(capitals_indices)


