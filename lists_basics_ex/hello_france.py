items_list = input().split("|")
budget = float(input())
purchases = 0
sales = 0

for i in range(len(items_list)):
    current_item = items_list[i].split("->")
    type_of_item = current_item[0]
    price_of_item = float(current_item[1])

    if ((type_of_item == "Clothes" and price_of_item <= 50.00) or (type_of_item == "Shoes" and price_of_item <= 35.00) \
        or (type_of_item == "Accessories" and price_of_item <= 20.50)) and budget >= price_of_item:
        budget -= price_of_item
        purchases += price_of_item
        sold = price_of_item * 1.4
        sales += sold
        print(f"{sold:.2f}", end=" ")

print(f"\nProfit: {sales - purchases:.2f}")
if sales + budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")