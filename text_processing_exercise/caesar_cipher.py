text = input()
result = ''
for char in text:
    result += char.replace(char, chr(ord(char) + 3))

print(result)
