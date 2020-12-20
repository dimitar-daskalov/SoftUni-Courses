command = input()
total_tickets_sold = 0
student_tickets_sold = 0
standard_tickets_sold = 0
kid_tickets_sold = 0

while command != "Finish":
    available_seats = int(input())
    special_movie_tickets_sold = 0

    ticket_type = input()
    while ticket_type != "End":
        special_movie_tickets_sold += 1
        total_tickets_sold += 1
        if ticket_type == "student":
            student_tickets_sold += 1
        elif ticket_type == "standard":
            standard_tickets_sold += 1
        elif ticket_type == "kid":
            kid_tickets_sold += 1

        if special_movie_tickets_sold == available_seats:
            break
        ticket_type = input()

    percent = (special_movie_tickets_sold / available_seats) * 100
    print(f"{command} - {percent:.2f}% full.")
    command = input()

print(f"Total tickets: {total_tickets_sold}")

percent_student_tickets = (student_tickets_sold / total_tickets_sold) * 100
print(f"{percent_student_tickets:.2f}% student tickets.")

percent_standard_tickets = (standard_tickets_sold / total_tickets_sold) * 100
print(f"{percent_standard_tickets:.2f}% standard tickets.")

percent_kid_tickets = (kid_tickets_sold / total_tickets_sold) * 100
print(f"{percent_kid_tickets:.2f}% kids tickets.")