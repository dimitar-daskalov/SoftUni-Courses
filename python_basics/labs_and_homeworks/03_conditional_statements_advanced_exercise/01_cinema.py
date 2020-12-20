projection_type = input()
count_rows = int(input())
count_columns = int(input())

total_seats = count_rows * count_columns

if projection_type == "Premiere":
    income = total_seats * 12
elif projection_type == "Normal":
    income = total_seats * 7.50
elif projection_type == "Discount":
    income = total_seats * 5.00

print(f"{income:.2f} leva")