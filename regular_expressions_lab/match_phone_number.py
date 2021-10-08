import re

pattern = r"(\+359 2 \d{3} \d{4})|(\+359-2-\d{3}-\d{4})"
text = input()

results = re.finditer(pattern, text)

valid_phones = [match.group() for match in results]

print(", ".join(valid_phones))
