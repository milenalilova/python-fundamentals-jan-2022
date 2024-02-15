sequence = map(int, input().split(' '))

filtered = list(filter(lambda x: x % 2 == 0, sequence))
print(filtered)


