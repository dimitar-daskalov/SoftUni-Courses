count_of_pages = int(input())
pages_read_per_hour = int(input())
count_of_days = int(input())

count_of_hours_per_book = count_of_pages / pages_read_per_hour

print(count_of_hours_per_book / count_of_days)