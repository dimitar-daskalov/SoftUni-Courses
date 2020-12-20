statistics_dict = {}

command = input()

while not command == "statistics":
    key, value = command.split(": ")
    value = int(value)
    if key not in statistics_dict:
        statistics_dict[key] = value
    else:
        statistics_dict[key] += value
    command = input()

print(f"Products in stock:")

for key, value in statistics_dict.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(statistics_dict)}", f"Total Quantity: {sum(statistics_dict.values())}", sep="\n")
