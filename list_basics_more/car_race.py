time = input().split(" ")
half_size = len(time) // 2
right_side = ""
left_side = ""
total_time_1 = 0
total_time_2 = 0
numbers = ""
right_side = time[:half_size:-1]
left_side = time[0:half_size]
for n in left_side:
    total_time_1 += int(n)
    if int(n) == 0:
        total_time_1 *= 0.8
for i in right_side:
    total_time_2 += int(i)
    if int(i) == 0:
        total_time_2 *= 0.8
if total_time_1 < total_time_2:
    print(f"The winner is left with total time: {total_time_1:.1f}")
else:
    print(f"The winner is right with total time: {total_time_2:.1f}")