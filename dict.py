# Student Result Management System

students = {
    "S001": {
        "name": "Zoya",
        "branch": "CSE",
        "marks": {
            "Python": 92,
            "DBMS": 85,
            "Machine Learning": 88,
            "Data Structures": 90
        }
    },

    "S002": {
        "name": "Aisha",
        "branch": "CSE",
        "marks": {
            "Python": 78,
            "DBMS": 82,
            "Machine Learning": 75,
            "Data Structures": 80
        }
    },

    "S003": {
        "name": "Rahul",
        "branch": "CSE",
        "marks": {
            "Python": 95,
            "DBMS": 91,
            "Machine Learning": 94,
            "Data Structures": 89
        }
    },

    "S004": {
        "name": "Aryan",
        "branch": "CSE",
        "marks": {
            "Python": 67,
            "DBMS": 73,
            "Machine Learning": 70,
            "Data Structures": 75
        }
    }
}


# ---------------------------------------------------
# 1. Calculate total and average marks
# ---------------------------------------------------

for student_id, student in students.items():

    marks = student["marks"]

    total = sum(marks.values())
    average = total / len(marks)

    student["total"] = total
    student["average"] = round(average, 2)


# ---------------------------------------------------
# 2. Assign grades using dictionary comprehension
# ---------------------------------------------------

for student in students.values():

    student["grade"] = (
        "A+" if student["average"] >= 90 else
        "A" if student["average"] >= 80 else
        "B" if student["average"] >= 70 else
        "C"
    )


# ---------------------------------------------------
# 3. Find the topper
# ---------------------------------------------------

topper_id = max(
    students,
    key=lambda x: students[x]["average"]
)

topper = students[topper_id]

print("\n===== TOPPER =====")
print("ID:", topper_id)
print("Name:", topper["name"])
print("Average:", topper["average"])
print("Grade:", topper["grade"])


# ---------------------------------------------------
# 4. Sort students according to their average marks
# ---------------------------------------------------

ranking = sorted(
    students.items(),
    key=lambda item: item[1]["average"],
    reverse=True
)

print("\n===== RANKING =====")

for rank, (student_id, student) in enumerate(ranking, start=1):

    print(
        rank,
        student_id,
        student["name"],
        student["average"],
        student["grade"]
    )


# ---------------------------------------------------
# 5. Find students who scored more than 85 in Python
# ---------------------------------------------------

python_toppers = {
    student_id: student["name"]
    for student_id, student in students.items()
    if student["marks"]["Python"] > 85
}

print("\n===== PYTHON TOPPERS =====")

for student_id, name in python_toppers.items():
    print(student_id, "->", name)


# ---------------------------------------------------
# 6. Calculate subject-wise average
# ---------------------------------------------------

subjects = students["S001"]["marks"].keys()

subject_average = {
    subject: round(
        sum(student["marks"][subject] for student in students.values())
        / len(students),
        2
    )
    for subject in subjects
}

print("\n===== SUBJECT AVERAGES =====")

for subject, average in subject_average.items():
    print(subject, ":", average)


# ---------------------------------------------------
# 7. Find the highest scorer in every subject
# ---------------------------------------------------

subject_toppers = {}

for subject in subjects:

    topper_id = max(
        students,
        key=lambda student_id:
        students[student_id]["marks"][subject]
    )

    subject_toppers[subject] = {
        "id": topper_id,
        "name": students[topper_id]["name"],
        "marks": students[topper_id]["marks"][subject]
    }


print("\n===== SUBJECT TOPPERS =====")

for subject, data in subject_toppers.items():

    print(
        subject,
        "->",
        data["name"],
        "(",
        data["marks"],
        ")"
    )


# ---------------------------------------------------
# 8. Filter students with average >= 80
# ---------------------------------------------------

excellent_students = {
    student_id: student["name"]
    for student_id, student in students.items()
    if student["average"] >= 80
}

print("\n===== EXCELLENT STUDENTS =====")

print(excellent_students)


# ---------------------------------------------------
# 9. Display complete student information
# ---------------------------------------------------

print("\n===== COMPLETE STUDENT DATABASE =====")

for student_id, student in students.items():

    print("\nID:", student_id)
    print("Name:", student["name"])
    print("Branch:", student["branch"])
    print("Marks:", student["marks"])
    print("Total:", student["total"])
    print("Average:", student["average"])
    print("Grade:", student["grade"])
