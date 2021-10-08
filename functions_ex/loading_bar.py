def loading_bar():
    number = int(input())
    list = []
    result = number // 10
    complete = (100 - number) // 10
    for i in range(1, result + 1):
        list.append("%")
    for n in range(1, complete + 1):
        list.append(".")
    if number == 100:
        print("100% Complete!")
        print(f'[{"".join(list)}]')
    else:
        print(f'{number}% [{"".join(list)}]')
        print("Still loading...")


loading_bar()