n = int(input())
opening_brackets = 0
closing_brackets = 0
is_balanced = True

for i in range(n):
    ch = input()

    if ch == "(":
        if opening_brackets > 0:
            is_balanced = False
            break
        else:
            opening_brackets += 1

    elif ch == ")":
        if opening_brackets != 1:
            is_balanced = False
            break
        elif opening_brackets == 1:
            opening_brackets = 0
        elif closing_brackets > 0:
            is_balanced = False
            break

if is_balanced:
    print("BALANCED")

else:
    print("UNBALANCED")
