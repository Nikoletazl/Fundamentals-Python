username = input()
command = input()

while command != "Registration":
    data = command.split()

    if data[0] == "Letters":
        case = data[1]
        if case == "Lower":
            username = username.lower()
            print(username)
        else:
            username = username.upper()
            print(username)
    elif data[0] == "Reverse":
        start_index = int(data[1])
        end_index = int(data[2])
        if 0 <= start_index < len(username) and 0 < end_index < len(username):
            reverse_username = username[start_index:end_index + 1]
            new_string = reverse_username[::-1]
            print(new_string)
    elif data[0] == "Substring":
        substring = data[1]
        if substring in username:
            username = username.replace(substring, "", 1)
            print(username)
        else:
            print(f"The username {username} doesn't contain {substring}.")
    elif data[0] == "Replace":
        char = data[1]
        username = username.replace(char, "-")
        print(username)
    elif data[0] == "IsValid":
        char = data[1]
        if char in username:
            print("Valid username.")
        else:
            print(f"{char} must be contained in your username.")

    command = input()