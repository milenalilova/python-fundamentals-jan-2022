from math import floor, sqrt


def get_distance(x1, y1, x2, y2):
    result = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return result


def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    first_line = get_distance(x1, y1, x2, y2)
    second_line = get_distance(x3, y3, x4, y4)

    if first_line >= second_line:
        x1y1 = get_distance(x1, y1, 0, 0)
        x2y2 = get_distance(x2, y2, 0, 0)

        if x1y1 <= x2y2:
            return f"({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})"
        else:
            return f"({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})"

    else:
        x3y3 = get_distance(x3, y3, 0, 0)
        x4y4 = get_distance(x4, y4, 0, 0)

        if x3y3 <= x4y4:
            return f"({floor(x3)}, {floor(y3)})({floor(x4)}, {floor(y4)})"
        else:
            return f"({floor(x4)}, {floor(y4)})({floor(x3)}, {floor(y3)})"


c_x1 = float(input())
c_y1 = float(input())
c_x2 = float(input())
c_y2 = float(input())
c_x3 = float(input())
c_y3 = float(input())
c_x4 = float(input())
c_y4 = float(input())

print(longer_line(c_x1, c_y1, c_x2, c_y2, c_x3, c_y3, c_x4, c_y4))

# import math


# def calculate_distance(x1, y1, x2=0, y2=0):
#     return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
#
#
# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())
# x3 = float(input())
# y3 = float(input())
# x4 = float(input())
# y4 = float(input())
#
# line_one_len = calculate_distance(x1, y1, 0, 0)
# line_two_len = calculate_distance(x3, y3, 0, 0)
#
# if line_one_len >= line_two_len:
#     if calculate_distance(x1, y1) <= calculate_distance(x2, y2):
#         print(f"({int(x1)}, {int(y1)})({int(x2)}, {int(y2)})")
#     else:
#         print(f"({int(x2)}, {int(y2)})({int(x1)}, {int(y1)})")
#
# else:
#
#     if calculate_distance(x3, y3) <= calculate_distance(x4, y4):
#         print(f"({int(x3)}, {int(y3)})({int(x4)}, {int(y4)})")
#
#     else:
#         print(f"({int(x4)}, {int(y4)})({int(x3)}, {int(y3)})")
#
