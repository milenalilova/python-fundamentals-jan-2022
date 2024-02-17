message = input().split(' ')

for word in message:
    letter = []
    for ch in word:
        if ch.isdigit():
            letter.append(ch)
    first_letter = chr(int(''.join(letter)))
    rest_word = [char for char in word if char.isalpha()]
    rest_word[0], rest_word[-1] = rest_word[-1], rest_word[0]
    rest_word.insert(0, first_letter)
    deciphered_word = ''.join(rest_word)
    print(deciphered_word, end=' ')
