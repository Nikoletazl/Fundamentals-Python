def is_index_valid(collection: list, index: int):
    if 0 <= index < len(collection):
        return True

    return False


def shoot_at_target(collection: list, target_index: int, power: int):
    if is_index_valid(collection, target_index):
        collection[target_index] -= power

        if collection[target_index] <= 0:
            collection.pop(target_index)

    return collection


def add_at_index(collection: list, append_index: int, value: int):
    if not is_index_valid(collection, append_index):
        print("Invalid placement!")

        return collection

    collection.insert(append_index, value)

    return collection


def strike_at_index(collection: list, strike_index: int, radius: int):
    left_strike_index = strike_index - radius
    right_strike_index = strike_index + radius

    if is_index_valid(collection, left_strike_index) and \
            is_index_valid(collection, strike_index) and \
            is_index_valid(collection, right_strike_index):

        for i in range(left_strike_index, right_strike_index + 1):
            collection.pop(left_strike_index)
    else:
        print("Strike missed!")

    return collection


numbers_str_list = input().split()
numbers = [int(num) for num in numbers_str_list]

command = input()
while command != "End":
    cmd_args = command.split()

    cmd_type = cmd_args[0]
    cmd_index = int(cmd_args[1])
    cmd_value = int(cmd_args[2])

    if cmd_type == "Shoot":
        numbers = shoot_at_target(numbers, cmd_index, cmd_value)
    elif cmd_type == "Add":
        numbers = add_at_index(numbers, cmd_index, cmd_value)
    elif cmd_type == "Strike":
        numbers = strike_at_index(numbers, cmd_index, cmd_value)

    command = input()

numbers_str_list = [str(num) for num in numbers]
print("|".join(numbers_str_list))

