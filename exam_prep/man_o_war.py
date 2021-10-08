pirate_ship = [int(num) for num in input().split(">")]
warship = [int(num) for num in input().split(">")]

max_health_capacity = int(input())

command = input()

while not command == "Retire":
    data = command.split()
    if data[0] == "Fire":
        index = int(data[1])
        damage = int(data[2])
        if 0 <= index < len(warship):
            warship[index] -= damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                break
    elif data[0] == "Defend":
        start_index = int(data[1])
        end_index = int(data[2])
        damage = int(data[3])
        if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
            for index in range(start_index, end_index + 1):
                pirate_ship[index] -= damage
                if pirate_ship[index] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    break
    elif data[0] == "Repair":
        index = int(data[1])
        health = int(data[2])
        if 0 <= index < len(pirate_ship):
            if pirate_ship[index] + health > max_health_capacity:
                pirate_ship[index] = max_health_capacity
            else:
                pirate_ship[index] += health
    elif data[0] == "Status":
        threshold = max_health_capacity * 0.2
        counter = 0
        for num in pirate_ship:
            if num < threshold:
                counter += 1
        print(f"{counter} sections need to be repair.")

    command = input()

print(f"")