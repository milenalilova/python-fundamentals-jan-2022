gifts = input().split(' ')
command = input().split(' ')

while 'No Money' not in command:
    if 'No' and 'Money' in command:
        break
    elif 'OutOfStock' in command:
        gift = command[1]
        for i in range(len(gifts)):
            if gifts[i] == gift:
                gifts[i] = 'None'
    elif 'Required' in command:
        gift = command[1]
        index = int(command[2])
        if 0 <= index <= len(gifts) - 1:
            gifts[index] = gift
    elif 'JustInCase' in command:
        gift = command[1]
        gifts[-1] = gift

    command = input().split(' ')

# for i in range(len(gifts) - 1, -1, -1):
#     if (str(gifts[i])) == 'None':
#         gifts.remove((gifts[i]))
#     OR better

while 'None' in gifts:
    gifts.remove('None')

print(' '.join(gifts))
