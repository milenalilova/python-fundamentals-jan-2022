people_waiting = int(input())
wagon_list = input().split(' ')
wagon_count = 0
has_empty_spots = False

for occupied_spaces in wagon_list:
    if int(occupied_spaces) >= 4:
        wagon_count += 1
    elif int(occupied_spaces) < 4:
        free_seats = 4 - int(occupied_spaces)
        if people_waiting <= free_seats:
            people_placed = people_waiting
            wagon_list[wagon_count] = str(int(occupied_spaces) + people_placed)
            people_waiting -= people_placed
            wagon_count += 1
        else:
            people_placed = free_seats
            wagon_list[wagon_count] = str(int(occupied_spaces) + people_placed)
            people_waiting -= people_placed
            wagon_count += 1

    if wagon_count >= len(wagon_list):
        break
    if people_waiting == 0:
        break

for i in wagon_list:
    if int(i) < 4:
        has_empty_spots = True

if people_waiting == 0 and has_empty_spots:
    print('The lift has empty spots!')
    print(*wagon_list)
elif people_waiting > 0 and not has_empty_spots:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(*wagon_list)
elif people_waiting == 0 and not has_empty_spots:
    print(*wagon_list)
