from collections import deque

customers_queue = deque()

command = input()
while not command == "End":
    if command == "Paid":
        if customers_queue:
            while len(customers_queue) > 0:
                print(customers_queue.popleft())
    else:
        customers_queue.append(command)
    command = input()
print(f"{len(customers_queue)} people remaining.")