numbers = input().split(', ')
numbers = list(map(int, numbers))
even_indices = []

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_indices.append(i)

print(even_indices)
