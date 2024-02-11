snowball_count = int(input())
highest_value = 0
best_snowball_data = ""

for balls in range(snowball_count):
    weight = int(input())
    time = int(input())
    quality = int(input())

    value = (weight / time) ** quality

    if value > highest_value:
        highest_value = value
        best_snowball_data = f"{weight} : {time} = {int(value)} ({quality})"

print(best_snowball_data)



# snowball_count = int(input())
# highest_value = 0
#
# for balls in range(snowball_count):
#     weight = int(input())
#     time = int(input())
#     quality = int(input())
#
#     value = int(weight / time) ** quality
#
#     if value > highest_value:
#         highest_value = value
#         current_weight = weight
#         current_time = time
#         current_quality = quality
#
# print(f"{current_weight} : {current_time} = {highest_value} ({current_quality})")
