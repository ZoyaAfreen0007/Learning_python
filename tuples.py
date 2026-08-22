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




'''Find Second Largest

Find the second-largest element in a tuple without using sort() or sorted().

Example:

numbers = (10, 45, 23, 89, 67, 89)'''




numbers = (10, 45, 23, 89, 67, 89)

largest = float('-inf')
second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest:", second_largest)









