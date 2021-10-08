numbers_str = input().split()
numbers_inverted = []
for number in numbers_str:
    number_inverted = int(number) * -1
    numbers_inverted.append(number_inverted)
print(numbers_inverted)
