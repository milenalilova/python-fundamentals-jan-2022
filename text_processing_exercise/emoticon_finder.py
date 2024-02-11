# text = input()
#
# for char in range(len(text)):
#     if text[char] == ":":
#         if text[char + 1] != " ":
#             print(text[char] + text[char + 1])


def emoticon_finder(text):
    result = [text[i] + text[i + 1] for i in range(len(text)) if text[i] == ':' and text[i + 1] != 0]
    print('\n'.join(result))


text = input()
emoticon_finder(text)
