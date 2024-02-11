number = int(input())
plants_rarity_dict = {}
plant_rating_dict = {}

for line in range(number):
    data = input().split("<->")
    plant = data[0]
    rarity = int(data[1])

    plants_rarity_dict[plant] = rarity
    plant_rating_dict[plant] = []

command = input()

while command != "Exhibition":
    info = command.split(" ")
    action = info[0]
    plant = info[1]

    if plant not in plants_rarity_dict:
        print('error')

    elif action == "Rate:":
        rating = int(info[3])
        plant_rating_dict[plant] += [rating]

    elif action == "Update:":
        pass
        new_rarity = int(info[3])
        plants_rarity_dict[plant] = new_rarity
    elif action == "Reset:":
        plant_rating_dict[plant].clear()

    command = input()

for plant, rate in plant_rating_dict.items():
    if sum(rate) == 0:
        av_rate = 0
    else:
        av_rate = sum(rate) / len(rate)
    plant_rating_dict[plant] = f"{av_rate:.2f}"

print("Plants for the exhibition:")

for plant, rarity in plants_rarity_dict.items():
    print(f'- {plant}; Rarity: {rarity}; Rating: {plant_rating_dict[plant]}')




# number_of_plants = int(input())
#
# database = dict()
#
# for i in range(number_of_plants):
#     plant_info = input().split("<->")
#     plant = plant_info[0]
#     rarity = int(plant_info[1])
#
#     database[plant] = dict()
#     database[plant]["Rarity"] = rarity
#     database[plant]["Rating"] = list()
#
# while True:
#     command = input()
#     if command == "Exhibition":
#         break
#     command = command.split(": ")
#
#     if command[0] == "Rate":
#         plant_info = command[1].split(" - ")
#         current_plant = plant_info[0]
#         rating = int(plant_info[1])
#         if current_plant not in database:
#             print("error")
#             continue
#         database[current_plant]["Rating"].append(rating)
#     elif command[0] == "Update":
#         plant_info = command[1].split(" - ")
#         current_plant = plant_info[0]
#         new_rarity = plant_info[1]
#         if current_plant not in database:
#             print("error")
#             continue
#         database[current_plant]["Rarity"] = new_rarity
#     elif command[0] == "Reset":
#         current_plant = command[1]
#         if current_plant not in database:
#             print("error")
#             continue
#         database[current_plant]["Rating"].clear()
#
# for plant in database:
#     if len(database[plant]["Rating"]) > 0:
#         database[plant]["Average rating"] = sum(database[plant]['Rating']) / len(database[plant]['Rating'])
#     else:
#         database[plant]["Average rating"] = 0
#
# print(f"Plants for the exhibition:")
# for plant in database:
#     print(f"- {plant}; Rarity: {database[plant]['Rarity']}; Rating: {database[plant]['Average rating']:.2f}")
#