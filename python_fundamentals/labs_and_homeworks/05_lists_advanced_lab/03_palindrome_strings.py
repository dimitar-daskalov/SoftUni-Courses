string_received = input().split()

palindrome_searched = input()
palindromes_found = []
found_palindrome = 0

for element in string_received:
    reversed_element = "".join(reversed(element))
    if element == reversed_element:
        palindromes_found.append(element)

for el in palindromes_found:
    if el == palindrome_searched:
        found_palindrome += 1

print(palindromes_found, f"Found palindrome {found_palindrome} times", sep="\n")