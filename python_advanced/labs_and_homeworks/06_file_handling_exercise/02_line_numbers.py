def output_result(result_received):
    with open("exercises_test_files/output.txt", "w") as output_file:
        output_file.writelines("\n".join(line for line in result_received))


def find_characters(line):
    count_characters = 0
    pattern = "-,.!,?' \n"
    for ch in line:
        if ch not in pattern:
            count_characters += 1
    return count_characters


def find_punctuation_marks(line):
    count_marks = 0
    pattern = "-,.!,?'"
    for ch in line:
        if ch in pattern:
            count_marks += 1
    return count_marks


received_result = []

with open("exercises_test_files/text.txt", "r") as file:
    file = [line[:-1] for line in file.readlines()]
    for line_index in range(len(file)):
        received_result.append(f"Line {line_index +1}: {file[line_index]} ({find_characters(file[line_index])})({find_punctuation_marks(file[line_index])})")

output_result(received_result)