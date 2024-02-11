ticket_info = input()
data = [x.strip() for x in ticket_info.split(',')]
symbols = ['@', '#', '$', '^']
count_first_part = 0
special_symbol_first_part = ''
count_second_part = 0
special_symbol_second_part = ''

for ticket in data:
    if len(ticket) != 20:
        print("invalid ticket")
    elif ticket[0] * 20 == ticket and ticket[0] in symbols:
        print(f'ticket "{ticket}" - 10{ticket[0]} Jackpot!')
    else:
        for ch in ticket[0:10]:
            if ch in symbols:
                special_symbol_first_part = ch
                count_first_part += 1
                # if count_first_part >= 6:
                #     break
            else:
                if count_first_part >= 6:
                    break
                # special_symbol_first_part = ''
                # count = 0

        for ch in ticket[10:]:
            if ch in symbols:
                special_symbol_second_part = ch
                count_second_part += 1
                # if count_second_part >= 6:
                #     break
            else:
                if count_second_part >= 6:
                    break
                # special_symbol_second_part = ''
                # count_second_part = 0

        if special_symbol_first_part == special_symbol_second_part:
            if special_symbol_first_part in symbols and special_symbol_second_part in symbols:
                if count_first_part >= 6 and count_second_part >= 6:
                    if count_first_part <= count_second_part:
                        print(f'ticket "{ticket}" - {count_first_part}{special_symbol_first_part}')
                    else:
                        print(f'ticket "{ticket}" - {count_second_part}{special_symbol_second_part}')
                else:
                    print(f'ticket "{ticket}" - no match')
            elif special_symbol_first_part not in symbols or special_symbol_second_part not in symbols:
                print(f'ticket "{ticket}" - no match')
        else:
            print(f'ticket "{ticket}" - no match')

        #
        # elif special_symbol_first_part == '' or special_symbol_second_part == '' \
        #         or special_symbol_first_part != special_symbol_second_part:
        #     print(f'ticket "{ticket}" - no match')
