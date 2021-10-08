substrings = input().split(", ")
strings = input().split(", ")
new_list = []

for str in substrings:
    for str_2 in strings:
        if str in str_2:
            if str in new_list:
                continue
            else:
                new_list.append(str)

print(new_list)

