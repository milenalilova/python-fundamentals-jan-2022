number = input()
largest_number = []
for ch in number:
    largest_number.append(int(ch))
    largest_number = sorted(largest_number, reverse=True)

print(''.join([str(x)for x in largest_number]))
