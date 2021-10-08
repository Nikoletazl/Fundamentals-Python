text = input()
result = ""

i = 0
while i < len(text):
    curr_ch = text[i]
    current_sequence_length = 1

    for j in range(i + 1, len(text)):
        next_ch = text[j]

        if curr_ch == next_ch:
            current_sequence_length += 1
        else:
            break

    result += curr_ch
    i += current_sequence_length

print(result)