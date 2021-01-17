from collections import deque

stops = int(input())

stops_queue = deque()

for stop in range(stops):
    amount, distance = input().split()
    stop_dict = {"amount": int(amount), "distance": int(distance)}
    stops_queue.append(stop_dict)

for big_stop_index in range(stops):
    petrol = 0
    is_valid = True
    for small_stop_index in range(stops):
        petrol += stops_queue[small_stop_index]["amount"] - stops_queue[small_stop_index]["distance"]

        if petrol < 0:
            is_valid = False
            stops_queue.append(stops_queue.popleft())
            break

    if is_valid:
        print(big_stop_index)
        break
