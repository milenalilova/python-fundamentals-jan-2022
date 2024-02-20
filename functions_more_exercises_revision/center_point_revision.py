from math import floor


def centre_point(x1, y1, x2, y2):
    if abs(0 - x1) <= abs(0 - x2) and abs(0 - y1) <= abs(0 - y2):
        return f"({floor(x1)}, {floor(y1)})"
    else:
        return f"({floor(x2)}, {floor(y2)})"


c_x1 = float(input())
c_y1 = float(input())
c_x2 = float(input())
c_y2 = float(input())

print(centre_point(c_x1, c_y1, c_x2, c_y2))
