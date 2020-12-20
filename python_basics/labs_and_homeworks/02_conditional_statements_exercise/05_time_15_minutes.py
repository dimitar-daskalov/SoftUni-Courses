hours = int(input())
minutes = int(input()) + 15
if minutes > 59:
    hours = hours + 1
    if hours >= 23:
        hours = 0
    remainder = minutes % 60
    if remainder < 10:
        minutes = f"0{remainder}"
    else:
        minutes = remainder
print(f"{hours}:{minutes}")