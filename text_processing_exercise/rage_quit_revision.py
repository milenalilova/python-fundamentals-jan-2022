sequence = input()
digit = ''
new_text = ''
current_seq = ''

for ch in range(len(sequence) - 1):
    if sequence[ch].isalpha():
        current_seq += sequence[ch].upper()

    elif sequence[ch].isdigit():
        digit += sequence[ch]

        if sequence[ch + 1].isdigit():
            continue
        else:
            new_text += current_seq * int(digit)
            digit = ''
            current_seq = ''

    else:
        current_seq += sequence[ch]

if not sequence[-1].isdigit():
    current_seq += sequence[-1].upper()
else:
    digit += sequence[-1]
    new_text += current_seq * int(digit)

print(f"Unique symbols used: {len(set(new_text))}")
print(new_text)

# text = input()
#
# word = ""
# digit = ""
# new_text = ""
#
# for char in range(len(text)):
#     if char != len(text) - 1:
#         if text[char].isdigit():
#             digit += text[char]
#             if text[char + 1].isdigit():
#                 continue
#             else:
#                 new_text += word * int(digit)
#                 word = ""
#                 digit = ""
#         else:
#             word += text[char].upper()
#     else:
#         if text[char].isdigit():
#             digit += text[char]
#         else:
#             word += text[char]
#         new_text += word * int(digit)
#
# print(f"Unique symbols used: {len(set(''.join(new_text)))}")
# print(''.join(new_text))
