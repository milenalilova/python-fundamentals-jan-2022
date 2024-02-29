sequence = input().split()
repeated_sequence = ''

for text in sequence:
    length = len(text)
    repeated_sequence += text * length

print(repeated_sequence)
