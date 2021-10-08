def characters(chr_1: str, chr_2: str):
    list = []
    for symbols in range(ord(chr_1) + 1, ord(chr_2)):
        current_symbol = chr(symbols)
        list.append(current_symbol)

    return list


char_1 = input()
char_2 = input()
result = characters(char_1, char_2)
print(" ".join(result))