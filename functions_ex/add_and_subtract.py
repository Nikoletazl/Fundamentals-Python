def sum_number(num_1, num_2):
    total = num_1 + num_2

    return total


def subtract(sum_1: int, num_3: int):
    total = sum_1 - num_3

    return total


def add_and_subtract(num_1: int, num_2: int, num_3: int):
    sum_1 = sum_number(num_1, num_2)
    result = subtract(sum_1, num_3)

    return result


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

print(add_and_subtract(num_1, num_2, num_3))