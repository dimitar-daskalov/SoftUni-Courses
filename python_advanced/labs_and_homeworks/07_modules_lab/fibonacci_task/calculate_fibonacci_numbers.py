def fibonacci_seq(number):
    if number == 1:
        return [0]
    sequence = [0, 1]
    for i in range(2, number):
        sequence.append(sequence[i - 2] + sequence[i - 1])
    return sequence


def location(number, sequence):
    if number in sequence:
        print(f"The number - {number} is at index {sequence.index(number)}")
    else:
        print(f"The number {number} is not in the sequence")
