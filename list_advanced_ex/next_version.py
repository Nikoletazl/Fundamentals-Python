version = input().split(".")
version_str = "".join(version)

version_num = int(version_str)
version_num += 1

next_version_str = str(version_num)
next_version = list(next_version_str)

print(f"{'.'.join(next_version)}")