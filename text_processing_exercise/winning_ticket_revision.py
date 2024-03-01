tickets = input().split(',')
symbols = ['@', '#', '$', '^']

for ticket in tickets:
    ticket = ticket.strip()

    special_symbol_left = ''
    count_left = 0
    special_symbol_right = ''
    count_right = 0

    if len(ticket) != 20:
        print("invalid ticket")
    else:
        special_symbol_left = ''
        count_left = 0
        special_symbol_right = ''
        count_right = 0

        if ticket[0] * 20 == ticket and ticket[0] in symbols:
            print(f'ticket "{ticket}" - 10{ticket[0]} Jackpot!')
            continue
        else:
            for i in range(10):
                if ticket[i] in symbols:
                    if ticket[i] == special_symbol_left:
                        count_left += 1
                    else:
                        if count_left >= 6:
                            break
                        special_symbol_left = ticket[i]
                        count_left = 1
                else:
                    if count_left >= 6:
                        break
                    else:
                        special_symbol_left = ''
                        count_left = 0

            for i in range(10, len(ticket)):
                if ticket[i] in symbols:
                    if ticket[i] == special_symbol_right:
                        count_right += 1
                    else:
                        if count_right >= 6:
                            break
                        special_symbol_right = ticket[i]
                        count_right = 1
                else:
                    if count_right >= 6:
                        break
                    else:
                        special_symbol_right = ''
                        count_right = 0

        if special_symbol_left == special_symbol_right and count_left >= 6 and count_right >= 6:
            print(f'ticket "{ticket}" - {min(count_left, count_right)}{special_symbol_left}')
        else:
            print(f'ticket "{ticket}" - no match')
