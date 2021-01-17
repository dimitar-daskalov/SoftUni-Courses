from collections import deque
from _datetime import datetime, timedelta

data = input().split(';')
robots = deque([])
products = deque([])

start_time = datetime.strptime(input(), '%H:%M:%S')
added_time = timedelta(seconds=1)
product_time = start_time + added_time

for el in data:
    robot = {}
    name, time = el.split('-')
    time = int(time)
    robot['name'] = name
    robot['processing_time'] = time
    robot['available_at'] = product_time
    robots.append(robot)

product = input()
while not product == 'End':
    products.append(product)
    product = input()

while len(products) > 0:
    current_product = products.popleft()
    is_available = False
    for current_robot in robots:
        if product_time >= current_robot['available_at']:
            current_robot['available_at'] = product_time + timedelta(seconds=current_robot['processing_time'])
            print(f'{current_robot["name"]} - {current_product} [{product_time.strftime("%H:%M:%S")}]')
            is_available = True
            break
    if not is_available:
        products.append(current_product)
    product_time += added_time