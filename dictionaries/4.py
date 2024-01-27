def count_students_per_course(school_courses):
    course_student_counts = {}
    for course, students in school_courses.items():
        student_count = len(students)
        course_student_counts[course] = student_count
    return course_student_counts


school_courses = {
    'Math': ['Abai', 'Akhan', 'Asanali'],
    'Science': ['Ismail', 'David'],
    'History': ['Ismail', 'Sergey', 'Kamila', 'Dilnaz']
}
print(count_students_per_course(school_courses))
