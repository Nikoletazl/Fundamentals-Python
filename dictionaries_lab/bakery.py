data = input().split()

product = {}

for index in range(0, len(data), 2):
    key = data[index]
    value = int(data[index + 1])
    product[key] = value

print(product)

