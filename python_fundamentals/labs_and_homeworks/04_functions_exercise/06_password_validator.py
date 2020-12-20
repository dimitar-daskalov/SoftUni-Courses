input_received = input()


def validator(password):
    error_message = ""
    is_password_wrong = False
    count_digits = 0
    length_received = len(password)
    if not (6 <= length_received <= 10):
        is_password_wrong = True
        error_message = "Password must be between 6 and 10 characters \n"
    for letter in password:
        if letter.isdigit() is not True and letter.isalpha() is not True:
            is_password_wrong = True
            error_message += "Password must consist only of letters and digits \n"
            break
        elif letter.isdigit():
            count_digits += 1
    if count_digits < 2:
        is_password_wrong = True
        error_message += "Password must have at least 2 digits \n"

    if is_password_wrong:
        print(error_message)
    else:
        print("Password is valid")


validator(input_received)
