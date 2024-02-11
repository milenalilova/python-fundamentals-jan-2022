text = input()

word = ""
digit = ""
new_text = ""

for char in range(len(text)):
    if char != len(text) - 1:
        if text[char].isdigit():
            digit += text[char]
            if text[char + 1].isdigit():
                continue
            else:
                new_text += word * int(digit)
                word = ""
                digit = ""
        else:
            word += text[char].upper()
    else:
        if text[char].isdigit():
            digit += text[char]
        else:
            word += text[char]
        new_text += word * int(digit)

print(f"Unique symbols used: {len(set(''.join(new_text)))}")
print(''.join(new_text))

# Regex also can be used
