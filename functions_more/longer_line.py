from math import floor


def calculate_coordinates(a, b):
    result = abs(a) + abs(b)
    return floor(result)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x4 = float(input())
y4 = float(input())
x5 = float(input())
y5 = float(input())
first_coordinate = calculate_coordinates(x1, y1)
second_coordinate = calculate_coordinates(x2, y2)
third_coordinate = calculate_coordinates(x4, y4)
fourth_coordinate = calculate_coordinates(x5, y5)

if first_coordinate >= second_coordinate:
    print(f"({floor(x2)}, {floor(y2)})")
elif second_coordinate >= first_coordinate:
    print(f"({floor(x1)}, {floor(y1)})")
if third_coordinate >= fourth_coordinate:
    print(f"({floor(x4)}, {floor(y4)})")
elif fourth_coordinate >= third_coordinate:
    print(f"({floor(x5)}, {floor(y5)})")

