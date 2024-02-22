people_waiting = int(input())
lift_list = [int(num) for num in input().split(' ')]
capacity = len(lift_list) * 4

while people_waiting > 0:
    if sum(lift_list) == capacity:
        break

    for lift in range(len(lift_list)):
        if lift_list[lift] < 4:
            free_space = 4 - lift_list[lift]
            if people_waiting > free_space:
                lift_list[lift] += free_space
                people_waiting -= free_space
            else:
                lift_list[lift] += people_waiting
                people_waiting -= people_waiting

result = [str(num) for num in lift_list]

if people_waiting == 0 and sum(lift_list) < capacity:
    print("The lift has empty spots!")
    print(' '.join(result))

elif people_waiting > 0 and sum(lift_list) == capacity:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(' '.join(result))

elif people_waiting == 0 and sum(lift_list) == capacity:
    print(' '.join(result))

