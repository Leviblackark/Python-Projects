student_scores = {
    'Bela': 88,
    'Alexandra': 78,
    'Tom': 95,
    'Amelia': 75,
    'Nancy': 60,
}

student_grades = {}

for score in student_scores:
    # student_scores[score] is the value of the current keyword
    if student_scores[score] >= 91:
        student_grades[score] = "Outstanding"
    elif student_scores[score] >= 81:
        student_grades[score] = "Exceeds Expectations"
    elif student_scores[score] >= 71:
        student_grades[score] = "Acceptable"
    else:
        student_grades[score] = "Fail"

for grade in student_grades:
    # prints the key
    print(grade)
    # prints the value
    print(student_grades[grade])
