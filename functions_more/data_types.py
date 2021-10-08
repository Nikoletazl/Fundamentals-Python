def reader():
    name = input()
    number = input()
    result = ""
    if name == "int":
        result = int(number) * 2
        print(result)
    elif name == "real":
        result = float(number) * 1.5
        print(f"{result:.2f}")
    elif name == "string":
        print(f"${str(number)}$")

reader()