fires = input().split("#")
water = int(input())

effort = 0
total_fire = 0
print("Cells:")

for cell in fires:
    fire_cells = cell.split(" = ")
    fire_type = fire_cells[0]
    fire_range = int(fire_cells[1])

    if fire_type == "High" and ((fire_range < 81) or (fire_range > 125)):
        continue
    if fire_type == "Medium" and ((fire_range < 51) or (fire_range > 80)):
        continue
    if fire_type == "Low" and ((fire_range < 1) or (fire_range > 50)):
        continue

        water -= fire_range
        total_fire += fire_range
        effort += fire_range * 0.25
        print(f"- {fire_range}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")