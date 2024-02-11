import re

# re.split()

# using regex

text = input()

pattern = r'#[a-zA-Z ]+#\d{2}\/\d{2}\/\d{2}#\d+#|\|[a-zA-Z ]+\|\d{2}\/\d{2}\/\d{2}\|\d+\|'

matches = re.findall(pattern, text)

total_calories = 0
for match in matches:
    info = re.split('[#,|]', match)
    item = info[1]
    date = info[2]
    calories = int(info[3])
    total_calories += calories

days_to_last = int(total_calories / 2000)

print(f'You have food to last you for: {days_to_last} days!')

for match in matches:
    info = re.split('[#,|]', match)
    item = info[1]
    date = info[2]
    calories = int(info[3])
    print(f'Item: {item}, Best before: {date}, Nutrition: {calories}')
