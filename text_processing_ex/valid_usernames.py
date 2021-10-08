# import re
#
# usernames = input().split(", ")
# pattern = r"[^A-Za-z0-9\-\_]"
#
# for username in usernames:
#     if 3 <= len(username) <= 16:
#         match = re.findall(pattern, username)
#         if not match:
#             print(username)

usernames = input().split(", ")

for username in usernames:
    if 3 <= len(username) <= 16:
        invalid_symbols = [el for el in username if
                           not el.isdigit() and not el.isalpha() and not el == "-" and not el == "_"]
        if len(invalid_symbols) == 0:
            print(username)