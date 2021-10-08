words = input().split()
word_one = words[0]
word_two = words[1]

total_sum = 0
shorter_Word_length = min(len(word_one), len(word_two))

for i in range(shorter_Word_length):
    word_one_curr_ch = word_one[i]
    word_two_curr_ch = word_two[i]

    ch_multiplication = ord(word_one_curr_ch) * ord(word_two_curr_ch)

    total_sum += ch_multiplication

longer_word_length = max(len(word_one), len(word_two))
for i in range(shorter_Word_length, longer_word_length):
    if len(word_one) > len(word_two):
        curr_word_ch = word_one[i]
    else:
        curr_word_ch = word_two[i]

    total_sum += ord(curr_word_ch)

print(total_sum)