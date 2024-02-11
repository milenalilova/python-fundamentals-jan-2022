# word = input()
#
# while word != 'end':
#     rev = reversed(word)
#     reversed_word = ""
#     for ch in rev:
#         reversed_word += ch
#     print(f"{word} = {reversed_word}")
#
#     word = input()
#


word = input()

while word != 'end':
    rev = reversed(word)
    reversed_word = "".join(rev)
    print(f"{word} = {reversed_word}")

    word = input()

