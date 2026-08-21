'''Nested Tuple Calculation

Given:

students = (
    ("Ali", 80, 75, 90),
    ("Sara", 85, 90, 88),
    ("John", 70, 65, 78)
)

Find:

Each student's total marks
Each student's average
The student with the highest average
'''


students = (
    ("Ali", 80, 75, 90),
    ("Sara", 85, 90, 88),
    ("John", 70, 65, 78)
)

highest_avg = 0
top_student = ""

for student in students:
    name = student[0]
    marks = student[1:]

    total = sum(marks)
    average = total / len(marks)

    print(name)
    print("Total:", total)
    print("Average:", average)

    if average > highest_avg:
        highest_avg = average
        top_student = name

print("\nStudent with highest average:", top_student)
print("Highest average:", highest_avg)




