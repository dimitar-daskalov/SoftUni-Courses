string_received = input()

brackets_stack = []

for i in range(len(string_received)):
    if string_received[i] == "(":
        brackets_stack.append(int(i))
    elif string_received[i] == ")":
        end_bracket = i + 1
        start_bracket = brackets_stack.pop()
        print(string_received[start_bracket:end_bracket])