def perfect_number_validator(number):
    summed_numbers = 1
    i = 2
    while i * i <= number:
        if number % i == 0:
            summed_numbers = summed_numbers + i + number / i
        i += 1

    if summed_numbers == number and number != 1:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number_received = int(input())

perfect_number_validator(number_received)
