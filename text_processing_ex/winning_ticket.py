tickets = [t.strip() for t in input().split(", ") if not t.isspace()]

winning_combo_at = "@" * 6
winning_combo_hash = "#" * 6
winning_combo_dollar = "$" * 6
winning_combo_circumflex = "^" * 6

for ticket in tickets:
    if len(ticket) != 20:
        print("invalid ticket")
        continue

    left_half = ticket[:10]
    right_half = ticket[10:]

    match_symbol = ""

    if winning_combo_at in left_half and winning_combo_at in right_half:
        match_symbol = "@"
    elif winning_combo_hash in left_half and winning_combo_hash in right_half:
        match_symbol = "#"
    elif winning_combo_dollar in left_half and winning_combo_dollar in right_half:
        match_symbol = "$"
    elif winning_combo_circumflex in left_half and winning_combo_circumflex in right_half:
        match_symbol = "^"
    else:
        print(f'ticket "{ticket}" - no match')
        continue

    left_matches = left_half.count(match_symbol)
    right_matches = right_half.count(match_symbol)

    min_matches = min(left_matches, right_matches)

    if min_matches == 10:
        print(f'ticket "{ticket}" - {min_matches}{match_symbol} Jackpot!')
    else:
        print(f'ticket "{ticket}" - {min_matches}{match_symbol}')




