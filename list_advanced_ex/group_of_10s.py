list = [int(x) for x in input().split(', ')]
y = 10
while list:
    group = [el for el in list if el <= y]
    for el in group:
        list.remove(el)
    print(f"Group of {y}'s: {group}")
    group = []
    y += 10