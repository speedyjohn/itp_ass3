def unique_vowels(s):
    vowels = "aeiou"
    return {char.lower() for char in s if char.lower() in vowels and 0 < string.count(char.lower()) < 2}


string = "Hello World!"
print(unique_vowels(string))
