palindrome_string = input().split(", ")


def is_palindrome(a):
    for el in a:
        if el == el[::-1]:
            print("True")
        else:
            print("False")


is_palindrome(palindrome_string)

