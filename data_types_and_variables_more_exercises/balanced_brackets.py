num_lines = int(input())
opening_bracket_count = 0
closing_bracket_count = 0

for char in range(num_lines):
    text = input()
    if '(' in text:
        opening_bracket_count += 1
    elif ')' in text:
        closing_bracket_count += 1
    if opening_bracket_count == 1 and closing_bracket_count == 1:
        opening_bracket_count = 0
        closing_bracket_count = 0

if opening_bracket_count == 2 or closing_bracket_count == 2 or opening_bracket_count != closing_bracket_count:
    print("UNBALANCED")
elif opening_bracket_count == closing_bracket_count:
    print("BALANCED")
