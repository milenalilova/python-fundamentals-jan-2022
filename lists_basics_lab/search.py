# number = int(input())
# word = input()
# strings = list()
# filtered = list()
#
# for str in range(number):
#     current_string = input()
#     strings.append(current_string)
#     if word in current_string:
#         filtered.append(current_string)
#
# print(strings)
# print(filtered)


number = int(input())
word = input()
strings = list()
filtered = list()

for strg in range(number):
    current_string = input()
    strings.append(current_string)
    if word in current_string:
        filtered.append(current_string)
print(strings)

for i in range(len(strings) - 1, -1, -1):
    element = strings[i]
    if word not in element:
        strings.remove(element)

print(strings)
