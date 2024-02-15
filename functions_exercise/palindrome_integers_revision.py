def palindromes(integers):
    for num in integers:
        if num == num[::-1]:
            print(True)
        else:
            print(False)


sequence = input().split(', ')
palindromes(sequence)
