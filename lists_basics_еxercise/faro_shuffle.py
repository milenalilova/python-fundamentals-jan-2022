cards = input().split()
shuffle = int(input())

cards_length = len(cards)
cards_middle = cards_length // 2

for i in range(shuffle):
    shuffled_list = []
    for p in range(cards_middle):
        shuffled_list.append(cards[p])
        shuffled_list.append(cards[cards_middle])
        cards_middle += 1
    cards = shuffled_list
    cards_middle = cards_length // 2

print(shuffled_list)
