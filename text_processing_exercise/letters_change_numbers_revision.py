words = input().split()
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

final_result = 0

for word in words:
    result = 0
    first_letter = word[0]
    last_letter = word[-1]
    number = int(word[1:-1])

    if first_letter.isupper():
        position = alphabet.index(first_letter) + 1
        result += number / position

    elif first_letter.islower():
        position = alphabet.index(first_letter.upper()) + 1
        result += number * position

    if last_letter.isupper():
        position = alphabet.index(last_letter) + 1
        result -= position

    elif last_letter.islower():
        position = alphabet.index(last_letter.upper()) + 1
        result += position

    final_result += result

print(f"{final_result:.2f}")
