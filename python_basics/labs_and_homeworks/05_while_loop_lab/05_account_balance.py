input_received = input()
total = 0.0
while input_received != "NoMoreMoney":
    increase = float(input_received)
    if increase < 0:
        print("Invalid operation!")
        break

    print(f"Increase: {increase:.2f}")
    total += increase
    input_received = input()

print(f"Total: {total:.2f}")