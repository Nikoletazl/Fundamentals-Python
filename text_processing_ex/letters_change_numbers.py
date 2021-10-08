text = input().split()

total = 0
results = []
total_result = 0

for word in text:
    if word[0].isupper():
        first_letter = ord(word[0].lower())
        first_letter -= 96
        number = int(word[1:-1])
        total = number / first_letter
    elif word[0].islower():
        first_letter = ord(word[0].lower())
        first_letter -= 96
        number = int(word[1:-1])
        total = number * first_letter
    if word[-1].isupper():
        end_letter = ord(word[-1].lower())
        end_letter -= 96
        total -= end_letter
        results.append(total)
    elif word[-1].islower():
        end_letter = ord(word[-1].lower())
        end_letter -= 96
        total += end_letter
        results.append(total)

for number in results:
    total_result += number

print(f"{total_result:.2f}")


