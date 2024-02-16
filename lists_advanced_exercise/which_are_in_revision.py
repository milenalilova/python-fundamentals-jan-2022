first_line = input().split(', ')
second_line = input()

subs_string = [x for x in first_line if x in second_line]

print(subs_string)
