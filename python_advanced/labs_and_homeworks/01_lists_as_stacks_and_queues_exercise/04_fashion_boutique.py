clothes_received = input().split()

capacity_of_the_rack = int(input())

summed_clothing = 0
count_racks = 1

while clothes_received:
    if capacity_of_the_rack >= summed_clothing + int(clothes_received[-1]):
        summed_clothing += int(clothes_received.pop())
    else:
        count_racks += 1
        summed_clothing = 0

print(count_racks)

