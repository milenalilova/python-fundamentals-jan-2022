animals = input().split(', ')
sheeps_count = 0

for i in range(len(animals) - 1, -1, -1):
    if animals[-1] == "wolf":
        print("Please go away and stop eating my sheep")
        break
    if animals[i] == "wolf":
        print(f"Oi! Sheep number {sheeps_count}! You are about to be eaten by a wolf!")
        break
    elif animals[i] == "sheep":
        sheeps_count += 1
