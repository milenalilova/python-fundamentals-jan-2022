import re

text = input()
items_dict = {}

pattern = r"([|#])([a-zA-Z ]+)\1([\d]{2}\/[\d]{2}\/[\d]{2})\1([\d]+)\1"

info = re.finditer(pattern, text)
total_calories = 0
info_list = list(info)

for match in info_list:
    item_name = match.group(2)
    expiration_date = match.group(3)
    calories = int(match.group(4))
    total_calories += calories

days_to_last = total_calories // 2000
print(f"You have food to last you for: {days_to_last} days!")

for match in info_list:
    item_name = match.group(2)
    expiration_date = match.group(3)
    calories = int(match.group(4))

    print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")




