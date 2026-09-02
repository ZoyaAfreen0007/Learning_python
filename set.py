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


'''Set Cover Problem:-
Given a universe of elements and several sets, find the minimum number of sets required to cover the entire universe.

'''

universe = {1, 2, 3, 4, 5, 6}

sets = [ {1, 2, 3},{2, 4},{3, 4, 5},{4, 5, 6}, {1, 6}]

#Write a function:

minimum_set_cover(universe, sets)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


'''Find Missing Elements
Given two sets representing expected and received IDs, find:

Missing IDs
Extra IDs
Common IDs

'''


def analyze_ids(expected_ids, received_ids):
    # Convert to sets
    expected = set(expected_ids)
    received = set(received_ids)

    # Find differences
    missing_ids = expected - received
    extra_ids = received - expected

    # Find common IDs
    common_ids = expected & received

    # Return result
    return {
        "missing_ids": sorted(missing_ids),
        "extra_ids": sorted(extra_ids),
        "common_ids": sorted(common_ids),
        "expected_count": len(expected),
        "received_count": len(received),
        "missing_count": len(missing_ids),
        "extra_count": len(extra_ids),
        "common_count": len(common_ids)
    }


# Example
expected_ids = {101, 102, 103, 104, 105, 106, 107}
received_ids = {101, 103, 104, 105, 108, 109}

result = analyze_ids(expected_ids, received_ids)

for key, value in result.items():
    print(f"{key}: {value}")

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


'''
Group Sets by Similarity
Given a list of sets, group sets whose Jaccard similarity is above 0.5.
'''

def jaccard_similarity(set1, set2):
    intersection = len(set1 & set2)
    union = len(set1 | set2)

    return intersection / union if union else 1.0


def group_similar_sets(sets, threshold=0.5):
    groups = []
    visited = set()

    for i in range(len(sets)):

        if i in visited:
            continue

        group = [i]
        visited.add(i)

        for j in range(i + 1, len(sets)):

            if j in visited:
                continue

            similarity = jaccard_similarity(sets[i], sets[j])

            if similarity > threshold:
                group.append(j)
                visited.add(j)

        groups.append(group)

    return [[sets[i] for i in group] for group in groups]


# Input
sets = [
    {1, 2, 3, 4},
    {1, 2, 3},
    {10, 20, 30},
    {10, 20, 40},
    {1, 2, 4},
    {100, 200}
]

result = group_similar_sets(sets)

for i, group in enumerate(result, 1):
    print(f"Group {i}:")
    for s in group:
        print(s)


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

'''Subset Chain Problem
Given:

sets = [
    {1, 2},
    {1, 2, 3},
    {1, 2, 3, 4},
    {1, 2, 3, 4, 5}
]

Check whether the sets form a valid subset chain.'''

sets = [
    {1, 2},
    {1, 2, 3},
    {1, 2, 3, 4},
    {1, 2, 3, 4, 5}
]

def is_subset_chain(sets):
    for i in range(len(sets) - 1):
        if not sets[i].issubset(sets[i + 1]):
            return False
    return True

if is_subset_chain(sets):
    print("Valid subset chain")
else:
    print("Not a valid subset chain")

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

'''
Duplicate Detection Using Sets
Given a list of integers, determine whether duplicates exist without using count() or Counter.

'''


def has_duplicates(numbers):
    seen = set()

    for num in numbers:
        if num in seen:
            return True
        seen.add(num)

    return False


numbers = [10, 20, 30, 40, 20, 50]

if has_duplicates(numbers):
    print("Duplicates exist")
else:
    print("No duplicates")


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

'''
Find Elements Appearing in Exactly Two Sets
Return all elements that occur in exactly two of the given sets.

'''
sets = [ {1, 2, 3, 4}, {3, 4, 5, 6}, {4, 5, 6, 7} ]

element_count = {}

# Count occurrence of each element across sets
for s in sets:
    for element in s:
        element_count[element] = element_count.get(element, 0) + 1

# Elements appearing in exactly two sets
result = {element for element, count in element_count.items() if count == 2}

print("Elements appearing in exactly two sets:", result)































