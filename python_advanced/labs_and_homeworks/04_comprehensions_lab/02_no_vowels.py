text_received = input()

lower_vowels_to_remove = {'a', 'o', 'u', 'e', 'i'}
upper_vowels_to_remove = {el.upper() for el in lower_vowels_to_remove}
all_vowels_to_remove = lower_vowels_to_remove.union(upper_vowels_to_remove)

print(''.join([ch for ch in text_received if ch not in all_vowels_to_remove]))