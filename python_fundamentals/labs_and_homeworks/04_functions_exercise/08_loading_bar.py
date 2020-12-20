def loading_bar(number):
    percentage = '%' * int(number / 10)
    added_dots = '.' * int(10 - number / 10)
    if number == 100:
        print(f"{number}% Complete!")
        print(f"[{percentage}]")
    else:
        print(f"{number}% [{percentage}{added_dots}]")
        print("Still loading...")


number_received = int(input())

loading_bar(number_received)
