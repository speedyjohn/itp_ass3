def sort_by_vowel_count(strings):
    vowels = "aeiouAEIOU"
    return sorted(strings, key=lambda s: sum(c in vowels for c in s))


strings = ["apple", "pear", "orange", "banana"]
print(sort_by_vowel_count(strings))
