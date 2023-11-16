import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student: random.randint(1, 100) for student in names}

# passed_students = {student for student in names if students_scores[student] > 50}
passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
