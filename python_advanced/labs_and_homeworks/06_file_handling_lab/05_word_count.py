import re


def output_result(result_received):
    with open("text_files/output.txt", "w") as file:
        file.writelines("\n".join(result_received))


def get_words_from_file(file_path):
    with open(file_path, "r") as file:
        text = "".join(file.readlines())
        return re.findall(r"[a-z']+", text.lower())


words_path = "text_files/words.txt"
text_path = "text_files/input.txt"

words_from_the_first_file = get_words_from_file(words_path)
words_from_the_second_file = get_words_from_file(text_path)

words_result = {}

for word in words_from_the_first_file:
    if word in words_from_the_second_file:
        words_result[word] = words_from_the_second_file.count(word)

result = [f"{el[0]} - {el[1]}" for el in sorted(words_result.items(), key=lambda x: -x[1])]

output_result(result)