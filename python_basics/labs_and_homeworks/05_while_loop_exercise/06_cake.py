cake_width = int(input())
cake_height = int(input())
command = input()
sum_pieces = 0
size_cake = cake_width * cake_height

while command != "STOP":
    sum_pieces += int(command)
    if sum_pieces >= size_cake:
        break
    command = input()

if size_cake > sum_pieces:
    diff = size_cake - sum_pieces
    print(f"{diff} pieces are left.")
else:
    diff = abs(size_cake - sum_pieces)
    print(f"No more cake left! You need {diff} pieces more.")