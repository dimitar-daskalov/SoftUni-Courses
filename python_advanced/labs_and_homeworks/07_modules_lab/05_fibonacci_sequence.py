from fibonacci_task.calculate_fibonacci_numbers import *

operations_mapper = {
    "Create Sequence": fibonacci_seq,
    "Locate": location,
}

current_sequence = []
command = input()
while not command == "Stop":
    action = " ".join(command.split()[:-1])
    number = int(command.split()[-1])
    if action == "Create Sequence":
        current_sequence = operations_mapper[action](number)
        print(" ".join((str(el) for el in current_sequence)))
    else:
        operations_mapper[action](number, current_sequence)
    command = input()