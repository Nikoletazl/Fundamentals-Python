numbers = list(map(int, input().split(", ")))

positive_number = [str(num) for num in numbers if num >= 0]
negative_number = [str(num) for num in numbers if num < 0]
even_number = [str(num) for num in numbers if num % 2 == 0]
odd_number = [str(num) for num in numbers if num % 2 != 0]

print(f"Positive: {', '.join(positive_number)}")
print(f"Negative: {', '.join(negative_number)}")
print(f"Even: {', '.join(even_number)}")
print(f"Odd: {', '.join(odd_number)}")