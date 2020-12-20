command = input()

user_points = {}
language_user = {}
while not command == "exam finished":
    command = command.split("-")
    user = command[0]
    if command[1] == "banned":
        del user_points[user]
    else:
        language = command[1]
        points = command[2]
        points = int(points)
        if user in user_points:
            user_points[user].append(points)
        else:
            user_points[user] = [points]
        if language in language_user:
            language_user[language].append(user)
        else:
            language_user[language] = [user]
    command = input()

print("Results:")

max_points_user = {}
for user, points in user_points.items():
    points = max(points)
    max_points_user[user] = points

max_points_user = dict(sorted(max_points_user.items(), key=lambda x: (-x[1], x[0])))
for key, value in max_points_user.items():
    print(f"{key} | {value}")

print("Submissions:")

max_language_user = dict(sorted(language_user.items(), key=lambda x: (-len(x[1]), x[0])))

for key, value in max_language_user.items():
    print(f"{key} - {len(value)}")