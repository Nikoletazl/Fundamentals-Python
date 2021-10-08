def calculate_total_price(product, quantity):
    if product == "water":
        return quantity
    elif product == "coke":
        return  quantity * 1.40
    elif product == "coffee":
        return quantity * 1.50
    elif product == "snacks":
        return  quantity * 2
type_product = input()
amount = int(input())
total_amount = calculate_total_price(type_product, amount)
print(f"{total_amount:.2f}")