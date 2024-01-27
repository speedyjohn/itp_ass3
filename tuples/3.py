def count_vowels_consonants(s):
    vowels = "aeiou"
    vowel_count = sum(c.lower() in vowels for c in s if c.isalpha())
    consonant_count = sum(c.lower() not in vowels for c in s if c.isalpha())
    return vowel_count, consonant_count


string = "Hello World"
print(count_vowels_consonants(string))
