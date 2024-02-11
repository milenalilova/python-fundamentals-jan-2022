# lost_fights_count = int(input())
# helmet_price = float(input())
# sword_price = float(input())
# shield_price = float(input())
# armor_price = float(input())

# repair_expenses = 0
# shield_count = 0
#
# for fight in range(1, lost_fights_count + 1):
#
#     if fight % 2 == 0:
#         repair_expenses += helmet_price
#
#     if fight % 3 == 0:
#         repair_expenses += sword_price
#
#     if fight % 2 == 0 and fight % 3 == 0:
#         repair_expenses += shield_price
#         shield_count += 1
#
#         if shield_count % 2 == 0:
#             repair_expenses += armor_price
#
# print(f"Gladiator expenses: {repair_expenses:.2f} aureus")


# lost_fights_count = int(input())
# helmet_price = float(input())
# sword_price = float(input())
# shield_price = float(input())
# armor_price = float(input())
#
# repair_expenses = 0
# shield_count = 0
#
# for fight in range(1, lost_fights_count + 1):
#
#     if fight % 2 == 0:
#         repair_expenses += helmet_price
#
#     if fight % 3 == 0:
#         repair_expenses += sword_price
#
#         if fight % 2 == 0:
#             repair_expenses += shield_price
#             shield_count += 1
#
#             if shield_count == 2:
#                 repair_expenses += armor_price
#                 shield_count = 0
#
# print(f"Gladiator expenses: {repair_expenses:.2f} aureus")


lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_helmets_broken = lost_fights_count // 2
total_sword_broken = lost_fights_count // 3
total_shield_broken = lost_fights_count // 6
total_armor_broken = total_shield_broken // 2

gladiator_expenses = total_helmets_broken * helmet_price + total_sword_broken * sword_price + \
                     total_shield_broken * shield_price + total_armor_broken * armor_price

print(f"Gladiator expenses: {gladiator_expenses:.2f} aureus")
