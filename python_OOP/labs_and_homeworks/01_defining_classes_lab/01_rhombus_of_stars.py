def draw_row(row_length, index, symbol):
    offset = (row_length - index) * " "
    content = (index * symbol).strip()
    print(f"{offset}{content}")


def draw_rhombus(n):
    for i in range(1, n + 1):
        draw_row(n, i, '* ')
    for i in range(n - 1, 0, -1):
        draw_row(n, i, '* ')


integer_received = int(input())
draw_rhombus(integer_received)


