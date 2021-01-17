from collections import deque

food_received = int(input())

list_customers = [int(order) for order in input().split()]
customers_queue = deque(list_customers)

print(max(customers_queue))

for order in list_customers:
    if food_received >= order:
        customers_queue.popleft()
        food_received -= order
    else:
        customers_queue = [str(el) for el in customers_queue]
        print(f"Orders left: {' '.join(customers_queue)}")
        break

if len(customers_queue) == 0:
    print("Orders complete")