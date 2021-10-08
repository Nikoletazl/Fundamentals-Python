items = input().split(", ")
command_input = input()

while command_input != "Craft!":
    command_token = command_input.split(" - ")
    command = command_token[0]
    item = command_token[1]
    if command == "Collect":
        if item in items:
            command_input = input()
        else:
            items.append(item)
            command_input = input()
    elif command == "Drop":
        if item in items:
            items.remove(item)
            command_input = input()
        else:
            command_input = input()
    elif command == "Combine Items":
        combine_items = item.split(":")
        old_item = combine_items[0]
        new_item = combine_items[1]
        if old_item in items:
            for i in range(len(items)):
                if items[i] == old_item:
                    items.insert(i + 1, new_item)
                    break
            command_input = input()
    elif command == "Renew":
        if items[-1] == item:
            command_input = input()
        elif item in items:
            items.append(items.pop(items.index(item)))
            command_input = input()
        else:
            command_input = input()

print(", ".join(items))