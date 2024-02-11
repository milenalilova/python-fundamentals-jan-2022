import re

participants = input().split(', ')
participants_dict = {}
first_name = ''
second_name = ''
third_name = ''

text = input()

while text != 'end of race':
    name_pattern = r'[A-Za-z]+'
    digits_pattern = r'\d+'
    name = ''
    digits = ''
    distance = 0

    name_match = re.finditer(name_pattern, text)
    digit_match = re.finditer(digits_pattern, text)

    for match in name_match:
        name += match.group()

    for match in digit_match:
        digits += match.group()

    for num in digits:
        distance += int(num)

    if name in participants:
        if name not in participants_dict:
            participants_dict[name] = distance
        else:
            participants_dict[name] += distance

    new_dict = sorted(participants_dict.items(), key=lambda x: x[1], reverse=True)
    # print(new_dict[0:3])

    for i in range(len(new_dict[0:3])):
        if i == 0:
            first_name = new_dict[0][0]
        elif i == 1:
            second_name = new_dict[1][0]
        elif i == 2:
            third_name = new_dict[2][0]

    text = input()

print(f"1st place: {first_name}")
print(f"2nd place: {second_name}")
print(f"3rd place: {third_name}")
