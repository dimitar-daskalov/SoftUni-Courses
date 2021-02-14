from collections import deque
from sys import maxsize


def best_list_pureness(list_of_numbers, K):
    list_of_numbers = deque(list_of_numbers)
    best_pureness = -maxsize
    best_rotation = 0
    for rotation in range(K + 1):
        current_pureness = 0
        for el_index in range(len(list_of_numbers)):
            current_pureness += list_of_numbers[el_index] * el_index
        list_of_numbers.appendleft(list_of_numbers.pop())
        if current_pureness > best_pureness:
            best_pureness = current_pureness
            best_rotation = rotation
    return f"Best pureness {best_pureness} after {best_rotation} rotations"