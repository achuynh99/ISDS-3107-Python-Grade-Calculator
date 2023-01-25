readings = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]  # grades as a percent score
assignments = [             # each line for assignments represents a new chapter
100,
96.67, 74.97, 100,
94.45, 91.57, 100,
100, 100, 100,
100, 100,
100, 100, 100,
0, 0, 100,      # missed assignments
100, 100, 100,
100, 95.84, 100,
100, 95.82,
100, 100, 100, 97.96,
100, 100, 89.16
]
quizzes = [96, 90, 90, 90, 92, 90, 100, 84, 90, 75, 80, 75]
exams = [57.19, 72.46, 89.29, 78.03, 88.89]
participation = 120         # there's only 120 participation points

def grader(list, points):   # list takes in what you scored and points is how many total possible points for each grade
    total = 0
    for x in list:
        temp = x / 100 * points
        total = total + temp
        temp = 0
    max = len(list) * points
    return total, max

readGrade = grader(readings, 10)
assignGrade = grader(assignments, 10)
quizGrade = grader(quizzes, 15)
examGrade = grader(exams, 100)

total = readGrade[0] + assignGrade[0] + quizGrade[0] + examGrade[0] + participation
max = readGrade[1] + assignGrade[1] + quizGrade[1] + examGrade [1] + participation
grade = total / max
print("You got", total, "points out of", max)
print ("So your grade is", grade)