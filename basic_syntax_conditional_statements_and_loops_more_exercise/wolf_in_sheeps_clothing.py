animals = input().split(', ')
animal_position = 0

if animals[-1] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    for current_animal in range(len(animals) - 1, -1, -1):
        animal_position += 1
        animal = animals[current_animal]
        if animal == 'wolf':
            print(f'Oi! Sheep number {animal_position-1}! You are about to be eaten by a wolf!')
