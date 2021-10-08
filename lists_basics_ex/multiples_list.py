factor = int(input())
count = int(input())
list = []
for i in range(1, count + 1):
    multiple = i * factor
    list.append(multiple)
    if multiple < 0:
        continue
print(list)