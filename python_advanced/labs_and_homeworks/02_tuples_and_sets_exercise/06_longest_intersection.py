number_of_ranges = int(input())
list_intersections = []

for _ in range(number_of_ranges):
    first_intersections, second_intersections = input().split("-")
    (first_intersections_start), first_intersections_end = first_intersections.split(",")
    second_intersections__start, second_intersections_end = second_intersections.split(",")
    intersection_length = list(set(range(int(first_intersections_start), int(first_intersections_end) + 1)).intersection(set(range(int(second_intersections__start), int(second_intersections_end) + 1))))
    list_intersections.append(intersection_length)

max_intersection = sorted(list_intersections, key=lambda x: -len(x))[0]

print(f"Longest intersection is {max_intersection} with length {len(max_intersection)}")