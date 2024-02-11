# number_rooms = int(input())
# free_chairs = 0
# condition = True
#
# for room in range(1, number_rooms + 1):
#     room_info = input().split(' ')
#     chairs_count = len(room_info[0])
#     visitors_count = int(room_info[1])
#     if chairs_count < visitors_count:
#         needed_chairs = visitors_count - chairs_count
#         print(f'{needed_chairs} more chairs needed in room {room}')
#         condition = False
#     else:
#         free_chairs += (chairs_count - visitors_count)
#
# if condition:
#     print(f'Game On, {free_chairs} free chairs left')


def office_management(number_of_rooms):
    left_chairs = 0
    condition = True

    for room_number in range(1, number_of_rooms + 1):
        data = input().split(' ')
        available_chairs = data[0]
        visitors = int(data[1])

        diff = abs(len(available_chairs) - visitors)

        if len(available_chairs) < visitors:
            condition = False
            print(f'{diff} more chairs needed in room {room_number}')
        elif len(available_chairs) > visitors:
            left_chairs += diff
    if condition:
        print(f'Game On, {left_chairs} free chairs left')


info = int(input())
office_management(info)
