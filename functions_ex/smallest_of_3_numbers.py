import sys

def smallest_number(num_1, num_2, num_3):
    small_number = min(num_1, num_2, num_3)

    return small_number

number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(smallest_number(number_1, number_2, number_3))