n = int(input())
plant_dict = {}

for i in range(n):
    info = input().split('<->')
    plant = info[0]
    rarity = int(info[1])
    plant_dict[plant] = {'rarity': rarity, 'rating': []}

command = input().split()

while command[0] != "Exhibition":
    instruction = command[0][:-1]
    plant = command[1]

    if plant not in plant_dict.keys():
        print("error")

    elif instruction == "Rate":
        rating = int(command[3])
        plant_dict[plant]['rating'].append(rating)

    elif instruction == "Update":
        new_rarity = int(command[3])
        plant_dict[plant]['rarity'] = new_rarity

    elif instruction == "Reset":
        plant_dict[plant]['rating'].clear()

    command = input().split()

print("Plants for the exhibition:")
for plant, info in plant_dict.items():
    rarity = info['rarity']
    ratings = info['rating']
    avg_rating = sum(ratings) / len(ratings) if ratings else 0
    print(f"- {plant}; Rarity: {rarity}; Rating: {avg_rating:.2f}")
