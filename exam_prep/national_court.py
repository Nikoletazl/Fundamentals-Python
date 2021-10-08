first_employee_people_count = int(input())
second_employee_people_count = int(input())
third_employee_people_count = int(input())

people_count = int(input())

people_per_hour = first_employee_people_count + second_employee_people_count + third_employee_people_count

hours = 0

while people_count > 0:
    hours += 1
    people_count -= people_per_hour

    if hours % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")

