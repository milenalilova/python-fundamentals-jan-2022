deck = input().split(' ')
shuffles = int(input())
mid = int(len(deck) / 2)


for j in range(shuffles):
    shuffle_deck = []
    for i in range(mid):
        shuffle_deck.append(deck[i])
        shuffle_deck.append(deck[mid])
        mid += 1
    deck = shuffle_deck
    mid = len(deck) // 2

print(shuffle_deck)
