text = input()
new_text = text[0]

for i in range(1, len(text)):
    if text[i] != text[i - 1]:
        new_text += text[i]

print(new_text)


# Variant 2

# text = input()
# new_text = ''
#
# for i in range(len(text) - 1):
#     if text[i] == text[i + 1]:
#         continue
#     else:
#         new_text += text[i]
# new_text += text[-1]
#
# print(new_text)
