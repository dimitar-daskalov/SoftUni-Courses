exam_hour = int(input())
exam_minute = int(input())
hour_of_arrival = int(input())
minute_of_arrival = int(input())

exam_time_minutes = (exam_hour * 60) + exam_minute
minutes_of_arrival = (hour_of_arrival * 60) + minute_of_arrival
minutes_late = minutes_of_arrival - exam_time_minutes
minutes_left = exam_time_minutes - minutes_of_arrival

if exam_time_minutes < minutes_of_arrival and minutes_late <= 59:
    print("Late")
    print(f"{minutes_late} minutes after the start")
elif exam_time_minutes < minutes_of_arrival and minutes_late > 59:
    late_hours = minutes_late // 60
    late_minutes = minutes_late % 60
    if late_minutes > 9:
        print("Late")
        print(f"{late_hours}:{late_minutes} hours after the start")
    else:
        print("Late")
        print(f"{late_hours}:0{late_minutes} hours after the start")
if exam_time_minutes > minutes_of_arrival and minutes_left > 30:
    left_hours = minutes_left // 60
    left_minutes = minutes_left % 60
    if left_minutes > 9 and left_hours != 0:
        print("Early")
        print(f"{left_hours}:{left_minutes} hours before the start")
    elif minutes_left <= 59 and left_minutes != 0:
        print("Early")
        print(f"{minutes_left} minutes before the start")
    elif left_minutes == 0:
        print("Early")
        print(f"{left_hours}:00 hours before the start")
    else:
        print("Early")
        print(f"{left_hours}:0{left_minutes} hours before the start")
elif exam_time_minutes >= minutes_of_arrival and minutes_left <= 30:
    if exam_time_minutes == minutes_of_arrival:
        print("On time")
    else:
        print("On time")
        print(f"{minutes_left} minutes before the start")