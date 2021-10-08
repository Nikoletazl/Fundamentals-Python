houses = [int(x) for x in input().split("@")]
command = input().split()
visiting = 0

while command[0] != "Love!":
    visiting += int(command[1])

    if not 0 <= visiting < len(houses):
        visiting = 0

    if houses[visiting] == 0:
        print(f"Place {visiting} already had Valentine's day.")

    else:
        houses[visiting] -= 2

        if houses[visiting] == 0:
            print(f"Place {visiting} has Valentine's day.")

    command = input().split()

missed = len(houses) - houses.count(0)
print(f"Cupid's last position was {visiting}.")
if missed == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {missed} places.")


