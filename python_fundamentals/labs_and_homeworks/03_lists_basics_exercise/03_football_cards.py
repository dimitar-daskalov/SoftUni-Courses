red_cards = input().split()
team_a = []
team_b = []

for player in red_cards:
    player_out = player.split("-")
    if 11 - len(team_a) < 7 or 11 - len(team_b) < 7:
        break
    if player_out[0] == "A":
        if player_out[1] not in team_a:
            team_a.append(player_out[1])
    elif player_out[0] == "B":
        if player_out[1] not in team_b:
            team_b.append(player_out[1])

print(f"Team A - {11 - len(team_a)}; Team B - {11 - len(team_b)}")

if 11 - len(team_a) < 7 or 11 - len(team_b) < 7:
    print("Game was terminated")
