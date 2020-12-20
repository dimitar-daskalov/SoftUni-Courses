list_received = input().split(".")

formatted_list = list(map(int, list_received))
number = int("".join(map(str, formatted_list)))

result = number + 1

print(".".join(str(result)))


