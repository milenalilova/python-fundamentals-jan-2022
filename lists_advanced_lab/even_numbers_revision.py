numbers_string = list(map(int, input().split(', ')))
found_indices = map(lambda x: x if numbers_string[x] % 2 == 0 else 'no', range(len(numbers_string)))

even_indices = list(filter(lambda x: x != 'no', found_indices))
print(even_indices)
