players_pool_dict = {}

command = input()

while command != "Season end":
    if '->' in command:
        player, position, skill = command.split(' -> ')
        skill = int(skill)
        if player not in players_pool_dict:
            players_pool_dict[player] = {position: skill}
        else:
            if position not in players_pool_dict[player]:
                players_pool_dict[player][position] = skill
            else:
                if skill > players_pool_dict[player][position]:
                    players_pool_dict[player][position] = skill

    elif 'vs' in command:
        player_one, player_two = command.split(' vs ')
        if player_one in players_pool_dict and player_two in players_pool_dict:
            common_positions = []
            for position in players_pool_dict[player_one]:
                if position in players_pool_dict[player_two]:
                    common_positions.append(position)
            if common_positions:
                total_skill_one = sum(players_pool_dict[player_one][pos] for pos in common_positions)
                total_skill_two = sum(players_pool_dict[player_two][pos] for pos in common_positions)
                if total_skill_one > total_skill_two:
                    del players_pool_dict[player_two]
                elif total_skill_one < total_skill_two:
                    del players_pool_dict[player_one]

    command = input()

for player, positions in sorted(players_pool_dict.items(), key=lambda x: (-sum(x[1].values()), x[0])):
    print(f"{player}: {sum(positions.values())} skill")
    for position, skill in sorted(positions.items(), key=lambda x: (-x[1], x[0])):
        print(f"- {position} <::> {skill}")


# Variant 2

# players_pool_dict = {}
#
# command = input()
#
# while command != "Season end":
#     if '->' in command:
#         player, position, skill = command.split(' -> ')
#         skill = int(skill)
#         if player not in players_pool_dict.keys():
#             players_pool_dict[player] = {position: skill}
#         else:
#             if position not in players_pool_dict[player].keys():
#                 players_pool_dict[player][position] = skill
#             else:
#                 if skill > players_pool_dict[player][position]:
#                     players_pool_dict[player][position] = skill
#
#
#     elif 'vs' in command:
#         player_one, player_two = command.split(' vs ')
#         if player_one in players_pool_dict.keys() and player_two in players_pool_dict.keys():
#             common_positions = set(players_pool_dict[player_one].keys()) & set(players_pool_dict[player_two].keys())
#             if common_positions:
#                 total_skill_one = sum(players_pool_dict[player_one][pos] for pos in common_positions)
#                 total_skill_two = sum(players_pool_dict[player_two][pos] for pos in common_positions)
#                 if total_skill_one > total_skill_two:
#                     del players_pool_dict[player_two]
#                 elif total_skill_one < total_skill_two:
#                     del players_pool_dict[player_one]
#
#     command = input()
#
# for player, positions in sorted(players_pool_dict.items(), key=lambda x: (-sum(x[1].values()), x[0])):
#     print(f"{player}: {sum(positions.values())} skill")
#     for position, skill in sorted(positions.items(), key=lambda x: (-x[1], x[0])):
#         print(f"- {position} <::> {skill}")
#