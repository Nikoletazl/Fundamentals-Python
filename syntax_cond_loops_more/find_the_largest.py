num = list(input())
num.sort(reverse=True)

for k in range(len(num)):
    print(num[k], end="")