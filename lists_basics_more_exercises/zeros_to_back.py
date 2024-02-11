text = input().split(', ')
copy_text = list(map(int, text))

for digit in copy_text:
    if digit == 0:
        copy_text.remove(digit)
        copy_text.append(digit)

print(copy_text)
