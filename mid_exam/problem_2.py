name = input().split("|")
command = input()
even_list = []
odd_list = []

while not command == "Done":
    command_tokens = command.split()
    to_do = command_tokens[0]

    if to_do == "Add":
        particle = command_tokens[1]
        index = int(command_tokens[2])
        if 0 <= index < len(name):
            name.insert(index, particle)
    elif to_do == "Remove":
        index = int(command_tokens[1])
        if 0 <= index < len(name):
            name.pop(index)
    elif to_do == "Check" and command_tokens[1] == "Even":
        for even in range(0, len(name)):
            if even % 2 == 0:
                even_el = name[even]
                even_list.append(even_el)
        print(" ".join(even_list))
    elif to_do == "Check" and command_tokens[1] == "Odd":
        for odd in range(0, len(name)):
            if odd % 2 != 0:
                odd_el = name[odd]
                odd_list.append(odd_el)
        print(" ".join(odd_list))

    command = input()

print(f"You crafted {''.join(name)}!")
