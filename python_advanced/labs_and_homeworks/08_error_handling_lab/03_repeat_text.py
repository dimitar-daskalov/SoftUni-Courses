def repeat_text(text, repeat_times):
    return text * int(repeat_times)


text_received = input()
times_to_repeat = input()

try:
    print(repeat_text(text_received, times_to_repeat))
except ValueError:
    print("Variable times must be an integer")

