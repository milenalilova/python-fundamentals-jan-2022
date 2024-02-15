def chars_in_range(first_char, second_char):
    for ch in range(ord(first_char) + 1, ord(second_char)):
        print(chr(ch), end=' ')


first_char = input()
second_char = input()
chars_in_range(first_char, second_char)
