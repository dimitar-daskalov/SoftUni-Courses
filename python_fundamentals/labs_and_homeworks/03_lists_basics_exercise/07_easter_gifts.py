names_of_the_gifts = input().split()
new_list = []
command = input()
while command != "No Money":
    listed_command = command.split()
    if listed_command[0] == "OutOfStock":
        for index in range(len(names_of_the_gifts)):
            if names_of_the_gifts[index] == listed_command[1]:
                names_of_the_gifts[index] = "None"
    elif listed_command[0] == "Required":
        index = int(listed_command[2])
        if 0 <= index <= (len(names_of_the_gifts) - 1):
            names_of_the_gifts[index] = listed_command[1]
    elif listed_command[0] == "JustInCase":
        names_of_the_gifts[-1] = listed_command[1]
    command = input()

for index_two in range(len(names_of_the_gifts)):
    if names_of_the_gifts[index_two] != "None":
        new_list.append(names_of_the_gifts[index_two])

print(" ".join(new_list))