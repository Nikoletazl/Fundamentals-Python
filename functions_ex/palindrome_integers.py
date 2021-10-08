def is_palindrome():
    list_of_number = input().split(", ")

    for el in list_of_number:
        if el == el[::-1]:
            is_true = True
            print(is_true)
        else:
            is_true = False
            print(is_true)


is_palindrome()