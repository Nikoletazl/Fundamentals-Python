list_of_gifts = input().split(" ")
command = input()

while command != "No Money":
    current_command = command.split()
    if current_command[0] == "OutOfStock":
        for gift in range(len(list_of_gifts)):
            if list_of_gifts[gift] == current_command[1]:
                list_of_gifts[gift] = 'None'
    elif current_command[0] == "Required":
        index = int(current_command[2])
        if 0 <= index <= (len(list_of_gifts)):
            list_of_gifts[index] = current_command[1]
    elif current_command[0] == "JustInCase":
        list_of_gifts[-1] = current_command[1]
    command = input()
for gift in list_of_gifts:
    if gift != "None":
        print(gift, end=" ")
