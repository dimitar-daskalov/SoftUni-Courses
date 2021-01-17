received_string = input()

brackets_stack = []

brackets_dict = {'(': ')', '[': ']', '{': '}'}

is_valid = False

for ch in received_string:
    if ch in "([{":
        brackets_stack.append(ch)
    else:
        if brackets_stack:
            if ch == brackets_dict[brackets_stack[-1]]:
                brackets_stack.pop()
                is_valid = True
            else:
                is_valid = False
                break
        else:
            is_valid = False
            break

if is_valid:
    print("YES")
else:
    print("NO")