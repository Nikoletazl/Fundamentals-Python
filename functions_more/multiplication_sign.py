def get_result(a, b, c):
    list = [a, b, c]
    negatives = 0
    for i in range(len(list)):
        if "-" in list[i]:
            negatives += 1
    if negatives % 2 != 0:
        return "negative"
    elif "0" in list:
        return "zero"
    else:
        return "positive"


first_num = input()
second_num = input()
third_num = input()

print(get_result(first_num, second_num, third_num))