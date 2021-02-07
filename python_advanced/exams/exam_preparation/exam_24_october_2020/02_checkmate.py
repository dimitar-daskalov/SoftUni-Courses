def is_position_valid(c_row, c_col, siz):
    if 0 <= c_row < siz and 0 <= c_col < siz:
        return True
    return False


def is_checkmate(queen_pos, size, chess_b):
    for directory in MOVES:
        current_q_row, current_q_col = queen_pos[0], queen_pos[1]
        dir_q_row, dir_q_col = MOVES[directory][0], MOVES[directory][1]
        while is_position_valid(current_q_row + dir_q_row, current_q_col + dir_q_col, size):
            current_q_row += dir_q_row
            current_q_col += dir_q_col
            if chess_b[current_q_row][current_q_col] == "Q":
                break
            elif chess_b[current_q_row][current_q_col] == "K":
                return True
    return False


MOVES = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
    "upper_left": (-1, -1),
    "upper_right": (-1, 1),
    "down_left": (1, -1),
    "down_right": (1, 1),
}

SIZE = 8
chess_board = []
kings_position = 0
queens_positions = []
winner_queens = []
for _ in range(SIZE):
    current_row = input().split()
    chess_board.append(current_row)

for row in range(SIZE):
    for col in range(SIZE):
        if chess_board[row][col] == "K":
            kings_position = (row, col)
        elif chess_board[row][col] == "Q":
            queens_positions.append((row, col))

for queen_p in queens_positions:
    if is_checkmate(queen_p, SIZE, chess_board):
        winner_queens.append(queen_p)

if winner_queens:
    [print([*queen]) for queen in winner_queens]
else:
    print("The king is safe!")
