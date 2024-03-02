n = int(input())

for i in range(n):
    name = ''
    age = ''
    first_idx = 0
    second_idx = 0

    line = input().split()

    for word in line:
        if '@' in word and '|' in word:
            first_idx = word.index('@') + 1
            second_idx = word.index('|')
            name = word[first_idx:second_idx]
        if '#' in word and '*' in word:
            first_idx = word.index('#') + 1
            second_idx = word.index('*')
            age = word[first_idx:second_idx]

    print(f"{name} is {age} years old.")
