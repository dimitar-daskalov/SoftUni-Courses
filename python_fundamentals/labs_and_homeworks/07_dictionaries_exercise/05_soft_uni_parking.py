number_of_commands = int(input())
registered_members = {}

for person in range(number_of_commands):
    command = input().split()
    action = command[0]
    username = command[1]
    if action == "register":
        licence_plate_number = command[2]
        if username not in registered_members:
            registered_members[username] = licence_plate_number
            print(f"{username} registered {licence_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {licence_plate_number}")
    elif action == "unregister":
        if username not in registered_members:
            print(f"ERROR: user {username} not found")
        else:
            registered_members.pop(username)
            print(f"{username} unregistered successfully")

for user, licence_plate in registered_members.items():
    print(f"{user} => {licence_plate}")

