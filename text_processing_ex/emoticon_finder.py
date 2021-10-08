text = input().split(":")
text.pop(0)

for element in text:
    if not element == "":
        # if element[0] != " ":
        symbol = element[0]
        print(f":{symbol}")
    else:
        print("::")