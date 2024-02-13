cards = input().split(' ')
team_a = 11
team_b = 11
game_terminated = False
a_red_cards = []
b_red_cards = []

for card in cards:

    team = card.split('-')[0]
    num = card.split('-')[1]

    if team == "A":
        if num not in a_red_cards:
            a_red_cards.append(num)
            team_a -= 1
            if team_a < 7:
                game_terminated = True
                break

    elif team == "B":
        if num not in b_red_cards:
            b_red_cards.append(num)
            team_b -= 1
            if team_b < 7:
                game_terminated = True
                break

print(f"Team A - {team_a}; Team B - {team_b}")
if game_terminated:
    print("Game was terminated")
