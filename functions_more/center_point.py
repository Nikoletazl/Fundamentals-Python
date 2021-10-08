from math import floor


def calculate_coordinates(a, b):
    result = abs(a) + abs(b)
    return floor(result)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

first_coordinate = calculate_coordinates(x1, y1)
second_coordinate = calculate_coordinates(x2, y2)
if first_coordinate >= second_coordinate:
    print(f"({floor(x2)}, {floor(y2)})")
else:
    print(f"({floor(x1)}, {floor(y1)})")