command = input()
chat = []

while not command == "end":
    command_tokens = command.split()
    to_do = command_tokens[0]

    if to_do == "Chat":
        message = command_tokens[1]
        chat.append(message)
    elif to_do == "Delete":
        message = command_tokens[1]
        if message in chat:
            chat.remove(message)
    elif to_do == "Edit":
        old_message = command_tokens[1]
        new_message = command_tokens[2]
        if old_message in chat:
            index = chat.index(old_message)
            chat[index] = new_message
    elif to_do == "Pin":
        message = command_tokens[1]
        if message in chat:
            chat.remove(message)
            chat.append(message)
    elif to_do == "Spam":
        for item in command_tokens[1:]:
            chat.append(item)

    command = input()

print("\n".join(chat))
