number = input()
new_number = []

for digit in range(len(number)):
    new_number.append(int(number[digit]))
    new_number.sort()
    new_number.reverse()

for i in new_number:
    print(i, end='')
