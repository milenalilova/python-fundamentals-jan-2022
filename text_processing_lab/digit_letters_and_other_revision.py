line = input()
digits_list = [ch for ch in line if ch.isdigit()]
letters_list = [ch for ch in line if ch.isalpha()]
chars_list = [ch for ch in line if not ch.isdigit() and not ch.isalpha()]

print(''.join(digits_list))
print(''.join(letters_list))
print(''.join(chars_list))
