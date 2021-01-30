def palindrome(word, start_index_word=0, end_index_word=-1):
    if start_index_word == len(word) // 2:
        return f"{word} is a palindrome"
    for i in range(len(word)):
        if word[start_index_word] == word[end_index_word]:
            return palindrome(word, start_index_word + 1, end_index_word - 1)
        else:
            return f"{word} is not a palindrome"
