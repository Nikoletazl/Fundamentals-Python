count_of_orders = int(input())
price_of_coffee = 0
total_price = 0
price_per_capsule = float(input())
days = int(input())
capsules_count = int(input())

while count_of_orders != 0:
    price_of_coffee = days * capsules_count * price_per_capsule
    total_price += price_of_coffee

    if count_of_orders > 0:
        print(f"The price for the coffee is: ${price_of_coffee:.2f}")
        price_of_coffee = 0
        count_of_orders -= 1

    if count_of_orders == 0:
        print(f"Total: ${total_price:.2f}")
        break

    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())


