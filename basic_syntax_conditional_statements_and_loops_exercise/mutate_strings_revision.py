first_string = input()
second_string = input()
replacement = ''

for i in range(len(second_string)):
    if first_string[i] != second_string[i]:
        replacement = second_string[i]
        new_string = first_string[0:i] + replacement + first_string[i + 1:]
        first_string = new_string
        print(new_string)
