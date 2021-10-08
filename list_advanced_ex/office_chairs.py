number_of_rooms = int(input())
needed = 0
room = 0
free_chairs = 0
total_chairs = 0

for room in range(1, number_of_rooms + 1):
    people_and_chairs = input().split()
    people = people_and_chairs[0]
    chairs = int(people_and_chairs[1])
    if len(people) == chairs:
        continue
    elif len(people) < chairs:
        needed = chairs - len(people)
        if free_chairs >= needed:
            total_chairs = abs(free_chairs - needed)
            free_chairs -= needed
            print(f"{total_chairs} more chairs needed in room {room}")
        else:
            free_chairs -= needed
            print(f"{needed} more chairs needed in room {room}")

        needed = 0

    elif len(people) > chairs:
        free_chairs += len(people) - chairs

if free_chairs >= 0:
    print(f"Game On, {free_chairs} free chairs left")
