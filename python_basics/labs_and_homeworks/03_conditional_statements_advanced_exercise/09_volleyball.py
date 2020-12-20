import math

year_type = input()

p_count_holidays_without_weekends = int(input())
h_count_weekends_hometown = int(input())

weekends = 48

weekends_in_sofia = weekends - h_count_weekends_hometown
weekends_played_in_sofia = weekends_in_sofia * 3/4
games_in_holidays = p_count_holidays_without_weekends * 2/3

total_games_played = weekends_played_in_sofia + h_count_weekends_hometown + games_in_holidays

if year_type == "leap":
    total_games_played += total_games_played * 0.15
else:
    total_games_played = weekends_played_in_sofia + h_count_weekends_hometown + games_in_holidays
print(math.floor(total_games_played))