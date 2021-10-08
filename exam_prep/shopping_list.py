groceries = input().split("!")

data = input()

while not data == "Go shopping!":
    command_data = data.split()
    if command_data[0] == "Urgent":
        item = command_data[1]
        if item not in groceries:
            groceries.insert(0, item)
    elif command_data[0] == "Unnecessary":
        item = command_data[1]
        if item in groceries:
            groceries.remove(item)
    elif command_data[0] == "Correct":
        old_item = command_data[1]
        new_item = command_data[2]
        if old_item in groceries:
            index = groceries.index(old_item)
            groceries[index] = new_item
    elif command_data[0] == "Rearrange":
        item = command_data[1]
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)

    data = input()

print(", ".join(groceries))
