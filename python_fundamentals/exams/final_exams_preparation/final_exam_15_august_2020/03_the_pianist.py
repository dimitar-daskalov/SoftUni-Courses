number_of_pieces = int(input())

pieces_dict = {}

for number_piece in range(number_of_pieces):
    piece, composer, key = input().split("|")
    pieces_dict[piece] = {"composer": composer, "key": key}

command = input()
while not command == "Stop":
    command = command.split("|")
    action = command[0]
    if action == "Add":
        piece = command[1]
        composer = command[2]
        key = command[3]
        if piece not in pieces_dict:
            pieces_dict[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif action == "Remove":
        piece = command[1]
        if piece not in pieces_dict:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            del pieces_dict[piece]
            print(f"Successfully removed {piece}!")
    elif action == "ChangeKey":
        piece = command[1]
        new_key = command[2]
        if piece not in pieces_dict:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            pieces_dict[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
    command = input()

sorted_pieces_dict = dict(sorted(pieces_dict.items(), key=lambda x: (x[0], x[1]["composer"])))

for piece, value in sorted_pieces_dict.items():
    print(f"{piece} -> Composer: {value['composer']}, Key: {value['key']}")
