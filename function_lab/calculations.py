def calculate(operator, num_1, num_2):
    if operator == "multiply":
        return num_1 * num_2
    elif operator == "divide":
        return num_1 // num_2
    elif operator == "add":
        return num_1 + num_2
    elif operator == "subtract":
        return num_1 - num_2
oper = input()
number_1 = int(input())
number_2 = int(input())
print(calculate(oper, number_1, number_2))