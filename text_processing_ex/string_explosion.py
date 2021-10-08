text = input()

result_text = ""

i = 0
bomb_power = 0

while i < len(text):
    curr_ch = text[i]

    if curr_ch != ">":
        result_text += curr_ch
    else:
        result_text += ">"
        bomb_power += int(text[i + 1])

        while bomb_power > 0:
            i += 1

            if i >= len(text):
                break
            curr_ch = text[i]

            if curr_ch == ">":
                result_text += ">"
                bomb_power += int(text[i + 1])
            else:
                bomb_power -= 1
    i += 1

print(result_text)