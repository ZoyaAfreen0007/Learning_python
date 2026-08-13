students = [
    ["Zoya", 85, 92, 78],
    ["Ayesha", 90, 88, 95],
    ["Sara", 72, 80, 75],
    ["Anaya", 95, 91, 89],
    ["Fatima", 65, 70, 68]
]

# 1. Calculate total marks for each student
student_totals = []

for student in students:
    name = student[0]
    marks = student[1:]
    total = sum(marks)

    student_totals.append([name, total])

print("Student Totals:")
print(student_totals)


# 2. Calculate average using List Comprehension
averages = [
    [student[0], sum(student[1:]) / len(student[1:])]
    for student in students
]

print("\nAverages:")
print(averages)


# 3. Find students with average >= 80
top_students = [
    student[0]
    for student in students
    if sum(student[1:]) / len(student[1:]) >= 80
]

print("\nTop Students:")
print(top_students)


# 4. Sort students according to total marks
sorted_students = sorted(
    students,
    key=lambda student: sum(student[1:]),
    reverse=True
)

print("\nStudents sorted by total marks:")

for student in sorted_students:
    print(student[0], sum(student[1:]))


# 5. Find highest scorer
highest_scorer = max(
    students,
    key=lambda student: sum(student[1:])
)

print("\nHighest Scorer:")
print(highest_scorer[0])
print("Total:", sum(highest_scorer[1:]))


# 6. Extract all marks into one list
all_marks = [
    mark
    for student in students
    for mark in student[1:]
]

print("\nAll Marks:")
print(all_marks)


# 7. Find marks greater than 85
high_marks = [mark for mark in all_marks if mark > 85]

print("\nMarks greater than 85:")
print(high_marks)


# 8. Remove duplicate marks using set
unique_marks = list(set(all_marks))

print("\nUnique Marks:")
print(unique_marks)


# 9. Find the second highest mark
unique_sorted_marks = sorted(set(all_marks), reverse=True)

second_highest = unique_sorted_marks[1]

print("\nSecond Highest Mark:")
print(second_highest)


# 10. List unpacking
student = ["Zoya", 85, 92, 78]

name, *marks = student

print("\nList Unpacking:")
print("Name:", name)
print("Marks:", marks)


# 11. Flatten a nested list
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]

flattened = [
    number
    for sublist in nested_list
    for number in sublist
]

print("\nFlattened List:")
print(flattened)


# 12. Create squares of even numbers
numbers = list(range(1, 21))

even_squares = [
    number ** 2
    for number in numbers
    if number % 2 == 0
]

print("\nSquares of even numbers:")
print(even_squares)
