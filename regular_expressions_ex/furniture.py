import re

pattern = r"^>>(?P<furniture_name>[A-Za-z]+)<<(?P<price>\d+\.?\d+)!(?P<quantity>\d+)$"
bought_furniture = []
total_price = 0

command = input()
while command != "Purchase":
    match = re.match(pattern, command)

    if match is not None:
        furniture_name = match.group("furniture_name")
        price = float(match.group("price"))
        qty = int(match.group("quantity"))

        bought_furniture.append(furniture_name)
        total_price += price * qty

    command = input()

print("Bought furniture:")

for furniture in bought_furniture:
    print(furniture)

print(f"Total money spend: {total_price:.2f}")