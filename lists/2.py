def generate_squares_cubes(n):
    return [x ** 2 if x % 2 == 0 else x ** 3 for x in range(1, n + 1)]


n = 10
print(generate_squares_cubes(n))
