n = int(input())

presentation = input()

total_average_sum = 0
total_presentation = 0

while presentation != "Finish":
    total_presentation += 1
    average_sum = 0
    for i in range(0, n):
        average_sum += float(input())

    average_sum /= n
    total_average_sum += average_sum

    print(f"{presentation} - {average_sum:.2f}.")

    presentation = input()

print(f"Student's final assessment is {total_average_sum / total_presentation:.2f}.")