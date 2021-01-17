from collections import deque

players = deque()

[players.append(player) for player in input().split()]

tosses = int(input())
count_tosses = 0

while len(players) > 1:
    count_tosses += 1
    if tosses == count_tosses:
        player_removed = players.popleft()
        print(f"Removed {player_removed}")
        count_tosses = 0
    else:
        players.append(players.popleft())

print(f"Last is {players[0]}")