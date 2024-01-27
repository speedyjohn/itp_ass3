def sort_students(students):
    under_18 = [name for name, age, grade in students if age < 18]
    grades_over_18 = [grade for name, age, grade in students if age > 18]
    return under_18, grades_over_18


students = [("John", 17, 'B'), ("Alice", 19, 'A'), ("Bob", 20, 'C'), ("Emma", 16, 'A')]
print(*sort_students(students))
