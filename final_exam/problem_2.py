import re

n = int(input())
ascii_numbers = []

for count in range(n):
    command = input()

    pattern = r"!(?P<command>[A-Z][a-z]{2,})!:\[(?P<string>[A-Za-z]{8,})\]"
    matches = re.finditer(pattern, command)
    if re.search(pattern, command) is not None:
        for match in matches:
            word_one = match.group("command")
            word_two = match.group("string")
            for char in word_two:
                ascii_numbers.append(ord(char))
            string = [str(num) for num in ascii_numbers]
            print(f"{word_one}: {' '.join(string)}")
    else:
        print("The message is invalid")