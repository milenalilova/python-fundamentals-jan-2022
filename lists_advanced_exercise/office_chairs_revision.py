rooms_count = int(input())
free_chairs = 0
not_enough_chairs = False

for room in range(1, rooms_count + 1):
    info = input().split(' ')
    chairs_count = len(info[0])
    visitors_count = int(info[1])
    if chairs_count >= visitors_count:
        free_chairs += chairs_count - visitors_count
    else:
        print(f"{visitors_count - chairs_count} more chairs needed in room {room}")
        not_enough_chairs = True

if not not_enough_chairs:
    print(f"Game On, {free_chairs} free chairs left")
