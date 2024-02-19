numbers = input().split(' ')
text = input()
index_list = []
message = ''

for el in numbers:
    index = 0
    for digit in range(len(el)):
        index += int(el[digit])
    index_list.append(index)

for index in index_list:
    if index >= len(text):
        index = index % len(text)
    message += text[index]
    text = text[0:index] + text[index + 1:]

print(message)

