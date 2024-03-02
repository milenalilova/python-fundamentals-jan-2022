first_char = input()
second_char = input()
line = input()

first_idx = ord(first_char)
second_idx = ord(second_char)

new_line = [ord(ch) for ch in line if first_idx < ord(ch) < second_idx]
print(sum(new_line))
