elements = input().split()

command = input()
moves = 0

while not command == "end":
    moves += 1
    index_1, index_2 = command.split()
    index_1, index_2 = int(index_1), int(index_2)
    if 0 <= index_1 < len(elements) and 0 <= index_2 < len(elements) and index_1 != index_2:
        if elements[index_1] == elements[index_2]:
            print(f"Congrats! You have found matching elements - {elements[index_1]}!")
            if index_1 > index_2:
                elements.pop(index_1)
                elements.pop(index_2)
            else:
                elements.pop(index_2)
                elements.pop(index_1)
            if len(elements) == 0:
                print(f"You have won in {moves} turns!")
                break
        elif not elements[index_1] == elements[index_2]:
            print("Try again!")
    else:
        elements_double_list = []
        elements_double_list.append(f"-{moves}a")
        elements_double_list.append(f"-{moves}a")
        elements[len(elements) // 2 : len(elements) // 2] = elements_double_list
        print("Invalid input! Adding additional elements to the board")

    command = input()

if len(elements) > 0:
    print(f"Sorry you lose :(", f"{' '.join(elements)}", sep="\n")
