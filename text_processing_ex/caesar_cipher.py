text = input()

encrypted_text = ""

for ch in text:
    curr_ch_code = ord(ch)

    encrypted_ch = chr(curr_ch_code + 3)

    encrypted_text += encrypted_ch

print(encrypted_text)