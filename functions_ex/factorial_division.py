def factorial():
    n = int(input())
    n_2 = int(input())
    division = 0
    factorial = 1
    factorial_2 = 1
    for i in range(1, n + 1):
        factorial *= i
    for j in range(1, n_2 + 1):
        factorial_2 *= j

    division = factorial / factorial_2
    print(f"{division:.2f}")

factorial()