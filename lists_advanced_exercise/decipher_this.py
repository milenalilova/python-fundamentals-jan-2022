def secret_message(data):
    for word in data:
        digit_list = [char for char in word if char.isdigit()]
        letter = chr(int(''.join(digit_list)))
        letters_list = [char for char in word if not char.isdigit()]
        letters_list[0], letters_list[-1] = letters_list[-1], letters_list[0]
        letters_list.insert(0, letter)
        print(''.join(letters_list), end=' ')


words = input().split(' ')
secret_message(words)
