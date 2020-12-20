command = float(input())

while True:
    if 1 <= command <= 100:
        break

    command = float(input())

print(f"The number {command} is between 1 and 100")