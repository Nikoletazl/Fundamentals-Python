n = int(input())
even = []
odd = []
negative = []
positive = []
for _ in range(n):
    current_num = int(input())
    if current_num % 2 == 0:
        even.append(current_num)
    if current_num >= 0:
        positive.append(current_num)
    if current_num % 2 == 1:
        odd.append(current_num)
    if current_num < 0:
        negative.append(current_num)
command = input()
if command == "even":
    print(even)
elif command == "odd":
    print(odd)
elif command == "positive":
    print(positive)
elif command == "negative":
    print(negative)