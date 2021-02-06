from collections import deque
from sys import maxsize


def best_list_pureness(list_of_numbers, rotation_times):
    list_of_numbers = deque(list_of_numbers)
    rotation_times = int(rotation_times)
    best_pureness = -maxsize
    best_rotation = []
    for rotation in range(rotation_times):
        if rotation > 0:
            list_of_numbers.appendleft(list_of_numbers.pop())
        current_pureness = 0
        for i in range(len(list_of_numbers)):
            current_pureness += list_of_numbers[i] * i
        if current_pureness >= best_pureness:
            best_pureness = current_pureness
            best_rotation.append(rotation)

    return f"Best pureness {best_pureness} after {best_rotation[0]} rotations"



