command = input()

liked_meals = {}
counter = 0

while command != "Stop":
    data = command.split("-")
    guest = data[1]
    meal = data[2]

    if data[0] == "Like":
        if guest not in liked_meals:
            liked_meals[guest] = {"meals": [], "count": 0}
            liked_meals[guest]["meals"].append(meal)
            liked_meals[guest]["count"] += 1
        else:
            if meal not in liked_meals[guest]["meals"]:
                liked_meals[guest]["meals"].append(meal)
                liked_meals[guest]["count"] += 1
    if data[0] == "Unlike":
        if guest in liked_meals:
            if meal in liked_meals[guest]["meals"]:
                counter += 1
                liked_meals[guest]["meals"].remove(meal)
                liked_meals[guest]["count"] -= 1
                print(f"{guest} doesn't like the {meal}.")
            else:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            print(f"{guest} is not at the party.")

    command = input()


for key, value in sorted(liked_meals.items(), key=lambda x: (-x[1]["count"], x[0])):
    name = key
    meals = ", ".join(value["meals"])
    print(f"{name}: {meals}")

print(f"Unliked meals: {counter}")


