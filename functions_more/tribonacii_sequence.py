def printTrib(n):
    if n < 1:
        return

    third = 1

    for i in range(3, n):
        curr = first + second + third
        first = second
        second = third
        third = curr

        print(curr, " ", end="")

n = int(input())
printTrib(n)