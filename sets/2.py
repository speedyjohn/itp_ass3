def unique_even_numbers(lst):
    return {num for num in lst if num % 2 == 0}


lst = [1, 2, 2, 3, 4, 5, 6, 7, 8, 8]
print(unique_even_numbers(lst))
