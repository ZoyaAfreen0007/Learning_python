def display_set(name, data):
    print(f"{name} = {sorted(data)}")


# -------------------------------------------------
# 1. Creating sets
# -------------------------------------------------

students_python = {
    "Aisha", "Rahul", "Zoya", "Arman",
    "Sara", "Kabir", "Neha"
}

students_sql = {
    "Zoya", "Arman", "Sara", "Vikram",
    "Neha", "Rohan"
}

students_powerbi = {
    "Zoya", "Sara", "Kabir", "Rohan",
    "Priya"
}

print("========== STUDENT SETS ==========")
display_set("Python", students_python)
display_set("SQL", students_sql)
display_set("Power BI", students_powerbi)


# -------------------------------------------------
# 2. Union
# Students who know at least one skill
# -------------------------------------------------

all_students = students_python | students_sql | students_powerbi

print("\n========== UNION ==========")
display_set("Students knowing at least one skill", all_students)
print("Total:", len(all_students))


# -------------------------------------------------
# 3. Intersection
# Students who know all three skills
# -------------------------------------------------

all_three = (
    students_python
    & students_sql
    & students_powerbi
)

print("\n========== INTERSECTION ==========")
display_set("Students knowing all 3 skills", all_three)


# -------------------------------------------------
# 4. Difference
# Students who know Python but NOT SQL
# -------------------------------------------------

python_not_sql = students_python - students_sql

print("\n========== DIFFERENCE ==========")
display_set("Python but not SQL", python_not_sql)


# -------------------------------------------------
# 5. Symmetric Difference
# Students who know Python or SQL, but NOT both
# -------------------------------------------------

python_sql_exclusive = (
    students_python ^ students_sql
)

print("\n========== SYMMETRIC DIFFERENCE ==========")
display_set(
    "Python or SQL but not both",
    python_sql_exclusive
)


# -------------------------------------------------
# 6. Subset and Superset
# -------------------------------------------------

advanced_python = {"Zoya", "Sara"}

print("\n========== SUBSET / SUPERSET ==========")

print(
    "Is advanced_python subset of Python?",
    advanced_python.issubset(students_python)
)

print(
    "Is Python superset of advanced_python?",
    students_python.issuperset(advanced_python)
)


# -------------------------------------------------
# 7. Disjoint Sets
# -------------------------------------------------

students_java = {"John", "Peter", "David"}

print("\n========== DISJOINT CHECK ==========")

print(
    "Are Python and Java students disjoint?",
    students_python.isdisjoint(students_java)
)


# -------------------------------------------------
# 8. Set Comprehension
# Generate squares of even numbers
# -------------------------------------------------

even_squares = {
    number ** 2
    for number in range(1, 21)
    if number % 2 == 0
}

print("\n========== SET COMPREHENSION ==========")
display_set("Even number squares", even_squares)


# -------------------------------------------------
# 9. Filtering a set
# Find students whose names have more than 4 letters
# -------------------------------------------------

long_names = {
    student
    for student in all_students
    if len(student) > 4
}

print("\n========== FILTERING ==========")
display_set("Names with more than 4 letters", long_names)


# -------------------------------------------------
# 10. Cartesian Product
# -------------------------------------------------

departments = {"CSE", "ECE"}
years = {1, 2, 3, 4}

student_categories = {
    (department, year)
    for department in departments
    for year in years
}

print("\n========== CARTESIAN PRODUCT ==========")

for category in sorted(student_categories):
    print(category)


# -------------------------------------------------
# 11. In-place set operations
# -------------------------------------------------

demo = students_python.copy()

demo.update(students_sql)       # Equivalent to |=
print("\nAfter update():")
display_set("demo", demo)

demo.intersection_update(students_powerbi)
print("\nAfter intersection_update():")
display_set("demo", demo)


# -------------------------------------------------
# 12. Removing elements safely
# -------------------------------------------------

demo = students_python.copy()

demo.discard("Unknown")     # Does NOT produce an error
demo.discard("Rahul")

print("\n========== DISCARD ==========")
display_set("After discard()", demo)


# -------------------------------------------------
# 13. Pop an arbitrary element
# -------------------------------------------------

demo = students_python.copy()

removed_student = demo.pop()

print("\n========== POP ==========")
print("Removed:", removed_student)
display_set("Remaining students", demo)


# -------------------------------------------------
# 14. Set algebra summary
# -------------------------------------------------

print("\n========== SET ALGEBRA SUMMARY ==========")

print("Union:", students_python | students_sql)
print("Intersection:", students_python & students_sql)
print("Difference:", students_python - students_sql)
print("Reverse Difference:", students_sql - students_python)
print("Symmetric Difference:", students_python ^ students_sql)


# -------------------------------------------------
# 15. Final statistics
# -------------------------------------------------

print("\n========== FINAL STATISTICS ==========")

print("Python students :", len(students_python))
print("SQL students    :", len(students_sql))
print("Power BI students:", len(students_powerbi))
print("Unique students :", len(all_students))
print("All 3 skills    :", len(all_three))
