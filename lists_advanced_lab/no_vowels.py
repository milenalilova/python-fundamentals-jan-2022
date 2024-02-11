# text = input()
# vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']
# no_vowels = []
#
# for i in text:
#     if i not in vowels:
#         no_vowels.append(i)
#
# print(''.join(no_vowels))

text = input()
vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']
no_vowels = [ch for ch in text if ch not in vowels]                 # ch.lower()???

print(''.join(no_vowels))
