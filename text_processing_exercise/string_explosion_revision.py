text = input()
new_text = ''
strength = 0

for ch in text:
    if ch.isdigit():
        strength += int(ch)
        strength -= 1
        continue
    else:
        if strength == 0:
            new_text += ch
        else:
            if ch == '>':
                new_text += ch
            else:
                strength -= 1
                continue

print(new_text)
