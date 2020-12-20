width = int(input())
length = int(input())
height = int(input())
command = input()
count_boxes = 0
total_space = width * length * height

while command != "Done":
    boxes = int(command)
    count_boxes += boxes

    if total_space < count_boxes:
        break
    command = input()

if total_space >= count_boxes:
    diff = (total_space - count_boxes)
    print(f"{diff} Cubic meters left.")
else:
    diff = abs(total_space - count_boxes)
    print(f"No more free space! You need {diff} Cubic meters more.")