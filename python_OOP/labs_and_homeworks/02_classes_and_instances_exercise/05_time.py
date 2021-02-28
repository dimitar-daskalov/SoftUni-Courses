from datetime import datetime, timedelta


class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.time = datetime(100, 1, 1, hours, minutes, seconds)

    def set_time(self, hours: int, minutes: int, seconds: int):
        self.time = datetime(100, 1, 1, hours, minutes, seconds)

    def get_time(self):
        date, time = str(self.time).split()
        return time

    def next_second(self):
        self.time += timedelta(seconds=1)
        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())

time = Time(10, 59, 59)
print(time.next_second())

time = Time(23, 59, 59)
print(time.next_second())
