string = input().split(",")
list = []
zero = []
for i in string:
    numbers = int(i)
    if numbers == 0:
        zero.append(numbers)
    elif numbers != 0:
        list.append(numbers)
print(list + zero)