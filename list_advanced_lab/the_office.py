nums = [int(el) for el in input().split()]
factor = int(input())

happiness = [el * factor for el in nums]
threshold = sum(happiness) / len(happiness)

happy_employees = [el for el in happiness if el >= threshold]
sad_employees = [el for el in happiness if el < threshold]
happy_message = "Employees are happy!"
sad_message = "Employees are not happy!"

if len(sad_employees) > len(happiness) / 2:
    print(f"Score: {len(happy_employees)}/{len(happiness)}. {sad_message}")
else:
    print(f"Score: {len(happy_employees)}/{len(happiness)}. {happy_message}")
