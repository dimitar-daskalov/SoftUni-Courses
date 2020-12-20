name_of_the_book = input()
counter_books = 0
is_book_found = False
name_of_the_current_book = input()

while name_of_the_current_book != "No More Books":
    if name_of_the_current_book == name_of_the_book:
        is_book_found = True
        print(f"You checked {counter_books} books and found it.")
        break

    counter_books += 1
    name_of_the_current_book = input()

if not is_book_found:
    print("The book you search is not here!")
    print(f"You checked {counter_books} books.")