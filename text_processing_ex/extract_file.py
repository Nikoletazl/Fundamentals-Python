file_path = input().split("\\")
file_name = ""
file_extension = ""

for word in file_path:
    if "." in word:
        index = word.index(".")
        file_name = word[:index]
        file_extension = word[index + 1:]

print(f"File name: {file_name}")
print(f"File extension: {file_extension}")

