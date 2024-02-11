key = int(input())
num_lines = int(input())

for char in range(num_lines):
    letter = input()
    # print(ord(letter))
    new_letter = ord(letter) + key
    print(chr(new_letter), end='')
