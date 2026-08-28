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

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Advanced Python Program: Set Operations

# Taking input from the user
A = set(map(int, input("Enter elements of Set A separated by space: ").split()))
B = set(map(int, input("Enter elements of Set B separated by space: ").split()))

print("\nSet A:", A)
print("Set B:", B)

# 1. Union
print("\n1. Union (A ∪ B):")
print(A | B)

# 2. Intersection
print("\n2. Intersection (A ∩ B):")
print(A & B)

# 3. Difference
print("\n3. Difference (A - B):")
print(A - B)

print("\n4. Difference (B - A):")
print(B - A)

# 4. Symmetric Difference
print("\n5. Symmetric Difference (A △ B):")
print(A ^ B)

# 5. Subset and Superset
print("\n6. Subset / Superset:")
print("A is subset of B:", A.issubset(B))
print("B is subset of A:", B.issubset(A))
print("A is superset of B:", A.issuperset(B))
print("B is superset of A:", B.issuperset(A))

# 6. Disjoint Check
print("\n7. Disjoint Check:")
print("A and B are disjoint:", A.isdisjoint(B))

# 7. Common elements
common = A.intersection(B)
print("\n8. Common Elements:")
print(common)

# 8. Elements appearing in exactly one set
unique = A.symmetric_difference(B)
print("\n9. Elements present in exactly one set:")
print(unique)

# 9. Set comprehension
even_numbers = {x for x in A | B if x % 2 == 0}
odd_numbers = {x for x in A | B if x % 2 != 0}

print("\n10. Even elements using Set Comprehension:")
print(even_numbers)

print("\n11. Odd elements using Set Comprehension:")
print(odd_numbers)

# 10. Cartesian Product
cartesian_product = {(x, y) for x in A for y in B}

print("\n12. Cartesian Product (A × B):")
print(cartesian_product)

# 11. Power-like operation: pairs having x < y
ordered_pairs = {(x, y) for x in A for y in B if x < y}

print("\n13. Ordered pairs where x < y:")
print(ordered_pairs)

# 12. Set statistics
combined = A | B

if combined:
    print("\n14. Set Statistics:")
    print("Number of unique elements:", len(combined))
    print("Minimum element:", min(combined))
    print("Maximum element:", max(combined))
    print("Sum of elements:", sum(combined))

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

'''Remove Elements Present in Another Set
Modify a set so that all elements that occur in another set are removed, without using difference() or difference_update().'''

A = {1, 2, 3, 4, 5, 6}
B = {4, 5, 6, 7, 8}

for element in B:
    A.discard(element)

print(A)




def remove_common(A, B):
    for element in B:
        A.discard(element)
    return A

A = {1, 2, 3, 4, 5}
B = {3, 4, 6}

print(remove_common(A, B))


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

'''Dynamic Access Control
Given users and their permission sets, write a function to determine whether a user can perform an operation based on:

Required permissions
User permissions
Admin override
Temporary permissions

'''


users = {
    "Ali": {
        "permissions": {"read", "write"},
        "temporary": {"delete"},
        "admin": False
    },
    "Sara": {
        "permissions": {"read", "write", "delete"},
        "temporary": set(),
        "admin": True
    },
    "John": {
        "permissions": {"read"},
        "temporary": {"write"},
        "admin": False
    }
}


check_access(users, "Ali", {"read"})
# True

check_access(users, "Ali", {"delete"})
# True   ← temporary permission

check_access(users, "Ali", {"read", "delete"})
# True

check_access(users, "John", {"read", "delete"})
# False

check_access(users, "Sara", {"delete", "admin_panel"})
# True   ← admin override

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


'''Set Cover Problem ⭐⭐⭐
Given a universe of elements and several sets, find the minimum number of sets required to cover the entire universe.

'''

universe = {1, 2, 3, 4, 5, 6}

sets = [ {1, 2, 3},{2, 4},{3, 4, 5},{4, 5, 6}, {1, 6}]

#Write a function:

minimum_set_cover(universe, sets)






















