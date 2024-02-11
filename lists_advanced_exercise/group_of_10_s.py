numbers = list(map(int, input().split(', ')))
divider = 10

while len(numbers) > 0:
    num_list = [num for num in numbers if num <= divider]
    for el in num_list:
        numbers.remove(el)
    print(f"Group of {divider}'s: {num_list}")
    divider += 10
